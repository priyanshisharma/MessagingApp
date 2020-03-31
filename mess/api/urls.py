from django.urls import path
from mess.api.views import views

urlpatterns = [
   path('<slug:username>/list',views.list),
   path('<slug:username>/create',views.create),
   
]