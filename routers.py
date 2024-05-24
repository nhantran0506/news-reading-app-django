from rest_framework import routers

from apps.articles.viewsets import ArticleViewSet
from apps.comments.viewsets import CommentViewSet
from apps.commissions.viewsets import CommissionViewSet
from apps.users.viewsets import UserViewSet

router = routers.SimpleRouter()

router.register(r'articles', ArticleViewSet, basename='articles')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'commissions', CommissionViewSet, basename='commissions')
router.register(r'users', UserViewSet, basename='users')


urlpatterns = router.urls
