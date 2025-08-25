from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def article_list(request):
    articles = Article.objects.all().order_by("-created_at")
    categories = Category.objects.all()
    context = {
        "articles": articles,
        "categories": categories,
    }
    return render(request, "knowledge_base/article_list.html", context)

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        "article": article,
    }
    return render(request, "knowledge_base/article_detail.html", context)

def category_article_list(request, pk):
    category = get_object_or_404(Category, pk=pk)
    articles = Article.objects.filter(category=category).order_by("-created_at")
    categories = Category.objects.all()
    context = {
        "category": category,
        "articles": articles,
        "categories": categories,
    }
    return render(request, "knowledge_base/category_article_list.html", context)
