from django.contrib import admin
from sevhotel.viewmodels.site_viewmodel import *


# Common

class SiteCommonViewModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'site_title', 'is_active']
    list_filter = ['is_active', ]

    fieldsets = (
        ('Options', {'fields': ('is_active', 'name')}),
        ('SEO', {'classes': ('collapse',), 'fields': ('site_title', 'site_meta_keywords', 'site_meta_description',)}),
        ('Buttons', {'classes': ('collapse',), 'fields': (
            'btn_ok_content', 'btn_cancel_content', 'btn_details_content', 'btn_booking_content',)}),
        ('Navigation', {'classes': ('collapse',), 'fields': ('nav_page_homepage', 'nav_page_top_content',)}),
        ('Booking form', {'classes': ('collapse',), 'fields': (
            'frm_booking_title',
            'frm_booking_label_last_name', 'frm_booking_label_first_name', 'frm_booking_label_email',
            'frm_booking_label_arrival', 'frm_booking_label_departure',
            'frm_booking_label_adults', 'frm_booking_label_children',
            'frm_booking_label_comment',
            'frm_booking_agree_is_active', 'frm_booking_label_agree_title', 'frm_booking_label_agree_content',)}),
        ('Message form', {'classes': ('collapse',), 'fields': ('frm_messages_title',)}),
    )

    class Meta:
        model = SiteCommonViewModel


admin.site.register(SiteCommonViewModel, SiteCommonViewModelAdmin)


class SiteSectionFooterViewModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'social_links_is_active', 'links_is_active', 'locations_is_active', 'is_active', ]
    list_filter = ['is_active', ]

    fieldsets = (
        ('Options', {'fields': ('is_active', 'name')}),
        ('Social links',
         {'classes': ('collapse',), 'fields': ('social_links_is_active', 'social_links_title', 'social_links',)}),
        ('Links', {'classes': ('collapse',), 'fields': ('links_is_active', 'links_title', 'links',)}),
        ('Locations', {'classes': ('collapse',), 'fields': ('locations_is_active', 'locations_title', 'locations',)}),
        ('Advanced', {'classes': ('collapse',), 'fields': ('copyright_string',)}),
    )

    class Meta:
        model = SiteSectionFooterViewModel


admin.site.register(SiteSectionFooterViewModel, SiteSectionFooterViewModelAdmin)


# HomePage

class SiteSectionTopCarouselViewModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'slide_2_is_active', 'slide_3_is_active', 'is_active']
    fieldsets = (
        ('Options', {'fields': ('is_active', 'name', 'title',)}),
        ('Slide 1', {'fields': ('slide_1_content', 'slide_1_image',)}),
        ('Slide 2', {'classes': ('collapse',), 'fields': ('slide_2_is_active', 'slide_2_content', 'slide_2_image',)}),
        ('Slide 3', {'classes': ('collapse',), 'fields': ('slide_3_is_active', 'slide_3_content', 'slide_3_image',)}),
    )

    list_filter = ['is_active', ]

    class Meta:
        model = SiteSectionTopCarouselViewModel


admin.site.register(SiteSectionTopCarouselViewModel, SiteSectionTopCarouselViewModelAdmin)


class SiteSectionAccommodationViewModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active', ]

    class Meta:
        model = SiteSectionAccommodationViewModel


admin.site.register(SiteSectionAccommodationViewModel, SiteSectionAccommodationViewModelAdmin)


class SiteSectionEnvironmentsViewModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active', ]

    class Meta:
        model = SiteSectionEnvironmentsViewModel


admin.site.register(SiteSectionEnvironmentsViewModel, SiteSectionEnvironmentsViewModelAdmin)


class SiteSectionHotelServiceViewModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active', ]

    class Meta:
        model = SiteSectionHotelServiceViewModel


admin.site.register(SiteSectionHotelServiceViewModel, SiteSectionHotelServiceViewModelAdmin)


class SiteSectionAboutUsViewModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active', ]

    class Meta:
        model = SiteSectionAboutUsViewModel


admin.site.register(SiteSectionAboutUsViewModel, SiteSectionAboutUsViewModelAdmin)


class SiteSectionLocationViewModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active', ]

    class Meta:
        model = SiteSectionLocationViewModel


admin.site.register(SiteSectionLocationViewModel, SiteSectionLocationViewModelAdmin)


class SiteSectionMapViewModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active', ]

    class Meta:
        model = SiteSectionMapViewModel


admin.site.register(SiteSectionMapViewModel, SiteSectionMapViewModelAdmin)


# Items

class HotelServiceItemViewModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_name', ]
    list_filter = ['icon_name', ]

    class Meta:
        model = HotelServiceItemViewModel


admin.site.register(HotelServiceItemViewModel, HotelServiceItemViewModelAdmin)


class LocationItemViewModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_name', ]
    list_filter = ['icon_name', ]

    class Meta:
        model = LocationItemViewModel


admin.site.register(LocationItemViewModel, LocationItemViewModelAdmin)


class SocialLinkViewModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_name', ]
    list_filter = ['icon_name', ]

    class Meta:
        model = SocialLinkViewModel


admin.site.register(SocialLinkViewModel, SocialLinkViewModelAdmin)


class LinkViewModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', ]
    list_filter = ['link', ]

    class Meta:
        model = LinkViewModel


admin.site.register(LinkViewModel, LinkViewModelAdmin)


# Selected room

class SiteSectionRoomViewModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active', ]

    class Meta:
        model = SiteSectionRoomViewModel


admin.site.register(SiteSectionRoomViewModel, SiteSectionRoomViewModelAdmin)


class SiteSectionRoomPricesViewModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active', ]

    class Meta:
        model = SiteSectionRoomPricesViewModel


admin.site.register(SiteSectionRoomPricesViewModel, SiteSectionRoomPricesViewModelAdmin)


# Selected Environment
class SiteSectionEnvironmentViewModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active', ]

    class Meta:
        model = SiteSectionEnvironmentViewModel


admin.site.register(SiteSectionEnvironmentViewModel, SiteSectionEnvironmentViewModelAdmin)


# Conditions

class SiteSectionConditionsViewModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active', ]

    class Meta:
        model = SiteSectionConditionsViewModel


admin.site.register(SiteSectionConditionsViewModel, SiteSectionConditionsViewModelAdmin)


# Conditions

class SiteSectionPricesViewModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active', ]

    class Meta:
        model = SiteSectionPricesViewModel


admin.site.register(SiteSectionPricesViewModel, SiteSectionPricesViewModelAdmin)
