from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from markup.models import LanguageSpec

from breadCrumbs   import breadCrumbs
  
  
def specfication(request, url_slug):
   spec  = LanguageSpec.objects.get(url_slug=url_slug)
   specs = LanguageSpec.objects.all()
   
   element_definitions = []
   
   for ed in spec.element_definitions.all():
     if ed.has_examples() or ed.has_rules(): 
       element_definitions.append(ed)
       
   request.session['oaa_bread_crumb_1_title'] = spec.abbr
   request.session['oaa_bread_crumb_1_url']   = reverse('show_markup', args=(spec.url_slug,) )
   request.session['oaa_bread_crumb_2_title'] = ''
   request.session['oaa_bread_crumb_2_url']   = ''
   request.session['oaa_bread_crumb_3_title'] = ''
   request.session['oaa_bread_crumb_3_url']   = ''       

   request.session['oaa_main_markup_url'] = reverse('show_markup', args=(spec.url_slug,) )
   request.session['oaa_main_markup_opt'] = spec.url_slug
       
   
   return render_to_response('markup/specification.html',{
      'website'  : 'OAA Specification: ' + spec.title,
      'title'    : 'Specification: ' + spec.title,
      'main'     : 'markup',
      'option'   : spec.url_slug,
      'specs'    : specs,
      'spec'     : spec,
      'element_definitions' : element_definitions,
      'bread_crumbs'  : breadCrumbs(request),
   },context_instance=RequestContext(request))
