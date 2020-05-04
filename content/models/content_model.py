from django.shortcuts import get_object_or_404

from content.models.models import *


class ContentModel:
    model = None

    def __init__(self, page_key=None, page_context_id=None):
        if page_key == 'homepage':
            self.model = {
                'categories': Category.objects.filter(is_active=True).order_by('index').all,
                'periods': Period.objects.filter(is_active=True).order_by('end_date').all,
                'rooms': Room.objects.filter(is_active=True).order_by('index').all,
                'rooms_images': RoomImage.objects.filter(is_active=True).order_by('index').all,
                'environments': Environment.objects.filter(is_active=True).order_by('index').all,
                'environments_images': EnvironmentImage.objects.filter(is_active=True).order_by('index').all,
            }
        elif page_key == 'room':
            _room_id = page_context_id
            _room = get_object_or_404(Room, id=_room_id)
            self.model = {
                'room': _room,
                'room_images': RoomImage.objects.filter(is_active=True, room=_room).order_by('index').all,
                'periods': Period.objects.filter(rate=_room.category.rate).order_by('end_date').all,
                'conditions': (Condition.objects.filter(is_active=True, is_common=True).order_by('index') |
                               Condition.objects.filter(is_active=True, is_common=False, room=_room).order_by('index')
                               ).all,
            }
        elif page_key == 'environment':
            _environment_id = page_context_id
            _environment = get_object_or_404(Environment, id=_environment_id)
            self.model = {
                'environment': _environment,
                'environment_images': EnvironmentImage.objects.filter(environment_id=_environment_id).all,
            }
        elif page_key == 'conditions':
            self.model = {
                'conditions': Condition.objects.filter(is_active=True, is_common=True).order_by('index').all,
            }
        elif page_key == 'prices':
            self.model = {
                'categories': Category.objects.filter(is_active=True).order_by('index').all,
                'periods': Period.objects.filter(is_active=True).order_by('end_date').all,
            }
        else:
            self.model = {
                'categories': Category.objects.filter(is_active=True).order_by('index'),
                'rates': Rate.objects.filter(is_active=True).order_by('category__index'),
                'periods': Period.objects.filter(is_active=True).order_by('end_date'),
                'rooms': Room.objects.filter(is_active=True).order_by('index'),
                'rooms_images': RoomImage.objects.filter(is_active=True).order_by('index'),
                'rooms_services': RoomService.objects.filter(is_active=True).order_by('index'),
                'environments': Environment.objects.filter(is_active=True).order_by('index'),
                'environments_images': EnvironmentImage.objects.filter(is_active=True).order_by('index'),
                'conditions': Condition.objects.filter(is_active=True).order_by('index'),
            }
