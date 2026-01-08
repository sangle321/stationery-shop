from decimal import Decimal
from django.conf import settings
from products.models import Product


class Cart:
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, color=None, note=""):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        # Create a unique key for the item based on product and color
        color_id = str(color.id) if color else "0"
        item_id = f"{product_id}_{color_id}"

        if item_id not in self.cart:
            self.cart[item_id] = {
                "quantity": 0,
                "price": str(product.price),
                "color_id": color.id if color else None,
                "color_name": color.name if color else None,
                "note": str(note),  # Store note
                "product_id": product.id,
            }

        # Determine if we are adding or overriding (simple addition for now)
        self.cart[item_id]["quantity"] += quantity
        # Update note if provided
        if note:
            self.cart[item_id]["note"] = str(note)

        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product_id, color_id="0"):
        """
        Remove a product from the cart.
        """
        item_id = f"{product_id}_{color_id}"
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database.
        """
        product_ids = [item["product_id"] for item in self.cart.values()]
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        # We need to map product objects back to cart items efficiently
        # Since multiple items might reference the same product (different colors),
        # we can't just loop through products.

        product_map = {p.id: p for p in products}

        for item_key, item in cart.items():
            product = product_map.get(item["product_id"])
            if product:
                item["product"] = product
                item["price"] = Decimal(item["price"])
                item["total_price"] = item["price"] * item["quantity"]
                item["item_id"] = item_key  # Useful for remove links
                yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
        )
