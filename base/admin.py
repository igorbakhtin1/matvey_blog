from django.contrib import admin

# Register your models here.

from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("headline",)}


admin.site.register(Post)
admin.site.register(Tag)
