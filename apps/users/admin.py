from django.contrib import admin
from apps.articles.models import Article
from apps.comments.models import Comment
from apps.commission_user.models import CommissionUser
from apps.commissions.models import Commission
from apps.followers.models import Follower
from apps.login.models import *
from apps.ratings.models import Rating
from apps.roles.models import *
from apps.users.models import User
from apps.notify.models import Notification

# Register your models here.


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(CommissionUser)
admin.site.register(Commission)
admin.site.register(Follower)
admin.site.register(Rating)
admin.site.register(User)
admin.site.register(Notification)