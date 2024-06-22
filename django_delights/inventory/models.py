from django.db import models

# model for ingredients
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.FloatField()
    price_per_unt = models.FloatField()

    def __str_(self):
        return self.name

# model for the meniu
class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.name
    

# model for Recipe
class RecipeRequirement(models.Model):
    menu = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quanity = models.FloatField()

    def __str__(self):
        return f"{self.quanity} of {self.ingredient.name} for {self.menu.name}"
    

#model for purchases
class Purchase(models.Model):
    menu = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase of {self.menu.name} at {self.timestamp}"

