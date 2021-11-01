from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from .serializers import (
    ArticleSerializer,
    UserSerializer,
)
from .permissions import IsSuperUser, IsOwnerOrReadOnly, UserReadAccess
from blog.models import Article
from django.contrib.auth.models import User

class ArticlesAPI(ListCreateAPIView):
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
        return get_object_or_404(Article.objects.all(), pk=self.kwargs.get('pk'))
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly,]

class SeeUsers(ListCreateAPIView):
    def get_queryset(self):
        return User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser,]

class UserApi(RetrieveUpdateDestroyAPIView):
    def get_object(self):
        return get_object_or_404(User.objects.all(), pk=self.kwargs.get('pk'))
    serializer_class = UserSerializer
    permission_classes = [UserReadAccess,]