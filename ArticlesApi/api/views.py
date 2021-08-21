from rest_framework import viewsets

from api.models import Article
from api.serializers import (AuthenticatedArticleSerializer,
                             NotAuthenticatedArticleSerializer)


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """ List/Retrieve view. Response Data can change depending on user authentication status"""
    queryset = Article.objects.all()
    serializer_class = NotAuthenticatedArticleSerializer
    filterset_fields  = ["title", "category"]
    search_fields = ["title", "category", "summary", "author__name"]

    def get_serializer_class(self):
        if self.action == "retrieve" and self.request.user.is_authenticated:
            return AuthenticatedArticleSerializer
        return self.serializer_class
