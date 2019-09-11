from django.contrib import admin

from .models import Cash, Wallet


class CashProfile(admin.ModelAdmin):
    list_display = ('date', 'user', 'card_details', 'card_type',
                    'amount_added', 'amount_deducted', 'total_amount')
    list_filter = ('user__username', 'card_type')
    search_fields = ['user__username']
    readonly_fields = ['date']
    fieldsets = (
        ("Card Informations", {
            'fields': (
                'date',
                'user',
                'card_details',
                'card_type',
                'total_amount',
                'amount_added',
                'amount_deducted'
            )
        }),
    )


class WalletProfile(admin.ModelAdmin):
    list_display = ('date_added', 'user', 'card_type',
                    'card_number', 'balance')
    list_filter = ('user__username', 'card_type')
    search_fields = ['user__username']
    readonly_fields = ['date_added']
    fieldsets = (
        ("User wallet Informations", {
            'fields': (
                'date_added',
                'user',
                'balance',
                'card_type',
                'card_number',
            )
        }),
    )

admin.site.register(Cash, CashProfile)
admin.site.register(Wallet, WalletProfile)
