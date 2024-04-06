from django.contrib.auth import authenticate
import re
from django.contrib.auth.models import User
from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Tài khoản")
    email = forms.CharField(label="Email")
    password1 = forms.CharField(label="Mật khẩu", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Nhập lại Mật khẩu", widget=forms.PasswordInput())

    def clean_password2(self):
        if "password1" in self.cleaned_data:
            password1 = self.cleaned_data["password1"]
            password2 = self.cleaned_data["password2"]
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không khớp")

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not re.search(r"^\w+$", username):
            raise forms.ValidationError("Tên tài khoản không hợp lệ")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")

    def save(self):
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password1"]  # Trỏ trực tiếp đến password1
        User.objects.create_user(username=username, email=email, password=password)


from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Tài khoản")
    password = forms.CharField(label="Mật khẩu", widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Tài khoản hoặc mật khẩu không đúng")
