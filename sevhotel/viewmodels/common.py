from django.db import models


# Baze model
class ViewModelBaze(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=256, blank=True, null=True, default=None,
                            help_text='Название секции сайта (используется в администрировании).')

    def __str__(self):
        if self.name:
            return "%s" % self.name
        return '%s object (%s)' % (self.__class__.__name__, self.pk)

    class Meta:
        abstract = True


# Site sections baze
class DescriptionViewModel(models.Model):
    description_id = models.CharField(max_length=256, blank=True, null=True, default=None,
                                      help_text='Идентификатор блока описания (используется навигационным меню).')
    description_name = models.CharField(max_length=256, blank=True, null=True, default=None,
                                        help_text='Название блока описания в навигационном меню.')
    description_title = models.CharField(max_length=256, blank=True, null=True, default=None,
                                         help_text='Заголовок блока описания (отображается пользователю)')
    description_content = models.TextField(blank=True, null=True, default=None,
                                           help_text='Содержание блока описания (отображается пользователю)')

    class Meta:
        abstract = True


class ContentViewModel(models.Model):
    content_id = models.CharField(max_length=256, blank=True, null=True, default=None,
                                  help_text='Идентификатор блока контента (используется навигационным меню).')
    content_name = models.CharField(max_length=256, blank=True, null=True, default=None,
                                    help_text='Название блока контента в навигационном меню.')

    class Meta:
        abstract = True


# Site items
class EnumerableViewModelBaze(ViewModelBaze):
    index = models.DecimalField(max_digits=10, decimal_places=0, default=0,
                                help_text='Порядок отображения набора (начиная с нуля).')

    def __str__(self):
        if self.name:
            return "%s (%s)" % (self.name, self.index)
        return '%s object (%s)' % (self.__class__.__name__, self.index)

    class Meta:
        abstract = True
        ordering = ['index']


# Site notifications
class MessageBaze:
    pass
