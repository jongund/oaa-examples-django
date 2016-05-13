from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from markup.models import ElementDefinition
from examples.models import Example

def role(request):
    defs = ElementDefinition.objects.all()
   
    return render_to_response('role.html',{
        'website'  : 'Role',
        'title'    : 'Role',
        'main'     : 'role',
        'defs'    : defs
      }, context_instance=RequestContext(request))

def properties(request):
    defs = ElementDefinition.objects.all()
   
    return render_to_response('properties.html',{
        'website'  : 'Properties',
        'title'    : 'Properties',
        'main'     : 'properties',
        'defs'    : defs
      }, context_instance=RequestContext(request))

def show_role_example(request, permanent_slug):
    example = Example.objects.get(permanent_slug=permanent_slug)
    defs = ElementDefinition.objects.all()

    return render_to_response('example_role.html',{
        'website'  : example.title_text,
        'title'    : example.title_text,
        'main'     : 'role',
        'example'  : example,
        'defs'     : defs,
        }, context_instance=RequestContext(request))

def show_properties_example(request, permanent_slug):
    example = Example.objects.get(permanent_slug=permanent_slug)
    defs = ElementDefinition.objects.all()

    return render_to_response('example_properties.html',{
        'website'  : example.title_text,
        'title'    : example.title_text,
        'main'     : 'properties',
        'example'  : example,
        'defs'     : defs,
        }, context_instance=RequestContext(request))