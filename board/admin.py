from django.contrib import admin
from board.models import Board


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass
