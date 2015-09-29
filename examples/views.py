from django.shortcuts         import render_to_response, HttpResponseRedirect
from django.http              import HttpResponse, Http404
from django.template          import RequestContext
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from wcag20.models         import WCAG20_Guideline
from ruleCategories.models import RuleCategory
from examples.models       import Example
from django.core import urlresolvers
import json

from breadCrumbs import breadCrumbs
  
  
def rule_categories(request):
   rule_categories = RuleCategory.objects.all().order_by('order')

   request.session['oaa_bread_crumb_1_title'] = 'Summary'
   request.session['oaa_bread_crumb_1_url']   = reverse('show_examples')
   request.session['oaa_bread_crumb_2_title'] = ''
   request.session['oaa_bread_crumb_2_url']   = ''
   request.session['oaa_bread_crumb_3_title'] = ''
   request.session['oaa_bread_crumb_3_url']   = ''

   request.session['oaa_main_examples_url']  = reverse('show_examples') 
   request.session['oaa_main_examples_opt']  = 'examples' 
      
   return render_to_response('examples/rule_categories.html',{
      'title'           : 'Summary of Examples by Rule Categories',
      'main'            : 'examples',
      'option'          : 'summary',
      'rule_categories' : rule_categories,
      'bread_crumbs'    : breadCrumbs(request),
   }, context_instance=RequestContext(request))


def ruleCategory(request, rule_category_slug):
   rule_category   = RuleCategory.objects.get(slug=rule_category_slug)
   rule_categories = RuleCategory.objects.all().order_by('order')

   title = rule_category.title + " Example Groups" 

   request.session['oaa_bread_crumb_1_title'] = title
   request.session['oaa_bread_crumb_1_url']   = reverse('show_examples_for_rule_category', args=(rule_category.slug,))
   request.session['oaa_bread_crumb_2_title'] = ''
   request.session['oaa_bread_crumb_2_url']   = ''
   request.session['oaa_bread_crumb_3_title'] = ''
   request.session['oaa_bread_crumb_3_url']   = ''

   request.session['oaa_main_examples_url']  = reverse('show_examples_for_rule_category', args=(rule_category.slug,)) 
   request.session['oaa_main_examples_opt']  = rule_category.slug
      
   return render_to_response('examples/rule_category.html',{
      'title'           : title,
      'main'            : 'examples',
      'option'          : rule_category.slug,
      'rule_category'   : rule_category,
      'rule_categories' : rule_categories,
      'bread_crumbs'    : breadCrumbs(request),
   },context_instance=RequestContext(request))

def example(request, example_id):
   example  = Example.objects.get(example_id=example_id)
   
   rule_categories = RuleCategory.objects.all().order_by('order')

   title = example.title_text

   request.session['oaa_bread_crumb_3_title'] = title 
   request.session['oaa_bread_crumb_3_url']   = reverse('show_example', args=(example.example_id,))
     
   return render_to_response('examples/example.html',{
      'website'         : "OAA Example: " + title,
      'title'           : title,
      'main'            : "examples",
      'option'          : request.session['oaa_main_examples_opt'],
      'example'         : example,
      'rule_categories' : rule_categories,
      'bread_crumbs'    : breadCrumbs(request),
   },context_instance=RequestContext(request))# Create your views here.


def examplePermanent(request, example_slug):
   example  = Example.objects.get(permanent_slug=example_slug)
   
   rule_categories = RuleCategory.objects.all().order_by('order')

   request.session['oaa_bread_crumb_3_title'] = "Example " + example.id
   request.session['oaa_bread_crumb_3_url']   = reverse('show_example', args=(example.example_id,))
     
   return render_to_response('examples/example.html',{
      'website'         : 'OAA Example: ' + example.title_text,
      'title'           : 'Example: ' + example.title_html,
      'main'            : 'examples',
      'option'          : request.session['oaa_main_examples_opt'],
      'example'         : example,
      'rule_categories' : rule_categories,
      'bread_crumbs'    : breadCrumbs(request),
   },context_instance=RequestContext(request))# Create your views here.