from sevhotel.viewmodels.site_common import *
from sevhotel.viewmodels.site_sections import *


class SiteViewModel:

    def __init__(self):
        # print('init SiteViewModel')

        self.common = SiteCommonViewModel.objects.filter(is_active=True).last or None
        self.footer = SiteSectionFooterViewModel.objects.filter(is_active=True).last or None

        self.homepage = [
            (SiteSectionTopCarouselViewModel.objects.filter(is_active=True).last or None, 'home/site_section_top.html'),
            (SiteSectionAccommodationViewModel.objects.filter(is_active=True).last or None, 'home/site_section_accommodation.html'),
            (SiteSectionEnvironmentsViewModel.objects.filter(is_active=True).last or None, 'home/site_section_environment.html'),
            (SiteSectionHotelServiceViewModel.objects.filter(is_active=True).last or None, 'home/site_section_services.html'),
            (SiteSectionAboutUsViewModel.objects.filter(is_active=True).last or None, 'home/site_section_about.html'),
            (SiteSectionLocationViewModel.objects.filter(is_active=True).last or None, 'home/site_section_location.html'),
            (SiteSectionMapViewModel.objects.filter(is_active=True).last or None, 'home/site_section_map.html')]

        self.room = [
            (SiteSectionRoomViewModel.objects.filter(is_active=True).last or None, 'content/room/site_section_room.html'),
            (SiteSectionRoomPricesViewModel.objects.filter(is_active=True).last or None, 'content/room/site_section_prices.html'),
            (SiteSectionConditionsViewModel.objects.filter(is_active=True).last or None, 'content/room/site_section_conditions.html'),
        ]

        self.environment = [
            (SiteSectionEnvironmentViewModel.objects.filter(is_active=True).last or None, 'content/environment/site_section_environment.html'),
        ]

        self.conditions = [
            (SiteSectionConditionsViewModel.objects.filter(is_active=True).last or None, 'individual/сonditions/site_section_conditions.html'),
        ]

        self.prices = [
            (SiteSectionPricesViewModel.objects.filter(is_active=True).last or None, 'individual/prices/site_section_prices.html'),
        ]