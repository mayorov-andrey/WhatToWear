from django import forms
from .models import GuestBook


class GuestBookForm(forms.ModelForm):
    class Meta:
        model = GuestBook
        fields = '__all__'
    user = forms.CharField(max_length=20, label="Пользователь")
    content = forms.CharField(widget=forms.Textarea, label="Содержание")
    honeypot = forms.CharField(required=False, label="Ловушка для спамеров")
