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
    url(r'^about$', 'abouts.views.about', name='show_about'),

    url(r'^example/(?P<example_id>[\w-]+)/$', 'abouts.views.show_example',        name='show_home_example'),

    # Rule Categories
    #url(r'^rc/$', 'ruleCategories.views.rule_categories', name='show_rule_categories'),
    #url(r'^rc/(?P<permanent_slug>[\w-]+)/$', 'ruleCategories.views.show_example', name='show_rc_example'),
    
    # WCAG 2.0
    #url(r'^wcag20/$', 'wcag20.views.wcag20', name='show_wcag20'),
    #url(r'^wcag20/(?P<permanent_slug>[\w-]+)/$', 'wcag20.views.show_example', name='show_wcag20_example'),

    # About
    #url(r'^abouts/(?P<about_slug>[\w-]+)/$', 'abouts.views.about', name='show_about'),
    
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    
    # Markup
    url(r'^role/$', 'markup.views.role', name='show_role'),
    url(r'^properties/$', 'markup.views.properties', name='show_properties'),
    url(r'^exampler/(?P<permanent_slug>[\w-]+)/$', 'markup.views.show_role_example',        name='show_role_example'),
    url(r'^examplep/(?P<permanent_slug>[\w-]+)/$', 'markup.views.show_properties_example',        name='show_properties_example'),

]
