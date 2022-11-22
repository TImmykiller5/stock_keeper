from django import forms
from .models import Stock


class CreateItem(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ['name', 'quantity', 'PurchasePrice', 'SellingPrice']
