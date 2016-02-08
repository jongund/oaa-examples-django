from django.core.exceptions import ObjectDoesNotExist
from pop_examples import *

order = 1

spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='checkbox')
m2 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='presentation')
m3 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-checked')
m4 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-describedby')
m5 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-labelledby')
m6 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='group')

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

# =============================
# Example 4
# =============================

order += 1

example_obj             = example_object()
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order          = order
example_obj.title       = 'Checkbox group using IMG elements for visual state'
example_obj.permanent_slug = 'checkbox4'

example_obj.a11y_features = """
Simple example of a checkbox group using inline images to display the visual state of the boxes in the group.
"""
example_obj.keyboard    = """
* Tab: Move between button items and text area.
* Enter or space: Toggle aria-checked state of checkbox with keyboard focus.
"""

example_obj.markup = [m1,m2,m3,m4,m5,m6]

example_obj.html       = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>

<div role="application">

<h3 id="id_cond">Sandwich Condiments</h3>


<ul id="id_cb1" class="checkboxes" role="group" aria-labelledby="cond">

    <li id="id_cb1_all"
        role="checkbox" 
	class="groupbox"
        aria-checked="mixed" 
        tabindex="0">
	<img src="{{EXAMPLE_MEDIA}}images/checkbox-mixed-black.png" role="presentation">
        All condiments
        
     </li>   
            <li id="id_cb1_a" 
                role="checkbox" 
		class="checkbox"
                aria-checked="false" 
                aria-describedby="id_desc1"
                tabindex="0">
		<img src="{{EXAMPLE_MEDIA}}images/checkbox-unchecked-black.png" role="presentation">
                Lettuce
            </li>
            
            <li id="id_cb1_b" 
                role="checkbox" 
		class="checkbox"
                aria-checked="true" 
                aria-describedby="id_desc2"
                tabindex="0">
		<img src="{{EXAMPLE_MEDIA}}images/checkbox-checked-black.png" role="presentation">
                Tomato
            </li>
            
            <li id="id_cb1_c" 
                role="checkbox" 
		class="checkbox"
                aria-checked="true" 
                aria-describedby="id_desc3"
                tabindex="0">
		<img src="{{EXAMPLE_MEDIA}}images/checkbox-checked-black.png" role="presentation">
                Mustard
            </li>
            
            <li id="id_cb1_d" 
                role="checkbox" 
		class="checkbox"
                aria-checked="true" 
                aria-describedby="id_desc4"
                tabindex="0">
		<img src="{{EXAMPLE_MEDIA}}images/checkbox-checked-black.png" role="presentation">
                Sprouts
            </li>            
   
</ul>

<p id="id_desc1" class="hidden">Not your average lettuce</p>
<p id="id_desc2" class="hidden">Organically grown beef steak tomatos</p>
<p id="id_desc3" class="hidden">Brown and spicy mustard</p>
<p id="id_desc4" class="hidden">Fresh alfalfa sprouts, organically grown</p> 


</div>
"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};
var KEY_SPACE = 32;

$(document).ready(function() {

	var checkboxGroupApp = new OAA_EXAMPLES.checkboxGroup("cb1");

}); // end ready event

/**
* Function keyCodes() is an object to contain keycodes needed for the application
*/
function keyCodes() {
	this.space = 32;
}

/**
* @constructor checkboxGroup
*
* @memberOf OAA_EXAMPLES
*
* @desc a class constructor for the implementation of a checkbox group widget.
* checkboxGroup() requires an unordered list structure, with the first list entry being the group
* checkbox and the remaining entries being the checkboxes controlled by the group. Each list entry
* must contain an image tag that will be used to display the state of the checkbox.
*
* @param {String} list - the id of the unordered list that checkboxgroup is to be bound to
*
* @return {N/A}
*/

/**
* @private
* @constructor Internal Properties
* 
* @property {obj} $id - JQuery id object
* @property {obj} keys - assigns a list of keycodes
* 
* @property {integer} unchecked - (set to 0) value which corresponds to an unchecked checkbox
* @property {integer} checked - (set to 1) value which corresponds to a checked checkbox
* @property {integer} mixed - (set to 2) value which corresponds to a mixed checkbox
*
* @property {obj} $groupBox - JQuery object for a group box
* @property {obj} $checkboxes - JQuery object for a check box
* @property {obj} checkedCount - set to the number of checkboxes that are checked
*/
OAA_EXAMPLES.checkboxGroup = function(list) {

	// define object properties
	this.$id = $('#' + list);
	this.keys = new keyCodes();

	this.unchecked = 0;
	this.checked = 1;
	this.mixed = 2;

	this.$groupBox = this.$id.find('li').first();
	this.$checkboxes = this.$groupBox.siblings();
	this.checkedCount = 0;
	// initialize the checkboxGroup object
	this.init();

	// bind event handlers
	this.bindHandlers();

} // end checkboxGroup() constructor

/** 
* @method init
* 
* @memberOf OAA_EXAMPLES
*
* @desc a member function to initialize the checkboxGroup object. Initial checkbox
* states are set according to the aria-checked property of the checkboxes in the group.
*
* return {N/A}
*/

OAA_EXAMPLES.checkboxGroup.prototype.init = function() {

	var thisObj = this;

	this.$checkboxes.each(function() {
		if ($(this).attr('aria-checked') == 'true') {
			thisObj.adjCheckedCount(true);
		}
	});

} // end init()

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers to the checkboxes in the checkbox group.
*
* @return {N/A}
*/

OAA_EXAMPLES.checkboxGroup.prototype.bindHandlers = function() {

	var thisObj = this;

	/////////// Bind groupbox handlers ////////////////
	
	// bind a click handler
	this.$groupBox.click(function(e) {
		return thisObj.handleGroupboxClick($(this), e);
	});

	// bind a keydown handler
	this.$groupBox.keydown(function(e) {
		return thisObj.handleGroupboxKeyDown($(this), e);
	});

	// bind a keypress handler
	this.$groupBox.keypress(function(e) {
		return thisObj.handleBoxKeyPress($(this), e);
	});

	// bind a mouseover handler
	this.$groupBox.mouseover(function(e) {
		return thisObj.handleBoxMouseOver($(this), e);
	});

	// bind a mouseout handler
	this.$groupBox.mouseout(function(e) {
		return thisObj.handleBoxMouseOut($(this), e);
	});

	// bind a focus handler
	this.$groupBox.focus(function(e) {
		return thisObj.handleBoxFocus($(this), e);
	});

	// bind a blur handler
	this.$groupBox.blur(function(e) {
		return thisObj.handleBoxBlur($(this), e);
	});

	/////////// Bind checkbox handlers ////////////////
	
	// bind a click handler
	this.$checkboxes.click(function(e) {
		return thisObj.handleCheckboxClick($(this), e);
	});

	// bind a keydown handler
	this.$checkboxes.keydown(function(e) {
		return thisObj.handleCheckboxKeyDown($(this), e);
	});

	// bind a keypress handler
	this.$checkboxes.keypress(function(e) {
		return thisObj.handleBoxKeyPress($(this), e);
	});

	// bind a mouseover handler
	this.$checkboxes.mouseover(function(e) {
		return thisObj.handleBoxMouseOver($(this), e);
	});

	// bind a mouseout handler
	this.$checkboxes.mouseout(function(e) {
		return thisObj.handleBoxMouseOut($(this), e);
	});

	// bind a focus handler
	this.$checkboxes.focus(function(e) {
		return thisObj.handleBoxFocus($(this), e);
	});

	// bind a blur handler
	this.$checkboxes.blur(function(e) {
		return thisObj.handleBoxBlur($(this), e);
	});

} // end bindHandlers()

/**
* @method setBoxState
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set a checkbox state. This function sets the
* aria-checked property to the passed state value and changes the box image to display the new
* box state.
*
* @param {obj} $boxID - the jquery object of the checkbox to manipulate
*
* @param {integer} state - the check state to set the box
*
* @return {N/A}
*/

OAA_EXAMPLES.checkboxGroup.prototype.setBoxState = function($boxID, state) {

	var $img = $boxID.find('img');

	switch (state) {
		case this.unchecked: {
			$boxID.attr('aria-checked', 'false');
			$img.attr('src','{{EXAMPLE_MEDIA}}images/checkbox-unchecked-black.png');

			break;
		}
		case this.checked: {
			$boxID.attr('aria-checked', 'true');
			$img.attr('src','{{EXAMPLE_MEDIA}}images/checkbox-checked-black.png');
			break;
		}
		case this.mixed: {
			$boxID.attr('aria-checked', 'mixed');
			$img.attr('src','{{EXAMPLE_MEDIA}}images/checkbox-mixed-black.png');
			break;
		}
	} // end switch

} // end setBoxState()

/**
* @method adjCheckedCount
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to increment or decrement the count of checked
* boxes. The function modifies the checkes state of the group box accordingly.
*
* @param {boolean} inc - true if incrementing the checked count, false if decrementing
*
* @return {N/A}
*/

OAA_EXAMPLES.checkboxGroup.prototype.adjCheckedCount = function(inc) {

	// increment or decrement the count
	if (inc == true) {
		this.checkedCount++;
	}
	else {
		this.checkedCount--;
	}

	// modify the group box state
	if (this.checkedCount == this.$checkboxes.length) {
		// all the boxes are checked
		this.setBoxState(this.$groupBox, this.checked);
	}
	else if (this.checkedCount > 0) {
		// some of the boxes are checked
		this.setBoxState(this.$groupBox, this.mixed);
	}
	else {
		// all boxes are unchecked
		this.setBoxState(this.$groupBox, this.unchecked);
	}

} // end adjCheckedCount()


/** Groupbox event handlers
*
*
* Function handleGroupboxClick() is a member function to handle click events for group checkbox
*
* @param ($id object) $id is the jquery object of the checkbox
*
* @param (e object) e is the event object associated with the keydown event
*
* @return (boolean) Returns false if processing; true of doing nothing
*/
OAA_EXAMPLES.checkboxGroup.prototype.handleGroupboxClick = function($id, e) {
		 
	var thisObj = this;

	if (e.altkey || e.ctrlKey || e.shiftKey) {
		// do nothing;
		return true;
	}

	switch ($id.attr('aria-checked')) {
		case 'true' : {
			// uncheck the group

			// clear the groupbox
			this.setBoxState($id, this.unchecked);

			// clear all the checkboxes in the group
			this.$checkboxes.each(function() {

				// clear the groupbox
				thisObj.setBoxState($(this), thisObj.unchecked);
			});

			// reset the checked count
			this.checkedCount = 0;

			break;
		}
		case 'mixed' :
		case 'false' : {
			// check the group

			// set the groupbox to checked
			this.setBoxState($id, this.checked);

			// check all the checkboxes in the group
			this.$checkboxes.each(function() {

				// clear the groupbox
				thisObj.setBoxState($(this), thisObj.checked);
			});

			// set the checked count
			this.checkedCount = this.$checkboxes.length;

			break;
		}
	} // end switch

	e.stopPropagation();
	return false;
	
} // end handleGroupboxClick()
	
/**
* @method handleGroupboxKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle keydown events for the group checkbox
*
* @param {obj} $id - the jquery object of the checkbox
*
* @param {obj} e - the event object associated with the keydown event
*
* @return {boolean} Returns false if processing; true of doing nothing
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleGroupboxKeyDown = function($id, e) {
		 
	var thisObj = this;

	if (e.altkey || e.ctrlKey || e.shiftKey) {
		// do nothing;
		return true;
	}

	if( e.keyCode == this.keys.space ) {

		switch ($id.attr('aria-checked')) {
			case 'true' : {
				// uncheck the group
	
				// clear the groupbox
				this.setBoxState($id, this.unchecked);
	
				// clear all the checkboxes in the group
				this.$checkboxes.each(function() {
	
					// clear the groupbox
					thisObj.setBoxState($(this), thisObj.unchecked);
				});
	
				// reset the checked count
				this.checkedCount = 0;
	
				break;
			}
			case 'mixed' :
			case 'false' : {
				// check the group
	
				// set the groupbox to checked
				this.setBoxState($id, this.checked);
	
				// check all the checkboxes in the group
				this.$checkboxes.each(function() {
	
					// clear the groupbox
					thisObj.setBoxState($(this), thisObj.checked);
				});
	
				// set the checked count
				this.checkedCount = this.$checkboxes.length;
	
				break;
			}
		} // end switch

		e.stopPropagation();
		return false;
	} // endif

	return true;
	
} // end handleGroupboxKeyDown()
	

/**
* @method handleCheckboxClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle click events for checkboxes
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the keydown event
*
* @return {boolean} Returns false if processing; true of doing nothing
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleCheckboxClick = function($id, e) {
		 
	if (e.altKey || e.ctrlKey || e.shiftKey) {
		// do nothing;
		return true;
	}

	// toggle the checkbox state

	if($id.attr('aria-checked') == 'true') {
		this.setBoxState($id, this.unchecked);
		this.adjCheckedCount(false);
	} else {
		this.setBoxState($id, this.checked);
		this.adjCheckedCount(true);
	}  // endif

	e.stopPropagation();
	return false;
	
} // end handleCheckboxClick()
	
/**
* @method handleCheckboxKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle keydown events for checkboxes
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the keydown event
*
* @return {boolean} Returns false if processing; true of doing nothing
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleCheckboxKeyDown = function($id, e) {
		 
	if (e.altkey || e.ctrlKey || e.shiftKey) {
		// do nothing;
		return true;
	}

	if( e.keyCode == this.keys.space ) {

		// toggle the checkbox state

		if($id.attr('aria-checked') == 'true') {
			this.setBoxState($id, this.unchecked);
			this.adjCheckedCount(false);
		} else {
			this.setBoxState($id, this.checked);
			this.adjCheckedCount(true);
		}  // endif

		e.stopPropagation();
		return false;
	} // endif

	return true;
	
} // end handleCheckboxKeyDown()
	
/**
* @method handleBoxKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle keypress events for checkboxes.
* This function is needed to consume events for browsers, such as Opera, that perform window
* manipulation on keypress events.
*
* @param {object} $id is the jquery object of the checkbox
*
* @param {object} e - the event object associated with the keydown event
*
* @return {boolean} Returns false if processing; true of doing nothing
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleBoxKeyPress = function($id, e) {
		 
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
	
} // end handleBoxKeyPress()

/**
* @method handleBoxMouseOver
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle mouseover events for checkboxes
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e is the event object associated with the mouseover event
*
* @return {boolean} Returns false;
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleBoxMouseOver = function($id, e) {
		 
	// if the box does not have the focus class add the hover highlight
	if ($id.not('.focus')) {
		$id.addClass('hover');
	}

	e.stopPropagation();
	return false;
	
} // end handleBoxMouseOver()

/**
* @method handleBoxMouseOut
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle mouseout events for checkboxes
*
* @param {object} $id is the jquery object of the checkbox
*
* @param {object} e - the event object associated with the mouseout event
*
* @return {boolean} Returns false;
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleBoxMouseOut = function($id, e) {
		 
	$id.removeClass('hover');

	e.stopPropagation();
	return false;
	
} // end handleBoxMouseOut()

/**
* @method handleBoxFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle focus events for checkboxes
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the focus event
*
* @return {boolean} Returns true;
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleBoxFocus = function($id, e) {
		 
	$id.addClass('focus');

	// remove the hover class if it is applied
	$id.removeClass('hover');

	return true;
	
} // end handleBoxFocus()

/**
* @method handleBoxBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc  a member function to handle blur events for checkboxes
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the blur event
*
* @return {boolean} Returns true;
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleBoxBlur = function($id, e) {
		 
	$id.removeClass('focus');
	return true;
	
} // end handleBoxBlur()
"""

example_obj.style       = """

ul.checkboxes {
   margin: 0;
   padding: 0;
}

ul.checkboxes li img {
   margin-right: .5em;
}

li.groupbox {
   margin-left: 1em;
   padding: 0;
   padding-left: .5em;
   list-style: none;
   width: 7.5em;
   border: 2px solid transparent;
}

li.checkbox {
   margin-left: 2.5em;
   padding: 0;
   padding-left: .5em;
   list-style: none;
   width: 7em;
   border: 2px solid transparent;
}

li.hover {
   border: 2px solid #777;
}

li.focus {
   border: 2px solid black;
}

.hidden {
   position: absolute;
   top: -30em;
   left: -300em;
} 
"""

example4 = create_example(example_obj)

# =============================
# Example 5
# =============================
order += 1

example_obj             = example_object()
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order          = order
example_obj.title       = 'Checkbox group using background images for visual state'
example_obj.permanent_slug = 'checkbox5'

example_obj.a11y_features = """
Simple example of a checkbox group using background images to display the visual state of the boxes in the group. Background images are typically not displayed in high contrast mode. For this reason, background images should not be relied upon to display essential visual information.
"""
example_obj.keyboard    = """
* Tab: Move between button items and text area.
* Enter or space: Toggle aria-checked state of checkbox with keyboard focus.
"""

example_obj.markup = [m1,m3,m4,m5,m6]

example_obj.html       = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<div role="application">

<h3 id="cond">Sandwich Condiments</h3>


<ul id="cb1" class="checkboxes" role="group" aria-labelledby="cond">

    <li id="cb1all"
        role="checkbox" 
        class="groupbox mixed"
        aria-checked="mixed" 
        tabindex="0">
        All condiments
        
     </li>   
            <li id="cb1a" 
                role="checkbox" 
                class="checkbox unchecked"
                aria-checked="false" 
                aria-describedby="desc1"
                tabindex="0">
                Lettuce
            </li>
            
            <li id="cb1b" 
                role="checkbox" 
                class="checkbox checked"
                aria-checked="true" 
                aria-describedby="desc2"
                tabindex="0">
                Tomato
            </li>
            
            <li id="cb1c" 
                role="checkbox" 
                class="checkbox checked"
                aria-checked="true" 
                aria-describedby="desc3"
                tabindex="0">
                Mustard
            </li>
            
            <li id="cb1d" 
                role="checkbox" 
                class="checkbox checked"
                aria-checked="true" 
                aria-describedby="desc4"
                tabindex="0">
                Sprouts
            </li>            
   
</ul>

<p id="desc1" class="hidden">Not your average lettuce</p>
<p id="desc2" class="hidden">Organically grown beef steak tomatos</p>
<p id="desc3" class="hidden">Brown and spicy mustard</p>
<p id="desc4" class="hidden">Fresh alfalfa sprouts, organically grown</p> 


</div>
"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};
var KEY_SPACE = 32;

$(document).ready(function() {
	var checkboxGroupApp = new OAA_EXAMPLES.checkboxGroup("cb1");

}); // end ready event

/**
* Function keyCodes() is an object to contain keycodes needed for the application
*/
function keyCodes() {
	this.space = 32;
}

/**
* @constructor checkboxGroup
*
* @memberOf OAA_EXAMPLES
*
* @desc a class constructor for the implementation of a checkbox group widget.
* checkboxGroup() requires an unordered list structure, with the first list entry being the group
* checkbox and the remaining entries being the checkboxes controlled by the group.
* This implementation of checkboxGroup() uses background images to represent the check state of the
* group. This version will not work in high contrast modes, where background images are not displayed.
*
* @param {string} list - the id of the unordered list that checkboxgroup is to be bound to
*
* @return {N/A}
*/

/**
* @private
* @constructor Internal Properties
* 
* @property {object} $id - jquery identification object
* @property {object} keys - assigns key codes
*
* @property {integer} unchecked - (set to 0) corresponds to an unchecked box
* @property {integer} checked - (set to 1) corresponds to a checked box
* @property {integer} mixed - (set to 2) corresponds to a mixed box
* @property {integer} checkedCount - set to the number of checkboxes that are checked
*/

OAA_EXAMPLES.checkboxGroup = function(list) {

	// define object properties
	this.$id = $('#' + list);
	this.keys = new keyCodes();

	this.unchecked = 0;
	this.checked = 1;
	this.mixed = 2;

	this.$groupBox = this.$id.find('li').first();
	this.$checkboxes = this.$groupBox.siblings();
	this.checkedCount = 0; // set to the number of checkboxes that are checked

	// initialize the checkboxGroup object
	this.init();

	// bind event handlers
	this.bindHandlers();

} // end checkboxGroup() constructor

/**
* @method init
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to initialize the checkboxGroup object. Initial checkbox
* states are set according to the aria-checked property of the checkboxes in the group.
*
* return {N/A}
*/

OAA_EXAMPLES.checkboxGroup.prototype.init = function() {

	var thisObj = this;

	this.$checkboxes.each(function() {
		if ($(this).attr('aria-checked') == 'true') {
			thisObj.adjCheckedCount(true);
		}
	});

} // end init()

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers to the checkboxes in the checkbox group.
*
* @return {N/A}
*/

OAA_EXAMPLES.checkboxGroup.prototype.bindHandlers = function() {

	var thisObj = this;

	/////////// Bind groupbox handlers ////////////////
	
	// bind a click handler
	this.$groupBox.click(function(e) {
		return thisObj.handleGroupboxClick($(this), e);
	});

	// bind a keydown handler
	this.$groupBox.keydown(function(e) {
		return thisObj.handleGroupboxKeyDown($(this), e);
	});

	// bind a keypress handler
	this.$groupBox.keypress(function(e) {
		return thisObj.handleBoxKeyPress($(this), e);
	});

	// bind a mouseover handler
	this.$groupBox.mouseover(function(e) {
		return thisObj.handleBoxMouseOver($(this), e);
	});

	// bind a mouseout handler
	this.$groupBox.mouseout(function(e) {
		return thisObj.handleBoxMouseOut($(this), e);
	});

	// bind a focus handler
	this.$groupBox.focus(function(e) {
		return thisObj.handleBoxFocus($(this), e);
	});

	// bind a blur handler
	this.$groupBox.blur(function(e) {
		return thisObj.handleBoxBlur($(this), e);
	});

	/////////// Bind checkbox handlers ////////////////
	
	// bind a click handler
	this.$checkboxes.click(function(e) {
		return thisObj.handleCheckboxClick($(this), e);
	});

	// bind a keydown handler
	this.$checkboxes.keydown(function(e) {
		return thisObj.handleCheckboxKeyDown($(this), e);
	});

	// bind a keypress handler
	this.$checkboxes.keypress(function(e) {
		return thisObj.handleBoxKeyPress($(this), e);
	});

	// bind a mouseover handler
	this.$checkboxes.mouseover(function(e) {
		return thisObj.handleBoxMouseOver($(this), e);
	});

	// bind a mouseout handler
	this.$checkboxes.mouseout(function(e) {
		return thisObj.handleBoxMouseOut($(this), e);
	});

	// bind a focus handler
	this.$checkboxes.focus(function(e) {
		return thisObj.handleBoxFocus($(this), e);
	});

	// bind a blur handler
	this.$checkboxes.blur(function(e) {
		return thisObj.handleBoxBlur($(this), e);
	});

} // end bindHandlers()

/**
* @method setBoxState
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set a checkbox state. This function sets the
* aria-checked property to the passed state value and changes the box image to display the new box state.
*
* @param {object} $boxID - the jquery object of the checkbox to manipulate
*
* @param {integer} state - the check state to set the box
*
* @return {N/A}
*/

OAA_EXAMPLES.checkboxGroup.prototype.setBoxState = function($boxID, state) {

	switch (state) {
		case this.unchecked: {
			$boxID.attr('aria-checked', 'false');
			$boxID.removeClass('checked mixed');
			$boxID.addClass('unchecked');

			break;
		}
		case this.checked: {
			$boxID.attr('aria-checked', 'true');
			$boxID.removeClass('unchecked mixed');
			$boxID.addClass('checked');
			break;
		}
		case this.mixed: {
			$boxID.attr('aria-checked', 'mixed');
			$boxID.removeClass('unchecked checked');
			$boxID.addClass('mixed');
			break;
		}
	} // end switch

} // end setBoxState()

/**
* @method adjCheckedCount
* 
* @memberOf OAA_EXAMPLES
*
* @desc a member function to increment or decrement the count of checked
* boxes. The function modifies the checkes state of the group box accordingly.
*
* @param {boolean} inc - true if incrementing the checked count, false if decrementing
*
* @return {N/A}
*/

OAA_EXAMPLES.checkboxGroup.prototype.adjCheckedCount = function(inc) {

	// increment or decrement the count
	if (inc == true) {
		this.checkedCount++;
	}
	else {
		this.checkedCount--;
	}

	// modify the group box state
	if (this.checkedCount == this.$checkboxes.length) {
		// all the boxes are checked
		this.setBoxState(this.$groupBox, this.checked);
	}
	else if (this.checkedCount > 0) {
		// some of the boxes are checked
		this.setBoxState(this.$groupBox, this.mixed);
	}
	else {
		// all boxes are unchecked
		this.setBoxState(this.$groupBox, this.unchecked);
	}

} // end adjCheckedCount()




/**
* @method handleGroupboxClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle click events for group checkbox
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the keydown event
*
* @return {boolean} Returns false if processing; true of doing nothing
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleGroupboxClick = function($id, e) {
		 
	var thisObj = this;

	if (e.altkey || e.ctrlKey || e.shiftKey) {
		// do nothing;
		return true;
	}

	switch ($id.attr('aria-checked')) {
		case 'true' : {
			// uncheck the group

			// clear the groupbox
			this.setBoxState($id, this.unchecked);

			// clear all the checkboxes in the group
			this.$checkboxes.each(function() {

				// clear the groupbox
				thisObj.setBoxState($(this), thisObj.unchecked);
			});

			// reset the checked count
			this.checkedCount = 0;

			break;
		}
		case 'mixed' : {
			
		}
		case 'false' : {
			// check the group

			// set the groupbox to checked
			this.setBoxState($id, this.checked);

			// check all the checkboxes in the group
			this.$checkboxes.each(function() {

				// clear the groupbox
				thisObj.setBoxState($(this), thisObj.checked);
			});

			// set the checked count
			this.checkedCount = this.$checkboxes.length;

			break;
		}
	} // end switch

	e.stopPropagation();
	return false;
	
} // end handleGroupboxClick()
	
/**
* @method handleGroupboxKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle keydown events for the group checkbox
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the keydown event
*
* @return {boolean} Returns false if processing; true of doing nothing
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleGroupboxKeyDown = function($id, e) {
		 
	var thisObj = this;

	if (e.altkey || e.ctrlKey || e.shiftKey) {
		// do nothing;
		return true;
	}

	if( e.keyCode == this.keys.space ) {

		switch ($id.attr('aria-checked')) {
			case 'true' : {
				// uncheck the group
	
				// clear the groupbox
				this.setBoxState($id, this.unchecked);
	
				// clear all the checkboxes in the group
				this.$checkboxes.each(function() {
	
					// clear the groupbox
					thisObj.setBoxState($(this), thisObj.unchecked);
				});
	
				// reset the checked count
				this.checkedCount = 0;
	
				break;
			}
			case 'mixed' :{
				
			}
			case 'false' : {
				// check the group
	
				// set the groupbox to checked
				this.setBoxState($id, this.checked);
	
				// check all the checkboxes in the group
				this.$checkboxes.each(function() {
	
					// clear the groupbox
					thisObj.setBoxState($(this), thisObj.checked);
				});
	
				// set the checked count
				this.checkedCount = this.$checkboxes.length;
	
				break;
			}
		} // end switch

		e.stopPropagation();
		return false;
	} // endif

	return true;
	
} // end handleGroupboxKeyDown()
	

/**
* @method handleCheckboxClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle click events for checkboxes
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the keydown event
*
* @return {boolean} Returns false if processing; true of doing nothing
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleCheckboxClick = function($id, e) {
		 
	if (e.altkey || e.ctrlKey || e.shiftKey) {
		// do nothing;
		return true;
	}

	// toggle the checkbox state

	if($id.attr('aria-checked') == 'true') {
		this.setBoxState($id, this.unchecked);
		this.adjCheckedCount(false);
	} else {
		this.setBoxState($id, this.checked);
		this.adjCheckedCount(true);
	}  // endif

	e.stopPropagation();
	return false;
	
} // end handleCheckboxClick()
	
/*
* @method handleCheckboxKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle keydown events for checkboxes
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the keydown event
*
* @return {boolean} Returns false if processing; true of doing nothing
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleCheckboxKeyDown = function($id, e) {
		 
	if (e.altkey || e.ctrlKey || e.shiftKey) {
		// do nothing;
		return true;
	}

	if( e.keyCode == this.keys.space ) {

		// toggle the checkbox state

		if($id.attr('aria-checked') == 'true') {
			this.setBoxState($id, this.unchecked);
			this.adjCheckedCount(false);
		} else {
			this.setBoxState($id, this.checked);
			this.adjCheckedCount(true);
		}  // endif

		e.stopPropagation();
		return false;
	} // endif

	return true;
	
} // end handleCheckboxKeyDown()
	
/**
* @method handleBoxKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle keypress events for checkboxes
* This function is needed to consume events for browsers, such as Opera, that perform window
* manipulation on keypress events.
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the keydown event
*
* @return {boolean} Returns false if processing; true of doing nothing
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleBoxKeyPress = function($id, e) {
		 
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
	
} // end handleBoxKeyPress()

/**
* @method handleBoxMouseOver
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle mouseover events for checkboxes
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the mouseover event
*
* @return {boolean} Returns false;
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleBoxMouseOver = function($id, e) {
		 
	// if the box does not have the focus class add the hover highlight
	if ($id.not('.focus')) {
		$id.addClass('hover');
	}

	e.stopPropagation();
	return false;
	
} // end handleBoxMouseOver()

/**
* @method handleBoxMouseOut
*
* @memberOf OAA_EXAMPLES
*
* @desca member function to handle mouseout events for checkboxes
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the mouseout event
*
* @return {boolean} Returns false;
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleBoxMouseOut = function($id, e) {
		 
	$id.removeClass('hover');

	e.stopPropagation();
	return false;
	
} // end handleBoxMouseOut()

/**
* @method handleBoxFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle focus events for checkboxes
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the focus event
*
* @return {boolean} Returns true;
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleBoxFocus = function($id, e) {
		 
	$id.addClass('focus');

	// remove the hover class if it is applied
	$id.removeClass('hover');

	return true;
	
} // end handleBoxFocus()

/**
* @method handleBoxBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle blur events for checkboxes
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the blur event
*
* @return {boolean} Returns true;
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleBoxBlur = function($id, e) {
		 
	$id.removeClass('focus');
	return true;
	
} // end handleBoxBlur()
"""

example_obj.style       = """
ul.checkboxes {
   margin: 0;
   padding: 0;
}

li.groupbox {
   margin-left: 1em;
   padding: 0;
   padding-left: 2em;
   list-style: none;
   width: 7em;
   border: 2px solid transparent;
}

li.checkbox {
   margin-left: 2.5em;
   padding: 0;
   padding-left: 2em;
   list-style: none;
   width: 7em;
   border: 2px solid transparent;
}

li.unchecked {
   background: url('{{EXAMPLE_MEDIA}}images/checkbox-unchecked-black.png') no-repeat .5em center;
}

li.checked {
   background: url('{{EXAMPLE_MEDIA}}images/checkbox-checked-black.png') no-repeat .5em center;;
}

li.mixed {
   background: url('{{EXAMPLE_MEDIA}}images/checkbox-mixed-black.png') no-repeat .5em center;
}
   
li.hover {
   border: 2px solid #777;
}

li.focus {
   border: 2px solid black;
}

.hidden {
   position: absolute;
   top: -30em;
   left: -300em;
} 
"""

example5 = create_example(example_obj)

# =============================
# Example 6
# =============================

order += 1

example_obj             = example_object()
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order          = order
example_obj.title       = 'Checkbox group using ARIA CSS selectors for visual state'
example_obj.permanent_slug = 'checkbox6'

example_obj.a11y_features = """
Simple example of a checkbox group using ARIA CSS selectors to display the visual state of the boxes in the group. Background images are typically not displayed in high contrast mode. For this reason, background images should not be relied upon to display essential visual information.
"""
example_obj.keyboard    = """
* Tab: Move between button items and text area.
* Enter or space: Toggle aria-checked state of checkbox with keyboard focus.
"""

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='group')
m2 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='checkbox')
m3 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-checked')
m4 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-describedby')
m5 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-labelledby')

example_obj.markup = [m1,m3,m4,m5,m6]

example_obj.html       = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<div role="application">

<h3 id="cond">Sandwich Condiments</h3>


<ul id="cb1" class="checkboxes" role="group" aria-labelledby="cond">

    <li id="cb1all"
        role="checkbox" 
        class="groupbox"
        aria-checked="mixed" 
        tabindex="0">
        All condiments
        
     </li>   
            <li id="cb1a" 
                role="checkbox" 
                class="checkbox"
                aria-checked="false" 
                aria-describedby="desc1"
                tabindex="0">
                Lettuce
            </li>
            
            <li id="cb1b" 
                role="checkbox" 
                class="checkbox"
                aria-checked="true" 
                aria-describedby="desc2"
                tabindex="0">
                Tomato
            </li>
            
            <li id="cb1c" 
                role="checkbox" 
                class="checkbox"
                aria-checked="true" 
                aria-describedby="desc3"
                tabindex="0">
                Mustard
            </li>
            
            <li id="cb1d" 
                role="checkbox" 
                class="checkbox"
                aria-checked="true" 
                aria-describedby="desc4"
                tabindex="0">
                Sprouts
            </li>            
   
</ul>

<p id="desc1" class="hidden">Not your average lettuce</p>
<p id="desc2" class="hidden">Organically grown beef steak tomatos</p>
<p id="desc3" class="hidden">Brown and spicy mustard</p>
<p id="desc4" class="hidden">Fresh alfalfa sprouts, organically grown</p> 


</div>
"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};
var KEY_SPACE = 32;

$(document).ready(function() {

	var checkboxGroupApp = new OAA_EXAMPLES.checkboxGroup("cb1");

}); // end ready event

/*
* Function keyCodes() is an object to contain keycodes needed for the application
*/
function keyCodes() {
	this.space = 32;
}

/**
* @constructor checkboxGroup
*
* @memberOf OAA_EXAMPLES
*
* @desc a class constructor for the implementation of a checkbox group widget.
* checkboxGroup() requires an unordered list structure, with the first list entry being the group
* checkbox and the remaining entries being the checkboxes controlled by the group.
* 
* This implementation of checkboxGroup() uses background images to represent the check state of the
* group. This version will not work in high contrast modes, where background images are not displayed.
*
* @param {string} list - the id of the unordered list that checkboxgroup is to be bound to
*
* @return {N/A}
*/

/**
* @private
* @constructor Internal Properties
* 
* @property {object} id - the jquery id object
* @property {object} keys - assigns keycodes
*
* @property {integer} unchecked - (set to 0) corresponds to an unchecked box
* @property {integer} checked - (set to 1) corresponds to a checked box
* @property {integer} mixed - (set to 2) corresponds to a mixed box
* @property {integer} checkedCount - set to the number of checkboxes that are checked
*/

OAA_EXAMPLES.checkboxGroup = function(list) {

	// define object properties
	this.$id = $('#' + list);
	this.keys = new keyCodes();

	this.unchecked = 0;
	this.checked = 1;
	this.mixed = 2;

	this.$groupBox = this.$id.find('li').first();
	this.$checkboxes = this.$groupBox.siblings();
	this.checkedCount = 0;

	// initialize the checkboxGroup object
	this.init();

	// bind event handlers
	this.bindHandlers();

} // end checkboxGroup() constructor

/**
* @method init
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to initialize the checkboxGroup object. Initial checkbox
* states are set according to the aria-checked property of the checkboxes in the group.
*
* return {N/A}
*/

OAA_EXAMPLES.checkboxGroup.prototype.init = function() {

	var thisObj = this;

	this.$checkboxes.each(function() {
		if ($(this).attr('aria-checked') == 'true') {
			thisObj.adjCheckedCount(true);
		}
	});

} // end init()

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers to the checkboxes in the
* checkbox group.
*
* @return {N/A}
*/

OAA_EXAMPLES.checkboxGroup.prototype.bindHandlers = function() {

	var thisObj = this;

	/////////// Bind groupbox handlers ////////////////
	
	// bind a click handler
	this.$groupBox.click(function(e) {
		return thisObj.handleGroupboxClick($(this), e);
	});

	// bind a keydown handler
	this.$groupBox.keydown(function(e) {
		return thisObj.handleGroupboxKeyDown($(this), e);
	});

	// bind a keypress handler
	this.$groupBox.keypress(function(e) {
		return thisObj.handleBoxKeyPress($(this), e);
	});

	// bind a mouseover handler
	this.$groupBox.mouseover(function(e) {
		return thisObj.handleBoxMouseOver($(this), e);
	});

	// bind a mouseout handler
	this.$groupBox.mouseout(function(e) {
		return thisObj.handleBoxMouseOut($(this), e);
	});

	// bind a focus handler
	this.$groupBox.focus(function(e) {
		return thisObj.handleBoxFocus($(this), e);
	});

	// bind a blur handler
	this.$groupBox.blur(function(e) {
		return thisObj.handleBoxBlur($(this), e);
	});

	/////////// Bind checkbox handlers ////////////////
	
	// bind a click handler
	this.$checkboxes.click(function(e) {
		return thisObj.handleCheckboxClick($(this), e);
	});

	// bind a keydown handler
	this.$checkboxes.keydown(function(e) {
		return thisObj.handleCheckboxKeyDown($(this), e);
	});

	// bind a keypress handler
	this.$checkboxes.keypress(function(e) {
		return thisObj.handleBoxKeyPress($(this), e);
	});

	// bind a mouseover handler
	this.$checkboxes.mouseover(function(e) {
		return thisObj.handleBoxMouseOver($(this), e);
	});

	// bind a mouseout handler
	this.$checkboxes.mouseout(function(e) {
		return thisObj.handleBoxMouseOut($(this), e);
	});

	// bind a focus handler
	this.$checkboxes.focus(function(e) {
		return thisObj.handleBoxFocus($(this), e);
	});

	// bind a blur handler
	this.$checkboxes.blur(function(e) {
		return thisObj.handleBoxBlur($(this), e);
	});

} // end bindHandlers()

/**
* @method setBoxState
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set a checkbox state. This function sets the
* aria-checked property to the passed state value and changes the box image to display the new
* box state.
*
* @param {object} $boxID - the jquery object of the checkbox to manipulate
*
* @param {integer} state - the check state to set the box
*
* @return {N/A}
*/

OAA_EXAMPLES.checkboxGroup.prototype.setBoxState = function($boxID, state) {

	switch (state) {
		case this.unchecked: {
			$boxID.attr('aria-checked', 'false');

			break;
		}
		case this.checked: {
			$boxID.attr('aria-checked', 'true');
			break;
		}
		case this.mixed: {
			$boxID.attr('aria-checked', 'mixed');
			break;
		}
	} // end switch

} // end setBoxState()

/**
* @method adjCheckedCount
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to increment or decrement the count of checked
* boxes. The function modifies the checkes state of the group box accordingly.
*
* @param(inc boolean) inc is true if incrementing the checked count, false if decrementing
*
* @return N/A
*/

OAA_EXAMPLES.checkboxGroup.prototype.adjCheckedCount = function(inc) {

	// increment or decrement the count
	if (inc == true) {
		this.checkedCount++;
	}
	else {
		this.checkedCount--;
	}

	// modify the group box state
	if (this.checkedCount == this.$checkboxes.length) {
		// all the boxes are checked
		this.setBoxState(this.$groupBox, this.checked);
	}
	else if (this.checkedCount > 0) {
		// some of the boxes are checked
		this.setBoxState(this.$groupBox, this.mixed);
	}
	else {
		// all boxes are unchecked
		this.setBoxState(this.$groupBox, this.unchecked);
	}

} // end adjCheckedCount()


/**
* @method handleGroupboxClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle click events for group checkbox
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the keydown event
*
* @return {boolean} Returns false if processing; true of doing nothing
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleGroupboxClick = function($id, e) {
		 
	var thisObj = this;

	if (e.altkey || e.ctrlKey || e.shiftKey) {
		// do nothing;
		return true;
	}

	switch ($id.attr('aria-checked')) {
		case 'true' : {
			// uncheck the group

			// clear the groupbox
			this.setBoxState($id, this.unchecked);

			// clear all the checkboxes in the group
			this.$checkboxes.each(function() {

				// clear the groupbox
				thisObj.setBoxState($(this), thisObj.unchecked);
			});

			// reset the checked count
			this.checkedCount = 0;

			break;
		}
		case 'mixed' :
		case 'false' : {
			// check the group

			// set the groupbox to checked
			this.setBoxState($id, this.checked);

			// check all the checkboxes in the group
			this.$checkboxes.each(function() {

				// clear the groupbox
				thisObj.setBoxState($(this), thisObj.checked);
			});

			// set the checked count
			this.checkedCount = this.$checkboxes.length;

			break;
		}
	} // end switch

	e.stopPropagation();
	return false;
	
} // end handleGroupboxClick()
	
/**
* @method handleGroupboxKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle keydown events for the group checkbox
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the keydown event
*
* @return {boolean} Returns false if processing; true of doing nothing
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleGroupboxKeyDown = function($id, e) {
		 
	var thisObj = this;

	if (e.altkey || e.ctrlKey || e.shiftKey) {
		// do nothing;
		return true;
	}

	if( e.keyCode == this.keys.space ) {

		switch ($id.attr('aria-checked')) {
			case 'true' : {
				// uncheck the group
	
				// clear the groupbox
				this.setBoxState($id, this.unchecked);
	
				// clear all the checkboxes in the group
				this.$checkboxes.each(function() {
	
					// clear the groupbox
					thisObj.setBoxState($(this), thisObj.unchecked);
				});
	
				// reset the checked count
				this.checkedCount = 0;
	
				break;
			}
			case 'mixed' :{

			}
			case 'false' : {
				// check the group
	
				// set the groupbox to checked
				this.setBoxState($id, this.checked);
	
				// check all the checkboxes in the group
				this.$checkboxes.each(function() {
	
					// clear the groupbox
					thisObj.setBoxState($(this), thisObj.checked);
				});
	
				// set the checked count
				this.checkedCount = this.$checkboxes.length;
	
				break;
			}
		} // end switch

		e.stopPropagation();
		return false;
	} // endif

	return true;
	
} // end handleGroupboxKeyDown()
	
/**
* @method handleCheckboxClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle click events for checkboxes
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the keydown event
*
* @return {boolean} Returns false if processing; true of doing nothing
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleCheckboxClick = function($id, e) {
		 
	if (e.altkey || e.ctrlKey || e.shiftKey) {
		// do nothing;
		return true;
	}

	// toggle the checkbox state

	if($id.attr('aria-checked') == 'true') {
		this.setBoxState($id, this.unchecked);
		this.adjCheckedCount(false);
	} else {
		this.setBoxState($id, this.checked);
		this.adjCheckedCount(true);
	}  // endif

	e.stopPropagation();
	return false;
	
} // end handleCheckboxClick()
	
/**
* @method handleCheckboxKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle keydown events for checkboxes
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the keydown event
*
* @return {boolean} Returns false if processing; true of doing nothing
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleCheckboxKeyDown = function($id, e) {
		 
	if (e.altkey || e.ctrlKey || e.shiftKey) {
		// do nothing;
		return true;
	}

	if( e.keyCode == this.keys.space ) {

		// toggle the checkbox state

		if($id.attr('aria-checked') == 'true') {
			this.setBoxState($id, this.unchecked);
			this.adjCheckedCount(false);
		} else {
			this.setBoxState($id, this.checked);
			this.adjCheckedCount(true);
		}  // endif

		e.stopPropagation();
		return false;
	} // endif

	return true;
	
} // end handleCheckboxKeyDown()
	
/**
* @method handleBoxKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle keypress events for checkboxes.
* This function is needed to consume events for browsers, such as Opera, that perform window
* manipulation on keypress events.
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the keydown event
*
* @return {boolean} Returns false if processing; true of doing nothing
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleBoxKeyPress = function($id, e) {
		 
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
	
} // end handleBoxKeyPress()

/**
* @method handleBoxMouseOver
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle mouseover events for checkboxes
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the mouseover event
*
* @return {boolean} Returns false;
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleBoxMouseOver = function($id, e) {
		 
	// if the box does not have the focus class add the hover highlight
	if ($id.not('.focus')) {
		$id.addClass('hover');
	}

	e.stopPropagation();
	return false;
	
} // end handleBoxMouseOver()

/**
* @method handleBoxMouseOut
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle mouseout events for checkboxes
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the mouseout event
*
* @return {boolean} Returns false;
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleBoxMouseOut = function($id, e) {
		 
	$id.removeClass('hover');

	e.stopPropagation();
	return false;
	
} // end handleBoxMouseOut()

/**
* @method handleBoxFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle focus events for checkboxes
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the focus event
*
* @return {boolean} Returns true;
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleBoxFocus = function($id, e) {
		 
	$id.addClass('focus');

	// remove the hover class if it is applied
	$id.removeClass('hover');

	return true;
	
} // end handleBoxFocus()

/**
* @method handleBoxBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle blur events for checkboxes
*
* @param {object} $id - the jquery object of the checkbox
*
* @param {object} e - the event object associated with the blur event
*
* @return {boolean} Returns true;
*/

OAA_EXAMPLES.checkboxGroup.prototype.handleBoxBlur = function($id, e) {
		 
	$id.removeClass('focus');
	return true;
	
} // end handleBoxBlur()
"""

example_obj.style       = """
ul.checkboxes {
   margin: 0;
   padding: 0;
}

li.groupbox {
   margin-left: 1em;
   padding: 0;
   padding-left: 2em;
   list-style: none;
   width: 7em;
   border: 2px solid transparent;
}

li.checkbox {
   margin-left: 2.5em;
   padding: 0;
   padding-left: 2em;
   list-style: none;
   width: 7em;
   border: 2px solid transparent;
}

li[aria-checked='false'] {
   background: url('{{EXAMPLE_MEDIA}}images/checkbox-unchecked-black.png') no-repeat .5em center;
}

li[aria-checked='true'] {
   background: url('{{EXAMPLE_MEDIA}}images/checkbox-checked-black.png') no-repeat .5em center;;
}

li[aria-checked='mixed'] {
   background: url('{{EXAMPLE_MEDIA}}images/checkbox-mixed-black.png') no-repeat .5em center;
}
   
li.hover {
   border: 2px solid #777;
}

li.focus {
   border: 2px solid black;
}

.hidden {
   position: absolute;
   top: -30em;
   left: -300em;
} 
"""

example6 = create_example(example_obj)