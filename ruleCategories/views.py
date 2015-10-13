from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import RuleCategory
# Create your views here.

class RuleCategoryView(TemplateView):
    template_name = 'rule_categories.html'
    model = RuleCategory