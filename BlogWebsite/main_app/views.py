from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.

def add_post(request:HttpRequest):

    if request.method == "POST":

        new_post = Post(title=request.POST["title"], content=request.POST["content"],
                         is_published=request.POST["is_published"], publish_date=request.POST["publish_date"])
        new_post.save()
        return redirect("main_app:index_page")

    return render(request, "main_app/add_post.html")



def index_page(request:HttpRequest):

    posts = Post.objects.all()

    return render(request, "main_app/index.html", {"posts" : posts})
