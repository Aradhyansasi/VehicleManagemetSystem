from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView
from superAdmin.models import Details
from superAdmin.forms import VehicleRegistrationForm
from django.urls import reverse_lazy
from django.contrib import messages
from vehicleApp.decorators import signin_required
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(signin_required,name='dispatch')
class SuperAdminHomeView(TemplateView):
    template_name = 'superAdminHome.html'

@method_decorator(signin_required,name='dispatch')
class RegNumCreateView(CreateView):
    model = Details
    form_class = VehicleRegistrationForm
    template_name = 'add_regNum.html'
    success_url = reverse_lazy('list-reg')

    def form_valid(self, form):
        messages.success(self.request, 'Job has been posted successfully')
        return super().form_valid(form)

@method_decorator(signin_required,name='dispatch')
class ListAllRegNums(ListView):
    model = Details
    context_object_name = 'regnums'
    template_name = 'RegNumList.html'
    ordering = ['-id']
    paginate_by = 3

@method_decorator(signin_required,name='dispatch')
class UpdateRegNumView(UpdateView):
    print("in update method")
    model = Details
    form_class = VehicleRegistrationForm
    template_name = 'edit_regNum.html'
    success_url = reverse_lazy('list-reg')
    pk_url_kwarg = 'id'

@method_decorator(signin_required,name='dispatch')
def regnumDelete(request, *args, **kwargs):
    id = kwargs.get('id')
    Details.objects.get(id=id).delete()
    return redirect('list-reg')
