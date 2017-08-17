from django.conf.urls import url

from api.api import StatusView

urlpatterns = [
    url('^status/$', StatusView.as_view(), name='status'),
]
