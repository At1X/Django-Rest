from django.shortcuts import render
from blog.models import Article
from django.views.generic import ListView
class ArticleList(ListView):
    def get_queryset(self):
        return Article.objects.all()

# Create your views here.
