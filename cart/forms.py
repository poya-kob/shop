from django import forms


class UserNewOrderForm(forms.Form):
    product_id = forms.ImageField(
        widget=forms.HiddenInput(),
    )

    count = forms.ImageField(
        widget=forms.NumberInput(),
        initial=1
    )
