from django.db import models
from django.contrib.auth.models import User
class Article(models.Model):
    name = models.CharField(max_length=20, verbose_name='نام')
    slug = models.SlugField(max_length=20)
    desc = models.TextField(verbose_name='توضیحات')
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='نویسنده')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.name
# Create your models here.
