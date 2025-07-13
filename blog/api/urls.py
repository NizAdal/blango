from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from blog.api.views import PostList, PostDetail
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
import os
from rest_framework.routers import DefaultRouter
from blog.api.views import PostList, PostDetail, UserDetail, TagViewSet
router = DefaultRouter()
router.register("tags", TagViewSet)
router.register("posts", PostViewSet)
from blog.api.views import UserDetail, TagViewSet, PostViewSet


urlpatterns = [
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
]


urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    path("auth/", include("rest_framework.urls")),
    path("", include(router.urls)),
    path("token-auth/", views.obtain_auth_token),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
