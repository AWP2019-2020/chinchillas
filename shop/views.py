from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    View, TemplateView, CreateView,
    UpdateView, DeleteView, DetailView)

from shop.forms import ReviewForm
from shop.models import User, Product, Category, Review, ShoppingCart, UserProfile
from django.urls import reverse, reverse_lazy


def homepage(request):
    category_list = Category.objects.all();
    return render(request, 'index.html', {'category_list': category_list})


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    model = User

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(username=data['username'],
                                        password=data['password1'])
        UserProfile.objects.create(user=user)
        shopping_cart = ShoppingCart.objects.create(user=user, state=True)
        shopping_cart.save()
        return redirect('index')


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


def shoppingCart(request):
    shoppingCart = ShoppingCart.objects.filter(user=request.user, state=True)
    if len(shoppingCart):
        shoppingCart = shoppingCart.first()
        return render(request, "shoppingCart.html", {"shoppingCart": shoppingCart})
    return redirect(reverse('index'))


def deactivate_cart(request, pk):
    shoppingCart = ShoppingCart.objects.get(id=pk, state=True)
    shoppingCart.state = False
    shoppingCart.save()
    ShoppingCart.objects.create(user=request.user, state=True)
    return redirect(reverse("index"))


@login_required
def review_create(request, pk):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            product = Product.objects.get(id=pk)
            Review.objects.create(
                created_by=request.user,
                product=product,
                **form.cleaned_data
            )
            return redirect(reverse_lazy("product_detail", kwargs={"pk": pk}))
            # review_ = Review.objects.get(id=pk)
            # return render(request, "review__detail.html", {"review_": review_})


class ReviewEditView(LoginRequiredMixin, UpdateView):
    model = Review
    pk_url_kwarg = 'pk_review'
    template_name = 'review_update.html'
    form_class = ReviewForm

    def form_valid(self, form):
        review = Review.objects.get(pk=self.kwargs['pk_review'])
        review.text = form.cleaned_data['title']
        review.desc = form.cleaned_data['desc']
        review.rating = form.cleaned_data['rating']
        review.save()
        return redirect(reverse_lazy("product_detail", kwargs={"pk": self.kwargs['pk']}))


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "review_delete.html"
    model = Review
    pk_url_kwarg = 'pk_review'

    def get_success_url(self):
        return reverse_lazy("product_detail", kwargs={"pk": self.kwargs['pk']})


class UserProfileView(LoginRequiredMixin, DetailView):
    template_name = 'user_profile.html'
    context_object_name = 'userprofile'

    def get_object(self):
        user = User.objects.get(id=self.kwargs['pk'])
        userprofile = user.profile.first()
        return userprofile
