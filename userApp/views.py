from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from superAdmin.models import Details
from vehicleApp.decorators import signin_required
from django.utils.decorators import method_decorator
# Create your views here.


@method_decorator(signin_required,name='dispatch')
class UserHomeView(TemplateView):
    template_name = 'user-home.html'


@method_decorator(signin_required,name='dispatch')
class AllRegNumView(ListView):
    model = Details
    template_name = 'reg-list.html'
    context_object_name = 'regnums'
    ordering = ['-id']
    paginate_by = 2