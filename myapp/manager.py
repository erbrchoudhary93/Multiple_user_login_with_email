from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier 
    for authentication insted of usernsme
    """
    def create_user(self,email,password,**extra_fields):
        """
        Create and save a user with the given email and password .
        """
        if not email:
            raise ValueError(_('Email must be set'))
        email= self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        """
        Create and save Superuser with the given email and password .
        """
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        if extra_fields.get('is_staff',True) is not True:
            raise ValueError(_("Super user must have is_staff = True"))
        if extra_fields.get('is_superuser',True) is not True:
            raise ValueError(_("Super user must have is_superuser = True"))
        return self.create_user(email,password,**extra_fields)