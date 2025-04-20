from django.contrib import admin

from book.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year')


admin.site.register(Book, BookAdmin)
