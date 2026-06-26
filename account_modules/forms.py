from django import forms
from django.contrib.auth import authenticate
from .models import User


class SignupForm(forms.Form):
    username = forms.CharField(max_length=30, error_messages={
        'required': 'وارد کردن نام کاربری الزامی است',
        'max_length': 'نام کاربری نمی‌تواند بیشتر از ۳۰ کاراکتر باشد'
    })
    email = forms.EmailField(error_messages={
        'required':'وارد کردن ایمیل الزامی است',
        'invalid':'ایمیل وارد شده معتبر نیست'
    })
    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
        'required':'رمز عبور الزامی است'
    })

    def clean_email(self):
        email = self.cleaned_data.get('email')

        print('EMAIL =', email)
        print(
            User.objects.filter(
                email__iexact=email
            ).values('id', 'email')
        )

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'این ایمیل قبلا ثبت شده است'
            )

        return email

class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={
        'required': 'وارد کردن ایمیل الزامی است',
        'invalid': 'ایمیل وارد شده معتبر نیست'
    })
    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
        'required': 'رمز عبور الزامی است'
    })

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if not email or not password:
            return cleaned_data

        user = User.objects.filter(email__iexact=email).first()
        if not user:
            raise forms.ValidationError('کاربری بااین ایمیل وجود ندارد')

        user = authenticate(username=user.username, password=password)

        if user is None:
            raise forms.ValidationError('ایمیل یا رمز عبور اشتباه است')

        self.user = user
        return cleaned_data

class EmailForgotPasswordForm(forms.Form):
    email = forms.EmailField(error_messages={
        'required': 'وارد کردن ایمیل الزامی است',
        'invalid': 'ایمیل وارد شده معتبر نیست'
    })


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'رمز عبور الزامی است'
        }
    )



