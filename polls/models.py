# -*- coding:utf-8 -*-

from django.db import models

# Create your models here.

class Survey(models.Model):
	notice = models.TextField(blank=True)
	pub_date = models.DateTimeField('date published',auto_now_add=True, auto_now=False)
	mod_date = models.DateTimeField('date modified',auto_now=True)
	publisher = models.CharField(max_length=30, default='GAN')
	title = models.CharField(max_length = 50)
	how_many_questions = models.PositiveIntegerField(default=0)
	how_many_voted = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return u'%s' % (self.title, )

class Question(models.Model):
	#initialize?
	CHAR = 'char'
	TEXT = 'text'
	RADIO = 'radio'
	CHECK = 'check'
	EMAIL = 'email'
	SELECT = 'select'

	#(variable's name , 'string that will be shown at template')
	QUESTION_TYPE = (
		(CHAR, 'character'),
		(TEXT, 'text'),
		(RADIO, 'radio button'),
		(CHECK, 'check box'),
		(EMAIL, 'e-mail'),
		(SELECT, 'select'),
	)

	survey = models.ForeignKey(Survey, null=True)
	question_text = models.CharField(max_length=100)
	question_type = models.CharField(max_length=30, choices=QUESTION_TYPE, default=RADIO)

	def __unicode__(self):
		return u'%s' % (self.question_text, )

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=30)
	votes = models.PositiveIntegerField(default=0)

class AnswerLog(models.Model):
	question = models.ForeignKey(Question)
	answer = models.TextField()