from rest_framework import routers
from api.views import ArticleViewSet

## Router
router = routers.SimpleRouter()

## Urls
router.register(r'articles', ArticleViewSet)

## Urls Register
urlpatterns = router.urls

