from django.db import models


class Link(models.Model):
    link = models.URLField(max_length=500)
    slug = models.SlugField(max_length=7, unique=True)
    redirect_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

