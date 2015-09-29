from django.core.urlresolvers import reverse


def breadCrumbs(request):

  links = []
  
  home = {
    "href"  : reverse('show_home'),
    "title" : 'home'
  }
  
  link1 = {
    "href"  : request.session['oaa_bread_crumb_1_url'],
    "title" : request.session['oaa_bread_crumb_1_title']
  }  
  
  if link1['title']:
    links.append(link1)


    link2 = {
      "href"  : request.session['oaa_bread_crumb_2_url'],
      "title" : request.session['oaa_bread_crumb_2_title']
    }  
  
    link3 = {
      "href"  : request.session['oaa_bread_crumb_3_url'],
      "title" : request.session['oaa_bread_crumb_3_title']
    }  
  

    if link2['title']:
      links.append(link2)
    
      if link3['title']:
        links.append(link3)

  else:  
    links.append(home)
    
  return links
