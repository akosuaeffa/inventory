from django.shortcuts import render, redirect
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from .forms import IngredientForm, MenuItemForm, PurchaseForm, ReceipeRequirementForm


# Create your views here.
# views for home page

def home(request):
    ingredients = Ingredient.objects.all()
    menu_items = MenuItem.objects.all()
    purchases = Purchase.objects.all()
    return render(request, )