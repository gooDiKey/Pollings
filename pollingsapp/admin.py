from django.contrib import admin

# Register your models here.
from .models import Answer, Polling, Question, Option

# admin.site.register(Polling)
# admin.site.register(Question)
# admin.site.register(Option)

class OptionInline(admin.TabularInline):
    model = Option
    extra = 2

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Poll information', {'fields': ['question_text', 'question_type']})
    ]
    inlines = [OptionInline]

class PollingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Poll information', {'fields': ['poll_title', 'poll_description']}),
        ('Date information', {'fields': ['start_date', 'end_date']})
    ]
    inlines = [QuestionInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Polling, PollingAdmin)
admin.site.register(Answer)
