from django.contrib import admin
from .models import Category, Product, Brand, Size, ProductBrand

# Inline model for adding sizes directly in the ProductBrand admin
class SizeInline(admin.TabularInline):
    model = ProductBrand.sizes.through

# ProductBrand admin configuration
class ProductBrandAdmin(admin.ModelAdmin):
    inlines = [SizeInline]
    list_display = ['product', 'brand']

# Register models with the admin site
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(ProductBrand, ProductBrandAdmin)

