from django.contrib import admin

from cats.web.models import Cat


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    pass
