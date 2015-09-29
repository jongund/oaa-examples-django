from django.db import models

## Choices for NLS language used throughout
NLS_LANGUAGES = (
  ('en', 'English'),
  ('fr', 'French'),
  ('de', 'German'),
  ('it', 'Italian'),
)



## A language spec (e.g. HTML5, HTML 4.01)  
class LanguageSpec(models.Model):
  abbr          = models.CharField(max_length=30)
  title         = models.CharField(null=True,blank=True,max_length=100)
  element_based = models.BooleanField("Element based markup (otherwise property based, i.e. CSS)", default=True)
  url           = models.URLField()
  url_slug      = models.SlugField(max_length=32)
  link_text     = models.CharField(max_length=20)

  class Meta:
        verbose_name="Language Specification"
        verbose_name_plural="Language Specifications"
        ordering = ['title']

  def __unicode__(self):
      return self.abbr

  @models.permalink
  def get_absolute_url(self):
    return ('show_markup', [self.url_slug])    

## CSS selector element definition (e.g. input, input[type], input[type="input"])
TYPE_CODES = (
    ('N', 'not any special type'),
    ('R', 'ARIA Role'),
    ('P', 'ARIA Property'),
    ('S', 'ARIA State'),
    ('E', 'Event'),
    ('F', 'Font'),
    ('C', 'Color'),
    ('O', 'Position'),    
    ('H', 'Highlight'),    
) 

class ElementDefinition(models.Model):
  spec            = models.ForeignKey(LanguageSpec, related_name='element_definitions')
  element         = models.CharField(null=True,blank=True,max_length=30)
  attribute       = models.CharField(null=True,blank=True,max_length=30)
  value           = models.CharField(null=True,blank=True,max_length=60)
  description     = models.TextField(null=True,blank=True)
  url             = models.URLField(null=True,blank=True)
  type            = models.CharField(max_length=1,choices=TYPE_CODES, default='N')  

  class Meta:
        verbose_name="Element Definition"
        verbose_name_plural="Element Definitions"
        ordering = ['element', 'attribute', 'value']

  @models.permalink
  def get_absolute_url(self):
    return ('show_specification', [self.spec.url_slug])         

  def has_examples(self):
    for e in self.examples.all():
      return True
    return False  

  def has_rules(self):
    for e in self.rules.all():
      return True
    return False  

  def __unicode__(self):
      tmpstring = self.element
      if self.attribute:
          tmpstring += '[' + self.attribute
          if self.value:
              tmpstring += '="' + self.value + '"]'
          else:
              tmpstring += ']'
      return tmpstring

  def title(self):
      str_title = '';

      if self.element:
         str_title += self.element
      
      if self.value:
         str_title += '[' + self.attribute + '=' + self.value + ']'      
      else:
         if self.attribute:
           str_title += '[' + self.attribute + ']'
  
      return str_title
      
  @staticmethod
  def get_by_title(title):
    element = title
    attribute = ""
    value = ""
    if "[" in title:
      parts = title.split('[')
      element = parts[0]
      parts = parts[1].split(']')
      attribute = parts[0]
      if "=" in attribute:
        parts = attribute.split('=')
        attribute = parts[0]
        value = parts[1]
#    print "  element: " + element + "  attribute: " + attribute + "  value: " + value    
    return ElementDefinition.objects.get(element=element,attribute=attribute,value=value)
