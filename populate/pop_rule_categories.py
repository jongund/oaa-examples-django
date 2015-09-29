import sys,os
sys.path.append(os.path.abspath('..'))
from django.core.exceptions import ObjectDoesNotExist

#from django.core.management import setup_environ 
#import coding.settings as settings
#setup_environ(settings)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OAAExamplesDjango.settings")
from django.conf import settings

"""This file is for updating and populating the database with Rule Categories and Rulesets"""

from ruleCategories.models import RuleCategory


def createRuleCategory(id, slug, abbrev, nls, order, title, title_plural, desc, num):

    try:
      rc = RuleCategory.objects.get(category_id=id)
      print ('Updating Rule Category: ' + title)
      rc.slug         = slug 
      rc.category_num = num
      rc.abbrev       = abbrev
      rc.title        = title
      rc.title_plural = title_plural
      rc.description  = desc
      rc.order         = order
            
    except ObjectDoesNotExist:

      print ("Creating Rule Category: " + title)
      rc = RuleCategory(category_id=id, slug=slug, category_num=num, abbrev=abbrev, title=title, title_plural=title_plural, description=desc, order=order)
      
    rc.save()

createRuleCategory('ID_CATEGORY_STRUCTURE',      'structure',  'SC', 'en',  1, 'Structure and Content',    'Structure and Content',    'Rules asscociated with page level structure and use of web standards',   0x000080)
createRuleCategory('ID_CATEGORY_IMAGES',         'images',     'I',  'en',  2, 'Image',                    'Images',                   'Rules asscociated with images',                                          0x000008)
createRuleCategory('ID_CATEGORY_FORM_CONTROLS',  'forms',      'F',  'en',  3, 'Form',                     'Forms',                    'Rules asscociated with form controls',                                   0x000004)
createRuleCategory('ID_CATEGORY_DATA_TABLES',    'tables',     'T',  'en',  4, 'Table',                    'Tables',                   'Rules asscociated with tabular data tables',                             0x000002)
createRuleCategory('ID_CATEGORY_LINKS',          'links',      'L',  'en',  5, 'Link',                     'Links',                    'Rules asscociated with links',                                           0x000020)
createRuleCategory('ID_CATEGORY_NAVIGATION',     'navigation', 'N',  'en',  6, 'Site Navigation',          'Site Navigation',          'Rules asscociated with website navigation and finding content',          0x000040)
createRuleCategory('ID_CATEGORY_KEYBOARD',       'keyboard',   'K',  'en',  7, 'Keyboard Support',         'Keyboard Support',         'Rules asscociated with keyboard support',                                0x000010)
createRuleCategory('ID_CATEGORY_AUDIO_VIDEO',    'media',      'AV', 'en',  8, 'Audio/Video',              'Audio/Video',              'Rules asscociated with audio, video and animation content',              0x000001)
createRuleCategory('ID_CATEGORY_STYLE',          'styling',    'SR', 'en',  9, 'Style or Readability',     'Styling and Readability',  'Rules asscociated with text styling, color constrast and reading order', 0x000100)
createRuleCategory('ID_CATEGORY_WIDGETS',        'widgets',    'W',  'en', 10, 'Widget or Scripting',      'Widgets and Scripting',     'Rules asscociated with widgets, timing and scripting',                   0x000200)

