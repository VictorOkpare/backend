from django.db import models

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, )

    def __str__(self):
        return self.name

# Brand Model
class Brand(models.Model):
    brandname = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.brandname

# Size Model
class Size(models.Model):
    sizename = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.sizename} - {self.quantity}"

# Product Model
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', default=1 )
    colour = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/', default='default_image.jpg')
    brands = models.ManyToManyField(Brand, related_name='products', through='ProductBrand')

    def __str__(self):
        return f"{self.title} - {self.colour}"

# Intermediate Model to link Products, Brands, and Sizes
class ProductBrand(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    sizes = models.ManyToManyField(Size, related_name='product_brands')

    def __str__(self):
        return f"{self.product.title} - {self.brand.brandname}"
