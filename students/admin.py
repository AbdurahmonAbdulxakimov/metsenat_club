from django.contrib import admin

from students import models 



@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['title', 'phone', 'university', 'type']
    readonly_fields = ['created_at', 'updated_at']
