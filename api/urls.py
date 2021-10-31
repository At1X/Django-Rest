from django.contrib import admin
from django.urls import path
from .views import ArticlesAPI, RetriveEditDeleteArticleApi, UserApi

app_name = 'api'


urlpatterns = [
    path('',ArticlesAPI.as_view(), name='article-api'),
    path('user/<int:pk>', UserApi.as_view(), name='edit-user'),
    path('<int:pk>', RetriveEditDeleteArticleApi.as_view(), name='edit-article'), #u can use slug instead of pk <slug:slug>
    # path('<int:pk>/retrive', RetrieveAPIView.as_view(), name='retrive-article'),
    # path('<int:pk>/update', UpdateArticleApi.as_view(), name='update-article'),
    # path('<int:pk>/delete', DestroyArticleApi.as_view(), name='destroy-article'),
]
