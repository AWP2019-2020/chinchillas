from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
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
