from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.utils import timezone
from django.template.context_processors import csrf
from django.contrib import messages

# Import the Post model from posts app
from posts.models import Post

def index(request):
    return render(request, 'index.html')

def logout(request):#Redirects user back to index page
    auth.logout(request)
    messages.success(request, "You have been successfuly logged out")
    return redirect(reverse('index'))
    
def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
                                    
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfuly logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})

@login_required
def user_profile(request):
    user = User.objects.get(email=request.user.email)
    user_posts = Post.objects.filter(author=user)
    return render(request, 'profile.html', {"profile": user, 'user_posts': user_posts})


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)
        