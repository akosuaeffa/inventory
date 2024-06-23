from django.shortcuts import render, redirect
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from .forms import IngredientForm, MenuItemForm, PurchaseForm, ReceipeRequirementForm


# Create your views here.
# views for home page

def home(request):
    ingredients = Ingredient.objects.all()
    menu_items = MenuItem.objects.all()
    purchases = Purchase.objects.all()
    return render(request, 'inventory/home.html', {
        'ingredients': ingredients,
        'menu_items': menu_items,
        'purchases': purchases,
    })

def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IngredientForm()
    return render(request, 'inventory/add_ingredient.html', {'form': form})