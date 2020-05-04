from content.models.common import *


class Condition(EnumerableModelBaze):
    is_common = models.BooleanField(default=False,
                                    help_text='Является ли условие общим.')
    title = models.CharField(max_length=256, blank=True, null=True, default=None,
                             help_text='Заголовок')
    content = models.TextField(blank=True, null=True, default=None,
                               help_text='Содержание')

    class Meta(EnumerableModelBaze.Meta):
        verbose_name = 'Условия проживания'
        verbose_name_plural = 'Условия проживания'


class RoomService(EnumerableModelBaze):
    title = models.CharField(max_length=256, blank=True, null=True, default=None,
                             help_text='Заголовок и всплывающая подсказка')
    prompt = models.CharField(max_length=256, blank=True, null=True, default=None,
                              help_text='Содержание (отображается рядом с иконкой)')
    icon_name = models.CharField(max_length=256, blank=True, null=True, default=None,
                                 help_text='Имя отображаемой иконки, например: fal fa-wifi')

    class Meta(EnumerableModelBaze.Meta):
        verbose_name = 'Сервис в номерах'
        verbose_name_plural = 'Сервис в номерах'
