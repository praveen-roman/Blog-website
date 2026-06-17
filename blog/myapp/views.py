from django.shortcuts import render, get_object_or_404,redirect
from .models import Categories, Article,About
from .form import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

from django.db.models import Q

def home(request):
    search = request.GET.get('search')

    posts = Article.objects.filter(
        is_feature=True
    ).order_by('-created_at')

    if search:
        posts = posts.filter(
            Q(title__icontains=search) | Q(short_description__icontains=search)
        )

    posts = posts[:6]

    return render(request, 'home.html', {
        'posts': posts
    })

def category_posts(request, id):

    category = get_object_or_404(
        Categories,
        id=id
    )

    posts = category.articles.all()

    context = {
        'category': category,
        'posts': posts
    }

    return render(request, 'category_post.html', context)


def post_detail(request, slug):

    post = get_object_or_404(
        Article,
        slug=slug,
        status='Published'
    )

    context = {
        'post': post
    }

    return render(request, 'post_detail.html', context)


def about(request):
    detail = About.objects.latest('created_at')

    return render(request, 'about.html', {'detail': detail})


def search(request):
    return render(request,'search.html')

def register(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Successfully Registered")
            return redirect('login_page')
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages

def login_page(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            messages.success(
                request,
                "You have logged in successfully!"
            )

            return redirect('home')

        messages.error(
            request,
            "Invalid username or password"
        )

    else:
        form = AuthenticationForm()

    return render(
        request,
        'login.html',
        {'form': form}
    )
# def login_page(request):
#     if request.method=='POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password']
#             user =authenticate(request,username=username,password=password)
#             if user is not None:
#                 login(request,user)
#                 messages.success(request,'You have logged in successfully!')
#                 return redirect('home')
#             else:
#                 messages.error(request, "Invalid username or password")
#     else:
#         form = LoginForm()
#     return render(request,'login.html',{'form':form})


def logout_page(request):

    if request.user.is_authenticated:
        logout(request)
        messages.success(
            request,
            "Logged out successfully!"
        )

    return redirect('home')