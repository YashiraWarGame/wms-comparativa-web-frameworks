from django.contrib import admin
from challenge.models import Challenge, Answer, Score


class ScoreInline(admin.TabularInline):
    model = Score
    extra = 1


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date', 'update_date')
    inlines = [ScoreInline, AnswerInline]


admin.site.register(Challenge, ChallengeAdmin)