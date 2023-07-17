from django.contrib import admin, messages
from django.core.exceptions import ValidationError

from order.forms import OrderForm
from order.models import Order
from order.services.order import order_update, order_save


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    form = OrderForm
    list_display = ('book', 'user', 'plated_end_at',)
    fields = ('book', 'user', 'created_at', 'end_at', 'plated_end_at',)
    readonly_fields = ('created_at',)
    autocomplete_fields = ('book', 'user',)

    def save_model(self, request, obj, form, change):
        try:
            cleaned_data = form.cleaned_data

            if change:
                order_update(
                    instance=obj,
                    **cleaned_data
                )
            else:
                order_save(obj)
        except ValidationError as exc:
            self.message_user(request, str(exc), messages.ERROR)
