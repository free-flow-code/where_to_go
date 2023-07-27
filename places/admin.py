from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image
from adminsortable2.admin import SortableAdminMixin, SortableStackedInline


class ImageStackedInline(SortableStackedInline):
    model = Image

    fields = [
        'image',
        'get_image_preview',
        'position',
    ]
    readonly_fields = ['get_image_preview']

    def get_image_preview(self, obj):
        return format_html('<img src={} width="200" height=auto />', obj.image.url)


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ('id', )
    inlines = [ImageStackedInline]
