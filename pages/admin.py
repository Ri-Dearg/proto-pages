from django.contrib import admin

from .models import PageData


@admin.register(PageData)
class PageDataAdmin(admin.ModelAdmin):
    pass
