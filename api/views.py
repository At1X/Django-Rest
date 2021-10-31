from django.shortcuts import render, get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from .serializers import (
    ArticleSerializer,
    UserSerializer,
)
from blog.models import Article
from django.contrib.auth.models import User

class ArticlesAPI(ListAPIView):
    def get_queryset(self):
        return Article.objects.all()
    serializer_class = ArticleSerializer
#
# class EditAndDeleteArticle(RetrieveUpdateDestroyAPIView):
#     def get_object(self):
#         return get_object_or_404(Article.objects.all(),pk=self.kwargs.get('pk'))
#     serializer_class = ArticleSerializer

class RetriveEditDeleteArticleApi(RetrieveUpdateDestroyAPIView):
    def get_object(self):
        return get_object_or_404(Article.objects.all(),pk=self.kwargs.get('pk'))
    serializer_class = ArticleSerializer

class UserApi(RetrieveUpdateDestroyAPIView):
    def get_object(self):
        return get_object_or_404(User.objects.all(),pk=self.kwargs.get('pk'))
    serializer_class = UserSerializer