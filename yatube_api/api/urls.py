from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import PostViewSet, CommentViewSet, GroupViewSet

routerV1 = DefaultRouter()
routerV1.register('posts', PostViewSet, basename='posts')
routerV1.register('groups', GroupViewSet, basename='groups')
routerV1.register(r'^posts/(?P<post_id>\d+)/comments',
                  CommentViewSet, basename='comments')


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(routerV1.urls)),
]
