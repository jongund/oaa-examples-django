"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""
import sys,os
sys.path.append(os.path.abspath('..'))

#from django.core.management import setup_environ 
#import coding.settings as settings
#setup_environ(settings)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oaa_examples_django.settings")
from django.conf import settings

from django.core.exceptions import ObjectDoesNotExist
from markup.models import LanguageSpec, ElementDefinition

from pop_examples_common import *

from examples.models       import Example
from ruleCategories.models import RuleCategory


# =============================
# Common Resources
# =============================

# =============================
# Initial scripts
# =============================

script1 = create_script('examples/js/jquery-1.4.2.min.js','JQuery 1.4.2 Library')
script2 = create_script('examples/js/jquery-2.0.2.min.js','JQuery 2.0.2 Library')
script_draganddrop = create_script('examples/js/draganddrop.js','Drag and Drop Common Script')
script_gfeed = create_script('examples/js/jquery.jGFeed.js','jQuery Google Feed Plugin')
script_live = create_script('examples/js/live.js','Live Region Common Script')
script_cycle = create_script('examples/js/jquery.cycle2.all.js','Cycle Script')


# =============================
# Initial images
# =============================

create_image('examples/images/arrow-down-black.png','Down Arrow: Black')
create_image('examples/images/arrow-down-gray.png','Down Arrow: Gray')
create_image('examples/images/arrow-down-white.png','Down Arrow: White')
create_image('examples/images/arrow-left-black.png','Left Arrow: Black')
create_image('examples/images/arrow-left-gray.png','Left Arrow: Gray')
create_image('examples/images/arrow-left-white.png','Left Arrow: White')
create_image('examples/images/arrow-right-black.png','Right Arrow: Black')
create_image('examples/images/arrow-right-gray.png','Right Arrow: Gray')
create_image('examples/images/arrow-right-white.png','Right Arrow: White')
create_image('examples/images/asterisk-blue.png','Asterisk: Blue')
create_image('examples/images/asterisk-green.png','Asterisk: Green')
create_image('examples/images/asterisk-red.png','Asterisk: Red')
create_image('examples/images/bullet-closed-black.png','Bullet (Closed): Black')
create_image('examples/images/bullet-closed-gray.png','Bullet (Closed): Gray')
create_image('examples/images/bullet-closed-white.png','Bullet (Closed): White')
create_image('examples/images/bullet-open-black.png','Bullet (Open): Black')
create_image('examples/images/bullet-open-gray.png','Bullet (Open): Gray')
create_image('examples/images/bullet-open-white.png','Bullet (Open): White')
create_image('examples/images/button-test.png','Button Test')
create_image('examples/images/checkbox-checked-black.png','Checkbox (Checked): Black')
create_image('examples/images/checkbox-checked-gray.png','Checkbox (Checked): Gray')
create_image('examples/images/checkbox-checked-white.png','Checkbox (Checked): White')
create_image('examples/images/checkbox-unchecked-black.png','Checkbox (Unchecked): Black')
create_image('examples/images/checkbox-unchecked-gray.png','Checkbox (Unchecked): Gray')
create_image('examples/images/checkbox-unchecked-white.png','Checkbox (Unchecked): White')
create_image('examples/images/closed-arrow.png','Arrow (Closed)')
create_image('examples/images/dummy-image-120-30.png','Dummy image 120px x 30px')
create_image('examples/images/dummy-image-15-15.png','Dummy image 15px x 15px')
create_image('examples/images/dummy-image-16-16.png','Dummy image 16px x 16px')
create_image('examples/images/dummy-image-7-7.png','Dummy image 7px x 7px')
create_image('examples/images/dummy-image-8-8.png','Dummy image 8px x 8px')
create_image('examples/images/eval-blink.png','Blink')
create_image('examples/images/eval-h3.png','Eval H3')
create_image('examples/images/imagemap1.png','Image map')
create_image('examples/images/minus-black.png','Minus Sign: Black')
create_image('examples/images/minus-gray.png','Minus Sign: Gray')
create_image('examples/images/minus-white.png','Minus Sign: White')
create_image('examples/images/open-arrow.png','Open Arrow')
create_image('examples/images/order-pizza.png','Order Pizza')
create_image('examples/images/plus-black.png','Plus Sign: Black')
create_image('examples/images/plus-gray.png','Plus Sign: Gray')
create_image('examples/images/plus-white.png','Plus Sign: White')
