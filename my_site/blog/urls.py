from django.urls import path
from . import views
urlpatterns = [
    path("",views.startingPage,name="starting-page"),
    path("posts",views.posts,name="posts-page"),
    path("post/<slug:slug>",views.postsDetails,name="post-details-page")
]
