from django.db import models

from login.models import User


class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards')
    title = models.CharField(max_length=30)
    content = models.TextField()
    is_hided = models.BooleanField(default=False)
    file = models.FileField(upload_to='media', null=True, blank=True)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
