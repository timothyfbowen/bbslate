from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User)
    date = models.DateTimeField()
    title = models.CharField(max_length=100)
    post = models.TextField()
    def __str__(self):
        return self.title
    class Admin:
        list_display = ('author', 'date', 'title')
        search_fields = ('title', 'post')
        list_filter = ('author', 'date')



# Create your models here.
