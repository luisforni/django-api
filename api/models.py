from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    grade = models.DecimalField(max_digits=3, decimal_places=1)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
