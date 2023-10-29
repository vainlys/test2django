from django.db import models
import datetime

class Post(models.Model):
    published_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField(default="This is the default content for new blog posts.")
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

