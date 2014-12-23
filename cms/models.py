# Django Modules
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=140, blank=False, null=False)
    slug = models.SlugField(max_length=140, unique=True)
    active = models.BooleanFiel(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-created']


class ArticleQuerySet(models.QuerySet):

    def published(self):
        return self.filter(publish=True)


class Article(models.Model):
    title = models.CharField(max_length=140, blank=False, null=False)
    slug = models.SlugField(max_length=140, unique=True)
    content = models.TextField()
    publish = models.BooleanFiel(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    objects = ArticleQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-created']


class Comment(models.Model):
    pass


class Link(models.Model):
    pass
