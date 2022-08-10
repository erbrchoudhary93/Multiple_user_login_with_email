from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import Customuser, Seller,SellerAddational

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=Customuser
        fields = ('email',)
        
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model= Customuser
        fields = ('email',)
        
        
class RegistrationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = Customuser
        fields = ['email','name','password1','password2']
       
# class RegistrationFormSeller(UserCreationForm):
#     gst = forms.CharField(max_length=10)
#     wherwhouse_location = forms.CharField(max_length=1000)
#     class Meta(UserCreationForm):
#         model = Seller
#         fields = ['email','name','password1','password2','gst','wherwhouse_location']
       
       
class RegistractionFormSeller2(forms.ModelForm):
    class Meta:
        model = SellerAddational
        fields = ['gst','wherwhouse_location']