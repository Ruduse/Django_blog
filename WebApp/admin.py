from django.contrib import admin
from .models import Comment, Post

# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
# admin.site.register(Comment, Comment)


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "dateTime", "body", "image", "audio"]
    list_filter = ["dateTime"]
    search_fields = ["title"]
    inlines = [CommentInline]


admin.site.register(Post, PostAdmin)
