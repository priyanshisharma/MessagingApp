from django.urls import path
from . import views

urlpatterns = [
   path('login',views.login),
   path('<username>/create',views.create), 
]