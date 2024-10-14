from django.contrib import admin
from .models import Book,Author,Address,Country


# class BookAdmin(admin.ModelAdmin):
#     readonly_fields = ("slug",)
#     prepopulated_fields = {'slug': ('title',)} 
    

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'rating', 'is_bestselling']
    # readonly_fields = ("slug",)
    prepopulated_fields = {'slug': ('title',)} 

admin.site.register(Book,BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
# Register your models here.
