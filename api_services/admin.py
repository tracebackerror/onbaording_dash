from django.contrib import admin

# Register your models here.

from .models import ParentTicket, SubTicket

class ParentTicketAdmin(admin.ModelAdmin):
    list_display = ('parent_ticket',)
    
admin.site.register(ParentTicket, ParentTicketAdmin)

class SubTicketAdmin(admin.ModelAdmin):
    list_display = ('onboarding_id', 'tracking_number')
   
       
admin.site.register(SubTicket, SubTicketAdmin)