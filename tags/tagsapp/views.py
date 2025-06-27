from django.shortcuts import render, redirect
import datetime
from .models import Blog, Subscriber# importing the blog
import markdown # importing the mark
from django.utils.safestring import mark_safe
from django.contrib import messages
# To send the email
from django.core.mail import send_mail
from django.conf import settings

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

def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email'] #obtaining the email value
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed.')
        else:
            subscriber = Subscriber(email=email)
            # Sending the email
            subject = 'Welcome to The Django Blog!'
            message = f'Hi {email} get ready to enjoy some interesting blogs.'
            from_email = settings.EMAIL_HOST_USER
            recepient_list = [email]
            send_mail(subject, message, from_email, recepient_list, fail_silently=False)
            subscriber.save()
            messages.success(request, 'Thank you for subscribing!')
            return redirect('subscribe')
    return render(request, 'subscribe.html')
