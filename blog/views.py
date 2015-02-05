# -*- coding: utf-8 -*-

#Python
import math

#Django
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required, permission_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views.generic import *
from django.views.generic.detail import SingleObjectMixin
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

#Project
from .models import *
from .forms import *

#Global variables

#-------------------------------Custom View--------------------------------------

#Original blog main page view
class MainView(ListView):
	model = Article
	template_name = 'blog/blog_main.html'
	context_object_name = 'article_list'
	paginate_by = 5

	def get_queryset(self):
		return Article.objects.order_by('-written_at')

	def get_context_data(self, **kwargs):
		context = super(MainView, self).get_context_data(**kwargs)
		context['latest_article_list'] = Article.objects.order_by('-modified_at')[:10]
		context['article_list'] = Article.objects.order_by('-written_at')
		context['category_list'] = Category.objects.order_by('order')
		context['user'] = self.request.user

		return context

#Show about page
class AboutView(TemplateView):
	template_name = 'blog/blog_about.html'

	def get_context_data(self, **kwargs):
		context = super(AboutView, self).get_context_data(**kwargs)
		context['category_list'] = Category.objects.order_by('order')
		return context

class SignUpView(FormView):
	form_class = SignUpForm
	template_name = 'blog/signup.html'
	success_url = '/blog/login/'

	def get_context_data(self, **kwargs):
		context = super(SignUpView, self).get_context_data(**kwargs)
		context['category_list'] = Category.objects.order_by('order')
		return context

	def form_valid(self, form):
		return form.signup(self.request)
		#return super(SignUpView, self).form_valid(form)


class LoginView(FormView):
	form_class = LoginForm
	template_name = 'blog/login.html'
	success_url = '/blog/'
	user_check = False

	@method_decorator(csrf_protect)
	@method_decorator(never_cache)
	def dispatch(self, request, *args, **kwargs):
		return super(LoginView, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(LoginView, self).get_context_data(**kwargs)
		context['category_list'] = Category.objects.order_by('order')
		return context

	def form_valid(self, form):
		return form.login(self.request)
		#return super(LoginView, self).form_valid(form)

	def form_invalid(self, form):
		print form.errors
		return super(LoginView, self).form_invalid(form)


class LogoutView(TemplateView):
	template_name= 'blog/logout.html'

	def dispatch(self, request, *args, **kwargs):
		logout(request)
		return redirect('/blog/')


#For write article (only for the root user)
class WriteArticleView(FormView):
	form_class = WriteArticleForm
	template_name = 'blog/write_article.html'
	success_url = '/blog/'

	@method_decorator(permission_required('blog.add_article'))
	def dispatch(self, *args, **kwargs):
		return super(WriteArticleView, self).dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(WriteArticleView, self).get_context_data(**kwargs)
		context['category_list'] = Category.objects.order_by('order')
		return context

	def form_valid(self, form):
		#This method is called when valid form data has been POSTed.
		form.write_article(self.request.POST)
		return super(WriteArticleView, self).form_valid(form)

	def form_invalid(self, form):
		print form.errors
		return super(WriteArticleView, self).form_invalid(form)

#For showing article list
class ArticleListView(ListView):
	model = Category
	template_name = 'blog/article_list.html'
	context_object_name = 'category_list'
	paginate_by = 5

	def get_context_data(self, **kwargs):
		context = super(ArticleListView, self).get_context_data(**kwargs)
		context['selected'] = Category.objects.filter(pk=self.kwargs['pk'])
		if self.kwargs['pk']=='1':
			context['article_list'] = Article.objects.all().order_by('-written_at')
		else:
			context['article_list'] = Article.objects.order_by('-written_at').filter(included_at=context['selected'])
		return context

class ArticleDetailView(DetailView):
	model = Article
	template_name = 'blog/article_detail.html'
	context_object_name = 'article'

	def get_context_data(self, **kwargs):
		context = super(ArticleDetailView, self).get_context_data(**kwargs)
		context['category_list'] = Category.objects.order_by('order')
		return context

#For searching articles by using search form (at top navigation bar)
class ArticleSearchView(ListView):
	model = Article
	template_name = 'blog/search_result.html'
	context_object_name = 'article'

	def get_context_data(self, **kwargs):
		context = super(ArticleSearchView, self).get_context_data(**kwargs)
		context['category_list'] = Category.objects.order_by('order')
		context['keyword'] = self.request.GET['search_content']
		context['searched_articles'] = Article.objects.filter(
			Q(subject__contains=self.request.GET['search_content'])
			|Q(writer__contains=self.request.GET['search_content'])
			|Q(contents__contains=self.request.GET['search_content'])
		)
		return context

