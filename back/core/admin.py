from .models import handbook, objects

from django.contrib import admin


# Register your models here.


class CounterpartyAdmin(admin.ModelAdmin):
	list_display = ('name', 'rating')
	list_filter = ('rating',)
	search_fields = ('name',)
	ordering = ('name',)


class DealAdmin(admin.ModelAdmin):
	list_display = (
		'type', 'deal_date', 'destination_place', 'amount', 'cost',
		'start_date', 'end_date', 'inventory', 'counterparty'
	)
	list_filter = ('type', 'counterparty', 'destination_place', 'inventory', 'deal_date', 'start_date', 'end_date')


admin.site.register(handbook.Rating)
admin.site.register(handbook.Place)
admin.site.register(handbook.Inventory)
admin.site.register(handbook.DealType)

admin.site.register(objects.Counterparty, CounterpartyAdmin)
admin.site.register(objects.Deal, DealAdmin)
