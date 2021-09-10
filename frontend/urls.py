from django.urls import path

from . import views
# from .views import home

urlpatterns = [
    path('', views.home, name='home'),
    # path('welcome/', views.welcome, name='welcome'),
    # path('payment', views.payment, name = 'payment'),
    path('payments', views.PaymentsView.as_view() ,name = 'payments'),
    # path(Login', views.Login_page, name='Login'),

    path('success', views.success, name = 'success'),
]