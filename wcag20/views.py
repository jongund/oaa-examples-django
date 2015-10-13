from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from .models import WCAG20_Principle
from .models import WCAG20_Guideline
from .models import WCAG20_SuccessCriterion
# Create your views here.

class Wcag20View(TemplateView):
    template_name = 'wcag20.html'
    model = WCAG20_Principle
    
    def get(self, request):
        principle = WCAG20_Principle.objects.all()

        return render_to_response('wcag20.html',{'principle': principle
   }, context_instance=RequestContext(request))
