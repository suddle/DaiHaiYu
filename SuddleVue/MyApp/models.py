from django.db import models


# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name


class User(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=60)
    phone=models.CharField(max_length=60)

    def __unicode__(self):
        return self.username

class Img(models.Model):
    imgpic=models.CharField(max_length=100)

"""
最小化按钮 颜色改
"""