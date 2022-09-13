from .models import handbook, objects

from django.contrib import admin


# Register your models here.


admin.site.register(handbook.Rating)
admin.site.register(handbook.Place)
admin.site.register(handbook.Inventory)
admin.site.register(handbook.DealType)

admin.site.register(objects.Counterparty)
admin.site.register(objects.Deal)