from django.contrib import admin
from .models import Board

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','contents','createdAt','updateAt']

admin.site.register(Board, ArticleAdmin)