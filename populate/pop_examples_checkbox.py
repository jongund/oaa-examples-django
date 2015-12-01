from django.core.exceptions import ObjectDoesNotExist
from pop_examples import *

order = 1

spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='checkbox')
m2 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='presentation')
m3 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-checked')
m4 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-describedby')
m5 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-labelledby')


# =============================
# Example 1
# =============================

example_obj = example_object()
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order = order
example_obj.title = 'Checkbox using IMG elements for visual state'
example_obj.permanent_slug = 'checkbox1'

example_obj.a11y_features = """
Simple example of a checkbox widget using inline images to display the visual state of the boxes in the group.
"""
example_obj.keyboard    = """
* Tab: Move between button items and text area.
* Enter or space: Toggle aria-checked state of checkbox with keyboard focus.
"""

example_obj.markup = [m1,m2,m3,m4,m5]

example_obj.html        = """
<h3 id="id_cond">Sandwich Condiments</h3>

<ul class="checkboxes" 
    aria-labelledby="id_cond">

  <li role="checkbox" 
      tabindex="0"
      aria-checked="false"
      aria-describedby="id_cond_desc1">
      <img src="{{EXAMPLE_MEDIA}}images/checkbox-unchecked-black.png" role="presentation">
      Lettuce
  </li>
            
  <li role="checkbox" 
      tabindex="0"
      aria-checked="true" 
      aria-describedby="id_cond_desc2">
      <img src="{{EXAMPLE_MEDIA}}images/checkbox-checked-black.png" role="presentation">
      Tomato
   </li>
            
   <li role="checkbox" 
       tabindex="0"
       aria-checked="true" 
       aria-describedby="id_cond_desc3">
       <img src="{{EXAMPLE_MEDIA}}images/checkbox-checked-black.png" role="presentation">
       Mustard
   </li>
            
   <li role="checkbox" 
       tabindex="0"
       aria-checked="true" 
       aria-describedby="id_cond_desc4">
       <img src="{{EXAMPLE_MEDIA}}images/checkbox-checked-black.png" role="presentation">
       Sprouts
  </li>            
   
</ul>
<div id="id_desc1" class="offscreen">The best available organic romaine lettuce grown locally.</div>
<div id="id_desc2" class="offscreen">These organically grown beef steak tomatoes are vide rippened.</div>
<div id="id_desc3" class="offscreen">This is a gourmet mustard from Germany.</div>
<div id="id_desc4" class="offscreen">These organically grown alfalfa sprouts are a great addition to any sandwich.</div>
"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};

$(document).ready(function() {

	var checkboxes = [];

	$('ul.checkboxes li').each(function(index) {
		if ($(this).attr('role') == 'checkbox') {
			checkboxes[index] = new OAA_EXAMPLES.checkbox($(this));
		};
	});

}); // end ready()

/**
* Function keyCodes() is an object to contain keycodes needed for the application
*/
function keyCodes() {
	this.space = 32;
}

/**
* @constructor checkbox
* 
* @memberOf OAA_EXAMPLES
*
* @desc a class constructor for the implementation of a checkbox widget.
* The element passed to checkbox() must contain an image tag that will be used to display
* the state of the checkbox.
*
* @param {String} id - the html id of the element to act as a checkbox
*
* @return {N/A}
*/

/**
* @private
* @constructor Internal Properties
*
* @memberOf OAA_EXAMPLES
* 
* @property {obj} id - the id assigned to the checkbox
* @property {obj} keys - the keycodes that are assigned
*/


OAA_EXAMPLES.checkbox = function($id) {

	// define object properties
	this.$id = $id;
	this.keys = new keyCodes();

	// bind event handlers
	this.bindHandlers();

} // end checkbox() constructor

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
* 
* @desc a member function to bind event handlers to the checkboxes in the checkbox group.
*
* @return {N/A}
*/

OAA_EXAMPLES.checkbox.prototype.bindHandlers = function() {

	var thisObj = this;

	// bind a click handler
	this.$id.click(function(e) {
		return thisObj.handleClick(e);
	});

	// bind a keydown handler
	this.$id.keydown(function(e) {
		return thisObj.handleKeyDown(e);
	});

	// bind a keypress handler
	this.$id.keypress(function(e) {
		return thisObj.handleKeyPress(e);
	});

	// bind a mouseover handler
	this.$id.mouseover(function(e) {
		return thisObj.handleMouseOver(e);
	});

	// bind a mouseout handler
	this.$id.mouseout(function(e) {
		return thisObj.handleMouseOut(e);
	});

	// bind a focus handler
	this.$id.focus(function(e) {
		return thisObj.handleFocus(e);
	});

	// bind a blur handler
	this.$id.blur(function(e) {
		return thisObj.handleBlur(e);
	});

} // end bindHandlers()

/**
* @method toggleState
* 
* @memberOf OAA_EXAMPLES
* 
* @desc a member function to toggle a checkbox state. This function sets the
* aria-checked property and changes the box image to display the new box state.
*
* @return {N/A}
*/

OAA_EXAMPLES.checkbox.prototype.toggleState = function() {

	var $img = this.$id.find('img');

	if (this.$id.attr('aria-checked') == 'true') {

		this.$id.attr('aria-checked', 'false');
		$img.attr('src','{{EXAMPLE_MEDIA}}images/checkbox-unchecked-black.png');
	}
	else {
		this.$id.attr('aria-checked', 'true');
		$img.attr('src','{{EXAMPLE_MEDIA}}images/checkbox-checked-black.png');
	}

} // end toggleState()

/**
* @method handleClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle click events for the checkbox.
*
* @param {obj} e - the event object associated with the keydown event
*
* @return {boolean} Returns false if processing; true of doing nothing
*/

OAA_EXAMPLES.checkbox.prototype.handleClick = function(e) {
		 
	if (e.altkey || e.ctrlKey || e.shiftKey) {
		// do nothing;
		return true;
	}

	// toggle the checkbox state
	this.toggleState();

	e.stopPropagation();
	return false;
	
} // end handleClick()
	
/**
* @method handleKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle keydown events for the checkbox.
*
* @param {obj} e - the event object associated with the keydown event
*
* @return {boolean} Returns false if processing; true of doing nothing
*/

OAA_EXAMPLES.checkbox.prototype.handleKeyDown = function(e) {
		 
	if (e.altkey || e.ctrlKey || e.shiftKey) {
		// do nothing;
		return true;
	}

	if( e.keyCode == this.keys.space ) {

		// toggle the checkbox state
		this.toggleState();

		e.stopPropagation();
		return false;
	} // endif

	return true;
	
} // end handleKeyDown()

/**
* @method handleKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle keypress events for the checkbox.
* This function is needed to consume events for browsers, such as Opera, that perform window
* manipulation on keypress events.
*
* @param {obj} e - the event object associated with the keydown event
*
* @return {boolean} Returns false if processing; true of doing nothing
*/

OAA_EXAMPLES.checkbox.prototype.handleKeyPress = function(e) {
		 
	if (e.altkey || e.ctrlKey || e.shiftKey) {
		// do nothing;
		return true;
	}

	if( e.keyCode == this.keys.space ) {
		// consume the event
		e.stopPropagation();
		return false;
	} // endif

	return true;
	
} // end handleKeyPress()

/**
* @method handleMouseOver
*
* @memberOf OAA_EXAMPLES
* 
* @desc a member function to handle mouseover events for the checkbox.
*
* @param {obj} e - the event object associated with the mouseover event
*
* @return {boolean} Returns false;
*/

OAA_EXAMPLES.checkbox.prototype.handleMouseOver = function(e) {
		 
	// if the box does not have the focus class add the hover highlight
	if (this.$id.not('.focus')) {
		this.$id.addClass('hover');
	}

	e.stopPropagation();
	return false;
	
} // end handleMouseOver()

/**
* @method handleMouseOut
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle mouseout events for the checkbox.
*
* @param {obj} e - the event object associated with the mouseout event
*
* @return {boolean} Returns false;
*/

OAA_EXAMPLES.checkbox.prototype.handleMouseOut = function(e) {
		 
	this.$id.removeClass('hover');

	e.stopPropagation();
	return false;
	
} // end handleMouseOut()

/**
* @method handleFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle focus events for the checkbox.
*
* @param {obj} e - the event object associated with the focus event
*
* @return {boolean} Returns true;
*/

OAA_EXAMPLES.checkbox.prototype.handleFocus = function(e) {
		 
	this.$id.addClass('focus');

	// remove the hover class if it is applied
	this.$id.removeClass('hover');

	return true;
	
} // end handleFocus()

/**
* @method handleBlur
*
* @memberOf OAA_EXAMPLES
* 
* @desc a member function to handle blur events for the checkbox.
*
* @param {obj} e - the event object associated with the blur event
*
* @return {boolean} Returns true;
*/

OAA_EXAMPLES.checkbox.prototype.handleBlur = function(e) {
		 
	this.$id.removeClass('focus');
	return true;
	
} // end handleBlur()
"""

example_obj.style       = """
ul.checkboxes {
   margin: 0;
   padding: 0;		
}

ul.checkboxes li   {
   margin: 2px 2px 2px 20px;
   padding: 2px; 
   list-style: none;
   width: 6em;	  
}
   
ul.checkboxes li.hover {
   margin: 2px 0px 2px 18px;
   padding: 0px 2px;
   border: 2px solid #777;
}

ul.checkboxes li.focus {
   margin: 2px 0px 2px 18px;
   padding: 0px 2px;
   border: 2px solid black;
}

.offscreen {
   position: absolute;
   left: -200em;
   top: -20em;
}
"""

example1 = create_example(example_obj)

# =============================
# Example 2
# =============================

order +=  1
example_obj = example_object()
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')

example_obj.order          = order
example_obj.title          = '@input[type=checkbox]@ - Labeling checkbox using @title@ attribute'
example_obj.permanent_slug = 'checkbox2'

example_obj.a11y_features = """
* Using the @title@ attribute to define @labels@ will work with assistive technologies but is not defined in the @HTML@ specifications
"""
example_obj.keyboard    = """
"""

example_obj.markup = [m1]

example_obj.html        = """
<div class="label">Select pizza toppings</div>
<ul class="checkbox">
  <li><input type="checkbox"  value="pepperoni" <HL1>title="<HL2>Pepperoni</HL2>"</HL1>/>Pepperoni</li>
  <li><input type="checkbox" value="sausage"  <HL1>title="<HL2>Sausage</HL2>"</HL1>/>Sausage</li>
  <li><input type="checkbox" value="mushrooms" <HL1>title="<HL2>Mushrooms</HL2>"</HL1>/>Mushrooms</li>
  <li><input type="checkbox" value="onions" <HL1>title="<HL2>Onions</HL2>"</HL1>/>Onions</li>
  <li><input type="checkbox" value="gpeppers" <HL1>title="<HL2>Green Peppers</HL2>"</HL1>/>Green Peppers</li>
  <li><input type="checkbox" value="xcheese" <HL1>title="<HL2>Extra Cheese</HL2>"</HL1>/>Extra Cheese</li>
</ul> 
"""

example_obj.script      = """"""

example_obj.style       = """
   <style type="text/css">
div.label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  font-size: 100%;
  font-weight: bold;
}

ul.checkbox   {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}

ul.checkbox li input {
  margin-right: .25em;
}
  </style>
"""

example2 = create_example(example_obj)

# =============================
# Example 3
# =============================

order +=  1

example_obj                = example_object()
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order          = order
example_obj.title          = '@input[type=checkbox]@ - Labeling using @label@ element encapsulating @input[type=checkbox]@'
example_obj.permanent_slug = 'checkbox3'

example_obj.a11y_features = """
* Encapsulation is compatible with assistive technologies and is defined in HTML specifications.
* @Label@ element content increases the active area for changing the selection
* What makes this a poor practice is the inconsistency with the labeling requirements of other form controls which need to use the @label@ by reference technique.
"""
example_obj.keyboard    = """
"""
example_obj.markup = [m1]

example_obj.html        = """
 <div class="label">Select pizza toppings</div>
<ul class="checkbox">
  <li><HL1><label></HL1><input type="checkbox"  value="pepperoni"/><HL2>Pepperoni</HL2><HL1></label></HL1></li>
  <li><HL1><label></HL1><input type="checkbox" value="sausage" /><HL2>Sausage</HL2><HL1></label></HL1></li>
  <li><HL1><label></HL1><input type="checkbox" value="mushrooms"/><HL2>Mushrooms<HL1></HL2></label></HL1></li>
  <li><HL1><label></HL1><input type="checkbox" value="onions"/><HL2>Onions</HL2><HL1></label></HL1></li>
  <li><HL1><label></HL1><input type="checkbox" value="gpeppers"/><HL2>Green Peppers</HL2><HL1></label></HL1></li>
  <li><HL1><label></HL1><input type="checkbox" value="xcheese"/><HL2>Extra Cheese</HL2><HL1></label></HL1></li>
</ul> 
"""

example_obj.script      = """"""

example_obj.style       = """
  <style type="text/css">
div.label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  font-size: 100%;
  font-weight: bold;
}

ul.checkbox   {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}

ul.checkbox li input {
  margin-right: .25em;
}
  </style>
"""

example3 = create_example(example_obj)