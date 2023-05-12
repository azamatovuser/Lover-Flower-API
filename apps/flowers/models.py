from django.db import models


class Color(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Price(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __int__(self):
        return self.price


class Ingredient(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Flower(models.Model):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='flower_image/')
    description = models.TextField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title