from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200)
    category_parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                                        related_name='categories'
                                        )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='articles'
                                 )
    user = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, blank=True, null=True,
                             related_name='articles'
                             )
    article_name = models.CharField(max_length=200)
    article_description = models.TextField(max_length=1000, blank=True, null=True)
    article_image = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.article_name
