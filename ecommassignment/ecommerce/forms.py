from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    # You can customize the form fields here if needed
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CheckoutForm(forms.Form):
    user = forms.CharField(widget=forms.HiddenInput())
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(min_value=1)
    subtotal = forms.DecimalField(widget=forms.HiddenInput())