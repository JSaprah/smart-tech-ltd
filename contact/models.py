from django.db import models

# Create your models here.


class CustomerMessage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(null=False, blank=False, max_length=50)
    email = models.EmailField(null=False, blank=False, max_length=254)
    subject = models.CharField(max_length=254)
    message = models.TextField(null=False, blank=False,)

    def __str__(self):
        return f" message from {self.email}"
