from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_filter = ('email', 'city', 'carTitle')
    search_fields = ('id', 'firstName', 'lastName', 'email', 'carTitle', 'city', 'added')
    list_display = ('id', 'firstName', 'lastName', 'email', 'carTitle', 'city', 'added')
    list_display_links = ('id', 'firstName', 'lastName')

admin.site.register(Contact, ContactAdmin)