from django.db import models


class Post(models.Model):
    titel = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    is_euabel = models.BooleanField(default=False)
    publish_data = models.DateField(null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
