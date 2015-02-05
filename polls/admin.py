# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Survey, Question, Choice, AnswerLog
# Register your models here.

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

#Help to identify for administrate article (for using id, date or any)
class SurveyAdmin(admin.ModelAdmin):
	list_display = ['id','title','pub_date','mod_date','how_many_questions','how_many_voted']
	list_filter = ['pub_date']
	search_fields = ['title']

class  QuestionAdmin(admin.ModelAdmin):
	list_display = ['id','survey','question_text','question_type']
	list_filter = ['survey']
	search_fields = ['question_text']

	fieldsets = [
		(None,				{'fields': ['survey','question_text']}),
		('Question information', 	{'fields': ['question_type'], })
	]
	inlines = [ChoiceInline]

class AnswerLogAdmin(admin.ModelAdmin):
	list_display = ['id', 'question', 'answer']
	list_filter = ['question']

#Help to identify for administrate category (for using id and title)
class ChoiceAdmin(admin.ModelAdmin):
	list_display = ['id', 'question','choice_text','votes']


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(AnswerLog, AnswerLogAdmin)