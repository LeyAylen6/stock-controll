from django.urls import path
from .views import home, ProductCreateView, get_products_list, ProviderCreateView, get_providers_list

app_name = 'buys'

urlpatterns = [
    path('', home, name='home'),

    path('products/', get_products_list, name='products_list'),
    path('products/new/', ProductCreateView.as_view(), name='post_product'),

    path('providers/', get_providers_list, name='providers_list'),
    path('providers/new/', ProviderCreateView.as_view(), name='post_provider')
]

