from django.contrib import admin

from .models import Favorite, Goal, Language, Lesson, Phrase, Scenario, StudyDay, StudyDayCompletion, UserProgress

admin.site.register(Language)
admin.site.register(Scenario)
admin.site.register(Phrase)
admin.site.register(Lesson)
admin.site.register(StudyDay)
admin.site.register(StudyDayCompletion)
admin.site.register(UserProgress)
admin.site.register(Favorite)
admin.site.register(Goal)
