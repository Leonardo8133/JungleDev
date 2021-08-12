from django.shortcuts import render
from rest_framework import viewsets
from api.models import Article, User
from api.serializers import NotAuthenticatedArticleSerializer, AuthenticatedArticleSerializer, CreateUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView

class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """ List/Retrieve view. """
    queryset = Article.objects.all()
    serializer_class = NotAuthenticatedArticleSerializer
    filterset_fields  = ["title", "category"]
    search_fields = ["title", "category", "summary"]

    def get_serializer_class(self):
        if self.action == "retrieve" and self.request.user.is_authenticated:
            return AuthenticatedArticleSerializer
        return self.serializer_class
