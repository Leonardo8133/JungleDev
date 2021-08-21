from rest_framework import viewsets

from api.models import Article
from api.serializers import (AuthenticatedArticleSerializer,
                             NotAuthenticatedArticleSerializer)


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """ List/Retrieve view. Response Data can change depending on user authentication status """
    queryset = Article.objects.all()
    serializer_class = NotAuthenticatedArticleSerializer

    def get_queryset(self):
        """ Filter the queryset by "category slug value """
        filter_string = self.request.query_params.get("category")
        if filter_string:
            filter_string = filter_string.replace("-", " ")
            return self.queryset.filter(category__iexact = filter_string)
        return self.queryset

    def get_serializer_class(self):
        if self.action == "retrieve" and self.request.user.is_authenticated:
            return AuthenticatedArticleSerializer
        return self.serializer_class
