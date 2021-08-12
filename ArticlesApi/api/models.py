import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.CharField(max_length=45, unique = False)


# Create your models here.
class Author(models.Model):
    '''  Author Model '''
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length = 255)
    picture = models.CharField(max_length = 255, blank = True, null = True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Article(models.Model):
    '''  Article Model '''
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length = 200)
    category = models.SlugField(max_length = 50)
    summary = models.TextField(max_length = 255, blank =True, null=True)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name = 'articles')

    class Meta:
        ordering = ['title']
    
    def get_first_paragraph(self):
        return self.text.split("    ")[0]
    
    def get_body(self):
        return " ".join(self.text.split("    ")[1:])
        
    def __str__(self):
        return self.title

