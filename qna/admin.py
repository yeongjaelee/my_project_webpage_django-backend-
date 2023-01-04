from django.contrib import admin

from qna.models import Question, Reply, Traffic


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    pass

@admin.register(Traffic)
class TrafficAdmin(admin.ModelAdmin):
    pass
