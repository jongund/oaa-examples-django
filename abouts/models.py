from django.db import models
from django.contrib.auth.models import User

import datetime
from utilities import OAAMarkupToText, OAAMarkupToHTML
import markdown

class Updated(models.Model):
  updated_date   = models.DateTimeField(auto_now=True, editable=False)
  #updated_editor = models.ForeignKey(User, editable=True)
    
class About(Updated):
  about_id     = models.AutoField(primary_key=True)  
  about_slug   = models.SlugField(null=True,blank=True)
  title        = models.CharField('About Title', max_length=512)
  title_html   = models.CharField(max_length=1024, default="")
  title_text   = models.CharField(max_length=512, default="")
  content      = models.TextField("Content (textile markup)", null=True,blank=True)
  content_html = models.TextField(default="", blank=True, null=True)
  order        = models.IntegerField(default=0)

  class Meta:
    verbose_name        = "About"
    verbose_name_plural = "Abouts"
    ordering = ['order']
  
  def save(self):
    if self.title:
      self.title_html    = OAAMarkupToHTML(self.title)
      self.title_text    = OAAMarkupToText(self.title)
    if self.content: 
      self.content_html  = markdown.markdown(self.content)
    self.updated_date  = datetime.datetime.now()
    super(About, self).save() # Call the "real" save() method.
    
  def __unicode__(self):
      return self.title_text 

  @models.permalink
  def get_absolute_url(self):
    return ('show_about', [self.about_slug])       
