from django.contrib import admin
from .models import Product, Provider

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "actual_stock", "provider", "created_at", "modified_at"]
    fields = ["name", "price", "actual_stock", "provider"]
    list_filter = ["provider", "created_at", "modified_at"]
    ordering = ["name", "price", "actual_stock", "provider", "created_at", "modified_at"]

class ProviderAdmin(admin.ModelAdmin):
    list_display = ["name", "lastname", "dni", "created_at", "modified_at"]
    fields = ["name", "lastname", "dni"]
    list_filter = ["dni", "created_at", "modified_at"]
    ordering = ["name", "lastname", "dni", "created_at", "modified_at"]

admin.site.register(Product, ProductAdmin)
admin.site.register(Provider, ProviderAdmin)