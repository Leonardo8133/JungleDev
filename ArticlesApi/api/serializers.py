from rest_framework import serializers
from rest_framework.authtoken.models import Token

from api.models import Article, Author, User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password', 'username','email')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        ## Create user token
        token = Token.objects.create(user = user)
        return user

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
