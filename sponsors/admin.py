from django.contrib import admin

from sponsors import models


@admin.register(models.Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['title', 'phone', 'amount']
    readonly_fields = ['created_at', 'updated_at']