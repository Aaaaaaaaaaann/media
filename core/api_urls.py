from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers as nested_routers

from community.views import CommentViewSet, PostViewSet, UserPostViewSet
from users.views import UserViewSet

router = SimpleRouter()

# community
router.register(r'posts', PostViewSet)

posts_router = nested_routers.NestedSimpleRouter(
    router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet)

# users
router.register(r'users', UserViewSet)

users_router = nested_routers.NestedSimpleRouter(
    router, r'users', lookup='author')
users_router.register(r'posts', UserPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(posts_router.urls)),
    path('', include(users_router.urls))
]
