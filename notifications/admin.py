from django.contrib import admin
from .model.models import *


class EmailBookingConfirmAdmin(admin.ModelAdmin):
    list_display = ['name', 'send_emails', 'recipient_list', 'send_messages', 'is_active']
    fieldsets = (
        ('Options', {'fields': ('is_active', 'name',)}),
        ('Emails', {'classes': ('collapse',), 'fields': ('send_emails',
                                                         'recipient_list',
                                                         'subject_template',
                                                         'message_template',
                                                         'html_message_template',
                                                         )}),
        ('Messages', {'classes': ('collapse',), 'fields': ('send_messages',
                                                           'info_message_template',
                                                           'success_message_template',
                                                           'warning_message_template',
                                                           'error_message_template',
                                                           )}),
    )

    list_filter = ['is_active', 'send_emails', 'send_messages', ]

    class Meta:
        model = BookingConfirm


admin.site.register(BookingConfirm, EmailBookingConfirmAdmin)
