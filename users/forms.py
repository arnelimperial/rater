from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput)
    first_name = forms.CharField(required=True, widget=forms.TextInput)
    last_name = forms.CharField(required=True, widget=forms.TextInput)
    password1 = forms.CharField(required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class SignUpChangeForm(UserChangeForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput)
    first_name = forms.CharField(required=True, widget=forms.TextInput)
    last_name = forms.CharField(required=True, widget=forms.TextInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)
