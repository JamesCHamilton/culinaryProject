from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Avg
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Recipe, Country, Ingredient, Favorite, Rating, DietaryTag
from .forms import RecipeForm
from .supabase_utils import get_supabase_client

def home(request):
    query = request.GET.get('q')
    country_filter = request.GET.get('country')
    ingredient_filter = request.GET.get('ingredient')
    tag_filter = request.GET.getlist('tag')
    
    # Only display recipes made by users
    recipes = Recipe.objects.filter(author__isnull=False).annotate(avg_score=Avg('ratings__score')).order_by('-created_at')
    
    if query:
        recipes = recipes.filter(
            Q(title__icontains=query) | 
            Q(instructions__icontains=query)
        )
    
    if country_filter:
        recipes = recipes.filter(country__name=country_filter)
        
    if ingredient_filter:
        recipes = recipes.filter(ingredients__name=ingredient_filter)

    if tag_filter:
        for tag in tag_filter:
            recipes = recipes.filter(dietary_tags__name=tag)
        
    countries = Country.objects.all()
    ingredients = Ingredient.objects.all()
    dietary_tags = DietaryTag.objects.all()
    
    context = {
        'recipes': recipes,
        'countries': countries,
        'ingredients': ingredients,
        'dietary_tags': dietary_tags,
        'selected_tags': tag_filter,
    }
    return render(request, 'recipes/home.html', context)


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        
        supabase = get_supabase_client()
        try:
            res = supabase.auth.sign_up({
                "email": email,
                "password": password,
            })
            if res.user:
                # Create Django user
                user, created = User.objects.get_or_create(email=email, defaults={'username': username or email.split('@')[0]})
                if not created:
                    user.username = username or user.username
                    user.save()
                
                # Log in to Django
                login(request, user)
                messages.success(request, "Account created successfully!")
                return redirect('home')
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            
    return render(request, 'recipes/signup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        supabase = get_supabase_client()
        try:
            res = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password,
            })
            if res.user:
                # Sync with Django user
                user = User.objects.filter(email=email).first()
                if not user:
                    user = User.objects.create_user(username=email.split('@')[0], email=email)
                
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('home')
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            
    return render(request, 'recipes/signin.html')

def signout(request):
    logout(request)
    messages.info(request, "Logged out.")
    return redirect('home')


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, recipe=recipe).exists()
    
    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'is_favorite': is_favorite,
        'stars': range(1, 6)
    })

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m() # Important for many-to-many relationships
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

@login_required
def toggle_favorite(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    favorite, created = Favorite.objects.get_or_create(user=request.user, recipe=recipe)
    if not created:
        favorite.delete()
    return redirect('recipe_detail', pk=pk)

@login_required
def rate_recipe(request, pk):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, pk=pk)
        score = request.POST.get('score')
        if score:
            Rating.objects.update_or_create(
                user=request.user, recipe=recipe,
                defaults={'score': score}
            )
    return redirect('recipe_detail', pk=pk)

