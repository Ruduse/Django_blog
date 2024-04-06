from django.db import models


# Create your models here.
class Member(models.Model):
    firstName = models.CharField(max_length=225)
    lastName = models.CharField(max_length=255)


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    dateTime = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title
