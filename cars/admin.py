from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.
class CarAdmin(admin.ModelAdmin):

    def picture(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo1.url))

    list_filter = ('brand', 'model', 'city', 'fuel')
    search_fields = ('title', 'brand', 'model', 'city', 'fuel')
    list_display = ('id', 'title', 'brand', 'model', 'picture', 'year', 'engine', 'fuel', 'city')
    list_display_links = ('id', 'title')

admin.site.register(Car, CarAdmin)