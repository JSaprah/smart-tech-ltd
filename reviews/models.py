from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_review')
    rating = models.PositiveIntegerField(
        null=False, blank=False, validators=[
            MinValueValidator(1), MaxValueValidator(5)])
    title = models.CharField(max_length=254, null=False, blank=False)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.author.username} for {self.product.name}'

    class Meta:
        ordering = ['-created_at']
