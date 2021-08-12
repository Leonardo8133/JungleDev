from collections import OrderedDict

from django.test import RequestFactory, TestCase
from django.urls import reverse
from rest_framework import routers
from rest_framework.test import force_authenticate
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList

from api.models import Article, Author, User
from api.views import ArticleViewSet, CreateUserView


class ArticlesViewTest(TestCase):
    """ Test Articles TestCase  """
    def setUp(self):
        text = "this is the title     this is the first paraph    this is the third paraph"
        author1 = Author.objects.create(name = "Max")
        author2 = Author.objects.create(name = "Vayne")
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username='scooby',
            password='zoinks',
            email='scooby@test.com')
        Article.objects.bulk_create([
        Article(title = "Black one", category = "action", text = text, author = author1),
        Article(title = "My Tasks", category = "adventure", text = text, author = author2),
        Article(title = "Random1", category = "romance fiction", text = text, author = author1),
        Article(title = "Random2", category = "science fiction", text = text, author = author1),
        Article(title = "Random3", category = "terror", text = text, author = author2),
        Article(title = "Random4", category = "comedy", text = text, author = author1),
        Article(title = "Random5", category = "documentary", text = text, author = author2)])

    def test_articles_view(self):
        ## LIST ARTICLES ##
        request = self.factory.get('/api/articles', {'get': 'list'})
        response = ArticleViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.data), ReturnList)
        self.assertEqual(len(response.data), 7)
        self.assertEqual(type(response.data[0]), OrderedDict)
        self.assertEqual(response.data[0].get("body", False), False)
        id1 = response.data[0]["id"]

        ## RETRIEVE ARTICLE - NOT AUTHENTICATED ##
        request = self.factory.get(f'/api/articles',{'get': 'retrieve'})
        response = ArticleViewSet.as_view({'get': 'retrieve'})(request, pk=id1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.data), ReturnDict)
        self.assertEqual(response.data.get("body", False), False)
    
        ## RETRIEVE ARTICLE - AUTHENTICATED ##
        request = self.factory.get(f'/api/articles', {'get': 'retrieve'})
        force_authenticate(request, user=self.user)
        response = ArticleViewSet.as_view({'get': 'retrieve'})(request, pk=id1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.data), ReturnDict)
        self.assertEqual(type(response.data.get("body", False)), str)


        ## SEARCH ARTICLES ##
        request = self.factory.get('/api/articles', {'search': 'fiction'})
        response = ArticleViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.data), ReturnList)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(type(response.data[0]), OrderedDict)
    
        ## FILTER ARTICLES ##
        request = self.factory.get('/api/articles', {'category': 'adventure'})
        response = ArticleViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.data), ReturnList)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "My Tasks")

        print("Finish testing Articles Endpoint")
