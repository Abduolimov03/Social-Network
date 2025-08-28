from django.urls import path
from .views import IndexView, create_post

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("post/new/", create_post, name="create_post"),
    # path("posts/", post_list, name="post_list"),
]
