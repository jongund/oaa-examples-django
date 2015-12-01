from django.shortcuts         import render_to_response, HttpResponseRedirect
from django.http              import HttpResponse, Http404
from django.template          import RequestContext
from django.core.urlresolvers import reverse
from django.contrib import messages

from wcag20.models         import WCAG20_Guideline
from ruleCategories.models import RuleCategory
from examples.models       import Example
from django.core import urlresolvers
import json

from breadCrumbs import breadCrumbs

def example(request, permanent_slug):
   example  = Example.objects.get(permanent_slug=permanent_slug)
   
   rule_categories = RuleCategory.objects.all().order_by('order')

   title = example.title_text
     
   return render_to_response('example.html',{
      'website'         : "OAA Example: " + title,
      'title'           : title,
      'main'            : "examples",
      'example'         : example,
      'rule_categories' : rule_categories,
   },context_instance=RequestContext(request))