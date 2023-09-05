from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView

from .models import Post, Author, Tag
from .forms import CommentForm

# Create your views here.


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})


def allPosts(request):
    posts = Post.objects.all()
    return render(request, "blog/all-posts.html", {"all_posts": posts})


class SinlePostView(DetailView):
    template_name = "blog/post-details.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context
    