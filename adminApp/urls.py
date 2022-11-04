from django.urls import path
from adminApp import views

urlpatterns=[
    path('ahome',views.AdminHomeView.as_view(),name="admin-home"),
    path('alist',views.AdminAllRegNumView.as_view(),name='admin-list'),
    path('aupdate/<int:id>',views.AdminUpdateRegNumView.as_view(),name='admin-edit'),
]