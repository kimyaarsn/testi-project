from django.shortcuts import render , redirect
from .forms import SignupForm,LoginForm,EmailForgotPasswordForm,ResetPasswordForm
from django.urls import reverse
from . models import User
from django.views import View
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.http import Http404 , HttpRequest
from django.contrib.auth import login , logout
from services.email_services import send_activation_email ,send_reset_password_email
import random
# Create your views here.

class SignupView(View):
      def get(self,request):
          signup_form = SignupForm()
          context = {'signup_form':signup_form}
          return render(request , 'account_modules/signup.html' , context)
      def post(self,request):
          signup_form = SignupForm(request.POST)
          context = {'signup_form':signup_form}

          if signup_form.is_valid():
              username = signup_form.cleaned_data.get('username')
              email = signup_form.cleaned_data.get('email')
              password = signup_form.cleaned_data.get('password')

              new_user = User.objects.create_user(username=username,email=email,password=password,is_active=False)

              new_user.email_active_code = get_random_string(20)
              new_user.email_active_code_created_date = timezone.now()
              new_user.save()

              send_activation_email(new_user)
              messages.success(request,'لینک فعالسازی به ایمیل شما ارسال شد.')
              return redirect('signup')
          return render(request , 'account_modules/signup.html' , context)

class ActivateAccountView(View):

    def get(self, request, code):

        user = User.objects.filter(
            email_active_code=code,
            is_active=False
        ).first()

        if user is None:
            return redirect('signup')

        expire_time = (
            user.email_active_code_created_date +
            timedelta(minutes=5)
        )

        if timezone.now() > expire_time:

            user.email_active_code = None
            user.email_active_code_created_date = None
            user.save()

            messages.error(
                request,
                'لینک فعال‌سازی منقضی شده است. دوباره ثبت‌نام کنید.'
            )

            return redirect('signup')

        user.is_active = True
        user.email_active_code = None
        user.email_active_code_created_date = None
        user.save()

        login(request, user)

        messages.success(
            request,
            f'خوش آمدید {user.username}، حساب کاربری شما با موفقیت فعال شد.'
        )

        return redirect('index')



class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')

        login_form = LoginForm()
        context = {'login_form': login_form}
        return render(request, 'account_modules/login.html', context)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('index')

        login_form = LoginForm(request.POST)
        context = {'login_form': login_form}

        if login_form.is_valid():
            login(request, login_form.user)

            messages.success(
                request,
                f'خوش آمدید {login_form.user.username}، با موفقیت وارد حساب کاربری خود شدید.'
            )

            return redirect('index')

        return render(request, 'account_modules/login.html', context)
class ForgotPasswordView(View):
    def get(self, request):
        forgot_password_form = EmailForgotPasswordForm()
        context = {'forgot_password_form': forgot_password_form}
        return render(request,'account_modules/email_forgot_password.html',context)
    def post(self, request):
        forgot_password_form = EmailForgotPasswordForm(request.POST)
        if forgot_password_form.is_valid():
            email = forgot_password_form.cleaned_data.get('email')
            user = User.objects.filter(email__iexact=email).first()
            if user is None:
                forgot_password_form.add_error('email','کاربری با این ایمیل یافت نشد')
            else:
                user.password_reset_code = get_random_string(20)
                user.password_reset_code_created_date = (timezone.now())
                user.save()
                send_reset_password_email(user)
                messages.success(request,'لینک بازیابی رمز عبور به ایمیل شما ارسال شد.')
                return redirect('forgot-password')
        context = {'forgot_password_form': forgot_password_form}
        return render(request,'account_modules/email_forgot_password.html',context)


class ResetPasswordView(View):
    def get(self, request, code):
        user = User.objects.filter(password_reset_code=code).first()
        if user is None:
            messages.error(request,'لینک بازیابی معتبر نیست.')
            return redirect('forgot-password')
        if user.password_reset_code_created_date is None:
            messages.error(request, 'لینک بازیابی معتبر نیست.')
            return redirect('forgot-password')
        expire_time = (user.password_reset_code_created_date +timedelta(minutes=5))

        if timezone.now() > expire_time:

            user.password_reset_code = None
            user.password_reset_code_created_date = None
            user.save()

            messages.error(request,'لینک بازیابی رمز عبور منقضی شده است.')
            return redirect('forgot-password')
        reset_form = ResetPasswordForm()
        context = {'reset_form': reset_form,'code': code}
        return render(request,'account_modules/reset_password.html',context)

    def post(self, request, code):
        reset_form = ResetPasswordForm(request.POST)
        user = User.objects.filter(password_reset_code=code).first()
        if user is None:
            messages.error(request,'لینک بازیابی معتبر نیست.')
            return redirect('forgot-password')
        if user.password_reset_code_created_date is None:
            messages.error(request, 'لینک بازیابی معتبر نیست.')
            return redirect('forgot-password')
        expire_time = (
            user.password_reset_code_created_date +timedelta(minutes=5))

        if timezone.now() > expire_time:

            user.password_reset_code = None
            user.password_reset_code_created_date = None
            user.save()

            messages.error(request,'لینک بازیابی رمز عبور منقضی شده است.')
            return redirect('forgot-password')
        if reset_form.is_valid():
            password = reset_form.cleaned_data.get('password')
            user.set_password(password)

            user.password_reset_code = None
            user.password_reset_code_created_date = None
            user.save()
            login(request, user)
            messages.success(request,'رمز عبور با موفقیت تغییر کرد.')
            return redirect('index')
        context = {'reset_form': reset_form,'code': code}

        return render(request,'account_modules/reset_password.html',context)

class LogoutView(View):
    def get(self, request):
        messages.success(request, 'با موفقیت از حساب کاربری خود خارج شدید.')
        logout(request)
        return redirect('index')