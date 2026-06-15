from django.shortcuts import render, get_object_or_404
from .models import Categories, Article


def home(request):

    posts = Article.objects.filter(
        is_feature=True
    ).order_by('-created_at')[:6]

    context = {
        'posts': posts
    }

    return render(request, 'home.html', context)


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


def post_detail(request, id):

    post = get_object_or_404(
        Article,
        id=id,
        status='Published'
    )

    context = {
        'post': post
    }

    return render(request, 'post_detail.html', context)