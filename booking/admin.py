from django.contrib import admin
from .models.models import *


class GuestAdmin(admin.ModelAdmin):
    list_display = ['last_name',
                    'first_name',
                    'email',
                    'room',
                    'arrival',
                    'departure',
                    'adults',
                    'children',
                    'comment',
                    'created',
                    'updated', ]

    class Meta:
        model = Guest
        ordering = ['-created']


admin.site.register(Guest, GuestAdmin)
