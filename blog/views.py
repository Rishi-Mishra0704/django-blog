from django.shortcuts import render
from datetime import date

from .models import Post, Author, Tag


posts = [

]

# Create your views here.


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})


def allPosts(request):

    return render(request, "blog/all-posts.html", { "all_posts": posts})


def post_details(request,slug):
    post =  next(post for post in posts if post['slug'] == slug)
    return render(request, "blog/post-details.html", { "post": post})
