from django.contrib import admin

from .models import Cash


class CashProfile(admin.ModelAdmin):
    list_display = ('date', 'user', 'card_details', 'card_type',
                    'amount_added', 'amount_deducted', 'total_amount')
    list_filter = ('user__username', 'card_type')
    search_fields = ['user_username']
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


admin.site.register(Cash, CashProfile)
