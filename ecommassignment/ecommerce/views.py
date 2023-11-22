from django.shortcuts import get_object_or_404, render,redirect
from .models import Categories, Products
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .forms import SignUpForm
from .forms import CheckoutForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            return redirect('ecommerce:login')
    else:
        form = SignUpForm()
    return render(request, 'ecommerce/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('ecommerce:product_all')  # Replace with the correct URL name
    else:
        form = AuthenticationForm()
    return render(request, 'ecommerce/login.html', {'form': form})
def product_all(request):
    products = Products.products.all()
    return render(request, 'ecommerce/home.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Categories, slug=category_slug)
    products = Products.objects.filter(category=category)
    return render(request, 'ecommerce/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug, in_stock=True)
    return render(request, 'ecommerce/products/single.html', {'product': product})

def checkout_view(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save order, update inventory, etc.)
            # You can access the form data using form.cleaned_data

            # Example: Get data from the form
            user = form.cleaned_data['user']
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']
            subtotal = form.cleaned_data['subtotal']

            # Add your logic here to process the order

            # Redirect to a thank you page or order summary
            return render(request, 'ecommerce/thank_you.html')
    else:
        # Initialize the form with initial data if needed
        form = CheckoutForm(initial={
            'user': request.user.username,  # Assuming user is logged in
            'product_id': 1,  # Example product ID
            'subtotal': 10.00  # Example subtotal
        })

    return render(request, 'ecommerce/checkout.html', {'form': form})