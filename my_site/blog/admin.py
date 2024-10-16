from django.contrib import admin
from .models import Tag, Author, Posts


class PostsAdmin(admin.ModelAdmin):
    list_filter = ["date"]
    list_display = ["title","slug","author","date"]
    prepopulated_fields = {"slug" : ("title",)}
     
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ["first_name"]
    list_display = ["first_name", "last_name"]


class TagAdmin(admin.ModelAdmin):
    list_filter = ["caption"]
    list_display = ["caption"]
# Register Tag model directly
admin.site.register(Tag,TagAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Posts,PostsAdmin) 