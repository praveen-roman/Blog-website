from django.shortcuts import render, get_object_or_404
from .models import Categories, Article,About


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