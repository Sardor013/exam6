from django.db import models


class CategoryProduct(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class PriceType(models.TextChoices):
    s = '$', 'USD'
    som = "So'm", "UZS"


class Products(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.TextField()
    product_category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='app_fruits/products')
    product_price = models.FloatField(max_length=50, choices=PriceType.choices)

    def __str__(self):
        return self.product_name


