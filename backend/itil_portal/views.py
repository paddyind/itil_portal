from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Article, Category

def health_check(request):
    return JsonResponse({"status": "ok"})

def article_list(request):
    """
    Display a list of all articles, ordered by the most recent.
    """
    articles = Article.objects.select_related('author', 'category').prefetch_related('tags').order_by('-created_at')
    context = {
        'articles': articles,
    }
    return render(request, 'knowledge_base/article_list.html', context)

def article_detail(request, pk):
    """
    Display a single article.
    """
    article = get_object_or_404(
        Article.objects.select_related('author', 'category').prefetch_related('tags'),
        pk=pk
    )
    context = {
        'article': article,
    }
    return render(request, 'knowledge_base/article_detail.html', context)

def category_article_list(request, category_id):
    """
    Display a list of articles filtered by a specific category.
    """
    category = get_object_or_404(Category, pk=category_id)
    articles = Article.objects.filter(category=category).select_related('author').prefetch_related('tags').order_by('-created_at')
    context = {
        'category': category,
        'articles': articles,
    }
    return render(request, 'knowledge_base/article_list.html', context)
