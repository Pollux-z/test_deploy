from django.forms.widgets import PasswordInput
from django.shortcuts import render, HttpResponse, redirect
from .models import Author, Post
from .form import ContactForm
# Create your views here.
def home(request):

    all_post = Post.objects.all()
    return render(request, "blog/home.html", {'all_post': all_post})

def blog_details(request, id):
    single_post = Post.objects.get(id=id)
    return render(request, "blog/blog-details.html", {'single_post': single_post})

def contact(request):
    form = ContactForm(request.POST)
    if request.method == "POST":
        #save to database
       if form.is_valid():
           form.save()
           return redirect('/')
    else:
       form = ContactForm()

    return render(request, "blog/form.html", {'form': form})