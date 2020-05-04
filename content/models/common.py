from django.db import models


class ModelBaze(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=256, blank=True, null=True, default=None,
                            help_text='Название.')

    def __str__(self):
        if self.name:
            return "%s" % self.name
        return '%s object (%s)' % (self.__class__.__name__, self.pk)

    class Meta:
        abstract = True


class EnumerableModelBaze(ModelBaze):
    index = models.DecimalField(max_digits=10, decimal_places=0, default=0,
                                help_text='Порядок отображения (начиная с нуля).')

    def __str__(self):
        if self.name:
            return "%s (%s)" % (self.name, self.index)
        return '%s object (%s)' % (self.__class__.__name__, self.index)

    class Meta:
        abstract = True
        ordering = ['index']


class DescribedModel(models.Model):
    short_description = models.TextField(blank=True, null=True, default=None,
                                         help_text='Краткое описание.')
    description = models.TextField(blank=True, null=True, default=None,
                                   help_text='Подробное описание.')

    class Meta:
        abstract = True


class ImageModel(models.Model):
    image = models.ImageField(upload_to='content/', null=True, default='common/default_960x540.png',
                              help_text='Изображение.')
    image_description = models.CharField(max_length=256, blank=True, null=True, default=None,
                                         help_text='Описание изображения.')

    class Meta:
        abstract = True
