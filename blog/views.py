from django.shortcuts import render, get_object_or_404

from .models import Post, Author, Tag

# Create your views here.


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})


def allPosts(request):
    posts = Post.objects.all()
    return render(request, "blog/all-posts.html", {"all_posts": posts})


def post_details(request, slug):
    post = get_object_or_404(Post,slug=slug)
    return render(request, "blog/post-details.html", {"post": post})
