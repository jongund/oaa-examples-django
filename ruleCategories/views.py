from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from ruleCategories.models import RuleCategory
from examples.models import Example
  
def rule_categories(request):
    rcs = RuleCategory.objects.all()
    
    return render_to_response('rule_categories.html',{
        'website'  : 'Rule Categories',
        'title'    : 'Rule Categories',
        'main'     : 'rule_categories',
        'rcs'      : rcs,
        }, context_instance=RequestContext(request))


def show_example(request, permanent_slug):
    example = Example.objects.get(permanent_slug=permanent_slug)
    
    return render_to_response('example_rc.html',{
        'website'  : example.title_text,
        'title'    : example.title_text,
        'main'     : 'rule_categories_example',
        'example'  : example,
        }, context_instance=RequestContext(request))