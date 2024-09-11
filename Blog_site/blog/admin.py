from django.contrib import admin
from .models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post,PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display =('name', 'post', 'post_date')
    list_filter = ('post_date',)
    search_fields = ['name','post_body']
admin.site.register(Comment, CommentAdmin)