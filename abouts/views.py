from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from django.contrib import messages
from django.contrib.sites.models import Site
from django.contrib.auth.decorators import login_required

from abouts.models import About
from examples.models import Example
from breadCrumbs   import breadCrumbs
from markup.models import ElementDefinition

  
def home(request):
   about = About.objects.get(about_slug='home')
   examples = Example.objects.all()
   defs = ElementDefinition.objects.all()

   request.session['oaa_bread_crumb_1_title'] = 'Home'
   request.session['oaa_bread_crumb_1_url']   = reverse('show_home')
   request.session['oaa_bread_crumb_2_title'] = ''
   request.session['oaa_bread_crumb_2_url']   = ''
   request.session['oaa_bread_crumb_3_title'] = ''
   request.session['oaa_bread_crumb_3_url']   = ''

   return render_to_response('home.html',{
      'title'         : about.title_text,
      'main'          : 'home',
      'about'         : about,
      'bread_crumbs'  : breadCrumbs(request),
      'examples'      : examples,
      'defs'          : defs,
   },context_instance=RequestContext(request))

def show_example(request, example_id):
    example = Example.objects.get(example_id=example_id)
    
    return render_to_response('example_home.html',{
        'website'  : example.title_text,
        'title'    : example.title_text,
        'main'     : 'home',
        'example'  : example,
        }, context_instance=RequestContext(request))

def base(request):
    defs = ElementDefinition.objects.all()

    return render_to_response('base.html',{
      'website'         : about.title_text,
      'title'         : about.title_text,
      'main'          : 'base',
      'defs'          : defs,
   },context_instance=RequestContext(request))