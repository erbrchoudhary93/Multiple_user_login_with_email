from email.policy import default
from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Permission ,PermissionsMixin
from .manager import CustomUserManager
from multiselectfield import MultiSelectField
from  django.db.models import Q



# class UserType(models.Model):
#     CUSTOMER = 1
#     SELLER = 2
#     TYPE_CHOICES = (
#         (SELLER,'seller'),
#         (CUSTOMER,'customer'),
#         )
#     id = models.PositiveSmallIntegerField(choices=TYPE_CHOICES,primary_key=True)
    
#     def __str__(self):
#         return self.get_id_display()

class Customuser(AbstractBaseUser,PermissionsMixin):
    # username=None
    email= models.EmailField(_('email address'),unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    # is_customer = models.BooleanField(default=True)
    # is_seller = models.BooleanField(default=False)
    
    # type = (
    #     (1,'seller'),
    #     (2,'customer'),
    #     )
    # user_type = models.IntegerField(choices=type,default=1)
    
    # user_type = models.ManyToManyField(UserType) 
    
    
    class Types(models.TextChoices):
        SELLER = "Seller","SELLER"
        CUSTOMER = "Customer","CUSTOMER"
        
    default_type = Types.CUSTOMER
    
    # type = models.CharField(_('Type'),max_length=255,choices=Types.choices , default=default_type)
    type = MultiSelectField(choices=Types.choices,default=[],null=True,blank=True)
    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= []
    
    objects=CustomUserManager()
    
    def __str__(self):
        return self.email
    
    # if not the code below then taking default value in User model not in proxy model
    def save(self ,*args,**kwargs):
        if not self.id:
            # self.type = self.default_type
            self.type.append(self.default_type)
            return super().save(*args,**kwargs)
    
    
class CustomerAddational(models.Model):
    user=models.OneToOneField(Customuser,on_delete=models.CASCADE)
    address = models.CharField(max_length=1000)
    def __str__(self):
        return self.user.email
    
class SellerAddational(models.Model):
    user=models.OneToOneField(Customuser,on_delete=models.CASCADE)
    gst = models.CharField(max_length=10)
    wherwhouse_location = models.CharField(max_length=1000)
    def __str__(self):
        return self.user.email



# Model manager for proxy model
class SellerManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        # return super().get_queryset(*args,**kwargs).filter(type=Customuser.Types.SELLER)
        return super().get_queryset(*args,**kwargs).filter(Q(type__contains=Customuser.Types.SELLER))
    
    
class CustomerManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        # return super().get_queryset(*args,**kwargs).filter(type=Customuser.Types.CUSTOMER)
        return super().get_queryset(*args,**kwargs).filter(Q(type__contains=Customuser.Types.CUSTOMER))
    
    
# Proxy Model . They do not crate a seprate table

class Seller(Customuser):
    default_type = Customuser.Types.SELLER
    objects= SellerManager()
    class Meta:
        proxy = True
    @property
    def showaddational(self):
        return self.selleraddational
        
        
class Customer(Customuser):
    default_type = Customuser.Types.CUSTOMER
    objects= CustomerManager()
    class Meta:
        proxy = True  
    property
    def showaddational(self):
        return self.customeraddational
        
    
    
