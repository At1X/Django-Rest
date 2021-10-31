from django.contrib import admin
from django.urls import path
from .views import ArticlesAPI

app_name = 'api'


urlpatterns = [
    path('',ArticlesAPI.as_view(), name='article-api')
]