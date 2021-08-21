from api.models import Article, Author
from api.serializers import AuthenticatedArticleSerializer, AuthorSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class AdminArticleViewSet(viewsets.ModelViewSet):
    """ List/Retrieve view. Response Data can change depending on user authentication status"""
    queryset = Article.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AuthenticatedArticleSerializer
    filterset_fields  = ["title", "category"]
    search_fields = ["title", "category", "summary", "author__name"]


class AdminAuthorViewSet(viewsets.ModelViewSet):
    """ List/Retrieve view. Response Data can change depending on user authentication status"""
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AuthorSerializer
    search_fields = ["name", ]
