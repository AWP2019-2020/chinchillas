from django.urls import path
from shop.views import (
  index,
  RegisterView,
  LoginView,
  LogoutView,
  product_detail, category_detail, review_create
)

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('product/<int:pk>', product_detail, name='product_detail'),
    path('category/<int:pk>', category_detail, name='category_detail'),
    path('product/<int:pk>/review/create', review_create, name='review_create'),
]
