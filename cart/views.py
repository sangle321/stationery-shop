from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product, Color
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data

        color_id = request.POST.get("color")
        color = None
        if color_id:
            color = get_object_or_404(Color, id=color_id)

        cart.add(product=product, quantity=cd["quantity"], color=color, note=cd["note"])
    return redirect("cart:cart_detail")


def cart_remove(request, product_id, color_id="0"):
    cart = Cart(request)
    # We pass product_id and color_id to remove specific variant
    cart.remove(product_id, str(color_id))
    return redirect("cart:cart_detail")


def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart/detail.html", {"cart": cart})
