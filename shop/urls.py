from django.urls import path
from shop.views import (
    index,
    RegisterView,
    LoginView,
    LogoutView,
    UserProfileView,
    product_detail, category_detail, review_create,
    shoppingCart, deactivate_cart, ReviewEditView, ReviewDeleteView)

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('shoppingCart', shoppingCart, name='shoppingCart_detail'),
    path('deactivate_cart/<int:pk>', deactivate_cart, name='deactivate_cart'),
    path('product/<int:pk>', product_detail, name='product_detail'),
    path('category/<int:pk>', category_detail, name='category_detail'),
    path('product/<int:pk>/review/create', review_create, name='review_create'),
    path('user_profile/<int:pk>', UserProfileView.as_view(), name='user_profile'),
    path('product/<int:pk>/review/<int:pk_review>/edit', ReviewEditView.as_view(), name='review_edit'),
    path('product/<int:pk>/review/<int:pk_review>/delete', ReviewDeleteView.as_view(), name='review_delete'),
]
