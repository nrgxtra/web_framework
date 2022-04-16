from django.contrib import admin

from ex2.notes.models import Note


@admin.register(Note)
class NotesAdmin(admin.ModelAdmin):
    pass
