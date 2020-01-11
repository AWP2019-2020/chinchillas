from django.contrib import admin

# Register your models here.
from shop import models
from shop.models import Product, Category, Review, UserProfile, Country

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(UserProfile)
admin.site.register(Country)