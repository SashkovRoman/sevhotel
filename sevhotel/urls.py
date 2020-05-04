from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from sevhotel.views import *

admin.autodiscover()

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', HomepageView.as_view(), name='home'),
                  url(r'^room/(?P<room_id>\w+)/$', RoomView.as_view(), name='room'),
                  url(r'^environment/(?P<environment_id>\w+)/$', EnvironmentView.as_view(), name='environment'),
                  url(r'^conditions/$', ConditionsView.as_view(), name='conditions'),
                  url(r'^prices/$', PricesView.as_view(), name='prices'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
