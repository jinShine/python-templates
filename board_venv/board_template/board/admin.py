from django.contrib import admin
from .models import Board


@admin.register(Board)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title',)