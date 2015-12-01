from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import re

# Rule Category models

import CONST

## Rule Categories (e.g. abbrev, audio, headings, images, links...)  
class RuleCategory(models.Model):
  category_num  = models.IntegerField(unique=True)
  category_id   = models.CharField(max_length=64) 
  abbrev        = models.CharField(max_length=2, default="x")
  title         = models.CharField(max_length=256)
  title_plural  = models.CharField("Title Plural", max_length=256)
  description   = models.TextField(null=True,blank=True)
  slug          = models.SlugField()
  order         = models.IntegerField()

  class Meta:
    verbose_name        = "Rule Category"
    verbose_name_plural = "Rule Categories"
    ordering = ['order','title']
    
  def __str__(self):
    return self.title

  def get_examples_url(self):
    return reverse('show_examples_for_rule_category', args=(self.slug,))
    
    
  def get_example_count(self):
    count = 0
        
    return count    
