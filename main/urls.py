from django.urls import path
from .views import IndexView, create_post, toggle_bookmark, bookmarks_list, post_list

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("post/new/", create_post, name="create_post"),
    path("bookmark/<int:post_id>/", toggle_bookmark, name="toggle_bookmark"),
    path("bookmarks/", bookmarks_list, name="bookmarks_list"),
    path("posts/", post_list, name="post_list"),
]
