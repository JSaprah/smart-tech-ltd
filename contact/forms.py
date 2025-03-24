from django import forms
from .models import CustomerMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = CustomerMessage
        fields = ['name', 'email', 'subject', 'message']
