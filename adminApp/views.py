from django.shortcuts import render,redirect
from django.views.generic import TemplateView,UpdateView,ListView
from superAdmin.models import Details
from superAdmin.forms import VehicleRegistrationForm
from django.urls import reverse_lazy
from vehicleApp.decorators import signin_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(signin_required,name='dispatch')
class AdminHomeView(TemplateView):
    template_name = 'admin-home.html'

@method_decorator(signin_required,name='dispatch')
class AdminAllRegNumView(ListView):
    model = Details
    template_name = 'adminReg-list.html'
    context_object_name = 'regnums'
    ordering = ['-id']
    paginate_by = 2

@method_decorator(signin_required,name='dispatch')
class AdminUpdateRegNumView(UpdateView):
    model = Details
    form_class = VehicleRegistrationForm
    template_name = 'adminEdit_reg.html'
    success_url = reverse_lazy('admin-list')
    pk_url_kwarg = 'id'
