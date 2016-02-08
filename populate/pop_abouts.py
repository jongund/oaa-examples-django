import sys,os
sys.path.append(os.path.abspath('..'))

#from django.core.management import setup_environ 
#import coding.settings as settings
#setup_environ(settings)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oaa_examples_django.settings")
from django.conf import settings

import django
django.setup()

"""This file is for populating the database with markup information
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from abouts.models import About
from django.contrib.auth.models import User

#editor = User.objects.all()[0]

def create_about(order, slug, title, content):
  try:
    about = About.objects.get(about_slug=slug)
    print ("  Updating About: " + slug )
    about.title    = title
    about.order    = order
    about.content  = content
    #updated_editor = editor
  except ObjectDoesNotExist:
    print ("  Creating About: " + slug)
    about = About(order=order, about_slug=slug, title=title, content=content)
  about.save()
  return about

content = """
The accessible coding practices resources provides tools, rules, techniques and examples to help web developers understand how to make their websites more accessible to people with disabilities.
The resources of the website are developed through the work of the Open Accessibility Alliance and the Open Ajax Accessibility Task Force.


h2. WCAG 2.0

* Content Required
* Content Required
* Content Required

h2. Rule Categories

* Content Required 
* Content Required
* Content Required

h2. Examples

* Examples demonstrate techniques that can be used to satisfy rule requirements
* Examples include information on assistive technology compatibility

h2. Markup

* Markup provides information on how a particular element or attribute may related to a rule or example
 
"""
  
create_about(-1, "home", "Welcome to the ARIA Examples", content)

content = """
* The purpose of accessible web coding practices website is to document the design patterns and the HTML/CSS/ARIA coding practices that lead to web resources being accessible and usable by people with disabilities.
* The rules and techniques in the coding practices resources and tools differ from the techniques and requirements of WCAG 2.0 in that the coding practice resources and tools emphesize both usability and accessibility, this to both improve accessibility of web resources to people with disabilities and to simplify explaining accessibility requirements to developers.  The legalistic "how to meet" sections of WCAG 2.0 often require complex logic to factor out usability concerns to interpret how to apply WCAG 2.0 requirements to a web resource to verify technical compliance.  If you are more concerned with technical compliance to WCAG 2.0 than with creating usable resources for people with disbabilities you may want to seek other resources to help you in your evaluation.
* The organization of the web site is based upon both the organization of the W3C "Web Content Accessibility Guidelines 2.0":http://www.w3.org/tr/wcag and rule categories based on "HTML4":http:/www.w3.org/tr/html4 and "HTML5":http://www.w3.org/tr/html5 element types.  The rule category organization is often more useful to web developers and designers trying to understand the techniques and requirements for making web content more accessible.
* The web site is based on the "OpenAjax Accesisbility Evaluation Library Rules":http://www.openajax.org/member/wiki/Accessibility for evaluting the accessibility of web resources.
* The resources are being developed as a collaboration of the "OpenAjax Accessibility Task Force":http://www.openajax.org/member/wiki/Accessibility and the "Open Accessibility Alliance":http://collaborate.athenpro.org/group/open-accessibility-alliance/ .
 
"""
  
create_about(1, "purpose", "Purpose", content)  

content = """

There are many people who are contributing to the development of the coding practices web resources through their participation in the "Open Accessibility Alliance":http://collaborate.athenpro.org/group/open-accessibility-alliance/ and the "OpenAjax Accessibility Task Force":http://www.openajax.org/member/wiki/Accessibility.
The following people are highlighted for their contributions to also assist in the development and editing the content on the coding practices web resources.  

*Note:* _The following names are based on the interests expressed in the Open Accessibility Alliance FTF meeing on June 25th and 26th at the University of Illinois.  Please let Jon Gunderson know of your interests in contributing the web site development._

h2. Conceptual Model

"Conceptual Model for Coding Practices":http://trac.web-accessibility-best-practices.org/wiki/design/conceptual-model 

* Nicholas Hoyt, University of Illinois

h2. Rule Definition and Messaging

* Jon Gunderson, University of Illinois
* Nicholas Hoyt, University of Illinois
* Mike Scott, DHSS

h2. Rule Validation Coding

* Jon Gunderson, University of Illinois

h2. Examples

* Jon Gunderson, University of Illinois
* Ken Petri, The Ohio State University
* Charles Swanson (Student), University of Illinois
* Todd Weissenberger, University of Iowa

h2. Assistive Technology Compatibility Testing

* Christy Blew, University of Illinois

h2. Video Resources

* Hao Luo, Northwestern University
* Ted Geis, Elsevier
* Christopher Walker, Northwestern University

"""
create_about(2, "contributors", "Contributors", content)

content = """

h2. Videos on the importance and impact of accessible IT resources

* "IT Accessibility: What Campus Leaders Have to Say":http://www.youtube.com/watch?feature=player_embedded&v=tnsB6YCHVXA
* "A Personal Look at Accessibility in Higher Education":http://www.youtube.com/watch?v=PQGFshzLPXE
* "Keeping Web Accessibility In Mind ":http://www.youtube.com/watch?v=yx7hdQqf8lE
* "Equal Access: Science and Students with Sensory Impairments ":http://www.youtube.com/watch?v=3-PoIJ6VjWA
"""

create_about(3, "importance", "Importance of IT Accessibility", content)    