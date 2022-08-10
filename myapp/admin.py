from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customuser ,Customer ,Seller,SellerAddational,CustomerAddational
from .forms import CustomUserChangeForm ,CustomUserCreationForm
from django.contrib.auth.models import User



class SellerAddationalInline(admin.TabularInline):
    model = SellerAddational

class CustomUserAdmin(UserAdmin):
    model= Customuser
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    list_display = ('email','name','type','is_staff','is_active',)
    list_filter = ('email','is_staff','is_active',)
    
    fieldsets = (
        (None,{'fields':('email','name','type')}),
        # (None,{'fields':('email','password','user_type')}),
        ('Permissions',{'fields':('is_staff',('is_active','is_superuser',))}),
        ('Important Dates',{'fields':('last_login','date_joined')}),
        ('Advanced Options',{
            'classes':('collapse',),
            'fields':('groups','user_permissions')}),
        )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','name','password1','password2','is_staff','is_active'),
            }),
        )
    search_fields = ('email','name')
    ordering = ('email','name')
    
    
    
class SellerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{'fields':('email','name','type')}),
    )
        
    inlines = (
        SellerAddationalInline,
        )
    
    
# admin.site.unregister(User)    
admin.site.register(Customuser,CustomUserAdmin)
# admin.site.register(User,UserAdmin)
# admin.site.register(Customuser)
# admin.site.register(Seller)
# admin.site.register(Seller)
admin.site.register(Seller,SellerAdmin)
admin.site.register(SellerAddational)
admin.site.register(Customer)
admin.site.register(CustomerAddational)
# admin.site.register(UserType)




