from django.db import models

from login.models import User


class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    is_hided = models.BooleanField(default=False)

    date_created = models.DateField(auto_now_add=True)
