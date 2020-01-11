from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from shop.models import Product


def index(request):
    return HttpResponse("MAINPAGE")


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product_detail.html", {"product": product})
