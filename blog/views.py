from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect
from .models import Post, Author, Tag
from .forms import CommentForm

# Create your views here.


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})


def allPosts(request):
    posts = Post.objects.all()
    return render(request, "blog/all-posts.html", {"all_posts": posts})


class SinglePostView(DetailView):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")[:3],
        }
        return render(request, "blog/post-details.html", context)

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post 
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
        }
        return render(request, "blog/post-details.html", context)
