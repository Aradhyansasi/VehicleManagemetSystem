from django.urls import path
from superAdmin import views

urlpatterns=[
    path('sadmin',views.SuperAdminHomeView.as_view(),name='sadmin-home'),
    path('addreg',views.RegNumCreateView.as_view(),name='add-reg'),
    path('listreg',views.ListAllRegNums.as_view(),name='list-reg'),
    path('editreg/<int:id>',views.UpdateRegNumView.as_view(),name='edit-reg'),
    path('removereg/<int:id>',views.regnumDelete,name='remove-reg')
]