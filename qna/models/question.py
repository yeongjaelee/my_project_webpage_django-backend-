from django.db import models

class Question(models.Model):
    email = models.CharField(max_length=100)
    contents = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)