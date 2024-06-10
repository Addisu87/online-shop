from django import forms
from django.utils.translation import gettext_lazy as _

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    # Adding items to the cart
    # this allows the user to select a quantity between 1 and 20
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label=_('Quantity')
    )
   #  to indicate whether the quantity has to be added or not
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
