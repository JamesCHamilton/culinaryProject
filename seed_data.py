import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flavorfusion.settings')
django.setup()

from recipes.models import Country, Ingredient, Recipe, DietaryTag

dietary_tags_data = [
    "Halal", "Contains Alcohol", "Vegan", "Vegetarian", "Gluten-Free", "Dairy-Free",
    "Nut-Free", "Kosher", "Keto-Friendly", "Low-Carb", "Pescatarian", "Sugar-Free", "Egg-Free"
]

data = {
    "Italian": [
        {"title": "Bolognese", "ingredients": ["Olive oil", "Butter", "Carrots", "Celery", "Onion", "Heavy cream", "Half and half", "Ground beef", "Store-bought marinara sauce"]},
        {"title": "Parmigiana di melanzane", "ingredients": ["Eggplant", "Eggs", "Breadcrumbs", "Olive oil", "Spaghetti sauce", "Tomato sauce", "Mozzarella cheese", "Parmesan"]},
        {"title": "Focaccia", "ingredients": ["All-purpose flour", "Kosher salt", "Instant yeast", "Tap water", "Soft butter", "Olive oil", "Fresh herbs or Italian seasoning", "Flaky sea salt"]}
    ],
    "Chinese": [
        {"title": "Chicken Udon Soup", "ingredients": ["Peanut oil", "Vegetable oil", "Boneless Chicken thigh", "Chicken breast", "Japanese sake", "Dry sherry", "Soy sauce", "Sugar", "Chicken broth", "Vegetable broth", "Brown mushrooms", "shiitake mushrooms", "Green onions", "Ginger", "Cabbage", "Udon noodles"]},
        {"title": "Scallion Pancakes with Dim Sum Dipper", "ingredients": ["Flour", "Salt", "Boiling water", "Grapeseed oil", "Olive oil", "Sesame oil", "Kosher salt", "Sea salt", "Scallions", "Soy sauce", "Rice vinegar", "Sambal oelek"]},
        {"title": "Air Fryer Egg Rolls", "ingredients": ["Cabbage", "Carrots", "Kosher salt", "Shrimp", "Vegetable oil", "Garlic", "Ginger", "Char siu", "Shaoxing rice wine", "cooking sherry", "oyster sauce", "soy sauce", "sugar", "white pepper", "cornstarch", "egg roll wrappers", "Canola oil spray", "Sweet chili sauce", "duck sauce"]}
    ],
    "Japanese": [
        {"title": "Gyudon", "ingredients": ["Onion", "Sliced beef", "Dashi", "Sake", "Mirin", "Soy sauce", "Sugar", "Japanese short-grain rice", "Pickled red ginger"]},
        {"title": "Soba Noodles Salad", "ingredients": ["Sesame oil", "Crushed red pepper", "Honey", "Soy sauce", "Soba noodles", "buckwheat noodles", "Onions", "Cilantro", "Coriander", "Toasted white sesame seeds"]},
        {"title": "Tamago Sando", "ingredients": ["Eggs", "Shokupan", "Japanese milk bread", "Salted butter", "Sugar", "Kosher Salt", "Black pepper", "Milk", "Kewpie mayonnaise"]}
    ],
    "Indian": [
        {"title": "Chicken Tikka Masala", "ingredients": ["basmati rice", "chicken thighs", "Kosher salt", "black pepper", "vegetable oil", "onion", "tomato paste", "garlic", "minced grated ginger", "garam masala", "chili powder", "ground turmeric", "tomato sauce", "chicken stock", "heavy cream", "Half and half", "fresh cilantro leaves"]},
        {"title": "Lentil Dal", "ingredients": ["Vegetable oil", "yellow onion", "Garlic", "Ginger", "Green chilis", "Cumin", "Coriander", "Turmeric", "Paprika", "Cinnamon", "Red lentils", "Diced tomatoes", "Vegetable broth", "Kosher salt", "Ground black pepper", "Yogurt"]}
    ],
    "American": [
        {"title": "Burger", "ingredients": ["Ground beef", "Bread crumbs", "Egg", "Butter", "Tomato sauce", "Lettuce", "Cheese", "Onion", "Ketchup", "Mayonnaise"]},
        {"title": "Pizza", "ingredients": ["Dough", "Tomato sauce", "Cheese", "Pizza sauce", "Diced tomatoes", "Bell peppers", "Onion", "Mushrooms", "Bacon", "Hot sauce"]}
    ]
}

def seed():
    # Seed tags
    for tag_name in dietary_tags_data:
        DietaryTag.objects.get_or_create(name=tag_name)
    
    for country_name, dishes in data.items():

        country, _ = Country.objects.get_or_create(name=country_name)
        for dish in dishes:
            recipe, created = Recipe.objects.get_or_create(
                title=dish["title"],
                country=country
            )
            for ing_name in dish["ingredients"]:
                ingredient, _ = Ingredient.objects.get_or_create(name=ing_name)
                recipe.ingredients.add(ingredient)
            if created:
                print(f"Created recipe: {recipe.title}")

if __name__ == "__main__":
    seed()
