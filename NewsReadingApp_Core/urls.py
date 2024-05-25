from django.contrib import admin
from django.urls import path, include
from routers import router

from apps.login.views import LoginView
from apps.articles.views import SummarizeView
from apps.followers.views import *
from apps.category.views import *
from apps.notify.views import *

urlpatterns = [
    path('/', include((router.urls, 'core_api'), namespace='core_api')),
    path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'core_api'), namespace='core_api')),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/summary/', SummarizeView.as_view(), name='summary'),
    path('api/followers/', followers_list, name='followers-list'),
    path('api/following/', following_list, name='following-list'),
    path('articles/category/', articles_by_category, name='articles_by_category'),
    path('api/user_notifications/', user_notifications, name='user-notifications'), 
]
