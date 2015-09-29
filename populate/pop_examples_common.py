"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""
import sys,os
sys.path.append(os.path.abspath('..'))

import datetime

#from django.core.management import setup_environ 
#import coding.settings as settings
#setup_environ(settings)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OAAExamplesDjango.settings")
from django.conf import settings

import textile

from django.core.exceptions import ObjectDoesNotExist
from markup.models          import LanguageSpec, ElementDefinition
from examples.models        import Example

from django.contrib.auth.models import User

# =============================
# Common Example
# =============================

user = User.objects.all()[0]

class example_object:
  order           = 0
  permanent_slug  = ""
  title           = ""
  description     = ""
  keyboard        = ""
  title_override  = ""
  style           = ""
  html            = ""
  script          = ""
  example_groups  = []
  markup          = []
  rule_references = []
  
class rule_reference_object:
  rule_id       = ""
  technique1_id  = ""
  technique2_id  = ""
  technique3_id  = ""
  validation    = "na"
  manual_check  = "na"
  note          = ""
  
  def __init__(self, r, v, mc, t1, t2, t3):
    self.rule_id       = r
    self.validation    = v
    self.manual_check  = mc
    self.technique1_id = t1
    self.technique2_id = t2
    self.technique3_id = t3

def create_rule_reference(example, rr):

  t1 = False
  t2 = False
  t3 = False

  try:
    r = Rule.objects.get(rule_id=rr.rule_id)
    if len(rr.technique1_id):
      t1 = Technique.objects.get(technique_id=rr.technique1_id)
    if len(rr.technique2_id):
      t2 = Technique.objects.get(technique_id=rr.technique2_id)
    if len(rr.technique3_id):
      t3 = Technique.objects.get(technique_id=rr.technique2_id)
    
    try:
      print ("Updating rule reference")
      example_rr = ExampleRuleReference.objects.get(example=example, rule=r)
      example_rr.techniques.clear()
      example_rr.save()   
      
      if t1: 
        example_rr.techniques.add(t1)
      if t2: 
        example_rr.techniques.add(t2)
      if t3: 
        example_rr.techniques.add(t3)
        
      example_rr.validation   = rr.validation
      example_rr.manual_check = rr.manual_check
      example_rr.note         = rr.note
      
    except ObjectDoesNotExist:
      print ("Creating rule reference")
      example_rr = ExampleRuleReference(example=example, rule=r, validation=rr.validation, manual_check=rr.manual_check, note=rr.note)
      example_rr.save()   
       
      if t1: 
        example_rr.techniques.add(t1)
      if t2: 
        example_rr.techniques.add(t2)
      if t3: 
        example_rr.techniques.add(t3)
            
    example_rr.save()
  except ObjectDoesNotExist:
    print ("Rule or technique not defined: " + rr.rule_id + " " + str(example))
  
  return example_rr

  
 
def create_example(example_info):
    print ('===================================')
    try:
      example = Example.objects.get(title=example_info.title)
      print ('  Updating Example ' + str(example.example_id) + ': ' + example.title )
      example.order           = example_info.order
      example.permanent_slug  = example_info.permanent_slug
      example.title           = example_info.title 
      example.description     = example_info.description
      example.keyboard        = example_info.keyboard
      example.title_override  = example_info.title_override
      example.style           = example_info.style
      example.html            = example_info.html
      example.script          = example_info.script
      example.updated_editor  = user
      
      example.markup.clear() 
	
    except ObjectDoesNotExist:
      print ('  Creating Example ' + example_info.title )
      
      example = Example( permanent_slug  = example_info.permanent_slug,
                         order           = example_info.order, 
                         title           = example_info.title, 
                         description     = example_info.description,
                         keyboard        = example_info.keyboard,
                         title_override  = example_info.title_override,
                         style           = example_info.style,
                         html            = example_info.html,
                         script          = example_info.script,
                         updated_editor  = user)

    example.save()

    for eg in example_info.example_groups:  
      example.example_group.add(eg) 
    
    example.save()
  
    for m in example_info.markup:
      example.markup.add(m)
    
    example.save()

    for rr in example_info.rule_references:
      try:
        rro = create_rule_reference(example, rr)
        example.rule_references.add(rro)
      except ObjectDoesNotExist:
        print ("*** Error creating rule reference: " + example)
    
    example.save()
    print ('  Saved Example ' + example.title_text + " (" + str(example.example_id) + ")" )
	
    return example    