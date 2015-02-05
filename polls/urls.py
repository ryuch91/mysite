# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('',
	url(r'^$', SurveyListView.as_view(), name='survey_list'),
	#url(r'^(?P<pk>\d+)/$', SurveyDetailView.as_view(), name='survey_detail'),
	url(r'^(?P<pk>\d+)/$', form, name='survey_detail'),
	url(r'^(?P<pk>\d+)/result/$', SurveyResultView.as_view(), name='survey_result'),
	url(r'^(?P<survey_id>\d+)/vote/$', vote , name='survey_vote'),
)