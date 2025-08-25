from django.urls import path
from . import views

app_name = "knowledge_base"

urlpatterns = [
    path("", views.article_list, name="article_list"),
    path("article/<int:pk>/", views.article_detail, name="article_detail"),
    path("category/<int:pk>/", views.category_article_list, name="category_article_list"),
]
