from rest_framework import routers

from apps.articles.viewsets import ArticleViewSet
from apps.comments.viewsets import CommentViewSet
from apps.commissions.viewsets import CommissionViewSet
from apps.users.viewsets import UserViewSet
from apps.followers.viewsets import FollowerViewSet
from apps.ratings.viewsets import RatingViewSet
router = routers.SimpleRouter()

router.register(r'articles', ArticleViewSet, basename='articles')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'commissions', CommissionViewSet, basename='commissions')
router.register(r'users', UserViewSet, basename='users')
router.register(r'follower', FollowerViewSet, basename='follower')
router.register(r'rating', RatingViewSet, basename='rating')


urlpatterns = router.urls
