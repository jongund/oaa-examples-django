"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples import *

order = 1

spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec = spec_aria10, attribute='role', value='tooltip')
m2 = ElementDefinition.objects.get(spec = spec_aria10, attribute='aria-describedby')
m3 = ElementDefinition.objects.get(spec = spec_aria10, attribute='aria-hidden')
m4 = ElementDefinition.objects.get(spec = spec_aria10, attribute='aria-labelledby')
m5 = ElementDefinition.objects.get(spec = spec_aria10, attribute='aria-required')

# =============================
# Example 1
# =============================

example_obj             = example_object()
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order          = order
example_obj.title       = 'Tooltip'
example_obj.permanent_slug = 'tooltip1'

example_obj.a11y_features = """
Simple example of a tooltip widget
"""

example_obj.keyboard    = """
"Based on the keyboard shortcuts defined in the AOL DHTML Style guide for tooltip":http://dev.aol.com/dhtml_style_guide/

    * Tab: When a form control receives focus a tooltip appears. The tooltip is hidden when the control loses focus.
    * ESCape: Closes tooltip. Once dismissed, mouse hover will display the tooltip as if the control does not have focus.

"""

example_obj.markup = [m1,m2,m3,m4,m5]

example_obj.html        = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<form action="#" method="post">

<h2>Create Account</h2>

  <div class="text">
     <label id="tp1-label" for="first">First Name:</label> 
	 <input type="text" id="first" name="first" size="20" aria-labelledby="tp1-label" aria-describedby="tp1" aria-required="false" />
     <div id="tp1" class="tooltip" role="tooltip" aria-hidden="true">Your first name is optional</div>
  </div>

  <div class="text">
     <label id="tp2-label" for="last">Last Name: </label> 
	 <input type="text" id="last" name="last" size="30" aria-labelledby="tp2-label" aria-describedby="tp2" aria-required="false" /> *
     <div id="tp2" class="tooltip" role="tooltip" aria-hidden="true">Your last name is a required field</div>
  </div>

  <div class="text">
     <label id="tp3-label" for="last">E-mail: </label> 
	 <input type="text" id="email" name="email" size="40" aria-labelledby="tp3-label" aria-describedby="tp3" aria-required="true" /> *
     <div id="tp3" class="tooltip" role="tooltip" aria-hidden="true">Your e-mail address will be your login name</div>
  </div>

  <div class="text">
     <label id="tp4-label" for="last">Password: </label> 
	 <input type="password" id="password" name="password" size="20" aria-labelledby="tp4-label" aria-describedby="tp4" aria-required="true" /> *
     <div id="tp4" class="tooltip" role="tooltip" aria-hidden="true">Password must be at least 8 character long and contain at least one capitol letter and a number</div>
  </div>
  
  <div class="text">
     <label id="tp5-label" for="last">Password Confirm: </label> 
	 <input type="password" id="confirm" name="confirm" size="20" aria-labelledby="tp5-label" aria-describedby="tp5" aria-required="true" /> *

     <div id="tp5" class="tooltip" role="tooltip" aria-hidden="true">Confirmation password must match password</div>
  </div>
    
  
  <input type="submit" value="Create Account" onclick="return false"/>


</form>
"""
example_obj.script      = """
var KEY_ESC = 27;
var OAA_EXAMPLES = OAA_EXAMPLES || {};
$(document).ready(function() {

	var tips = []; // an array of tooltips

	// create a tooltip object for each input
	$('div.text input').each(function(index) {
		tips[index] = new OAA_EXAMPLES.tooltip($(this));
	});
		
}); // end ready event

/**
* @constructor tooltip
*
* @memberOf OAA_EXAMPLES
*
* @desc a tooltip widget. It requires the element that has the tooltip to reference
* the tooltip via aria-describedby. Normally this is a div that contains text
*
* @param {object} $id - the jquery object of the input or other element to bind the widget to
*
* @return {N/A}
*/

/**
* @constructor Internal Properties
* @property {string} $id - jquery reference to object
* @property {string} $tip - 
*
* @proerty {boolean} mouseover - set to tru if the tooltop was displayed via mouseover. reset on mouseout.
*
* @property {boolean} focus - set to true of the input has focus (prevent hide on mouseout)
*
* @property {boolean} dismissed - set to true if the user dismissed the tooltip with the esc key. Reset on blur.
*/

OAA_EXAMPLES.tooltip = function($id) {

	// define the object properties

	this.$id = $id;
	this.$tip = $('#' + $id.attr('aria-describedby'));
	this.mouseover = false; 
	this.focus = false; 
	this.dismissed = false;

   this.position = {
                  top: this.$id.offset().top,
                  left: this.$id.offset().left + this.$id.width() + 10
                  }


	// bind key handlers
	this.bindHandlers();

   // perform initialization
   this.init();

} // end tooltip() constructor

/**
* @method init
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to perform iniatialization for the widget.
*
* return {N/A}
*/

OAA_EXAMPLES.tooltip.prototype.init = function() {

	// hide the tooltip
	this.hideTip();

   // change the positioning of the tooltip to absolute
   this.$tip.css('position', 'absolute');

   // set the position of the tooltip
   this.$tip.css('top', this.position.top + 'px');
   this.$tip.css('left', this.position.left + 'px');

} // end init()

/**
* @method showTip
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to display the tooltip
*
* @return {N/A}
*/

OAA_EXAMPLES.tooltip.prototype.showTip = function() {

	// display the tooltip
	this.$tip.css('display', 'inline').attr('aria-hidden', 'false');

} // end showtip()

/**
* @method hideTip
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to hide the tooltip
*
* @return {N/A}
*/

OAA_EXAMPLES.tooltip.prototype.hideTip = function() {

	// hide the tooltip
	this.$tip.hide().attr('aria-hidden', 'true');

} // end hidetip()

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers to the input
*
* @return {N/A}
*/

OAA_EXAMPLES.tooltip.prototype.bindHandlers = function() {

	var thisObj = this;

	this.$id.keydown(function(e) {
			return thisObj.handleKeyDown($(this), e);
	});

	this.$id.mouseover(function(e) {
			return thisObj.handleMouseOver($(this), e);
	});

	this.$id.mouseout(function(e) {
			return thisObj.handleMouseOut($(this), e);
	});

	this.$id.focus(function(e) {
			return thisObj.handleFocus($(this), e);
	});

	this.$id.blur(function(e) {
			return thisObj.handleBlur($(this), e);
	});

} // end bindHandlers()

/**
* @method handleKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for the input
*
* @param {object} $id - the jquery object of the element firing event
*
* @param {object} e - the event object associated with the event
*
* @return {boolean} returns false if processing; true if doing nothing
*/

OAA_EXAMPLES.tooltip.prototype.handleKeyDown = function($id, e) {

	if (e.altKey || e.shiftKey || e.ctrlKey) {
		// do nothing
		return true;
	}

	if (e.keyCode == KEY_ESC) {
		this.hideTip();
		this.dismissed = true;
		e.stopPropagation();
		return false;
	}

	return true;

} // end handleKeyDown()

/**
* @method handleMouseOver
*
* @memberOf OAA_EXAMPLES
*
* @param {object} $id - the jquery object of the element firing event
*
* @param {object} e - the event object associated with the event
*
* @return {boolean} returns false
*/

OAA_EXAMPLES.tooltip.prototype.handleMouseOver = function($id, e) {

	this.showTip();

	// set the mouseover flag to prevent blur dismissing tooltip
	this.mouseover = true;

	e.stopPropagation();
	return false;

} // end handleMouseOver()

/**
* @method handleMouseOut
*
* @memberOf OAA_EXAMPLES
*
* @desc  a member function to hide the tooltip on mouseout. If the input has
* focus and the user did not dismiss the tooltip, the tooltip is not hidden.
*
* @param {object} $id - the jquery object of the element firing event
*
* @param {object} e - the event object associated with the event
*
* @return {boolean} returns false
*/

OAA_EXAMPLES.tooltip.prototype.handleMouseOut = function($id, e) {

	if (this.dismissed == true || this.focus == false) {
		this.hideTip();
	}

	// reset the mouseover flag
	this.mouseover = false;

	e.stopPropagation();
	return false;

} // end handleMouseOut()

/**
* @method handleFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to display the tooltip on focus
*
* @param {object} $id - the jquery object of the element firing event
*
* @param {object} e - the event object associated with the event
*
* @return {boolean} returns false
*/

OAA_EXAMPLES.tooltip.prototype.handleFocus = function($id, e) {

	this.showTip();

	// set the focus flag to prevent mouseout from hiding the tooltip as long
	// as the input has focus
	this.focus = true;

	e.stopPropagation();
	return false;

} // end handleFocus()

/**
* @method handleBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to hide the tooltip on blur. The tooltip is not
* hidden if the mouseover flag is true (i.e. tooltip was displayed via mouseover).
*
* @param {object} $id - the jquery object of the element firing event
*
* @param {object} e - the event object associated with the event
*
* @return {boolean} returns false
*/

OAA_EXAMPLES.tooltip.prototype.handleBlur = function($id, e) {

	if (this.mouseover == false) {
		this.hideTip();
	}

	// reset the focus and dismissed flags
	this.focus = false;
	this.dismissed = false;

	e.stopPropagation();
	return false;

} // end handleBlur()
"""

example_obj.style       = """
div.text {
   margin: 5px;
   height: 1.5em;
}
div.text label {
   margin: 0;
   margin-top: 5px;
   padding: 0;
   padding-right: 5px;
   width: 10em;
   text-align: right;
   float: left;
}
div.text input {
   margin-top: 2px;
   float: left;
}

div.text input:focus,
div.text input:active {
   border: 1px solid purple;
}
div.tooltip {
  margin-left: 10px;
  padding: 2px 5px;
  background: #ffe;
  z-index: 10;
  border: 2px solid black;
}

input[type=submit] {
   padding: 0;
   margin: 0;
   margin-top: 1px;
   margin-left: 11em;
   font-size: 100% !important;
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
example_obj.title       = 'Tooltip: ARIA CSS selectors'
example_obj.permanent_slug = 'tooltip2'

example_obj.a11y_features = """
Simple example of a tooltip widget using ARIA CSS selectors.
"""
example_obj.keyboard    = """
"Based on the keyboard shortcuts defined in the AOL DHTML Style guide for tooltip":http://dev.aol.com/dhtml_style_guide/

    * Tab: When a form control receives focus a tooltip appears. The tooltip is hidden when the control loses focus.
    * ESCape: Closes tooltip. Once dismissed, mouse hover will display the tooltip as if the control does not have focus.

"""

example_obj.markup = [m1,m2,m3,m4,m5]

example_obj.html        = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<form action="#" method="post">

<h2>Create Account</h2>

  <div class="text">
     <label id="tp1-label" for="first">First Name:</label> 
	 <input type="text" id="first" name="first" size="20" aria-labelledby="tp1-label" aria-describedby="tp1" aria-required="false" />
     <div id="tp1" class="tooltip" role="tooltip" aria-hidden="true">Your first name is a optional</div>
  </div>

  <div class="text">
     <label id="tp2-label" for="last">Last Name: </label> 
	 <input type="text" id="last" name="last" size="30" aria-labelledby="tp2-label" aria-describedby="tp2" aria-required="false" /> *
     <div id="tp2" class="tooltip" role="tooltip" aria-hidden="true">Your last name is a optional</div>
  </div>

  <div class="text">
     <label id="tp3-label" for="last">E-mail: </label> 
	 <input type="text" id="email" name="email" size="40" aria-labelledby="tp3-label" aria-describedby="tp3" aria-required="true" /> *
     <div id="tp3" class="tooltip" role="tooltip" aria-hidden="true">Your e-mail address will be your login name</div>
  </div>

  <div class="text">
     <label id="tp4-label" for="last">Password: </label> 
	 <input type="password" id="password" name="password" size="20" aria-labelledby="tp4-label" aria-describedby="tp4" aria-required="true" /> *
     <div id="tp4" class="tooltip" role="tooltip" aria-hidden="true">Password must be at least 8 character long and contain at least one capitol letter and a number</div>
  </div>
  
  <div class="text">
     <label id="tp5-label" for="last">Password Confirm: </label> 
	 <input type="password" id="confirm" name="confirm" size="20" aria-labelledby="tp5-label" aria-describedby="tp5" aria-required="true" /> *

     <div id="tp5" class="tooltip" role="tooltip" aria-hidden="true">Confirmation password must match password</div>
  </div>
    
  
  <input type="submit" value="Create Account" onclick="return false"/>


</form>
"""
example_obj.script      = """
var KEY_ESC = 27;
var OAA_EXAMPLES = OAA_EXAMPLES || {};
$(document).ready(function() {

	var tips = []; // an array of tooltips

	// create a tooltip object for each input
	$('div.text input').each(function(index) {
		tips[index] = new OAA_EXAMPLES.tooltip($(this));
	});
		
}); // end ready event

/**
* @constructor tooltip
*
* @memberOf OAA_EXAMPLES
*
* @desc a tooltip widget. It requires the element that has the tooltip to reference
* the tooltip via aria-describedby. Normally this is a div that contains text
*
* @param {object} $id - the jquery object of the input or other element to bind the widget to
*
* @return {N/A}
*/

/**
* @constructor Internal Properties
*
* @property {string} $id - jquery reference to object
* @property {string} $tip - 
*
* @proerty {boolean} mouseover - set to tru if the tooltop was displayed via mouseover. reset on mouseout.
*
* @property {boolean} focus - set to true of the input has focus (prevent hide on mouseout)
*
* @property {boolean} dismissed - set to true if the user dismissed the tooltip with the esc key. Reset on blur.
*/

OAA_EXAMPLES.tooltip = function($id) {

	// define the object properties

	this.$id = $id;
	this.$tip = $('#' + $id.attr('aria-describedby'));
	this.mouseover = false;
	this.focus = false; 
	this.dismissed = false;

   this.position = {
                  top: this.$id.offset().top,
                  left: this.$id.offset().left + this.$id.width() + 10
                  }


	// bind key handlers
	this.bindHandlers();

   // perform initialization
   this.init();

} // end tooltip() constructor

/**
* @method init
*
* @memberOf OAA_EXAMPLEs
*
* @desc a member function to perform iniatialization for the widget.
*
* return {N/A}
*/

OAA_EXAMPLES.tooltip.prototype.init = function() {

	// hide the tooltip
	this.hideTip();

   // change the positioning of the tooltip to absolute
   this.$tip.css('position', 'absolute');

   // set the position of the tooltip
   this.$tip.css('top', this.position.top + 'px');
   this.$tip.css('left', this.position.left + 'px');

} // end init()

/**
* @method showTip
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to display the tooltip
*
* @return {N/A}
*/

OAA_EXAMPLES.tooltip.prototype.showTip = function() {

	// display the tooltip
	this.$tip.attr('aria-hidden', 'false');

} // end showtip()

/**
* @method hideTip
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to hide the tooltip
*
* @return {N/A}
*/

OAA_EXAMPLES.tooltip.prototype.hideTip = function() {

	// hide the tooltip
	this.$tip.attr('aria-hidden', 'true');

} // end hidetip()

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers to the input
*
* @return {N/A}
*/

OAA_EXAMPLES.tooltip.prototype.bindHandlers = function() {

	var thisObj = this;

	this.$id.keydown(function(e) {
			return thisObj.handleKeyDown($(this), e);
	});

	this.$id.mouseover(function(e) {
			return thisObj.handleMouseOver($(this), e);
	});

	this.$id.mouseout(function(e) {
			return thisObj.handleMouseOut($(this), e);
	});

	this.$id.focus(function(e) {
			return thisObj.handleFocus($(this), e);
	});

	this.$id.blur(function(e) {
			return thisObj.handleBlur($(this), e);
	});

} // end bindHandlers()

/**
* @method handleKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for the input
*
* @param {object} $id - the jquery object of the element firing event
*
* @param {object} e - the event object associated with the event
*
* @return {boolean} returns false if processing; true if doing nothing
*/

OAA_EXAMPLES.tooltip.prototype.handleKeyDown = function($id, e) {

	if (e.altKey || e.shiftKey || e.ctrlKey) {
		// do nothing
		return true;
	}

	if (e.keyCode == KEY_ESC) {
		this.hideTip();
		this.dismissed = true;
		e.stopPropagation();
		return false;
	}

	return true;

} // end handleKeyDown()

/**
* @method handleMouseOver
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to display the tooltip on mouseover
*
* @param {object} $id - the jquery object of the element firing event
*
* @param {object} e - the event object associated with the event
*
* @return {boolean} returns false
*/

OAA_EXAMPLES.tooltip.prototype.handleMouseOver = function($id, e) {

	this.showTip();

	// set the mouseover flag to prevent blur dismissing tooltip
	this.mouseover = true;

	e.stopPropagation();
	return false;

} // end handleMouseOver()

/**
* @method handleMouseOut
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to hide the tooltip on mouseout. If the input has
* focus and the user did not dismiss the tooltip, the tooltip is not hidden.
*
* @param {object} $id - the jquery object of the element firing event
*
* @param {object} e - the event object associated with the event
*
* @return {boolean} returns false
*/

OAA_EXAMPLES.tooltip.prototype.handleMouseOut = function($id, e) {

	if (this.dismissed == true || this.focus == false) {
		this.hideTip();
	}

	// reset the mouseover flag
	this.mouseover = false;

	e.stopPropagation();
	return false;

} // end handleMouseOut()

/**
* @method handleFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to display the tooltip on focus
*
* @param {object} $id - the jquery object of the element firing event
*
* @param {object} e - the event object associated with the event
*
* @return {boolean} returns false
*/

OAA_EXAMPLES.tooltip.prototype.handleFocus = function($id, e) {

	this.showTip();

	// set the focus flag to prevent mouseout from hiding the tooltip as long
	// as the input has focus
	this.focus = true;

	e.stopPropagation();
	return false;

} // end handleFocus()

/**
* @method handleBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to hide the tooltip on blur. The tooltip is not
* hidden if the mouseover flag is true (i.e. tooltip was displayed via mouseover).
*
* @param {object} $id - the jquery object of the element firing event
*
* @param {object} e - the event object associated with the event
*
* @return {boolean} returns false
*/

OAA_EXAMPLES.tooltip.prototype.handleBlur = function($id, e) {

	if (this.mouseover == false) {
		this.hideTip();
	}

	// reset the focus and dismissed flags
	this.focus = false;
	this.dismissed = false;

	e.stopPropagation();
	return false;

} // end handleBlur()
"""

example_obj.style       = """
div.text {
   margin: 5px;
   height: 1.5em;
}
div.text label {
   margin: 0;
   margin-top: 5px;
   padding: 0;
   padding-right: 5px;
   width: 10em;
   text-align: right;
   float: left;
}
div.text input {
   margin-top: 2px;
   float: left;
}

div.text input:focus,
div.text input:active {
   border: 1px solid purple;
}
div.tooltip {
  display: inline;
  margin-left: 10px;
  padding: 2px 5px;
  background: #ffe;
  z-index: 10;
  border: 2px solid black;
}
div.tooltip[aria-hidden="true"] {
  display: none;
}

input[type=submit] {
   padding: 0;
   margin: 0;
   margin-top: 1px;
   margin-left: 11em;
   font-size: 100% !important;
}
"""

example2 = create_example(example_obj)