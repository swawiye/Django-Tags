from django.shortcuts import render
import datetime
from .models import Blog # importing the blog
import markdown # importing the mark
from django.utils.safestring import mark_safe

# Create your views here.
def index(request) :
    return render(request, 'index.html',{"key_message": "Welcome to django"})

def about(request) :
    return render(request, 'about.html')

def contact(request) :
    return render(request, 'contact.html')

def filter_demo(request):
    context = {
        "my_string" : "Hello World",
        "my_date" : datetime.date(2025, 6, 9),
        "long_string" : "This is a long string to be displayed entirely.",
        "default_colour" : "",
        "lowercase_word" : "elephant",
        "fruits" : ['Watermelon', 'Avocado', 'Mango'],
        "intro" : "Good morning,\nmy name is Sovereign Wawiye.\nThis is my end of module Python presentation.",
    }
    return render(request, 'filters.html', context)

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def blog_list(request):
    blogs = Blog.objects.prefetch_related('editors').all()
    for blog in blogs:
        blog.rendered_text = mark_safe(markdown.markdown(blog.text))
    return render(request, 'blog_list.html', {'blogs':blogs})