from django import forms
from .models import Recipe, Ingredient, DietaryTag

class RecipeForm(forms.ModelForm):
    ingredients_text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter ingredients separated by commas'}),
        help_text="e.g. Tomato, Cheese, Basil",
        required=True
    )

    class Meta:
        model = Recipe
        fields = ['title', 'country', 'dietary_tags', 'instructions', 'calories', 'protein', 'carbs', 'fat']
        widgets = {
            'instructions': forms.Textarea(attrs={'rows': 5}),
            'dietary_tags': forms.CheckboxSelectMultiple(),
            'calories': forms.NumberInput(attrs={'placeholder': 'kcal'}),
            'protein': forms.NumberInput(attrs={'placeholder': 'g'}),
            'carbs': forms.NumberInput(attrs={'placeholder': 'g'}),
            'fat': forms.NumberInput(attrs={'placeholder': 'g'}),
        }



    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            # Handle ingredients string
            ingredients_list = [i.strip() for i in self.cleaned_data['ingredients_text'].split(',') if i.strip()]
            for name in ingredients_list:
                ingredient, _ = Ingredient.objects.get_or_create(name=name)
                instance.ingredients.add(ingredient)
        return instance
