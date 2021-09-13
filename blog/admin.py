from blog.models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    list_display = ('title' ,'slug', 'created_on')
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {
        'slug': ('title',)
    }

admin.site.register(Post, PostAdmin)
