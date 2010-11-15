# -*- coding: utf-8 -*-
from models import Verse, Author
from django.contrib import admin  

class VerseInline(admin.StackedInline):
    model = Verse
    
class AuthorAdmin(admin.ModelAdmin):
    inlines = [VerseInline,]
    list_display = (
        'name',
        'date_joined',
        'number_of_verses',
    )
    def date_joined(self, obj):
        if obj.user:
            return obj.user.date_joined
        return None
    def number_of_verses(self, obj):
        return len(obj.verses.all())

admin.site.register(Author, AuthorAdmin)
admin.site.register(Verse)

