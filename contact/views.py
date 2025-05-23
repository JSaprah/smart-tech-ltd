from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    """
    View to handle contact submissions
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent!")
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})
