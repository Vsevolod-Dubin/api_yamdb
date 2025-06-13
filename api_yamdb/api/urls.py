from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from api.views import (
    CategoryViewSet,
    CommentViewSet,
    GenreViewSet,
    ReviewViewSet,
    TitleViewSet,
)
from users.views import AuthViewSet, UserViewSet

router = DefaultRouter()
router.register("titles", TitleViewSet)
router.register("categories", CategoryViewSet)
router.register("genres", GenreViewSet)
router.register("users", UserViewSet, basename="users")
router.register("auth", AuthViewSet, basename="auth")

titles_router = NestedDefaultRouter(router, "titles", lookup="title")
titles_router.register("reviews", ReviewViewSet, basename="title-reviews")

reviews_router = NestedDefaultRouter(titles_router, "reviews", lookup="review")
reviews_router.register("comments", CommentViewSet, basename="review-comments")

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/", include(titles_router.urls)),
    path("v1/", include(reviews_router.urls)),
]
