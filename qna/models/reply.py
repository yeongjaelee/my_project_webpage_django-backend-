from django.contrib.auth.models import User
from django.db import models

from qna.models import Question


class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    contents = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='replies')

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)