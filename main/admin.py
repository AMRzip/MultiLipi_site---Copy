from django.contrib import admin
from . import models

@admin.register(models.Request_a_Demo)
class RequestADemoAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'full_name', 'email', 'phone_no', 'company_name', 'subject', 'message')