from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views

from api.views import ArticleViewSet, CreateUserView

## Router
router = routers.SimpleRouter()

## Urls
router.register(r'articles', ArticleViewSet)

## Urls Register
urlpatterns = router.urls
urlpatterns += [
    path('login/', views.obtain_auth_token),
    path('sign-up/', CreateUserView.as_view()),
]
