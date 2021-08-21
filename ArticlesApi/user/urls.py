from django.urls import path
from rest_framework.authtoken import views

from user.views import CreateUserView

## Urls Register
urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('sign-up/', CreateUserView.as_view()),
]
