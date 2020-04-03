from django.urls import path
from . import views

urlpatterns = [
  # path('login',views.login),
   path('<username>/create',views.create), 
   path('<int:pk>/delete',views.delete),
   path('<int:pk>/detail',views.message_detail),
   path('<username>/list',views.list),
 #   path('register',views.UserCreateAPIView.as_view(),name='login'),
]