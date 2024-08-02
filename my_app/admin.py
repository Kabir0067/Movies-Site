from django.contrib.auth.models import Group
from django.contrib import admin
from django.utils.html import format_html  
from .models import *


admin.site.unregister(Group)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)
    list_filter = ('name',)
    
    
@admin.register(Movies)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category', 'video_file', 'created_at', 'channel_name')  
    search_fields = ('title', 'category')
    list_filter = ('title',)
    
    def video_thumbnail(self, obj):
        if obj.video_file:
            return format_html('<video src="{}" width="90" height="65" controls></video>', obj.video_file.url)
        return "-"
    video_thumbnail.short_description = 'Video'


