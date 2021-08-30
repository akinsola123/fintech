from django.urls import path

from . import views
# from .views import home

urlpatterns = [
    path('', views.home, name='home'),
    # path(Login', views.Login_page, name='Login'),
]