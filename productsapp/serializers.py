from rest_framework import serializers
from .models import Category, Brand, Size, Product, ProductBrand

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# Size Serializer
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['sizename', 'quantity']

# Brand Serializer
class BrandSerializer(serializers.ModelSerializer):
    size = SizeSerializer(many=True, source='productbrand_set', read_only=True)  # Nested serializer to include sizes

    class Meta:
        model = Brand
        fields = ['brandname', 'price', 'size']

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    brands = BrandSerializer(many=True, source='productbrand_set', read_only=True)  # Nested serializer to include brands

    class Meta:
        model = Product
        fields = ['id', 'colour', 'title', 'image', 'brands']

# ProductBrand Serializer (Optional)
# This is useful if you want to explicitly manage the ProductBrand relationships.
class ProductBrandSerializer(serializers.ModelSerializer):
    sizes = SizeSerializer(many=True)

    class Meta:
        model = ProductBrand
        fields = ['product', 'brand', 'sizes']
