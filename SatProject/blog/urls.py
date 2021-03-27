from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('blog/<int:id>', views.blog_details, name="blog_details"),
    path('form', views.contact, name="contact")
]
