from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

admin.site.register(Feedback)
admin.site.register(Category)


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'get_html_photo', 'created_date']
    list_filter = ['available', 'created_date', 'updated_date']
    search_fields = ('name', 'description')
    readonly_fields = ('get_html_photo', 'created_date', 'updated_date')

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width=70>')

    get_html_photo.short_description = "Картинка"


admin.site.register(Item, ItemAdmin)

admin.site.site_title = "Ecohoney"
admin.site.site_header = "Админ-панель сайта Ecohoney"

