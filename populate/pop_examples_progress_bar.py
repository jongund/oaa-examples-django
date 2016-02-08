"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples import *

order = 1

spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute="role", value='slider')
m2 = ElementDefinition.objects.get(spec=spec_aria10, attribute="aria-valuemax")
m3 = ElementDefinition.objects.get(spec=spec_aria10, attribute="aria-valuemin")
m4 = ElementDefinition.objects.get(spec=spec_aria10,  attribute="aria-valuenow")

# =============================
# Example 1
# =============================

example_obj             = example_object()
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order = order
example_obj.title       = 'Progress Bar'
example_obj.permanent_slug = 'progressbar1'

example_obj.a11y_features = """
Simple examples of a progress bar widget.
"""
example_obj.keyboard    = """

"""

example_obj.markup = [m1,m2,m3,m4]

example_obj.html        = """
  <h3>Progressbar Example 1</h3>
 
  <button id="id_pb1_control">Start Example</button>
    <div label for="id_pb1" class="hidden">Example 1 Progressbar</div>
    <div id="id_pb1" class="progress" role="progressbar" aria-labelledby="pb1_label" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" tabindex="0"></div>

 
"""
example_obj.script      = """

var OAA_EXAMPLES = OAA_EXAMPLES || {};  // Class of Open Ajax Alliance methods used in the examples

var g_progress1 = null;
var g_$startButton = null;

var g_intervalID = null; // the handle of the interval set when the example is running
var g_curVal = 0;
var g_maxVal = 300;

/**
* @method increment
*
* @memberOf OAA_EXAMPLES
*
* @desc increments the value and passes the new value to the progress bar
* widget. If the progress bar is at 100%, it stops the increment.
*
* @return {N/A}
*/

OAA_EXAMPLES.doUpdate = function() {

   if (g_progress1.getProgress() == 100) {
      clearInterval(g_intervalID);
      g_intervalID = null;

      // make sure that the progress bar shows that it is full
      g_progress1.$progDiv.css('width', '100%');

      g_curVal = 0;
      g_$startButton.html('Reset Example');
      return;
   }

   g_curVal = g_curVal + 1;
   g_progress1.setValue(g_curVal);
}

$(document).ready(function() {

   var running = false; // true if example is running

  // progress1 is a progress bar
  g_progress1 = new OAA_EXAMPLES.progressbar('id_pb1', g_maxVal, true);

   g_$startButton = $('#id_pb1_control');

   // bind a click handler to the start  button
   g_$startButton.click(function(e) {

      if (g_progress1.getProgress() == 100) {
         g_progress1.setValue(0);
      }
            
      if (running == true) {
         clearInterval(g_intervalID);
         g_intervalID = null;
         g_$startButton.html('Start Example');
         running = false;
      }
      else {
         // create an interval timer to increment the count every second
         g_intervalID = setInterval("OAA_EXAMPLES.doUpdate()", 100);

         g_$startButton.html('Stop Example');

         running = true;
      }
   });
  
}); // end document ready


/**
* @constructor progressbar
*
* @memberOf OAA_EXAMPLES
*
* @desc a class to define an ARIA-enabled progressbar widget.
*
* @param {string} container_id - the containing div for the progressbar
* @param {integer} max - the maximum value for the values being set. Used to calculate percent progress
* @param {boolean} showVal - true if the current progress value should be shown
*
* @return {N/A}
*/

OAA_EXAMPLES.progressbar = function(container_id, max, showVal) {

  // define progressbar object properties

  this.$container = $('#' + container_id);
  this.valMax = max;
  this.showVal = showVal;
  this.divWidth = 0;

  // Store the size of the progress bar
  this.width = this.$container.width();

  // Store the page position of the widget

  this.left = Math.round(this.$container.offset().left);
  this.top = Math.round(this.$container.offset().top);

   // Create and initialize the progress indicator
   this.$container.append('<div id="progDiv" class="progressIndicator"></div>');
   this.$progDiv = $('#progDiv');
   this.$progDiv.css('width', '0%');

   // Create and initialize the value box
   this.$container.append('<div id="progVal" class="progressVal" aria-hidden="false"></div>');
   this.$progVal = $('#progVal');
   this.$progVal.html('0%');

   if (this.showVal == false) {
      this.$progVal.addClass('hidden').attr('aria-hidden', 'true');
   }

} // end progressbar constructor

/**
* @method setValue
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the value of the progress bar.
*
* @param {integer} val - the new value to calculate the progress from
*
* @return {N/A}
*/

OAA_EXAMPLES.progressbar.prototype.setValue = function(val)  {

   var percent = val * 100 / this.valMax;

   if (percent <= 100.0) {
      this.$container.attr('aria-valuenow', Math.round(percent));
      this.$progDiv.css('width', percent + '%'); //Math.round(percent) + '%');
      this.$progVal.html(this.$container.attr('aria-valuenow') + '%');
   }
}

/**
* @method getProgress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to return the percent progress
*
* @return {integer} Returns the percent progress in integer form (e.g. 50 represents 50%)
*/

OAA_EXAMPLES.progressbar.prototype.getProgress = function()  {

   return this.$container.attr('aria-valuenow');
}

/**
* @method positionHandle
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to position a handle at the specified value for the
* progressbar. If showVal is true, it also positions and updates the displayed value container.
*
* @param {object} $handle - a pointer to the handle jQuery object to manipulate
*
* @param {integer} val - the new value of the progressbar
*
* @return {N/A}
*/

OAA_EXAMPLES.progressbar.prototype.positionHandle = function($handle, val) {

  var handleHeight = $handle.outerHeight(); // the total height of the handle
  var handleWidth = $handle.outerWidth(); // the total width of the handle
  var handleOffset; // the distance from the value position for centering the handle
  var xPos; // calculated horizontal position of the handle;
  var yPos; // calculated vertical position of the handle;
  var valPos; //calculated new pixel position for the value;

    
   // calculate the horizontal pixel position of the specified value
   valPos = ((val - this.min) / (this.max - this.min)) * this.width + this.left;

   xPos = Math.round(valPos - (handleWidth / 2));
   yPos = Math.round(this.top + (this.height / 2) - (handleHeight / 2));

  // Set the position of the handle
  $handle.css('top', yPos + 'px');
  $handle.css('left', xPos + 'px');

  // Set the aria-valuenow position of the handle
  $handle.attr('aria-valuenow', val);

  // Update the stored handle values
  if (/1$/.test($handle.attr('id')) == true) {
    // first handle
    this.val1 = val;
  }
  else {
    // second handle
    this.val2 = val;
  }

  // if showVal is true, update the value container
  if (this.showVals == true) {
    this.updateValBox($handle, Math.round(valPos));
  }

} // end positionHandle()

/**
* @method updateValBox
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to reposition a handle value box and update its contents
*
* @return {N/A}
*/

OAA_EXAMPLES.progressbar.prototype.updateValBox = function() {

  var $valBox = $('#' + $handle.attr('id') + '_val');

  var xPos; // horizontal pixel position of the box
  var yPos; // vertical pixel position of the box

  // Set the position of the handle
   var boxWidth = $valBox.outerWidth();

   yPos = $handle.css('top');

   // Adjust the horizontal position to center the value box on the value position
   xPos = Math.round(valPos - (boxWidth / 2)) + 'px';

  // Set the position of the value box
  $valBox.css('top', yPos);
  $valBox.css('left', xPos);

  // Set the text in the box to the handle value
  $valBox.text($handle.attr('aria-valuenow'));

} // end updateValBox()
"""

example_obj.style       = """
/* CSS Document */

div.progress {
  margin: 50px;
  padding: 0;
  width: 540px;
  height: 20px;
  background-color: #eef;
  border: 2px solid black;
}

div.progressIndicator {
  margin: 0;
  padding: 0;
  background-color: #fbcb46;
  position: relative;
  top: 0;
  left: 0px;

  width: 10%;
  height: 100%;
}
  
div.progressVal  {
  position: relative;
  top: -18px;
  margin: 0;
  padding: 0;
  height: 20px;
  text-align: center;
  font-weight: bold;
}

.hidden {
  position: absolute !important;
  top: -20em;
  left: -200em;
}

.focus {
  background-color: #eee !important;
}
"""

example1 = create_example(example_obj)