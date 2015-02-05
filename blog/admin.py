# coding: utf-8

from django.contrib import admin
from blog.models import Article, Category
# Register your models here.

#Help to identify for administrate article (for using id, date or any)
class  ArticleAdmin(admin.ModelAdmin):
	list_display = ['id','subject','contents','written_at','modified_at']
	list_filter = ['written_at']
	search_fields = ['contents']
#Help to identify for administrate category (for using id and title)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id', 'title','order']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)