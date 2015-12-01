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
from wcag20.models import WCAG20_Principle, WCAG20_Guideline, WCAG20_SuccessCriterion
from markup.models import LanguageSpec, ElementDefinition
from ruleCategories.models import RuleCategory
from examples.models import Example
from django.contrib.auth.models import User

import datetime
import textile

from django.core.exceptions import ObjectDoesNotExist
from markup.models          import LanguageSpec, ElementDefinition
from examples.models        import Example

from django.contrib.auth.models import User

user = User.objects.all()[0]

class example_object:
    order           = 0
    rule_category = ""
    permanent_slug  = ""
    title           = ""
    a11y_features     = ""
    keyboard        = ""
    title_override  = ""
    style           = ""
    html            = ""
    script          = ""
    example_groups  = []
    markup          = []

def create_example(example_info):
    print( '===================================')
    try:
        example = Example.objects.get(title=example_info.title)
        print( '  Updating Example ' + str(example.example_id) + ': ' + example.title )
        example.order           = example_info.order
        example.rule_category   = example_info.rule_category
        example.permanent_slug  = example_info.permanent_slug
        example.title           = example_info.title 
        example.a11y_features     = example_info.a11y_features
        example.keyboard        = example_info.keyboard
        example.title_override  = example_info.title_override
        example.style           = example_info.style
        example.html            = example_info.html
        example.script          = example_info.script
        example.updated_editor  = user
      
        example.markup.clear() 
	
    except ObjectDoesNotExist:
        print('  Creating Example ' + example_info.title )

        example = Example( permanent_slug  = example_info.permanent_slug,
                         order           = example_info.order,
                         rule_category   = example_info.rule_category,
                         title           = example_info.title, 
                         a11y_features     = example_info.a11y_features,
                         keyboard        = example_info.keyboard,
                         style           = example_info.style,
                         html            = example_info.html,
                         script          = example_info.script)

    example.save()
  
    for m in example_info.markup:
        example.markup.add(m)
    
    example.save()

    print( '  Saved Example ' + example.title_text + " (" + str(example.example_id) + ")" )
	
    return example  