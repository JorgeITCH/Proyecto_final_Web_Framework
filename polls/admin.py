from django.contrib import admin

from .models import Choice, Question, Department


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class DepartmenAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['department_text']}),
        (None,               {'fields': ['max_number_questions']}),
    ]
    inlines = [QuestionInline]
    list_display = ('department_text','max_number_questions')
    search_fields = ['department_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Department, DepartmenAdmin)