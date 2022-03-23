from django.contrib import admin
from .models import Artical, Comment



class CommentInline(admin.StackedInline): # new
    model = Comment


class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
        CommentInline,
    ]


admin.site.register(Artical, ArticleAdmin)
admin.site.register(Comment)
