from django import forms
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fieldsa = ['name', 'quantity', 'price_per_unit']


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'price']

class ReceipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ['menu_item', 'ingredient', 'quantity']


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['menu_item']