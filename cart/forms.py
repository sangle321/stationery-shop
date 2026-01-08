from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "style": "width: 70px"}
        ),
    )
    note = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Ghi chú (tùy chọn)...",
            }
        ),
    )
    # Color will be handled dynamically in the view or using ModelChoiceField if strict validation is needed
    # For now, let's keep it simple and handle color ID from request.POST manual handling or add it here
