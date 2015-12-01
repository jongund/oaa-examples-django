from django.conf.urls import url
from .views import rule_categories

urlpatterns = [
        url(r'^$', rule_categories.as_view(), name='show_rule_categories'),
]