from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    View, TemplateView, CreateView, DetailView
)

from shop.forms import ReviewForm
from shop.models import User, Product, Category, Review, ShoppingCart
from django.urls import reverse, reverse_lazy


def index(request):
    return render(request, 'index.html')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    model = User

    # def form_valid(self, form):
    #     data = form.cleaned_data
    #     user = User.objects.create_user(username=data['username'],
    #                                     password=data['password1'])
    #     UserProfile.objects.create(user=user)
    #     return redirect('post_list')


class LoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self):
        form = AuthenticationForm()
        return {'form': form}

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'],
                                password=data['password'])
            login(request, user)
            return redirect(reverse('index'))
        else:
            return render(request, "login.html", {"form": form})


class LogoutView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('login'))


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product_detail.html", {"product": product})


def category_detail(request, pk):
    category = Category.objects.get(id=pk)
    return render(request, "category_detail.html", {"category": category})


def review_detail(request, pk):
    review = Review.objects.get(id=pk)
    return render(request, "review_detail.html", {"review": review})


def shoppingCart(request, pk):
    shoppingCart = ShoppingCart.objects.filter(user__id=pk)
    if len(shoppingCart):
        shoppingCart = shoppingCart.first()
    return render(request, "shoppingCart.html", {"shoppingCart": shoppingCart})


@login_required
def review_create(request, pk):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            product = Product.objects.get(id=pk)
            Review.objects.create(
                created_by=request.user,
                post=product,
                **form.cleaned_data
            )
            return redirect(reverse_lazy("product_detail", kwargs={"pk": pk}))

class UserProfileView(LoginRequiredMixin, DetailView):
    template_name = 'user_profile.html'
    context_object_name = 'userprofile'

    def get_object(self):
        user = User.objects.get(id=self.kwargs['pk'])
        userprofile = user.profile.first()
        return userprofile
