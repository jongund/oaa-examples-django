from django.conf.urls import url
from .views import RuleCategoryView

urlpatterns = [
    url(r'^$', RuleCategoryView.as_view(), name="rule_categories"),
]