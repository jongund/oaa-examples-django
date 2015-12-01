from django.conf.urls import url
from .views import markup

urlpatterns = [
        url(r'^$', markup.as_view(), name='show_markup'),
]