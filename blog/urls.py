from django.conf.urls import patterns, url

from blog import views


urlpatterns = patterns('',
	url(r'^$',  views.MainView.as_view(), name = 'main'),
	url(r'^write/$', views.WriteArticleView.as_view(), name = 'write_article'),
	url(r'^(?P<pk>\d+)/$', views.ArticleListView.as_view(paginate_by=10), name = 'article_list'),
	url(r'^article/(?P<pk>\d+)/$', views.ArticleDetailView.as_view(), name= 'article_detail'),
	url(r'^search/$', views.ArticleSearchView.as_view(), name='article_search'),
	url(r'^login/$', views.LoginView.as_view(), name='login'),
	url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
	url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
	url(r'^about/$', views.AboutView.as_view(), name='about'),
)