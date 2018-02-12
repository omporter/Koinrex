from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('home/', views.home, name="home"),
    path('withdrawals/', views.withdrawals, name="withdrawals"),
    path('deposits/', views.deposits, name="deposits"),
    path("withdrawals/success", views.withdrawals_success, name="withdrawals_success"),
	]