from django.contrib import admin

from base import models


@admin.register(models.Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ['sponsor', 'student', 'amount']