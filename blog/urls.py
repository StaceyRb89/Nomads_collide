from django.urls import path
from .views import (AddPost, BlogCategories,
                    ViewBlog, DeleteBlog, EditBlog, blog_home)
from home.views import Index


urlpatterns = [
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('', BlogCategories.as_view(), name='blog_categories'),
    path("blog/<slug:slug>/", ViewBlog.as_view(), name='view_blog'),
    path("delete/<int:pk>/", DeleteBlog.as_view(), name='delete_blog'),
    path("edit/<int:pk>/", EditBlog.as_view(), name='edit_blog'),
    path('', blog_home, name='blog_home')
]
