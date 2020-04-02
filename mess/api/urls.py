from django.urls import path
from . import views

urlpatterns = [
   path('login',views.login),
   path('<username>/create',views.create), 
 #   path('register',views.UserCreateAPIView.as_view(),name='login'),
]