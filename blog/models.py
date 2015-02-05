from django.db import models

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=50,blank=False)
	order = models.IntegerField(null=True,unique=True)

	def __unicode__(self):
		return u'%s' % (self.title, )

class Article(models.Model):
	included_at = models.ForeignKey(Category,null=True)
	subject = models.CharField(max_length=50)
	writer = models.CharField(max_length=30, default='GAN')
	written_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	modified_at = models.DateTimeField(auto_now=True)
	contents = models.TextField(max_length=2000)