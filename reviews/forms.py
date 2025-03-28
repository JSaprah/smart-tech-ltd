from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'title', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'title': 'Summarize your review in one line.',
            'content': 'Share more details about your experience.',
            'rating': 'Provide a rating (1 to 5 stars).',
        }

        self.fields['rating'].widget.attrs['min'] = 1
        self.fields['rating'].widget.attrs['max'] = 5

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs[
                'aria-label'] = placeholder
            self.fields[field].label = False
