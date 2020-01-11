from django.urls import path
from . import views
from .views import product_detail, category_detail

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:pk>', product_detail, name='product_detail'),
    path('category/<int:pk>', category_detail, name='category_detail'),

]