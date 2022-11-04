from django.urls import path
from userApp import views

urlpatterns=[
    path('uhome',views.UserHomeView.as_view(),name='u-home'),
    path('listreg',views.AllRegNumView.as_view(),name='list-regnum'),
]