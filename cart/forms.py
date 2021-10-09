from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int)

    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)


# class UserNewOrderForm(forms.Form):
#     product_id = forms.ImageField(
#         widget=forms.HiddenInput(),
#     )
#
#     count = forms.ImageField(
#         widget=forms.NumberInput(),
#         initial=1
#     )
