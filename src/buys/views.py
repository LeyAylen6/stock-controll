from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Provider
from django.views.generic.edit import CreateView

# Home
def home(request):
    return render(request, 'home.html')

# Products
def get_products_list(request):
    products = Product.objects.all()
    return render(request, 'products/products_list.html', { 'products': products })

class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "price", "actual_stock", "provider"] # or '__all__'
    template_name = 'products/create_product.html'
    success_url = '/buys/products'

# Providers
def get_providers_list(request):
    providers = Provider.objects.all()
    return render(request, 'providers/providers_list.html', { 'providers': providers })


class ProviderCreateView(CreateView):
    model = Provider
    fields = ["name", "lastname", "dni"] # or '__all__'
    template_name = 'providers/create_provider.html'
    success_url = '/buys/providers'


