from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import ArticleSerializer
from blog.models import Article


class ArticlesAPI(ListAPIView):
    def get_queryset(self):
        return Article.objects.all()
    serializer_class = ArticleSerializer
# Create your views here.
