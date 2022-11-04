from django.urls import path
from vehicleApp import views

urlpatterns=[
    path('signup',views.SignUpView.as_view(), name='signup'),
    path('login',views.SigninView.as_view(), name='login'),
    path('signout',views.signout,name='signout'),
]