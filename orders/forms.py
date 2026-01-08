from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["first_name", "last_name", "email", "phone", "address", "city"]
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Tên"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Họ"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Số điện thoại"}
            ),
            "address": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Địa chỉ"}
            ),
            "city": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Thành phố"}
            ),
        }
