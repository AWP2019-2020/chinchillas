from django.contrib import admin

# Register your models here.
from shop import models
from shop.models import Product, Category, Review, ShoppingCart, ShoppingCartProduct, UserProfile, Country


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_total_price']
    readonly_fields = ['get_total_price', 'get_cart_products']

    def get_total_price(self, obj):
        return obj.totalPrice

    def get_cart_products(self, obj):
        return obj.cartProducts

    get_total_price.short_description = "Price"
    get_cart_products.short_description = "Products"


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(ShoppingCartProduct)
admin.site.register(UserProfile)
admin.site.register(Country)