from django.contrib import admin

from api.models import Article, Author

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ["=id", "name"]

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author"]
    search_fields = ["=id", "title", "category"]
    list_filter = ["author", "category"]
    autocomplete_fields = ["author"]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
