from django.db import models
from django.contrib.auth.models import User

import datetime
import markdown

from utilities import OAAMarkupToText, OAAMarkupToHTML
from utilities import HTMLToSourceCodeFormat, OAAMarkupRemoveHighlightCode

# Example models

#from rules.models          import Updated
from ruleCategories.models import RuleCategory
from wcag20.models         import WCAG20_SuccessCriterion
from markup.models         import ElementDefinition
#from techniques.models     import Rule, Technique
#from manualChecks.models   import ManualCheck

from django.core import urlresolvers

EXAMPLE_PRACTICE = (
    ('bad', 'Not accessible'),
    ('poor', 'Poor Practice'),
    ('good', 'Good Practice'),
    ('best', 'Best Practice'),
)


EXAMPLE_STATUS = (
    ('acc', 'Accepted'),
    ('pro', 'Proposed'),
    ('dep', 'Deprecated'),
)

EXAMPLE_STATUS_HTML_CODE = (
    ('acc', '<span class="acc">Accepted</span>'),
    ('pro', '<span class="pro">Proposed</span>'),
    ('dep', '<span class="dep">Deprecated</span>'),
)

class Updated(models.Model):
  updated_date   = models.DateTimeField(auto_now=True, editable=False)


class Example(models.Model):
  example_id       = models.AutoField(primary_key=True)  
  permanent_slug   = models.SlugField(null=True,blank=False) #keep it
  title            = models.CharField(max_length=512) #markdown
  title_html       = models.CharField(max_length=1024, default="", editable=False) #plaintext version of title
  title_text       = models.CharField(max_length=512, default="", editable=False)

  a11y_features      = models.TextField("Describe accessibility features of example", null=True,blank=True)
  a11y_features_html = models.TextField(default="", editable=False)

  a11y_issues      = models.TextField("Describe accessibility issues of example", null=True,blank=True)
  a11y_issues_html = models.TextField(default="", editable=False)


  keyboard         = models.TextField("Information on keyboard shortcuts", null=True, blank=True)
  keyboard_html    = models.TextField(default="", editable=False)

  practice         = models.CharField(max_length=8,choices=EXAMPLE_PRACTICE,default='best')
  status           = models.CharField(max_length=8,choices=EXAMPLE_STATUS,default='acc')
    
  external_url     = models.URLField("External URL to example", max_length=512, blank=True)

  style            = models.TextField('CSS code', null=True,blank=True) #markup for highlighting
  style_code       = models.TextField(default='', editable=False)
  style_source     = models.TextField(default='', editable=False)
  html             = models.TextField('HTML code for inside body tag', null=True,blank=True)
  html_code        = models.TextField(default='', editable=False)
  html_source      = models.TextField(default='', editable=False)
  script           = models.TextField('Javascript code', null=True,blank=True)
  script_code      = models.TextField(default='', editable=False)
  script_source    = models.TextField(default='', editable=False)
  markup           = models.ManyToManyField(ElementDefinition,       related_name='examples', blank=True, null=True)
  rule_category    = models.ForeignKey(RuleCategory,related_name='examples', blank=True, null=True)
  success_criteria = models.ManyToManyField(WCAG20_SuccessCriterion, related_name='examples', blank=True, null=True)
  order            = models.IntegerField(default=0)
  
  class Meta:
    ordering = ['example_id','title']
    verbose_name        ="Example"
    verbose_name_plural ="Examples"
    
  @models.permalink
  def get_absolute_url(self):
    return ('show_example', [self.example_id])

  @models.permalink
  def get_permanent_url(self):
    return ('show_example_permanent', [self.permanent_slug])

  def save(self):
    if self.title:
      self.title_html       = OAAMarkupToHTML(self.title)
      self.title_text       = OAAMarkupToText(self.title)
      
    if self.keyboard:  
      self.keyboard_html = markdown.markdown(self.keyboard)

    if self.a11y_features:  
      self.a11y_features_html = markdown.markdown(self.a11y_features)
      

    if self.style:
      self.style_code   = OAAMarkupRemoveHighlightCode(self.style)
      self.style_source = HTMLToSourceCodeFormat(self.style)
      
    if self.html:
      self.html_code   = OAAMarkupRemoveHighlightCode(self.html)
      self.html_source = HTMLToSourceCodeFormat(self.html)

    if self.script:
      self.script_code   = OAAMarkupRemoveHighlightCode(self.script)
      self.script_source = HTMLToSourceCodeFormat(self.script)
      
      
    self.updated_date     = datetime.datetime.now()

    super(Example, self).save() # Call the "real" save() method.  
  
  def __str__(self):
      return 'Example : ' + self.title_text 

  def get_example_abbrev(self):
      return 'Example ' + self.example_group.rule_category.abbrev + "." + str(self.example_group.order) + "." + str(self.order)  

  def get_example_status(self):
    for shortp, longp in EXAMPLE_STATUS:
      if shortp == self.status:
        return longp
        
  def get_example_status_as_html(self):
    for shortp, longp in EXAMPLE_STATUS_HTML_CODE:
      if shortp == self.status:
        return longp 
        
  def get_rules_passed_count(self):
      count = 0

      for rr in self.rule_references.all():
        if rr.validation == "pass":
          count += 1
        else:  
          if rr.manual_check == "pass":
            count += 1
          
      return count

  def get_rules_failed_count(self):
      count = 0
      
      for rr in self.rule_references.all():
        if rr.validation == "fail":
          count += 1
        else:  
          if rr.manual_check == "fail":
            count += 1
          
      return count

  def get_admin_url(self):
    number = self.id - 583
    return urlresolvers.reverse('admin:examples_example_change', args=(number,))
