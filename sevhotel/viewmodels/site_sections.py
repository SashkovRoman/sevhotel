from sevhotel.viewmodels.common import *
from sevhotel.viewmodels.site_items import HotelServiceItemViewModel, LocationItemViewModel


# Homepage

class SiteSectionTopCarouselViewModel(ViewModelBaze):
    title = models.CharField(max_length=256, blank=True, null=True, default=None,
                             help_text='Заголовок (отображается на всех слайдах).')

    slide_2_is_active = models.BooleanField(default=False,
                                            help_text='Отобразить слайд №2 на странице.')
    slide_3_is_active = models.BooleanField(default=False,
                                            help_text='Отобразить слайд №3 на странице.')

    slide_1_content = models.CharField(max_length=256, blank=True, null=True, default=None,
                                       help_text='Контент слайда №1.')
    slide_2_content = models.CharField(max_length=256, blank=True, null=True, default=None,
                                       help_text='Контент слайда №2.')
    slide_3_content = models.CharField(max_length=256, blank=True, null=True, default=None,
                                       help_text='Контент слайда №3.')

    slide_1_image = models.ImageField(upload_to='homepage/', null=True, default='common/default_1900x1268.png',
                                      help_text='Фоновое изображение для слайда №1.')
    slide_2_image = models.ImageField(upload_to='homepage/', null=True, default='common/default_1900x1268.png',
                                      help_text='Фоновое изображение для слайда №2.')
    slide_3_image = models.ImageField(upload_to='homepage/', null=True, default='common/default_1900x1268.png',
                                      help_text='Фоновое изображение для слайда №3.')

    class Meta:
        verbose_name = 'Главная карусель'
        verbose_name_plural = 'Домашняя страница: Главная карусель'


class SiteSectionAccommodationViewModel(ViewModelBaze, DescriptionViewModel, ContentViewModel):
    category_name_template = models.TextField(blank=True, null=True, default=None,
                                              help_text='HTML код для форматирования имени категории размещения.')

    class Meta:
        verbose_name = 'Размещение'
        verbose_name_plural = 'Домашняя страница: Размещение'


class SiteSectionEnvironmentsViewModel(ViewModelBaze, DescriptionViewModel, ContentViewModel):
    class Meta:
        verbose_name = 'Инфраструктура'
        verbose_name_plural = 'Домашняя страница: Инфраструктуры'


class SiteSectionAboutUsViewModel(ViewModelBaze, DescriptionViewModel, ContentViewModel):
    content_title = models.CharField(max_length=256, blank=True, null=True, default=None,
                                     help_text='Заголовок блока контента (отображается пользователю)')
    content_content = models.TextField(blank=True, null=True, default=None,
                                       help_text='Содержание блока описания (отображается пользователю)')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'Домашняя страница: О нас'


class SiteSectionHotelServiceViewModel(ViewModelBaze, DescriptionViewModel, ContentViewModel):
    hotel_service_item = models.ManyToManyField(HotelServiceItemViewModel, blank=True, default=None)

    class Meta:
        verbose_name = 'Дополнительный сервис'
        verbose_name_plural = 'Домашняя страница: Дополнительный сервис'


class SiteSectionLocationViewModel(ViewModelBaze, DescriptionViewModel, ContentViewModel):
    location_item = models.ManyToManyField(LocationItemViewModel, blank=True, default=None)

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Домашняя страница: Контактные данные'


class SiteSectionMapViewModel(ViewModelBaze, DescriptionViewModel, ContentViewModel):
    html_code = models.TextField(blank=True, null=True, default=None,
                                 help_text='HTML код карты.')

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Домашняя страница: Карта'


# Selected room

class SiteSectionRoomViewModel(ViewModelBaze, DescriptionViewModel, ContentViewModel):
    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Страница номера: Номер'


class SiteSectionRoomPricesViewModel(ViewModelBaze, DescriptionViewModel, ContentViewModel):
    content_title_template = models.TextField(blank=True, null=True, default=None,
                                              help_text='HTML код для форматирования заголовка блока цен.')
    period_template = models.TextField(blank=True, null=True, default=None,
                                       help_text='HTML код для форматирования периода.')
    price_template = models.TextField(blank=True, null=True, default=None,
                                      help_text='HTML код для форматирования цены.')

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Страница номера: Цены'


# Selected Environment

class SiteSectionEnvironmentViewModel(ViewModelBaze, DescriptionViewModel, ContentViewModel):
    class Meta:
        verbose_name = 'Инфраструктура'
        verbose_name_plural = 'Страница инфраструктуры: Инфраструктура'


# Individual

#    Site Section Conditions

class SiteSectionConditionsViewModel(ViewModelBaze, DescriptionViewModel, ContentViewModel):
    class Meta:
        verbose_name = 'Условия проживания'
        verbose_name_plural = 'Страница: Условия проживания'


class SiteSectionPricesViewModel(ViewModelBaze, DescriptionViewModel, ContentViewModel):
    content_title_template = models.TextField(blank=True, null=True, default=None,
                                              help_text='HTML код для форматирования заголовка.')
    price_block_title_template = models.TextField(blank=True, null=True, default=None,
                                                  help_text='HTML код для форматирования заголовка блока цен.')
    period_template = models.TextField(blank=True, null=True, default=None,
                                       help_text='HTML код для форматирования периода.')
    price_template = models.TextField(blank=True, null=True, default=None,
                                      help_text='HTML код для форматирования цены.')

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Страница: Все цены'
