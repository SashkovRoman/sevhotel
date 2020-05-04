from django.shortcuts import render, get_object_or_404

from django.views.generic import View

from booking.forms import GuestForm
from sevhotel.utils import BookingMixin

from sevhotel.viewmodels.site_viewmodel import *
from content.models.content_model import *


class HomepageView(BookingMixin, View):
    template = 'home/home.html'
    context = {'SiteViewModel': SiteViewModel(), 'ContentModel': None, 'form': GuestForm}

    # noinspection PyTypeChecker
    def get(self, request):
        self.context['ContentModel'] = ContentModel('homepage')
        return render(request, self.template, context=self.context)


class RoomView(BookingMixin, View):
    template = 'content/room/room.html'
    context = {'SiteViewModel': SiteViewModel(), 'ContentModel': None, 'form': GuestForm}

    def get(self, request, room_id):
        # noinspection PyTypeChecker
        self.context['ContentModel'] = ContentModel('room', room_id)
        return render(request, self.template, context=self.context)


class EnvironmentView(View):
    template = 'content/environment/environment.html'
    context = {'SiteViewModel': SiteViewModel(), 'ContentModel': None, 'form': None}

    def get(self, request, environment_id):
        # noinspection PyTypeChecker
        self.context['ContentModel'] = ContentModel('environment', environment_id)
        return render(request, self.template, context=self.context)


class ConditionsView(View):
    template = 'individual/сonditions/сonditions.html'
    context = {'SiteViewModel': SiteViewModel(), 'ContentModel': None, 'form': None}

    def get(self, request):
        # noinspection PyTypeChecker
        self.context['ContentModel'] = ContentModel('conditions')
        return render(request, self.template, context=self.context)


class PricesView(View):
    template = 'individual/prices/prices.html'
    context = {'SiteViewModel': SiteViewModel(), 'ContentModel': None, 'form': None}

    def get(self, request):
        # noinspection PyTypeChecker
        self.context['ContentModel'] = ContentModel('prices')
        return render(request, self.template, context=self.context)
