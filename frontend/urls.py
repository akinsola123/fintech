from django.urls import path

from . import views
# from .views import home

urlpatterns = [
    path('', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    # path(Login', views.Login_page, name='Login'),
]