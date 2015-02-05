# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.views.generic import *
from django.http import HttpResponseRedirect, HttpResponse
from  .models import Survey, Question, Choice
from django.core.urlresolvers import reverse

from .forms import *
from .forms import IndividualForm

# Create your views here.

class SurveyListView(ListView):
	model = Survey
	template_name = 'polls/survey_list.html'
	context_object_name = 'survey_list'

	def get_queryset(self):
		#Return all surveys on database
		return Survey.objects.order_by('-pub_date')

class SurveyDetailView(DetailView):
	model = Survey
	template_name = 'polls/survey_detail.html'
	context_object_name = 'survey'
	
	def dispatch(self, request, *args, **kwargs):
		return super(SurveyDetailView, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(SurveyDetailView, self).get_context_data(**kwargs)
		context['questions'] = Question.objects.filter(survey=self.get_object())
		context['choices'] = Choice.objects.filter(question=context['questions'])

		return context

	def form_valid(self, form):
		form.insert(self.request.POST)

	def form_invalid(self):
		pass



class SurveyResultView(DetailView):
	model = Survey
	template_name = 'polls/survey_result.html'


def vote(request, survey_id):
	survey = get_object_or_404(Survey, pk=survey_id)

	selected_choices = request.POST

	return HttpResponseRedirect('/polls/'+survey_id+'/result', selected_choices)



#It is used for FORM request (get user's name by text-field : 'your_name')
def form(request, pk):
	def insert(post):
		from .models import AnswerLog
		for key, value in post.iteritems():
			if key != 'csrfmiddlewaretoken':
				answer = AnswerLog()
				answer.question = Question.objects.get(pk=key)
				answer.answer = value
				answer.save()
	survey = Survey.objects.get(pk=pk)
	questions = Question.objects.filter(survey=survey)
	# continue only when it is POST request
	if request.method == 'POST':
		form = IndividualForm(request.POST)
		if form.is_valid():
			#data is in the form.cleaned_data
			#...
			#redirect to new URL:
			return HttpResponseRedirect('/result/')

		insert(request.POST)
		

	#when method is others, create blank form 
	else:
		form =IndividualForm()

	return render(request, 'polls/survey_detail.html', {'form': form, 'questions':questions, 'survey': survey})