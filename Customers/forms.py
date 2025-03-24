from django import forms
from django.core.validators import RegexValidator
from .models import CustomUser, CustomerProfile

# Registration Form
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = CustomUser
        fields = ['email', 'phone_no']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email','class':'form-control'}),
            'phone_no': forms.TextInput(attrs={'placeholder': 'Phone Number','class':'form-control'}),
        }

    def clean_phone_no(self):
        phone_no = self.cleaned_data.get('phone_no')
        phone_regex = RegexValidator(regex=r'^[6-9]\d{9}$', message="Invalid phone number.")
        phone_regex(phone_no)
        return phone_no

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data

# Customer Profile Form
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['customer_name', 'address', 'pincode', 'designation', 'department']
        widgets = {
            'customer_name': forms.TextInput(attrs={'placeholder': 'Customer Name','class':'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address','class':'form-control'}),
            'pincode': forms.TextInput(attrs={'placeholder': 'Pincode','class':'form-control'}),
            'designation': forms.TextInput(attrs={'placeholder': 'Designation','class':'form-control'}),
            'department': forms.TextInput(attrs={'placeholder': 'Department','class':'form-control'}),
        }

# Login Form
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email or Phone Number'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        # Optionally add authenticate here
        return cleaned_data
