from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("", views.index_page, name="index_page"),
    path("posts/add/", views.add_post, name="add_post")
    ]