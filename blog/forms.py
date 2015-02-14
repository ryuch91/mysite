# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from django import forms
from .models import Category, Article

class WriteArticleForm(forms.Form):
	category_choices = []
	for category in Category.objects.all():
		category_choices.append((category, category.title))

	included_at = forms.ChoiceField(choices=category_choices)
	subject = forms.CharField(max_length=50)
	contents = forms.CharField(widget=forms.Textarea)

	def write_article(self, post):
		article = Article()
		if self.cleaned_data['included_at']:
			article.included_at = Category.objects.filter(title=self.cleaned_data['included_at'])[0]
		article.subject = self.cleaned_data['subject']
		article.contents = self.cleaned_data['contents']
		print article.contents

		article.save()

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	session_check = forms.BooleanField(required=False)

	def login(self, request):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']
		session_check = self.cleaned_data['session_check']

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				if not session_check:
					request.session.set_expiry(0)

				return HttpResponseRedirect('/blog/')
			else :
				return render_to_response('blog/login.html',{
					'errors': 'User is not active, please ask to admin',
					'username': username,
					'form':LoginForm(request.POST)
					})
		else :
			return render_to_response('blog/login.html',{
					'errors': 'Username or password incorrect',
					'username': username,
					'form':LoginForm(request.POST)
					})

		


class SignUpForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	password_check = forms.CharField(widget=forms.PasswordInput)
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.CharField(required=False)

	def signup(self, request):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']
		password_check = self.cleaned_data['password_check']
		first_name = self.cleaned_data['first_name']
		last_name = self.cleaned_data['last_name']
		email = self.cleaned_data['email']

		if password != password_check:
			return render_to_response('blog/signup.html',{
				'errors': 'Password is not same, please enter same password',
				'form':SignUpForm(request.POST)
				})
		else:
			user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
			user.save()
			return HttpResponseRedirect('/blog/login/')


			


