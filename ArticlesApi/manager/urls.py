from rest_framework import routers
from manager.views import AdminAuthorViewSet, AdminArticleViewSet

## Router
router = routers.SimpleRouter()

## Urls
router.register(r'articles', AdminArticleViewSet)
router.register(r'authors', AdminAuthorViewSet)

## Urls Register
urlpatterns = router.urls

