from django.shortcuts import render
from .models import Product

# retrieves the search term from the URL.

def product_list(request):
    query = request.GET.get('q')

# searches product names without considering uppercase or lowercase differences.

    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

# render() – sends the products to an HTML template for display.

    return render(request, 'products/product_list.html', {
        'products': products,
        'query': query
    })