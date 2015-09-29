from django.db import models

# Create your models here.

## WCAG Principal
class WCAG20_Principle(models.Model):
  title = models.CharField(max_length=200)
  num   = models.IntegerField()
  url   = models.URLField(null=True,blank=True)

  @models.permalink
  def get_absolute_url(self):
    return ('show_wcag20')     

  class Meta:
        ordering = ['num']
        verbose_name="WCAG 2.0 Principle"
        verbose_name_plural="WCAG 2.0 Principles"
  
  def __unicode__(self):
      return 'Principle ' + str(self.num) + '. ' + self.title

  def number(self):
    return "%s."%(self.num)

  def guidelines_set(self):
    return self.guidelines.all()


from django.db import models
from django.contrib.auth.models import User
import re

## WCAG Guideline

class WCAG20_Guideline(models.Model):
  principle = models.ForeignKey(WCAG20_Principle,related_name='guidelines')
  title     = models.CharField(max_length=200)
  num       = models.IntegerField()
  url       = models.URLField(null=True,blank=True)

  class Meta:
        ordering = ['principle__num', 'num']
        verbose_name="WCAG 2.0 Guideline"
        verbose_name_plural="WCAG 2.0 Guidelines"
  
  def __unicode__(self):
      return 'Guideline ' + str(self.principle.num) + '.' + str(self.num) + ' ' + self.title

  def number(self):
    return "%d.%d"%(self.principle.num,self.num)

  def requirements_set(self):
    return self.requirements.all()

  def get_rule_count(self):

    count = 0  
  
    for sc in self.success_criteria.all():
      for r in sc.rules.all():
        count += 1
        
    return count  

  def get_example_count(self):

    count = 0  
  
    for sc in self.success_criteria.all():
      for r in sc.examples.all():
        count += 1
        
    return count  

## WCAG Success Crieterion
WCAG20_LEVEL = (
    ('1', 'Level A'),
    ('2', 'Level AA'),
    ('3', 'Level AAA'),
)


## WCAG Success Crieterion
WCAG20_LEVEL_HTML_CODE = (
    ('1', '<span class="level_a">A</span>'),
    ('2', '<span class="level_aa">AA</span>'),
    ('3', '<span class="level_aaa">AAA</span>'),
)
class WCAG20_SuccessCriterion(models.Model):
  guideline  = models.ForeignKey(WCAG20_Guideline,related_name='success_criteria')
  title      = models.TextField()
  level      = models.CharField(max_length=2,choices=WCAG20_LEVEL)  
  num        = models.IntegerField()
  url            = models.URLField(null=True,blank=True)
  url_meet       = models.URLField(null=True,blank=True)
  url_understand = models.URLField(null=True,blank=True)

  class Meta:
        ordering = ['guideline__principle__num', 'guideline__num', 'num']
        verbose_name="WCAG 2.0 Success Criterion"
        verbose_name_plural="WCAG 2.0 Success Criteria"
  
  def __unicode__(self):
      return 'Success Criterion ' + str(self.guideline.principle.num) + '.' + str(self.guideline.num) + '.' + str(self.num) + ' ' + self.title
     

  def show_level(self):
      for shortp, longp in WCAG20_LEVEL:
          if shortp == self.level:
              return longp

  def show_level_html_code(self):
      for shortp, longp in WCAG20_LEVEL_HTML_CODE:
          if shortp == self.level:
              return longp

  def number(self):
    return "%d.%d.%d"%(self.guideline.principle.num,self.guideline.num,self.num)

  @staticmethod
  def get_by_wcag_number(num):
    parts = num.split('.')
    return WCAG20_SuccessCriterion.objects.get(num=parts[2],guideline__num=parts[1],guideline__principle__num=parts[0])
