from django.contrib import admin
from .models import Author, Tag, Post, Comment

# Register your models here.


class postAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date")
    list_display = ("title", "date", "author")
    prepopulated_fields = {"slug": ("title",)}



class commentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")
    list_filter = ("user_name", "post", "user_email")


admin.site.register(Post, postAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, commentAdmin)
