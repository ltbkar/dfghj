from django.contrib import admin
from .models import Book
from .import models


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at',)


admin.site.register(models.Review)
