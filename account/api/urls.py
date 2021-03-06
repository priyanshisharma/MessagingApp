from django.urls import path
from account.api.views import(
	registration_view,
	ObtainAuthTokenView,
)

urlpatterns = [
	path('login', ObtainAuthTokenView.as_view(), name="login"),
	path('register', registration_view, name="register"),
]
