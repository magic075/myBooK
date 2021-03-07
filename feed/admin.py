from django.contrib import admin
from .models import Post, Comment


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['postAuthor', 'postDate', 'postContent']


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['commentAuthor', 'commentContent', 'commentDate', 'post']


