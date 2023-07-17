from django import forms

from order.models import Order
from order.services.order import validate_data


class OrderForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        validate_data(
            user=cleaned_data.get('user'),
            created_at=cleaned_data.get('created_at'),
            end_at=cleaned_data.get('end_at'),
            plated_end_at=cleaned_data.get('plated_end_at')
        )
        return self.cleaned_data

    class Meta:
        model = Order
        fields = '__all__'
