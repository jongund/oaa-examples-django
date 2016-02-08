"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples import *

order = 1

spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='button')
m2 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='presentation')
m3 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='spinbutton')
m4 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-labelledby')
m5 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-valuemax')
m6 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-valuemin')
m7 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-valuenow')

# =============================
# Example 1
# =============================

example_obj             = example_object()
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order          = order
example_obj.title       = 'Spinbutton using IMG elements for buttons'
example_obj.permanent_slug = 'spinbutton1'

example_obj.a11y_features = """
Simple example of a spinbutton widget using inline images to display the buttons.
"""

example_obj.keyboard    = """
The following keyboard shortcuts are implemented for this example (based on recommended shortcuts specified by the <a href="http://dev.aol.com/dhtml_style_guide">DHTML Style Guide Working Group</a>.):
* Right and Up Arrows: increase the value
* Left and Down Arrows decrease the value
* Home and End key: move to the maximum or minimum values
* Page Up and Page Down: incrementally increase or decrease the value
* Note: Focus should remain on the edit field
"""

example_obj.markup = [m1,m2,m3,m4,m5,m6,m7]

example_obj.html        = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<label id="sb1_label" class="sbLabel" for="sb1">Choose a number between 0 and 100</label>
<div class="spinControl">
	<div id="sb1" class="spinbutton" role="spinbutton"
            aria-labelledby="sb1_label"
            aria-valuemin="0" 
            aria-valuemax="100" 
            aria-valuenow="50"
            tabindex="0">
            50
	</div>
	<div id="sb1_up" class="button" role="button" title="Increase Value">
		<img src="{{EXAMPLE_MEDIA}}images/button-arrow-up.png" role="presentation">
	</div>
	<div id="sb1_down" class="button" role="button" title="Decrease Value">
		<img src="{{EXAMPLE_MEDIA}}images/button-arrow-down.png" role="presentation">
	</div>
</div>

<label id="sb2_label" class="sbLabel" for="sb2">Choose a number between 500 and 1000</label>
<div class="spinControl">
	<div id="sb2" class="spinbutton" role="spinbutton"
            aria-labelledby="sb2_label"
            aria-valuemin="500" 
            aria-valuemax="1000" 
            aria-valuenow="750"
            tabindex="0">
            750
	</div>
	<div id="sb2_up" class="button" role="button" title="Increase Value">
		<img src="{{EXAMPLE_MEDIA}}images/button-arrow-up.png" role="presentation">	
	</div>
	<div id="sb2_down" class="button" role="button" title="Decrease Value">
		<img src="{{EXAMPLE_MEDIA}}images/button-arrow-down.png" role="presentation">	
	</div>
</div>
"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {} ;

$(document).ready(function () {
	var spin1 = new OAA_EXAMPLES.spinbutton('sb1', 'sb1_up', 'sb1_down', 10);	
	var spin2 = new OAA_EXAMPLES.spinbutton('sb2', 'sb2_up', 'sb2_down', 50);	
}); // end ready

/**
* @method spinbutton
*
* @memberOf OAA_EXAMPLES
*
* @desc a constructor for an ARIA spinbutton widget. The widget
* binds to an element with role='spinbutton'.
*
* @param {string} id - the html id of the spinbutton element
*
* @param {string} upID - the html id of the spinbutton control's increase value button
*
* @param {string} downID - the html id of the spinbutton control's decrease value button
*
* @param {integer} skipVal - the amount to change the control by for pgUp/pgDown
* @return {N/A}
*/

OAA_EXAMPLES.spinbutton = function(id, upID, downID, skipVal) {

	// define widget attributes
	this.$id = $('#' + id);

	this.upID = upID;
	this.$upButton = $('#' + upID);
	this.downID = downID;
	this.$downButton = $('#' + downID);
	this.skipVal = skipVal;

	this.valMin = parseInt(this.$id.attr('aria-valuemin'));
	this.valMax = parseInt(this.$id.attr('aria-valuemax'));
	this.valNow = parseInt(this.$id.attr('aria-valuenow'));

	this.keys = {
		pageup:   33,
		pagedown: 34,
		end:      35,
		home:     36,
		left:     37,
		up:       38,
		right:    39,
		down:     40 
	};
		
	// bind event handlers
	this.bindHandlers();
}

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers for the spinbutton control
*
* @return {N/A}
*/

OAA_EXAMPLES.spinbutton.prototype.bindHandlers = function() {

	var thisObj = this;

	//////// bind mouse event handlers to the up button //////////////
	this.$upButton.mousedown(function(e) {
		return thisObj.handleMouseDown(e, $(this)); 
	});

	this.$upButton.mouseup(function(e) {
		return thisObj.handleMouseUp(e, $(this)); 
	});

	this.$upButton.mouseenter(function(e) {
		return thisObj.handleMouseEnter(e, $(this)); 
	});

	this.$upButton.mouseout(function(e) {
		return thisObj.handleMouseOut(e, $(this)); 
	});

	this.$upButton.click(function(e) {
		return thisObj.handleClick(e, $(this)); 
	});

	//////// bind mouse event handlers to the down button //////////////
	this.$downButton.mousedown(function(e) {
		return thisObj.handleMouseDown(e, $(this)); 
	});

	this.$downButton.mouseup(function(e) {
		return thisObj.handleMouseUp(e, $(this)); 
	});

	this.$downButton.mouseenter(function(e) {
		return thisObj.handleMouseEnter(e, $(this)); 
	});

	this.$downButton.mouseout(function(e) {
		return thisObj.handleMouseOut(e, $(this)); 
	});

	this.$downButton.focus(function(e) {
		return thisObj.handleFocus(e, $(this)); 
	});

	this.$downButton.click(function(e) {
		return thisObj.handleClick(e, $(this)); 
	});

	//////// bind event handlers to the spinbutton //////////////
	this.$id.keydown(function(e) {
		return thisObj.handleKeyDown(e); 
	});

	this.$id.keypress(function(e) {
		return thisObj.handleKeyPress(e); 
	});

	this.$id.focus(function(e) {
		return thisObj.handleFocus(e); 
	});

	this.$id.blur(function(e) {
		return thisObj.handleBlur(e); 
	});

	this.$id.parent().focusout(function(e) {
		return thisObj.handleBlur(e); 
	});

} // end bindHandlers()

/**
* @method handleClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle click events for the control buttons
*
* @param (e object) e is the event object
*
* @param {object} $button - the jQuery object of the button clicked
*
* @return {boolean} Returns false
*/

OAA_EXAMPLES.spinbutton.prototype.handleClick = function(e, $button) {


	if ($button.attr('id') == this.upID) {

		// if valuemax isn't met, increment valnow
		if (this.valNow < this.valMax) {
			this.valNow++;

			this.$id.text(this.valNow);
			this.$id.attr('aria-valuenow', this.valNow);
		}
	}
	else {

		// if valuemax isn't met, decrement valnow
		if (this.valNow > this.valMin) {
			this.valNow--;

			this.$id.text(this.valNow);
			this.$id.attr('aria-valuenow', this.valNow);
		}
	}

	// set focus on the spinbutton
	this.$id.focus();
		
	e.stopPropagation();
	return false;

} // end handleClick()

/**
* @method handleMouseDown
*
* @memberOf OAA_EXAMPLES
*
* @des a member function to handle mousedown events for the control buttons
*
* @param {object} e - the event object
*
* @param {object} $button - the jQuery object of the button clicked
*
* @return {boolean} Returns false
*/

OAA_EXAMPLES.spinbutton.prototype.handleMouseDown = function(e, $button) {

	var $img = $button.find('img');

	if ($button.attr('id') == this.upID) {
		$img.attr('src', "{{EXAMPLE_MEDIA}}images/button-arrow-up-pressed-hl.png");
	}
	else {
		$img.attr('src', "{{EXAMPLE_MEDIA}}images/button-arrow-down-pressed-hl.png");
	}

	e.stopPropagation();
	return false;

} // end handleMouseDown()

/**
* @method handleMouseUp
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle mouseup events for the control buttons
*
* @param {object} e - the event object
*
* @param {object} $button - the jQuery object of the button clicked
*
* @return {boolean} Returns false
*/

OAA_EXAMPLES.spinbutton.prototype.handleMouseUp = function(e, $button) {

	var $img = $button.find('img');

	if ($button.attr('id') == this.upID) {
		$img.attr('src', "{{EXAMPLE_MEDIA}}images/button-arrow-up-hl.png");
	}
	else {
		$img.attr('src', "{{EXAMPLE_MEDIA}}images/button-arrow-down-hl.png");
	}

	e.stopPropagation();
	return false;

} // end handleMouseUp()

/**
* @method handleMouseEnter
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle mouseenter events for the control buttons
*
* @param {object} e - the event object
*
* @param {object} $button - the jQuery object of the button
*
* @return {boolean} Returns false
*/

OAA_EXAMPLES.spinbutton.prototype.handleMouseEnter = function(e, $button) {

	var $img = $button.find('img');

	if ($button.attr('id') == this.upID) {
		$img.attr('src', "{{EXAMPLE_MEDIA}}images/button-arrow-up-hl.png");
	}
	else {
		$img.attr('src', "{{EXAMPLE_MEDIA}}images/button-arrow-down-hl.png");
	}

	e.stopPropagation();
	return false;

} // end handleMouseOutEnter()

/**
* @method handleMouseOut
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle mouseout events for the control buttons
*
* @param {object} e - the event object
*
* @param {object} $button - the jQuery object of the button
*
* @return {boolean} Returns false
*/

OAA_EXAMPLES.spinbutton.prototype.handleMouseOut = function(e, $button) {

	var $img = $button.find('img');

	if ($button.attr('id') == this.upID) {
		$img.attr('src', "{{EXAMPLE_MEDIA}}images/button-arrow-up.png");
	}
	else {
		$img.attr('src', "{{EXAMPLE_MEDIA}}images/button-arrow-down.png");
	}

	e.stopPropagation();
	return false;

} // end handleMouseOutUp()

/**
* @method handleKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle keydown events for the control.
*
* @param {object} e - the event object
*
* @return {boolean} Returns false if consuming; true if propagating
*/

OAA_EXAMPLES.spinbutton.prototype.handleKeyDown = function(e) {

	if (e.altKey || e.ctrlKey || e.shiftKey) {
		// do nothing
		return true;
	}

	switch(e.keyCode) {
		case this.keys.pageup: {

			if (this.valNow < this.valMax) {

				// if valnow is small enough, increase by the skipVal,
				// otherwise just set to valmax
				if (this.valNow < this.valMax - this.skipVal) {
					this.valNow += this.skipVal;
				}	
				else {
					this.valNow = this.valMax;
				}

				// update the control
				this.$id.attr('aria-valuenow', this.valNow);
				this.$id.html(this.valNow);
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.pagedown: {

			if (this.valNow > this.valMin) {

				// if valNow is big enough, decrease by the skipVal,
				// otherwise just set to valmin
				if (this.valNow > this.valMin + this.skipVal) {
					this.valNow -= this.skipVal;
				}	
				else {
					this.valNow = this.valMin;
				}

				// update the control
				this.$id.attr('aria-valuenow', this.valNow);
				this.$id.html(this.valNow);
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.home: {

			if (this.valNow < this.valMax) {
				this.valNow = this.valMax;
				this.$id.attr('aria-valuenow', this.valNow);
				this.$id.html(this.valNow);
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.end: {

			if (this.valNow > this.valMin) {
				this.valNow = this.valMin;
				this.$id.attr('aria-valuenow', this.valNow);
				this.$id.html(this.valNow);
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.right:
		case this.keys.up: {

			// if valuemin isn't met, increment valnow
			if (this.valNow < this.valMax) {
				this.valNow++;

				this.$id.text(this.valNow);
				this.$id.attr('aria-valuenow', this.valNow);
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.left:
		case this.keys.down: {

			// if valuemax isn't met, decrement valnow
			if (this.valNow > this.valMin) {
				this.valNow--;

				this.$id.text(this.valNow);
				this.$id.attr('aria-valuenow', this.valNow);
			}

			e.stopPropagation();
			return false;
		}
	}
	return true;

} // end handleKeyDown()

/**
* @method handleKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle keypress events for the control.
* This function is required to prevent browser that manipulate the window 
* on keypress (such as Opera) from performing unwanted scrolling.
*
* @param {object} e - the event object
*
* @return {boolean} Returns false if consuming; true if propagating
*/

OAA_EXAMPLES.spinbutton.prototype.handleKeyPress = function(e) {


	if (e.altKey || e.ctrlKey || e.shiftKey) {
		// do nothing
		return true;
	}

	switch(e.keyCode) {
		case this.keys.pageup:
		case this.keys.pagedown:
		case this.keys.home:
		case this.keys.end:
		case this.keys.left:
		case this.keys.up:
		case this.keys.right:
		case this.keys.down: {
			// consume the event
			e.stopPropagation();
			return false;
		}
	}
	return true;

} // end handleKeyPress()

/**
* @method handleFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle focus events for the control.
*
* @param {object} e - the event object
*
* @return {boolean} Returns true
*/

OAA_EXAMPLES.spinbutton.prototype.handleFocus = function(e) {

	// add the focus styling class to the control
	this.$id.addClass('focus');

	return true;

} // end handleFocus()

/**
* @method handleBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to handle blur events for the control.
*
* @param {object} e - the event object
*
* @return {boolean} Returns true
*/

OAA_EXAMPLES.spinbutton.prototype.handleBlur = function(e) {

	// Remove the focus styling class from the control
	this.$id.removeClass('focus');

	return true;

} // end handleBlur()
"""

example_obj.style       = """
div.spinControl {
	margin: 20px;
	margin-left: 40px;
	width: 100px;
	height: 44px;
	border: 1px solid black;
}
div.spinbutton {
	float: left;
	display: inline;
	margin: 1px;
	text-align: right;
	font-weight: bold;
	font-size: 1.6em;
	padding: 7px 10px 7px 0;
	width: 65px;
	height: 28px;
	background-color: #faf7f0;
}
div.spinbutton:active,
div.spinbutton:hover,
div.spinbutton.focus {
	margin: 0;
	background-color: #faf7f0;
	border: 1px solid red;
}
div.button {
	margin: 0;
	margin-left: 77px;
	padding: 0;
	height: 22px;
}
div.button img {
	margin: 0;
	padding: 0;
	border-left: 1px solid black;
}
label.sbLabel {
	font-weight: bold;
	font-size: 1.2em;
}
"""

example1 = create_example(example_obj)