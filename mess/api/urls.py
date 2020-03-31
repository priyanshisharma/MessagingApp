from django.urls import path
from . import views

urlpatterns = [
   path('login',views.login),
   path('<slug:username>/create',views.create),  
]