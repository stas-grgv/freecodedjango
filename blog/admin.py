from django.contrib import admin

# Register your models here.
from blog.models import Article, Publication, Profile

admin.site.register(Article)
admin.site.register(Publication)
admin.site.register(Profile)
