from django.conf.urls import url

from .views import StatusView

urlpatterns = [
    url('^status/$', StatusView.as_view(), name='status'),
]
