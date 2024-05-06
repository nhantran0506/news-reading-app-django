from rest_framework import routers

from apps.articles.viewsets import ArticleViewSets
from apps.comments.viewsets import CommentViewSets
from apps.commissions.viewsets import CommissionViewSets
from apps.notifications.viewsets import NotificationViewSets
from apps.users.viewsets import UserViewSets

router = routers.SimpleRouter()

router.register(r'articles', ArticleViewSets, basename='articles')
router.register(r'comments', CommentViewSets, basename='comments')
router.register(r'commissions', CommissionViewSets, basename='commissions')
router.register(r'notifications', NotificationViewSets, basename='notifications')
router.register(r'users', UserViewSets, basename='users')

urlpatterns = router.urls
