from django.contrib import admin
from .models import Grimoire, Order, OrderItem


@admin.register(Grimoire)
class GrimoireAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'stock', 'is_active', 'created_at')
    search_fields = ('title',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'created_at')
    inlines = [OrderItemInline]
    search_fields = ('user__username', 'status')
    list_filter = ('status', 'created_at')

