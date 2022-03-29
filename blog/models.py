from turtle import update
from django import views
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from pymysql import TIMESTAMP
# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=20)
    content=models.TextField()
    author=models.CharField(max_length=50)
    slug=models.CharField(max_length=300)
    views = models.IntegerField(default=0)
    created=models.DateTimeField(blank=True)
    update=models.DateTimeField(auto_now=True)


    def __str__(self):
       return f"{self.title}-{self.author}"


class BlogComment(models.Model):
    sno=models.AutoField( primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13]+"...."+"by"+self.user.username
    