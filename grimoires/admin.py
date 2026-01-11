from django.contrib import admin
from .models import Grimoire, Order


@admin.register(Grimoire)
class GrimoireAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'stock', 'is_active', 'created_at')
    search_fields = ('title',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'created_at')
    search_fields = ('user__username', 'status')
    list_filter = ('status', 'created_at')
