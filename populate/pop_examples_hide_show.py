"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples import *

order = 1

spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='button')
m2 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='region')
m3 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-controls')
m4 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-expanded')
m5 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-labelledby')

# =============================
# Example 1
# =============================

example_obj             = example_object()
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order          = order
example_obj.title       = 'Hide/Show: Region follows button'
example_obj.permanent_slug = 'hideshow1'

example_obj.a11y_features = """
Simple example of hiding and showing regions using aria-expanded. aria-controls is used to maintain markup associations.'
"""
example_obj.keyboard    = """
* Tab: Move between button items and text area.
* Enter or space: Toggle display of hide/show regions.
"""

example_obj.markup = [m1,m2,m3,m4,m5]

example_obj.html        = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<h2 id="t1-label">Topic 1</h2>

<p class="button">
    <button id="button1" class="buttonControl" aria-controls="t1"><span>Show</span> Topic 1</button>
</p>

<div id="t1" class="topic" role="region" aria-labelledby="t1-label" tabindex="-1" aria-expanded="false">
    Topic 1 is all about being Topic 1 and may or may not have anything to do with other topics.
</div>

<h2 id="t2-label">Topic 2</h2>

<p class="button">
    <button id="button2" class="buttonControl" aria-controls="t2"><span>Show</span> Topic 2</button>
</p>

<div id="t2" class="topic" role="region" aria-labelledby="m2-label" tabindex="-1" aria-expanded="false">
       Topic 2 is all about being Topic 2 and may or may not have anything to do with other topics.
</div>

<h2 id="t3-label">Topic 3</h2>

<p class="button">
    <button id="button3" class="buttonControl" aria-controls="t3"><span>Show</span> Topic 3</button>
</p>

<div id="t3" class="topic" role="region" aria-labelledby="m3-label" tabindex="-1" aria-expanded="false">
       Topic 3 is all about being Topic 3 and may or may not have anything to do with other topics.
</div>

<h2 id="t4-label">Topic 4</h2>

<p class="button">
    <button id="button4" class="buttonControl" aria-controls="t4"><span>Show</span> Topic 4</button>
</p>

<div id="t4" class="topic" role="region" aria-labelledby="m4-label" tabindex="-1" aria-expanded="false">
       Topic 3 is all about being Topic 3 and may or may not have anything to do with other topics.
</div>
"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};
$(document).ready(function() {

   var hs1 = new OAA_EXAMPLES.hideShow('button1');
   var hs2 = new OAA_EXAMPLES.hideShow('button2');
   var hs3 = new OAA_EXAMPLES.hideShow('button3');
   var hs4 = new OAA_EXAMPLES.hideShow('button4');
  
}); // end ready()

/**
* @constructor hideShow
*
* @memberOf OAA_EXAMPLES
*
* @desc the constructor for a hideShow widget. it accepts the html ID
* of an element to attach to.
*
* @param {string} id - the html ID of the element to attach to
*
* @return N/A
*/

/**
* @constructor Internal Properties
*
* @property {string} $id - the jquery pointer of the element
*
* @property {integer} toggleSpeed - initialized to 100
*/

OAA_EXAMPLES.hideShow = function(id) {

   this.$id = $('#' + id);
   this.$region = $('#' + this.$id.attr('aria-controls'));

   this.keys = {
               enter: 13,
               space: 32
               };

   this.toggleSpeed = 100;

   // bind handlers
   this.bindHandlers();

} // end hidShow() constructor

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers to the hideShow region
*
* return {N/A}
*/

OAA_EXAMPLES.hideShow.prototype.bindHandlers = function() {

   var thisObj = this;

   this.$id.click(function(e) {

      thisObj.toggleRegion();

      e.stopPropagation();
      return false;
   });
}

/**
* @method toggleRegion
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to toggle the display of the hideShow region
*
* return {N/A}
*/

OAA_EXAMPLES.hideShow.prototype.toggleRegion = function() {

      var thisObj = this;

		// toggle the region
		this.$region.slideToggle(this.toggleSpeed, function() {

			if ($(this).attr('aria-expanded') == 'false') { // region is collapsed

				// update the aria-expanded attribute of the region
				$(this).attr('aria-expanded', 'true');

				// move focus to the region
				$(this).focus();

				// update the button label
				thisObj.$id.find('span').html('Hide');

			}
			else { // region is expanded

				// update the aria-expanded attribute of the region
				$(this).attr('aria-expanded', 'false');

				// update the button label
				thisObj.$id.find('span').html('Show');
			}
		});

} // end toggleRegion()

"""

example_obj.style       = """
div.topic {
    display: none; 
    margin-bottom: 1em;
    padding: .25em;
    border: black thin solid;
    background-color: #EEEEFF;
    width: 40em;
}

p.button {
    margin: .25em;
    padding: .25em;   
}

h2 {
  margin: 0;
  padding: 0;
  margin-top: 1em;  
  
}

a.buttonControl {
  color: #004400;
  text-decoration: none;
  border-bottom: 1px solid #004400;
}

a.buttonControl:hover,
a.buttonControl:active,
a.buttonControl:focus {
  color: #880000;
  border-bottom: 2px solid #880000;
}
"""

example1 = create_example(example_obj)

# =============================
# Example 2
# =============================

order += 1

example_obj             = example_object()
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order          = order
example_obj.title       = 'Hide/Show: Region does not follow button'
example_obj.permanent_slug = 'hideshow2'

example_obj.a11y_features = """
Simple example of hiding and showing regions using aria-expanded. aria-controls is used to maintain markup associations.'
"""
example_obj.keyboard    = """
	Tab: Move between button items and text area.
	Enter or space: Toggle display of hide/show regions.

"""

example_obj.markup = [m1,m2,m3,m4,m5]

example_obj.html        = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<h2>List of Messages</h2>

<ul class="msglinks">
  <li>
      <button id="open1" class="buttonControl" aria-controls="m1">
            <span>Show</span> 
            Message 1
      </button>
  </li> 
  <li>
      <button id="open2" class="buttonControl" aria-controls="m2">
           <span>Show</span> 
           Message 2
      </button>
  </li> 
  <li>
      <button id="open3" class="buttonControl" aria-controls="m3">
           <span>Show</span> 
           Message 3
      </button>
  </li> 
  <li>
      <button id="open4" class="buttonControl" aria-controls="m4">
           <span>Show</span> 
           Message 4
      </button>
  </li> 
</ul>

<div id="m1" class="message" tabindex="-1" role="region" aria-labelledby="m1-label" aria-expanded="false">
    <h2 id="m1-label">Message 1</h2>
    <p>Message 1 is all about being message 1 and has nothing to do with any other messages.</p>
    <p>
        <button id="close1" class="buttonControl" aria-controls="m1">
             Close 
             <span class="hidden">Message 1</span>
        </button>
    </p>
</div>

<div id="m2" class="message" role="region" aria-labelledby="m2-label" tabindex="-1" aria-expanded="false">
      <h2 id="m2-label">Message 2</h2>
      <p>Message 2 is all about being message 2 and has nothing to do with any other messages.</p>
      <p>
        <button id="close2" class="buttonControl" aria-controls="m2">
            Close 
            <span class="hidden">Message 2</span>
        </button>
    </p>
</div>

<div id="m3" class="message" role="region" aria-labelledby="m3-label" tabindex="-1" aria-expanded="false">
       <h2 id="m3-label">Message 3</h2>
       <p>Message 3 is all about being message 3 and has nothing to do with any other messages.</p>
       <p>
         <button id="close3" class="buttonControl" aria-controls="m3">
            Close 
            <span class="hidden">Message 3</span>
         </button>
       </p>
</div>

<div id="m4" class="message" role="region" aria-labelledby="m4-label" tabindex="-1" aria-expanded="false">
       <h2 id="m4-label">Message 4</h2>
       <p>Message 4 is all about being message 4 and has nothing to do with any other messages.</p>
       <p>
         <button id="close4" class="buttonControl" aria-controls="m4">
            Close 
            <span class="hidden">Message 4</span>
         </button>
       </p>
</div>
"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};
$(document).ready(function() {

   var hs1 = new OAA_EXAMPLES.hideShow('open1', 'close1');
   var hs2 = new OAA_EXAMPLES.hideShow('open2', 'close2');
   var hs3 = new OAA_EXAMPLES.hideShow('open3', 'close3');
   var hs4 = new OAA_EXAMPLES.hideShow('open4', 'close4');
  
}); // end ready()

/**
* @constructor hideShow
*
* @memberOf OAA_EXAMPLES
*
* @desc the constructor for a hideShow widget. It accepts two html IDs:
* 1. the button to toggle the region
* 2. A close button within the region to hide it and return focus to the toggle button
*
* The widget moves focus to the region when expanding it, and returns focus to the toggle button
* when closing it.
*
* @param {string} toggleID - the html ID of the toggle button to attach to
*
* @param {string} closeID - the html ID of the close button to attach to
*
* @return {N/A}
*/

/**
* @constructor Internal Properties
*
* @property {object} $toggle - jquery object pointer to the toggleID
* @property {object} $close - jquery object pointer to the closeID
* @property {object} $region - jquery object pointer to the aria controls
*/

OAA_EXAMPLES.hideShow = function(toggleID, closeID) {

   this.$toggle = $('#' + toggleID);
   this.$close = $('#' + closeID);
   this.$region = $('#' + this.$toggle.attr('aria-controls'));

   this.keys = {
               enter: 13,
               space: 32
               };

   this.toggleSpeed = 100;

   // bind handlers
   this.bindHandlers();

} // end hidShow() constructor

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers to the hideShow region
*
* return {N/A}
*/

OAA_EXAMPLES.hideShow.prototype.bindHandlers = function() {

   var thisObj = this;

   this.$toggle.click(function(e) {

      thisObj.toggleRegion();

      e.stopPropagation();
      return false;
   });

   this.$close.click(function(e) {

      thisObj.hideRegion();

      e.stopPropagation();
      return false;
   });
}

/** 
* @method hideRegion
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to hide an expanded region and return focus to the toggle button
*
* return {N/A}
*/

OAA_EXAMPLES.hideShow.prototype.hideRegion = function() {

   // hide the region and update the aria-expanded attribute
   this.$region.hide().attr('aria-expanded', 'false');

   // update the button label
   this.$toggle.find('span').html('Show');

   // return focus to the toggle button
   this.$toggle.focus();

} // end hideRegion()

/**
* @method toggleRegion
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to toggle the display of the hideShow region
*
* return {N/A}
*/

OAA_EXAMPLES.hideShow.prototype.toggleRegion = function() {

      var thisObj = this;

		// toggle the region
		this.$region.slideToggle(this.toggleSpeed, function() {

			if ($(this).attr('aria-expanded') == 'false') { // region is collapsed

				// update the aria-expanded attribute of the region
				$(this).attr('aria-expanded', 'true');

				// move focus to the region
				$(this).focus();

				// update the button label
				thisObj.$toggle.find('span').html('Hide');

			}
			else { // region is expanded

				// update the aria-expanded attribute of the region
				$(this).attr('aria-expanded', 'false');

				// update the button label
				thisObj.$toggle.find('span').html('Show');
			}
		});

} // end toggleRegion()

"""

example_obj.style       = """
.hidden {
    display: none; 
}

ul.msglinks {
   list-style: none;
}
div.message
{
  display: none;
  margin: .5em;
  padding: .5em; 
  border: 2px solid #880000;
  width: 40em;
}

div#m1 {
  background-color: #ffefef;
}

div#m2 {
  background-color: #efffef;
}

div#m3 {
  background-color: #efefff;
}

div#m4 {
  background-color: #efffff;
}

a.buttonControl {
  color: #004400;
  text-decoration: none;
  border-bottom: 1px solid #004400;
}

a.buttonControl:hover,
a.buttonControl:active,
a.buttonControl:focus {
  color: #880000;
  border-bottom: 2px solid #880000;
}
"""

example2 = create_example(example_obj)

# =============================
# Example 3
# =============================

order += 1

example_obj             = example_object()
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order          = order
example_obj.title       = 'Hide/Show: Region is exclusive'
example_obj.permanent_slug = 'hideshow3'

example_obj.a11y_features = """
Simple example of hiding and showing regions using aria-expanded. aria-controls is used to maintain markup associations. Only one region may be displayed at a time.'
"""
example_obj.keyboard    = """
* Tab: Move between button items and text area.
* Enter or space: Toggle display of hide/show regions.
"""

example_obj.markup = [m1,m2,m3,m4,m5]

example_obj.html        = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<h2>List of Messages</h2>

<ul class="controls">
  <li role="button" aria-controls="m1" aria-expanded="false" tabindex="0">
         <span>Show</span> 
         Message 1
  </li> 
  <li role="button" aria-controls="m2" aria-expanded="false" tabindex="0">
         <span>Show</span> 
         Message 2
  </li> 
  <li role="button" aria-controls="m3" aria-expanded="false" tabindex="0">
         <span>Show</span> 
         Message 3
  </li> 
  <li role="button" aria-controls="m4" aria-expanded="false" tabindex="0">
         <span>Show</span> 
         Message 4
  </li> 
</ul>

<div id="region_wrapper">
   <div id="m1" class="message" tabindex="-1" role="region" aria-labelledby="m1-label" aria-hidden="true">
       <h2 id="m1-label">Message 1</h2>
       <p>Message 1 is all about being message 1 and has nothing to do with any other messages.</p>
   </div>

   <div id="m2" class="message" role="region" aria-labelledby="m2-label" tabindex="-1" aria-hidden="true">
         <h2 id="m2-label">Message 2</h2>
         <p>Message 2 is all about being message 2 and has nothing to do with any other messages.</p>
   </div>

   <div id="m3" class="message" role="region" aria-labelledby="m3-label" tabindex="-1" aria-hidden="true">
          <h2 id="m3-label">Message 3</h2>
          <p>Message 3 is all about being message 3 and has nothing to do with any other messages.</p>
   </div>

   <div id="m4" class="message" role="region" aria-labelledby="m4-label" tabindex="-1" aria-hidden="true">
          <h2 id="m4-label">Message 4</h2>
          <p>Message 4 is all about being message 4 and has nothing to do with any other messages.</p>
   </div>
</div>

"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};
$(document).ready(function() {
   var keys = {
            enter: 13,
            space: 32
            };

   var $rgns = $('message');

   $('li').keydown(function(e) {

      if (e.altKey||e.ctrlKey||e.shiftKey) {
            // do nothing
      }
      else if (e.keyCode == keys.enter || e.keyCode == keys.space) {

         var $rgn =  $('#' + $(this).attr('aria-controls'));

         if ($(this).attr('aria-expanded') == 'true') {

            $(this).attr('aria-expanded', 'false');
            $rgn.attr('aria-hidden', 'true');

            $(this).find('span').html('Show');
         }
         else {
            $(this).attr('aria-expanded', 'true');
            $rgn.attr('aria-hidden', 'false');

            $(this).siblings().attr('aria-expanded', 'false');
            $rgn.siblings().attr('aria-hidden', 'true');

            $(this).siblings().find('span').html('Show');
            $(this).find('span').html('Hide');
         }

         e.stopPropagation();
         return false;
      }

      return true;
   });
  
   $('li').click(function(e) {

         var $rgn =  $('#' + $(this).attr('aria-controls'));

         if ($(this).attr('aria-expanded') == 'true') {

            $(this).attr('aria-expanded', 'false');
            $rgn.attr('aria-hidden', 'true');

            $(this).find('span').html('Show');
         }
         else {
            $(this).attr('aria-expanded', 'true');
            $rgn.attr('aria-hidden', 'false');

            $(this).siblings().attr('aria-expanded', 'false');
            $rgn.siblings().attr('aria-hidden', 'true');

            $(this).siblings().find('span').html('Show');
            $(this).find('span').html('Hide');
         }

      e.stopPropagation();
      return false;
   });
}); // end ready()
"""

example_obj.style       = """
.hidden {
    display: none; 
}

ul.controls {
   margin: 10px;
   padding: 0;
   list-style: none outside none;
}
ul.controls li {
   float: left;
   margin-bottom: 5px;
   padding: 5px 10px;
   width: 130px;
   text-align: center;
   border: 1px solid black;
}
ul.controls li {
   color: #004400;
   text-decoration: none;
}

ul.controls li:hover,
ul.controls li:active,
ul.controls li:focus {
   font-weight: bold;
   background-color: #fc3;
}
ul.controls li[aria-expanded="true"] {
   font-weight: bold;
}

div#region_wrapper {
   clear: both;
   width: 660px;
   height: 124px;
   background-color: #ccc;
   border: 1px solid black;
}
div.message
{
   padding: .5em; 
   border: 2px solid #880000;
   width: 40em;
}

div.message[aria-hidden="true"] {
   display: none;
}

div#m1 {
   background-color: #ffefef;
}

div#m2 {
   background-color: #efffef;
}

div#m3 {
   background-color: #efefff;
}

div#m4 {
  background-color: #efffff;
}
"""

example3 = create_example(example_obj)