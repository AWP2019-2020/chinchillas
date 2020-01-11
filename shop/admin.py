from django.contrib import admin

# Register your models here.
from shop import models
from shop.models import Product, Category, Review, UserProfile, Country

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_by', 'post')
