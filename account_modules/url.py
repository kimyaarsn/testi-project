from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('active-account/<str:code>', views.ActivateAccountView.as_view(), name='active-account'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('forgot-password/', views.ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/<str:code>', views.ResetPasswordView.as_view(), name='reset-password'),
]