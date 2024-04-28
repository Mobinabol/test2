from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['titel', 'is_euabel', 'publish_data', 'created_time']


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'text', 'created_time', 'update_time']


admin.site.register(Comment, CommentAdmin)
