from django.contrib import admin
from .models import Grimoire, Order, OrderItem
from django.utils.html import format_html


@admin.register(Grimoire)
class GrimoireAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'stock', 'image_preview', 'is_active', 'created_at')
    search_fields = ('title',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 60px; height: auto;" />',
                obj.image.url
            )
        return '—'

    image_preview.short_description = '画像'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'created_at')
    inlines = [OrderItemInline]
    search_fields = ('user__username', 'status')
    list_filter = ('status', 'created_at')

