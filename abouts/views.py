from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from django.contrib import messages
from django.contrib.sites.models import Site
from django.contrib.auth.decorators import login_required

from abouts.models import About
from breadCrumbs   import breadCrumbs

  
def home(request):
   about = About.objects.get(about_slug='home')

   request.session['oaa_bread_crumb_1_title'] = 'Home'
   request.session['oaa_bread_crumb_1_url']   = reverse('show_home')
   request.session['oaa_bread_crumb_2_title'] = ''
   request.session['oaa_bread_crumb_2_url']   = ''
   request.session['oaa_bread_crumb_3_title'] = ''
   request.session['oaa_bread_crumb_3_url']   = ''

   return render_to_response('abouts/home.html',{
      'title'         : about.title_text,
      'main'          : 'home',
      'about'         : about,
      'bread_crumbs'  : breadCrumbs(request),
   },context_instance=RequestContext(request))


def about(request, about_slug):
   about  = About.objects.get(about_slug=about_slug)
   abouts = About.objects.all()

   request.session['oaa_bread_crumb_1_title'] = about.title_text
   request.session['oaa_bread_crumb_1_url']   = about.get_absolute_url()
   request.session['oaa_bread_crumb_2_title'] = ''
   request.session['oaa_bread_crumb_2_url']   = ''
   request.session['oaa_bread_crumb_3_title'] = ''
   request.session['oaa_bread_crumb_3_url']   = ''

   request.session['oaa_main_abouts_url']     = about.get_absolute_url()      
   
   return render_to_response('abouts/about.html',{
      'title'        : about.title_text,
      'main'         : 'abouts',
      'about'        : about,
      'abouts'       : abouts,
      'bread_crumbs' : breadCrumbs(request),
   },context_instance=RequestContext(request))
