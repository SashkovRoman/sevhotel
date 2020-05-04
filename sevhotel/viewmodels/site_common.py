from sevhotel.viewmodels.common import *
from sevhotel.viewmodels.site_items import SocialLinkViewModel, LocationItemViewModel, LinkViewModel


class SiteCommonViewModel(ViewModelBaze):
    site_title = models.TextField(blank=True, null=True, default=None,
                                  help_text='Заголовок сайта title')
    site_meta_keywords = models.TextField(blank=True, null=True, default=None,
                                          help_text='Ключевые слова meta "keywords"')
    site_meta_description = models.TextField(blank=True, null=True, default=None,
                                             help_text='Описание сайта meta "description"')

    # Кнопки
    btn_ok_content = models.CharField(max_length=256, blank=True, null=True, default=None,
                                      help_text='Кнопка "Подтвердить"')
    btn_cancel_content = models.CharField(max_length=256, blank=True, null=True, default=None,
                                          help_text='Кнопка "Отмена"')
    btn_details_content = models.CharField(max_length=256, blank=True, null=True, default=None,
                                           help_text='Кнопка "Подробнее"')
    btn_booking_content = models.CharField(max_length=256, blank=True, null=True, default=None,
                                           help_text='Кнопка "Бронирование"')

    # Навигация
    nav_page_top_content = models.CharField(max_length=256, blank=True, null=True, default=None,
                                            help_text='Нозвание кнопки "Вверх страницы" в навигационном меню"')
    nav_page_homepage = models.CharField(max_length=256, blank=True, null=True, default=None,
                                         help_text='Нозвание кнопки "На домашнюю страницу" в навигационном меню"')

    # Форма бронирования
    frm_booking_title = models.CharField(max_length=256, blank=True, null=True, default=None,
                                         help_text='Заголовок формы')
    frm_booking_label_last_name = models.CharField(max_length=256, blank=True, null=True, default=None,
                                                   help_text='Поле "Фамилия"')
    frm_booking_label_first_name = models.CharField(max_length=256, blank=True, null=True, default=None,
                                                    help_text='Поле "Имя"')
    frm_booking_label_email = models.CharField(max_length=256, blank=True, null=True, default=None,
                                               help_text='Поле "адреса электронной почты"')
    frm_booking_label_arrival = models.CharField(max_length=256, blank=True, null=True, default=None,
                                                 help_text='Поле "Дата прибытия"')
    frm_booking_label_departure = models.CharField(max_length=256, blank=True, null=True, default=None,
                                                   help_text='Поле "Дата отправления"')
    frm_booking_label_adults = models.CharField(max_length=256, blank=True, null=True, default=None,
                                                help_text='Поле "Взрослых"')
    frm_booking_label_children = models.CharField(max_length=256, blank=True, null=True, default=None,
                                                  help_text='Поле "Детей"')
    frm_booking_label_comment = models.CharField(max_length=256, blank=True, null=True, default=None,
                                                 help_text='Поле "Комментарий"')
    frm_booking_agree_is_active = models.BooleanField(default=False,
                                                      help_text='Тебуется дополнительное согласие')
    frm_booking_label_agree_title = models.CharField(max_length=256, blank=True, null=True, default=None,
                                                     help_text='Заголовок дополнительного согласия')
    frm_booking_label_agree_content = models.CharField(max_length=256, blank=True, null=True, default=None,
                                                       help_text='Подсказка дополнительного согласия')

    # Сообщения
    frm_messages_title = models.CharField(max_length=256, blank=True, null=True, default=None,
                                          help_text='Заголовок формы')

    class Meta:
        verbose_name = 'Общие настройки'
        verbose_name_plural = 'Oбщее: Oбщие настройки'


class SiteSectionFooterViewModel(ViewModelBaze):
    social_links_is_active = models.BooleanField(default=True)
    social_links_title = models.CharField(max_length=32, blank=True, null=True, default=None,
                                          help_text='Заголовок блока с ссылками на социальные сети.')
    social_links = models.ManyToManyField(SocialLinkViewModel, blank=True, default=None)

    links_is_active = models.BooleanField(default=True)
    links_title = models.CharField(max_length=255, blank=True, null=True, default=None,
                                   help_text='Заголовок блока с дополнительными ссылками.')
    links = models.ManyToManyField(LinkViewModel, blank=True, default=None)

    locations_is_active = models.BooleanField(default=True)
    locations_title = models.CharField(max_length=32, blank=True, null=True, default=None,
                                       help_text='Заголовок блока с контактными данными.')
    locations = models.ManyToManyField(LocationItemViewModel, blank=True, default=None)

    copyright_string = models.CharField(max_length=255, blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Oбщее: Футеры'
