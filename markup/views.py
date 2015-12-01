from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from markup.models import ElementDefinition
from examples.models import Example
  
def markup(request):
    defs = ElementDefinition.objects.all()
   
    return render_to_response('markup.html',{
        'website'  : 'Markup',
        'title'    : 'Markup',
        'main'     : 'markup',
        'defs'    : defs
      }, context_instance=RequestContext(request))

def show_example(request, permanent_slug):
    example = Example.objects.get(permanent_slug=permanent_slug)
    
    return render_to_response('example_markup.html',{
        'website'  : example.title_text,
        'title'    : example.title_text,
        'main'     : 'markup_example',
        'example'  : example,
        }, context_instance=RequestContext(request))