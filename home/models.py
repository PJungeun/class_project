from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()

    def published(self):
        self.save()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.text[:100]

class Comment(models.Model):
    post=models.ForeignKey('home.Post',related_name='comments', on_delete=models.CASCADE)
    nickname=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
   
    def __str__(self):
        return self.text
