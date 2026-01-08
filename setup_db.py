import os
import django
from django.core.management import execute_from_command_line

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myshop.settings")
django.setup()


def setup():
    print("Running migrations...")
    try:
        execute_from_command_line(["manage.py", "makemigrations", "products"])
        execute_from_command_line(["manage.py", "migrate"])
    except Exception as e:
        print(f"Migration failed: {e}")
        return

    print("Creating categories...")
    from products.models import Category

    categories = ["Bút viết", "Sổ tay", "Bìa hồ sơ", "Khác"]
    for name in categories:
        from django.utils.text import slugify

        # slugify might not handle unicode well by default without allow_unicode=True,
        # but for simplicity we will just map them or use a safer slugify if needed.
        # Django's slugify removes non-ascii.
        # Let's simple create a robust slug.
        slug_map = {
            "Bút viết": "but-viet",
            "Sổ tay": "so-tay",
            "Bìa hồ sơ": "bia-ho-so",
            "Khác": "khac",
        }
        slug = slug_map.get(name, "other")

        Category.objects.get_or_create(name=name, defaults={"slug": slug})
        print(f"Category {name} created.")


if __name__ == "__main__":
    setup()
