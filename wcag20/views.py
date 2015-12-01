from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from wcag20.models import WCAG20_Principle
from wcag20.models import WCAG20_Guideline
from wcag20.models import WCAG20_SuccessCriterion
from examples.models import Example
  
def wcag20(request):
    wps = WCAG20_Principle.objects.all()
    wgs = WCAG20_Guideline.objects.all()
    wss = WCAG20_SuccessCriterion.objects.all()
    
    return render_to_response('wcag20.html',{
      'website'  : 'WCAG 2.0',
      'title'    : 'WCAG 2.0',
      'main'     : 'wcag20',
      'wps'    : wps,
      'wgs'    : wgs,
      'wss'    : wss
    }, context_instance=RequestContext(request))

def show_example(request, permanent_slug):
    example = Example.objects.get(permanent_slug=permanent_slug)
    
    return render_to_response('example_wcag20.html',{
        'website'  : example.title_text,
        'title'    : example.title_text,
        'main'     : 'wcag20_example',
        'example'  : example,
        }, context_instance=RequestContext(request))