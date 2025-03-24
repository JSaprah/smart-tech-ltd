from django.contrib import admin
from .models import CustomerMessage

# Register your models here.

@admin.register(CustomerMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
