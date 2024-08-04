from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from accounts.models import User, OtpCode


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name')

    def clean_password2(self):
        cd = self.cleaned_data
        p1 = cd['password1']
        p2 = cd['password2']
        if p1 and p2 and p1 != p2:
            raise ValidationError('passwords must match')
        return cd['password2']

    def save(self, commit=True):  # پسورد را اول میگیره بعد هش می کنه و سیو می کنه
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserRegisterForm(forms.Form):
    email = forms.EmailField(label='ایمیل')
    phone_number = forms.CharField(max_length=11, label='شماره موبایل')
    full_name = forms.CharField(max_length=11, label='نام')
    password1 = forms.CharField(widget=forms.PasswordInput, label='پسورد')
    password2 = forms.CharField(widget=forms.PasswordInput, label='تایید پسورد')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('این ایمیل از قبل موجود می باشد')

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        if User.objects.filter(phone_number=phone).exists():
            raise ValidationError('این شماره موبایل از قبل موجود می باشد')
        OtpCode.objects.filter(phone_number=phone).delete()
        return phone

    def clean_password2(self):
        cd = self.cleaned_data
        p1 = cd['password1']
        p2 = cd['password2']
        if p1 and p2 and p1 != p2:
            raise ValidationError('باید هر دو رمز عبور یکسان باشد')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="you cant change password using <a href=\"../password/\">this form</a>.")

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name', 'password', 'last_login')


class UserLoginForm(forms.Form):
    phone_number = forms.CharField(label='شماره موبایل')
    password = forms.CharField(widget=forms.PasswordInput, label='پسورد')


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()