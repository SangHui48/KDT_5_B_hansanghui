from django import forms
from .models import Coffee

class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ("name", "price", "is_ice")
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': '상품명',
            'price': '가격',
        }