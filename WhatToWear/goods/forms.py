from django import forms
from .models import Good


class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = '__all__'