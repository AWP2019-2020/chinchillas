from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)
    price = models.FloatField()
    rating = models.FloatField()
    image = models.FileField(upload_to='uploads/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)
    rating = models.FloatField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Country(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    birthday = models.DateField(blank=True, null=True)
    avatar = models.FileField(upload_to='media/', blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="profiles", blank=True, null=True)




class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def totalPrice(self):
        sum = 0
        for product in list(self.products.all()):
            sum += product.product.price * product.quantity
        return sum

    @property
    def cart_products(self):
        return list(self.products.all())


class ShoppingCartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shoppingCart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name="products")
    quantity = models.IntegerField()

