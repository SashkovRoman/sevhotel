from django.contrib import admin
from content.models.models import *


# class PeriodAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Period._meta.fields]
#
#     class Meta:
#         model = Period
#
#
# admin.site.register(Period, PeriodAdmin)


class PeriodAdmin(admin.TabularInline):
    model = Period
    extra = 0


class RateAdmin(admin.ModelAdmin):
    list_display = ['name', 'begin_date', 'end_date', 'is_active']
    fieldsets = (
        ('Options', {'fields': ('is_active', 'name')}),

    )
    list_filter = ['is_active', ]

    inlines = [
        PeriodAdmin,
    ]

    class Meta:
        model = Rate


admin.site.register(Rate, RateAdmin)


class ConditionAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_common', 'title', 'index', 'is_active']
    fieldsets = (
        ('Options', {'fields': ('is_active', 'name', 'is_common', 'index',)}),
        ('Advanced options', {'classes': ('collapse',), 'fields': ('title', 'content',)}),
    )
    list_filter = ['is_active', 'is_common', ]

    class Meta:
        model = Condition


admin.site.register(Condition, ConditionAdmin)


class RoomServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon_name', 'index', 'is_active']
    fieldsets = (
        ('Options', {'fields': ('is_active', 'name', 'icon_name', 'index',)}),
        ('Advanced options', {'classes': ('collapse',), 'fields': ('title', 'prompt',)}),
    )

    class Meta:
        model = RoomService


admin.site.register(RoomService, RoomServiceAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'rate', 'index', 'is_active']
    fieldsets = (
        ('Options', {'fields': ('is_active', 'name', 'rate', 'index',)}),
        ('Advanced options', {'classes': ('collapse',), 'fields': ('short_description', 'description',)}),

    )
    list_filter = ['is_active', 'rate', ]

    class Meta:
        model = Category
        rate = Category.rate


admin.site.register(Category, CategoryAdmin)


# class RoomImageAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in RoomImage._meta.fields]
#
#     class Meta:
#         model = RoomImage
#
#
# admin.site.register(RoomImage, RoomImageAdmin)


class RoomImageAdmin(admin.TabularInline):
    model = RoomImage
    extra = 0


class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'index', 'is_active']
    fieldsets = (
        ('Options', {'fields': ('is_active', 'name', 'category', 'index',)}),
        ('Advanced options', {'classes': ('collapse',), 'fields': ('short_description', 'description',)}),
        ('Units', {'classes': ('collapse',), 'fields': ('room_services', 'conditions',)}),
    )

    list_filter = ['is_active', 'category', ]

    inlines = [
        RoomImageAdmin,
    ]

    class Meta:
        model = Room
        category = Room.category


admin.site.register(Room, RoomAdmin)


# class EnvironmentImageAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in EnvironmentImage._meta.fields]
#
#     class Meta:
#         model = EnvironmentImage
#
#
# admin.site.register(EnvironmentImage, EnvironmentImageAdmin)


class EnvironmentImageAdmin(admin.TabularInline):
    model = EnvironmentImage
    extra = 0


class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'index', 'is_active']
    fieldsets = (
        ('Options', {'fields': ('is_active', 'name', 'index',)}),
        ('Advanced options', {'classes': ('collapse',), 'fields': ('short_description', 'description',)}),
    )

    list_filter = ['is_active']

    inlines = [
        EnvironmentImageAdmin,
    ]

    class Meta:
        model = Environment


admin.site.register(Environment, EnvironmentAdmin)
