from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    dateTime = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images", null=True, default=None)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null="False", default="1"
    )
    description = models.TextField()
    audio = models.FileField(upload_to="media/music", null=True)

    def get_absolute_url(self):
        return reverse("pages/add_blogs")

    def get_Post(id):
        return Post.objects.get(id=id)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    dateTime = models.DateTimeField(auto_now_add=True)
