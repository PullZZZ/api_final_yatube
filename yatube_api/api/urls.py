from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

app_name = 'api'

v1_router = routers.DefaultRouter()

v1_router.register(r'posts', PostViewSet)
v1_router.register(r'posts', PostViewSet)
v1_router.register(r'groups', GroupViewSet)
v1_router.register(r'follow', FollowViewSet, basename='follow')
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='commens')

jwt_urlpatterns = [
    path('create/', views.TokenObtainPairView.as_view(), name="jwt-create"),
    path('refresh/', views.TokenRefreshView.as_view(), name="jwt-refresh"),
    path('verify/', views.TokenVerifyView.as_view(), name="jwt-verify"),
]

urlpatterns = [
    path('v1/jwt/', include(jwt_urlpatterns)),
    path('v1/', include(v1_router.urls)),
]
