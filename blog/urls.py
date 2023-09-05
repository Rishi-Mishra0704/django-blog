from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts/", views.allPosts, name="posts-page"),
    path("posts/<slug:slug>", views.SinlePostView.as_view(), name="post-detail-page"),
]
