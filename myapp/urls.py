
from django.urls import path 
from . import views

urlpatterns = [
    
    path('',views.Index.as_view(),name='index'),
 
    path('signup/',views.RegisterView.as_view(),name='signup'),
    path('signupseller/',views.RegisterViewSeller.as_view(),name='signupseller'),
    path('login/',views.LoginViewUser.as_view(),name='login'),
    path('logout/',views.LogoutViewUser.as_view(),name='logout'),
    # path('signupseller/',views.RegisterViewSeller.as_view(),name='signupseller'),
   
]