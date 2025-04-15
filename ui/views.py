from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm



# Create your views here.

def homepage(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories':categories, 'products':products})

def product_page(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_page.html', {'product': product})

def equipments(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            full_message = f"""
            You have a new contact request:

            Name: {name}
            Email: {email}
            Message: 
            {message}
            """

            send_mail(
                subject=f"New Contact Message from {name}",
                message=full_message,
                from_email=email,
                recipient_list=['amehlawal@gmail.com'],
                fail_silently=False,
            )

            return render(request, 'equipment.html', {'name': name})
    else:
        form = ContactForm()

    return render(request, 'equipment.html', {'categories':categories,'products':products, 'form': form})
    # return render(request, 'contact.html', {'form': form})
    # return render(request, 'equipment.html', {'categories':categories,'products':products})

def models(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'models.html', {'categories':categories, 'products':products})

# views.py


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            full_message = f"""
            You have a new contact request:

            Name: {name}
            Email: {email}
            Message: 
            {message}
            """

            send_mail(
                subject=f"New Contact Message from {name}",
                message=full_message,
                from_email=email,
                recipient_list=['yourgmail@gmail.com'],
                fail_silently=False,
            )

            return render(request, 'contact_success.html', {'name': name})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def search(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        products = Product.objects.filter(title__icontains=query)
        return render(request, 'search.html', {'query':query, 'products': products})
    else:
        return render(request, 'search.html', {})
    
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)

    return render(request, 'category_detail.html', {
        'category': category,
        'products': products
    })
