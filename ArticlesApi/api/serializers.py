from rest_framework import serializers

from api.models import Article, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'picture']


class NotAuthenticatedArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    firstParagraph = serializers.CharField(source='get_first_paragraph')

    class Meta:
        model = Article
        fields = ['id', 'author', 'category', 'title', 'summary', 'firstParagraph']
    

class AuthenticatedArticleSerializer(NotAuthenticatedArticleSerializer):
    body = serializers.CharField(source='get_body')

    class Meta:
        model = Article
        fields = ['id', 'author', 'category', 'title', 'summary', 'firstParagraph', 'body']
