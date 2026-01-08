from django.shortcuts import render, get_object_or_404
from .models import Product


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, "products/detail.html", {"product": product})
