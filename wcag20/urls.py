from django.conf.urls import url
from .views import Wcag20View

urlpatterns = [
    url(r'^$', Wcag20View.as_view(), name="wcag20"),
]