from django.contrib import admin
from .models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'card_type', 'card_number', 'created_at')
    list_display_links = ('id',)
    list_per_page = 10
    search_fields = ('card_type',)


admin.site.register(Card, CardAdmin)
