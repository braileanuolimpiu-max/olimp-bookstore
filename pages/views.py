from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def homepage(request):
    query = request.GET.get('q', '')
    if query:
        books = Book.objects.filter(title__contains=query)
    else:
        books = Book.objects.all()
    context = {
        "name": "Olimp",
        "city": "Chisinau",
        "books": books,
        "licence": True,
    }
    return render(request, "pages/home.html", context)
def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        print(f"Message from {name}: {message}")
        messages.success(request, f"Thanks {name}! We received your message.")
    context = {
        "title": "About Olimp Books",
        "description": "Your favourite bookstore in Chisinau.",
    }
    return render(request, "pages/about.html", context)
@login_required
def book_detail(request, pk):
      book = get_object_or_404(Book, pk=pk)
      return render(request, 'pages/book_detail.html', {'book': book})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
def add_to_cart(request, pk):
    book = get_object_or_404(Book, pk=pk)
    cart = request.session.get('cart', {})
    pk_str = str(pk)
    if pk_str in cart:
        cart[pk_str] += 1
    else:
        cart[pk_str] = 1
    request.session['cart'] = cart
    request.session.modified = True
    messages.success(request, f'"{book.title}" added to cart!')
    return redirect(f'/books/{pk}/')

def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    pk_str = str(pk)
    if pk_str in cart:
        del cart[pk_str]
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('/cart/')
def cart(request):
    cart = request.session.get('cart', {})
    books = []
    total = 0
    for pk_str, quantity in cart.items():
        book = get_object_or_404(Book, pk=int(pk_str))
        books.append({'book': book, 'quantity': quantity})
        total += book.price * quantity
    return render(request, 'pages/cart.html', {'books': books, 'total': total})