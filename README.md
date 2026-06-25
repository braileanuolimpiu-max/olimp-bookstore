# Olimp Books

A full-stack bookstore web application built with Django. Users can browse books, search by title, view book details, register an account, log in, and manage a shopping cart.

## Features

- Book catalogue with cover images, price, and stock status
- Search bar to filter books by title
- Book detail page with description and Add to Cart button
- Shopping cart with item quantities and total price (session-based)
- User registration and login / logout
- Admin panel to manage books
- Responsive design using Bootstrap 5

## Tech Stack

- Python 3.11
- Django 5.2
- SQLite
- Bootstrap 5
- Pillow (image handling)

## How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/braileanuolimpiu-max/olimp-bookstore.git
cd olimp-bookstore

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create an admin account
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser.

To add books, go to http://127.0.0.1:8000/admin/ and log in with the superuser account.
