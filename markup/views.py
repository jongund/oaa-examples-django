from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from markup.models import LanguageSpec

from breadCrumbs   import breadCrumbs
  
  
def specfication(request):
   specs = LanguageSpec.objects.all()
   
   return render_to_response('markup/specification.html',{
      'website'  : 'Specification',
      'title'    : 'Specification',
      'main'     : 'markup',
      'specs'    : specs
   }, context_instance=RequestContext(request))
