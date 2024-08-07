import random
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from Utils import send_otp_code
from accounts.forms import UserRegisterForm, VerifyCodeForm, UserLoginForm
from accounts.models import OtpCode, User


# Create your views here.
class RegisterUserView(View):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['phone_number'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone_number'], code=random_code)
            request.session['user_registration_info'] = {
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'phone_number': form.cleaned_data['phone_number'],
                'password1': form.cleaned_data['password1']
            }
            messages.success(request, 'کد تایید یه را به شماره موبایل شماارسال کردیم', 'success')
            return redirect('accounts:verify')
        return render(request, self.template_name, {'forms': form})


class VerifyUserView(View):
    form_class = VerifyCodeForm
    template_name = 'accounts/verify.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            if form.cleaned_data['code'] == code_instance.code:
                print(user_session)
                User.objects.create_user(user_session['email'], user_session['full_name'], user_session['phone_number'],
                                         user_session['password1'])
                messages.success(request, 'شما با موفقیت ثبت نام کردید', 'success')
                return redirect('shop:home')
            else:
                messages.error(request, 'کد وارد شده صحیح نمی باشد', 'danger')
                return redirect('accounts:verify')
            return render(request, self.template_name, {'form': form})


class LoginUserView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('shop:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, phone_number=cd['phone_number'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'شما با موفقیت وارد شدید', 'success')
                return redirect('shop:home')
            messages.error(request, 'اطلاعات وارد شده صحیح نمی باشد', 'danger')
            return render(request, self.template_name, {'form': form})


class LogoutUserView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, 'شما با موفقیت خارج شدید', 'info')
        return redirect('shop:home')