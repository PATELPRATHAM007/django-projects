from django.shortcuts import render,get_object_or_404
from datetime import date
from .models import Posts
# Define posts
all_posts = [
    
]

# Helper function to get the post date
def get_date(post):
    return post["date"]

# Corrected startingPage view function 
def startingPage(request):
    latest_post = Posts.objects.all().order_by("-date")[:3]
    return render(request, "blog/startingPage.html", {"posts": latest_post})

# View for displaying all posts
def posts(request):
    all_post = Posts.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {"posts": all_post})

# View for displaying post details based on the slug
def postsDetails(request, slug):
    # indetify_post = Posts.objects.get(slug=slug)
    indetify_post = get_object_or_404(Posts,slug=slug)

    return render(request, "blog/post-details.html", {"post": indetify_post})
