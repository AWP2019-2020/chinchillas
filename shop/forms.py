from django import forms
from shop import models


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['title', 'desc', 'rating']
