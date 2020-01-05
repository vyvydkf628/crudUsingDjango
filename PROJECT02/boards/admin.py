from django.contrib import admin
from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content','created_at','updated_at')

admin.site.register(Comment, CommentAdmin)
