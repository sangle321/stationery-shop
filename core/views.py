from django.shortcuts import render
from products.models import Product, Category


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    cat_slug = request.GET.get("category")
    if cat_slug:
        products = products.filter(category__slug=cat_slug)

    query = request.GET.get("q")
    if query:
        from django.db.models import Q

        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    context = {
        "products": products,
        "categories": categories,
    }
    return render(request, "home.html", context)
