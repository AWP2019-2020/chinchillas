from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.urls import reverse_lazy

from shop.forms import ReviewForm
from shop.models import Product, Category, Review


def index(request):
    return HttpResponse("MAINPAGE")


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product_detail.html", {"product": product})


def category_detail(request, pk):
    category = Category.objects.get(id=pk)
    return render(request, "category_detail.html", {"category": category})


def review_detail(request, pk):
    review_ = Review.objects.get(id=pk)
    return render(request, "review__detail.html", {"review_": review_})


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
