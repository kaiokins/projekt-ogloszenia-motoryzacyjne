from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def picture(self, object):
        return format_html('<img src="{}" width="30" />'.format(object.photo.url))

    list_filter = ('qualification',)
    search_fields = ('firstName', 'lastName', 'qualification')
    list_display = ('id', 'firstName', 'lastName', 'picture', 'qualification', 'createdDate')
    list_display_links = ('id', 'firstName', 'lastName')

admin.site.register(Team, TeamAdmin)
