from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('enter_code', views.enter_code, name='enter_code'),
    path('redeem_code', views.redeem_code, name='redeem_code'),
]