from sevhotel.viewmodels.common import *


class HotelServiceItemViewModel(EnumerableViewModelBaze):
    title = models.CharField(max_length=256, blank=True, null=True, default=None,
                             help_text='Заголовок.')
    content = models.TextField(blank=True, null=True, default=None,
                               help_text='Контент.')
    icon_name = models.CharField(max_length=256, blank=True, null=True, default=None,
                                 help_text='Имя отображаемой иконки, например: fal fa-plane-arrival')

    class Meta(EnumerableViewModelBaze.Meta):
        verbose_name = 'Дополнительный сервис'
        verbose_name_plural = 'Спецнабор: Дополнительный сервис'


class LocationItemViewModel(EnumerableViewModelBaze):
    title = models.CharField(max_length=256, blank=True, null=True, default=None,
                             help_text='Заголовок.')
    content = models.TextField(blank=True, null=True, default=None,
                               help_text='Контент.')
    icon_name = models.CharField(max_length=256, blank=True, null=True, default=None,
                                 help_text='Имя отображаемой иконки, например: fas fa-phone-alt')

    class Meta(EnumerableViewModelBaze.Meta):
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Oбщее: Контактные данные'


class SocialLinkViewModel(EnumerableViewModelBaze):
    title = models.CharField(max_length=256, blank=True, null=True, default=None,
                             help_text='Заголовок')
    link = models.CharField(max_length=256, blank=True, null=True, default=None,
                            help_text='Ссылка. Например: https://vk.com/letosev')
    icon_name = models.CharField(max_length=256, blank=True, null=True, default=None,
                                 help_text='Имя отображаемой иконки, например: fab fa-vk')

    class Meta(EnumerableViewModelBaze.Meta):
        verbose_name = 'Ссылка на социальные сети'
        verbose_name_plural = 'Спецнабор: Ссылки на социальные сети'


class LinkViewModel(EnumerableViewModelBaze):
    title = models.CharField(max_length=256, blank=True, null=True, default=None,
                             help_text='Заголовок')
    link = models.CharField(max_length=256, blank=True, null=True, default=None,
                            help_text='Ссылка. Например: http://namore92.ru')

    class Meta(EnumerableViewModelBaze.Meta):
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Спецнабор: Ссылки'
