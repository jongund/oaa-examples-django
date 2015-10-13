"""oaa_examples_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    
    # Home
    url(r'^$', 'abouts.views.home', name='show_home'),
    # Rule Categories
    url(r'^rule_categories/', include('ruleCategories.urls')),
    
    # WCAG 2.0
    url(r'^wcag20/', include('wcag20.urls')),
    
    # About
    url(r'^abouts/(?P<about_slug>[\w-]+)/$',  'abouts.views.about',            name='show_about'),
    
    #Examples
    url(r'^examples/$', 'examples.views.rule_categories', name='show_examples'),
    
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    # Markup
    url(r'^markup/$', 'markup.views.specfication', name='show_markup'),
]
