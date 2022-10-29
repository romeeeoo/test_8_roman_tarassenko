from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Login')
    password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput)
    # next = forms.CharField(required=False, widget=forms.HiddenInput)


class MyUserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Password", strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirm password", required=True, widget=forms.PasswordInput,
                                       strip=False)
    email = forms.EmailField(required=True, label="Email", widget=forms.EmailInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match!")
        if not cleaned_data.get("first_name") and not cleaned_data.get("last_name"):
            raise forms.ValidationError("Please feel last or first name")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', "email"]