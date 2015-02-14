
#Django
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User

#External
from rest_framework import routers, serializers, viewsets

#Project
from blog import views
from polls import views
from homepage import views


#------------------class-----------------
# Serializers define  the API representation
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'is_staff')

#ViewSets define  the view behavior
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)






#-----------------urls-------------------
# Wire up our API using automatic URL routing.
#Additionally, we include login URLs for the browsable API.

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^blog/',  include('blog.urls', namespace="blog")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^homepage/', include('homepage.urls', namespace="homepage")),

    #For using django_summernote
    url(r'^summernote/', include('django_summernote.urls')),

    #For using django_rest_framework
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)
