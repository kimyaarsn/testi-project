from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('about/', views.HomeAboutView.as_view(), name='about'),

]


