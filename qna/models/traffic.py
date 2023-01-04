from django.contrib.auth.models import User
from django.db import models

from qna.models import Question


class Traffic(models.Model):
    ip = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)