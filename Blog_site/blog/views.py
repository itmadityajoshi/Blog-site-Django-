from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Post, Comment



# Create your views here.
def blogs(request):
    post = Post.objects.all()
    context = {
        'post':post
    }
    return render(request,'posts.html', context)



def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
  
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('login')
    
    return render(request, 'auth/login.html')


def register_view(request):
    if request.method == "POST":
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password_confirmation']

        if password != cpassword:
            return redirect('register')
        else:
            user = User.objects.create(username=email, email=email, password=cpassword)
            user.last_name = lname
            user.first_name = fname
            user.save()
            # messages.success(request, "Your Account Created Successfully.")
            return redirect('login')
        
    return render(request, 'auth/register.html')



def logout_view(request):
    logout(request)
    return redirect('/')


def post_detail(request,id):

    comment = Comment.objects.all()

    post = Post.objects.filter(id=id)
    context = {'post': post,
               'comment': comment,}
    return render(request, 'singleContent.html', context) 