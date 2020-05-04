from content.models.finance import *


class Category(EnumerableModelBaze, DescribedModel):
    rate = models.ForeignKey(Rate, blank=True, null=True, default=None, on_delete=models.SET_NULL,
                             help_text='Применяемый тариф.')

    class Meta(EnumerableModelBaze.Meta):
        verbose_name = 'Категория размещения'
        verbose_name_plural = 'Категории размещения'


class Room(EnumerableModelBaze, DescribedModel):
    category = models.ForeignKey(Category, blank=True, null=True, default=None, on_delete=models.SET_NULL,
                                 help_text='Категория, которой пренадлежит номер.')
    room_services = models.ManyToManyField(RoomService, blank=True, default=None)
    conditions = models.ManyToManyField(Condition, blank=True, default=None)

    class Meta(EnumerableModelBaze.Meta):
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'


class RoomImage(EnumerableModelBaze, ImageModel):
    room = models.ForeignKey(Room, blank=True, null=True, default=None, on_delete=models.CASCADE,
                             help_text='Номер, которому пренадлежит изображение.')

    class Meta(EnumerableModelBaze.Meta):
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения номера'


class Environment(EnumerableModelBaze, DescribedModel):
    class Meta(EnumerableModelBaze.Meta):
        verbose_name = 'Окружение'
        verbose_name_plural = 'Окружения'


class EnvironmentImage(EnumerableModelBaze, ImageModel):
    environment = models.ForeignKey(Environment, blank=True, null=True, default=None, on_delete=models.CASCADE,
                                    help_text='Окружение, которому пренадлежит изображение.')

    class Meta(EnumerableModelBaze.Meta):
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения окружения'
