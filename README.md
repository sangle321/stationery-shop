# VPP BEES25 - Stationery Shop

A modern e-commerce website for stationery products built with Django.

## Features
- **Product Catalog:** Browse products by category.
- **Shopping Cart:** Add products to cart with custom notes.
- **Checkout Flow:** Simple checkout process with Cash on Delivery (COD).
- **Responsive Design:** Optimized for both desktop and mobile devices.
- **Visuals:** Modern UI with glassmorphism header and vibrant design.

## Tech Stack
- **Backend:** Django 5.0
- **Frontend:** HTML5, Vanilla CSS, FontAwesome 6
- **Database:** SQLite (Default)

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Shop
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/macOS
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize Database:**
   The project includes a setup script that runs migrations and creates initial categories.
   ```bash
   python setup_db.py
   ```

5. **Run Development Server:**
   ```bash
   python manage.py runserver
   ```

6. **Usage:**
   - Homepage: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Admin Panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) (Requires creating a superuser via `python manage.py createsuperuser`)

## License
MIT
