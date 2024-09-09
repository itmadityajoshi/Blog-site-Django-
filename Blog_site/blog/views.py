from django.shortcuts import render
from .models import Post
# Create your views here.


def blogs(request):
    post = Post.objects.all()
    context = {
        'post':post
    }
    return render(request,'posts.html', context)



def login_view(request):
    return render(request, 'auth/login.html')


def register_view(request):
    return render(request, 'auth/register.html')