from django.contrib import admin

from author.models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'id_num')


admin.site.register(Author, AuthorAdmin)


