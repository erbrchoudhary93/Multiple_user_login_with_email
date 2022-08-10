from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from myapp.models import Customuser,SellerAddational
from . forms import RegistrationForm ,RegistractionFormSeller2
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView ,LogoutView


# Create your views here

class Index(CreateView):
    template_name = 'myapp/index.html'
    model=Customuser
    fields = '__all__'
    success_url = reverse_lazy('index')
    
    
    
    
    
class RegisterView(CreateView):
    template_name = 'myapp/registerbasicuser.html'
    form_class =RegistrationForm
    success_url = reverse_lazy('index')
    
    
class LoginViewUser(LoginView):
    template_name = 'myapp/login.html'
    
    
    
    
class RegisterViewSeller(LoginRequiredMixin,CreateView):
    template_name = 'myapp/registerseller.html'
    form_class =RegistractionFormSeller2
    success_url = reverse_lazy('index')
    
    
    def form_valid(self,form):
        user= self.request.user
        user.type.append(user.Types.SELLER)
        user.save()
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class LogoutViewUser(LogoutView):
    success_url = reverse_lazy('index')
        
    
        
        
# class RegisterViewSEller(CreateView):
#     template_name = 'myapp/register.html'
#     form_class =RegistrationFormSeller
#     success_url = reverse_lazy('index')
    
    
#     def post(self,request,*args,**kwargs):
#         response = super().post(request,*args,**kwargs)
#         if response.status_code == 302:
#             gst = request.POST.get(gst)
#             wherwhouse_location = request.POST.get(wherwhouse_location)
#             user= Customuser.objects.get(email=request.POST.get('email'))
#             s_add= SellerAddational.objects.create(user=user,gst=gst,wherwhouse_location=wherwhouse_location)
#             return response
#         else:
#             return response
    
    
