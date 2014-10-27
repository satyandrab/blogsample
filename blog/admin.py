from django.contrib import admin
from models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
