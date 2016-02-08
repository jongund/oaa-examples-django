"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples import *

order = 1

spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='combobox')
m2 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='listbox')
m3 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='option')
m4 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-expanded')
m5 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-labelledby')
m6 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-owns')

# =============================
# Example 1
# =============================

example_obj             = example_object()
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order          = order
example_obj.title       = 'Combobox with aria-autocomplete="none"'
example_obj.permanent_slug = 'combobox1'

example_obj.a11y_features = """
This is example implements a combobox widget with aria-autocomplete="none". The edit box is read only. The application is required to manage focus for the list box so assistive technologies can follow the currently selected option. For clarity, this example was designed not to update the edit box until the user makes a choice from the list.
"""
example_obj.keyboard    = """
If focus is on the edit box:
* Up Arrow: Move upward in list, even if the list box is closed.
* Down Arrow: Move downward in list, even if the list box is closed.
* Alt + Up Arrow/Down Arrow: Open or close the list box. Focus moves to selected option in list.<br>Note: Opera does not propagate alt key modifer events to the web page. Alt+Arrow key combinations will not work in Opera.


If focus is on the list box:</p>
* Enter: Select highlighted option and close the list box. Focus moves to the edit box.
* Escape: Close list box without changing the combobox value (e.g. no selection is made). Focus moves to the edit box.
* Up Arrow: Move upward in list.</li>
* Down Arrow: Move downward in list.</li>
* Home: Move to first option in list.</li>
* End: Move to last option in list.</li>
* Tab: Select highlighted option and close list box. Focus moves to the next focusable element in page.
* Shift+Tab: Same as tab key except focus moves to previous focusable item in page.

"""

example_obj.markup = [m1,m2,m3,m4,m5,m6]

example_obj.html       = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<div role="application" tabindex="-1">

<form autocomplete="off">
<div id="cb1" class="cb">
	<div class="cb_label"><label id="cb1-label" for="cb1-edit">State</label>:</div>
	<input id="cb1-edit" class="cb_edit" type="text"
      role="combobox"
		aria-labelledby="cb1-label"
		aria-autocomplete="none"
		aria-readonly="true"
		aria-owns="cb1-list"
		tabindex="0" />
	<div id="cb1-button-label" class="hidden">Open list of states</div>
	<button id="cb1-button" class="cb_button" aria-labelledby="cb1-button-label" aria-controls="cb1-list" tabindex="-1">
		<img src="{{EXAMPLE_MEDIA}}images/button-arrow-down.png" alt="Open or close the list box" />
	</button>

	<ul id="cb1-list" class="cb_list" tabindex="-1" aria-expanded="true" role="listbox">
		<li id="cb1-opt1" role="option" class="cb_option" tabindex="-1">Alabama</li>
		<li id="cb1-opt2" role="option" class="cb_option" tabindex="-1">Alaska</li>
		<li id="cb1-opt3" role="option" class="cb_option" tabindex="-1">American Samoa</li>
		<li id="cb1-opt4" role="option" class="cb_option" tabindex="-1">Arizona</li>
		<li id="cb1-opt5" role="option" class="cb_option" tabindex="-1">Arkansas</li>
		<li id="cb1-opt6" role="option" class="cb_option" tabindex="-1">California</li>
		<li id="cb1-opt7" role="option" class="cb_option" tabindex="-1">Colorado</li>
		<li id="cb1-opt8" role="option" class="cb_option" tabindex="-1">Connecticut</li>
		<li id="cb1-opt9" role="option" class="cb_option" tabindex="-1">Delaware</li>
		<li id="cb1-opt10" role="option" class="cb_option" tabindex="-1">District of Columbia</li>
		<li id="cb1-opt11" role="option" class="cb_option" tabindex="-1">Florida</li>
		<li id="cb1-opt12" role="option" class="cb_option" tabindex="-1">Georgia</li>
		<li id="cb1-opt13" role="option" class="cb_option" tabindex="-1">Guam</li>
		<li id="cb1-opt14" role="option" class="cb_option" tabindex="-1">Hawaii</li>
		<li id="cb1-opt15" role="option" class="cb_option" tabindex="-1">Idaho</li>
		<li id="cb1-opt16" role="option" class="cb_option selected" tabindex="-1">Illinois</li>
		<li id="cb1-opt17" role="option" class="cb_option" tabindex="-1">Indiana</li>
		<li id="cb1-opt18" role="option" class="cb_option" tabindex="-1">Iowa</li>
		<li id="cb1-opt19" role="option" class="cb_option" tabindex="-1">Kansas</li>
		<li id="cb1-opt20" role="option" class="cb_option" tabindex="-1">Kentucky</li>
		<li id="cb1-opt21" role="option" class="cb_option" tabindex="-1">Louisiana</li>
		<li id="cb1-opt22" role="option" class="cb_option" tabindex="-1">Maine</li>
		<li id="cb1-opt23" role="option" class="cb_option" tabindex="-1">Maryland</li>
		<li id="cb1-opt24" role="option" class="cb_option" tabindex="-1">Massachusetts</li>
		<li id="cb1-opt25" role="option" class="cb_option" tabindex="-1">Michigan</li>
		<li id="cb1-opt26" role="option" class="cb_option" tabindex="-1">Minnesota</li>
		<li id="cb1-opt27" role="option" class="cb_option" tabindex="-1">Mississippi</li>
		<li id="cb1-opt28" role="option" class="cb_option" tabindex="-1">Missouri</li>
		<li id="cb1-opt29" role="option" class="cb_option" tabindex="-1">Montana</li>
		<li id="cb1-opt30" role="option" class="cb_option" tabindex="-1">Nebraska</li>
		<li id="cb1-opt31" role="option" class="cb_option" tabindex="-1">Nevada</li>
		<li id="cb1-opt32" role="option" class="cb_option" tabindex="-1">New Hampshire</li>
		<li id="cb1-opt33" role="option" class="cb_option" tabindex="-1">New Jersey</li>
		<li id="cb1-opt34" role="option" class="cb_option" tabindex="-1">New Mexico</li>
		<li id="cb1-opt35" role="option" class="cb_option" tabindex="-1">New York</li>
		<li id="cb1-opt36" role="option" class="cb_option" tabindex="-1">North Carolina</li>
		<li id="cb1-opt37" role="option" class="cb_option" tabindex="-1">North Dakota</li>
		<li id="cb1-opt38" role="option" class="cb_option" tabindex="-1">Northern Marianas Islands</li>
		<li id="cb1-opt39" role="option" class="cb_option" tabindex="-1">Ohio</li>
		<li id="cb1-opt40" role="option" class="cb_option" tabindex="-1">Oklahoma</li>
		<li id="cb1-opt41" role="option" class="cb_option" tabindex="-1">Oregon</li>
		<li id="cb1-opt42" role="option" class="cb_option" tabindex="-1">Pennsylvania</li>
		<li id="cb1-opt43" role="option" class="cb_option" tabindex="-1">Puerto Rico</li>
		<li id="cb1-opt44" role="option" class="cb_option" tabindex="-1">Rhode Island</li>
		<li id="cb1-opt45" role="option" class="cb_option" tabindex="-1">South Carolina</li>
		<li id="cb1-opt47" role="option" class="cb_option" tabindex="-1">South Dakota</li>
		<li id="cb1-opt48" role="option" class="cb_option" tabindex="-1">Tennessee</li>
		<li id="cb1-opt49" role="option" class="cb_option" tabindex="-1">Texas</li>
		<li id="cb1-opt50" role="option" class="cb_option" tabindex="-1">Utah</li>
		<li id="cb1-opt51" role="option" class="cb_option" tabindex="-1">Vermont</li>
		<li id="cb1-opt52" role="option" class="cb_option" tabindex="-1">Virginia</li>
		<li id="cb1-opt53" role="option" class="cb_option" tabindex="-1">Virgin Islands</li>
		<li id="cb1-opt54" role="option" class="cb_option" tabindex="-1">Washington</li>
		<li id="cb1-opt55" role="option" class="cb_option" tabindex="-1">West Virginia</li>
		<li id="cb1-opt56" role="option" class="cb_option" tabindex="-1">Wisconsin</li>
		<li id="cb1-opt57" role="option" class="cb_option" tabindex="-1">Wyoming</li>
	</ul>
</div>
</form>
</div>
"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};
var g_cb1 = null;  // set to active combobox for blur function

$(document).ready(function() {

	g_cb1 = new OAA_EXAMPLES.combobox('cb1', false);
}); // end ready

/**
* keyCodes() is an object to contain keycodes needed for the application
*/
function keyCodes() {
	// Define values for keycodes
	this.backspace  = 8;
	this.tab        = 9;
	this.enter      = 13;
	this.esc        = 27;

	this.space      = 32;
	this.pageup     = 33;
	this.pagedown   = 34;
	this.end        = 35;
	this.home       = 36;

	this.up         = 38;
	this.down       = 40; 
	
	this.del        = 46;

} // end keyCodes

/**
* @constructor combobox
*
* @memberOf OAA_EXAMPLES
*
* @desc a class for an ARIA-enabled combobox widget
*
* @param {string} id - the id of the div containing the combobox. Text input must have role="combobox".
*
* @param {boolean} editable - true if the edit box should be editable; false if read-only.
*
* @return {N/A}
*/

/**
* @private
* @constructor Internal Properties
*
* @desc Define the object properties
* @property {object} id - The jQuery object of the div containing the combobox
* @property {object} keyCodes - assigns keycodes
* @property {boolean} editable - True if the edit box is editable
*
* @desc Store jQuery objects for the elements of the combobox
* @property {object} $button - The jQuery object of the edit box
* @property {object} $edit - The jQuery object of the button
* @property {object} $buttonImg - The jQuery object of the button image
* @property {object} $list - The jQuery object of the option list
* @property {object} $options - an array of jQuery objects for the combobox options
*
* @property {boolean} $selected - the current value of the combobox
* @property {boolean} $focused - the currently selected option in the combo list
* @property {object} $timer - stores the close list timer that is set when combo looses focus
*/

OAA_EXAMPLES.combobox = function(id, editable) {

	this.$id = $('#' + id);
	this.editable = editable;   
	this.keys = new keyCodes();

	this.$edit = $('#' + id + '-edit');  
	this.$button = $('#' + id + '-button');  
	this.$buttonImg = $('#' + id).find('img'); 
	this.$list = $('#' + id + '-list'); 
	this.$options = this.$list.find('li'); 

	this.$selected;
	this.$focused; 
	this.timer = null; 
	// Initalize the combobox
	this.init();

	// bind event handlers for the widget
	this.bindHandlers();

} // end combobox constructor


/**
* @method init
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to initialize the combobox elements. Hides the list and sets ARIA attributes
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.init = function() {

	// Hide the list of options
	this.$list.hide().attr('aria-expanded', 'false');

	// If the edit box is to be readonly, aria-readonly must be defined as true
	if (this.editable == false) {
		this.$edit.attr('aria-readonly', 'true');
	}

	// Set initial value for the edit box
	this.$selected = this.$options.filter('.selected');

	if (this.$selected.length > 0) {
		this.$edit.val(this.$selected.text());
	}

} // end initCombo()

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers for the combobox elements
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.bindHandlers = function() {

	var thisObj = this;

	///////////////// bind editbox handlers /////////////////////////

	this.$edit.keydown(function(e) {
		return thisObj.handleEditKeyDown($(this), e);
	});

	this.$edit.keypress(function(e) {
		return thisObj.handleEditKeyPress($(this), e);
	});

	this.$edit.blur(function(e) {
		return thisObj.handleComboBlur($(this), e);
	});

	///////////////// bind handlers for the button /////////////////////////
	
	this.$button.click(function(e) {
		return thisObj.handleButtonClick($(this), e);
	});

	this.$button.mouseover(function(e) {
		return thisObj.handleButtonMouseOver($(this), e);
	});

	this.$button.mouseout(function(e) {
		return thisObj.handleButtonMouseOut($(this), e);
	});

	this.$button.mousedown(function(e) {
		return thisObj.handleButtonMouseDown($(this), e);
	});

	this.$button.mouseup(function(e) {
		return thisObj.handleButtonMouseUp($(this), e);
	});

	///////////////// bind listbox handlers /////////////////////////

	this.$list.focus(function(e) {
		return thisObj.handleComboFocus($(this), e);
	});

	this.$list.blur(function(e) {
		return thisObj.handleComboBlur($(this), e);
	});

	///////////////// bind list option handlers /////////////////////////

	this.$options.keydown(function(e) {
		return thisObj.handleOptionKeyDown($(this), e);
	});

	this.$options.keypress(function(e) {
		return thisObj.handleOptionKeyPress($(this), e);
	});

	this.$options.click(function(e) {
		return thisObj.handleOptionClick($(this), e);
	});

	this.$options.focus(function(e) {
		return thisObj.handleComboFocus($(this), e);
	});

	this.$options.blur(function(e) {
		return thisObj.handleComboBlur($(this), e);
	});

} // end bindHandlers()

/**
* @method isOpen
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to get the current state of the list box
*
* @return {boolean} returns true if list box is open; false if it is not
*/

OAA_EXAMPLES.combobox.prototype.isOpen = function() {

	if (this.$list.attr('aria-expanded') == 'true') {
		return true;
	}
	else {
		return false;
	}

} // end isOpen

/**
* @method closeList
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to close the list box if it is open
*
* @param {boolean} restore - true if function should restore higlight to stored list selection
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.closeList = function(restore) {

	var $curOption = this.$options.filter('.selected');

	if (restore == true) {
		$curOption = this.$selected;

		// remove the selected class from the other list items
		this.$options.removeClass('selected');

		// add selected class to the stored selection
		$curOption.addClass('selected');
	}

	this.$list.hide().attr('aria-expanded', 'false');

	// set focus on the edit box
	this.$edit.focus();

} // end closeList()

/**
* @method openList
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to open the list box if it is closed
*
* @param {booleam} restore - true if function should restore higlight to stored list selection
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.openList = function(restore) {

	var $curOption = this.$options.filter('.selected');


	if (restore == true) {

		if (this.$selected.length == 0) {
			// select the first item
			this.selectOption(this.$options.first());
		}

		$curOption = this.$selected;

		// remove the selected class from the other list items
		this.$options.removeClass('selected');

		// add selected class to the stored selection
		$curOption.addClass('selected');
	}

	this.$list.show().attr('aria-expanded', 'true');

	// scroll to the currently selected option
	this.$list.scrollTop(this.calcOffset($curOption));

	// set focus on the selected item
	this.$selected.focus();

} // end openList();

/**
* @method toggleList
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to toggle the display of the combobox options.
*
* @param (restore booleam) restore is true if toggle should restore higlight to stored list selection
*
* Return N/A
*/

OAA_EXAMPLES.combobox.prototype.toggleList = function(restore) {

	if (this.isOpen() == true) {

		this.closeList(restore);
	}
	else {
		this.openList(restore);
	}

} // end toggleList()

/**
* @method selectOption
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to select a new combobox option.
* The jQuery object for the new option is stored and the selected class is added
*
* @param {object} $id - the jQuery object of the new option to select
*
* @return {N/A}
*/ 

OAA_EXAMPLES.combobox.prototype.selectOption = function($id) {

	// If there is a selected option, remove the selected class from it
	if (this.$selected.length > 0) {
		this.$selected.removeClass('selected');
	}
	
	// add the selected class to the new option
	$id.addClass('selected');

	// store the newly selected option
	this.$selected = $id;

	// update the edit box
	this.$edit.val($id.text());
	
} // end selectOption

/**
* @method calcOffset
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to calculate the pixel offset of a list option from the top of the list
*
* @param {obj} $id - the jQuery object of the option to scroll to
*
* @return {integer} returns the pixel offset of the option
*/

OAA_EXAMPLES.combobox.prototype.calcOffset = function($id) {
	var offset = 0;
	var selectedNdx = this.$options.index($id);

	for (var ndx = 0; ndx < selectedNdx; ndx++) {
		offset += this.$options.eq(ndx).outerHeight();
	}

	return offset;

} // end calcOffset

/**
* @method handleButtonClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to consume button click events. This handler prevents
* clicks on the button from reloading the page. This could also be done by adding 'onclick="false";' to the
* button HTML markup.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean}  returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonClick = function($id,  e) {

	e.stopPropagation();
	return false;

} // end handleButtonClick();

/**
* @method handleButtonMouseOver
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mouseover events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseOver = function($id,  e) {

	// change the button image to reflect the highlight state
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down-hl.png');

	e.stopPropagation();
	return false;

} // end handleButtonMouseOver();

/**
* @method handleButtonMouseOut
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mouseout events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return (boolean)  returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseOut = function($id,  e) {

	// reset image to normal state
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down.png');

	e.stopPropagation();
	return false;

} // end handleButtonMouseOut();

/**
* @method handleButtonMouseDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mousedown events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return (boolean)  returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseDown = function($id,  e) {

	// change the button image to reflect the pressed state
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down-pressed-hl.png');

	// toggle the display of the option list
	this.toggleList(true);

	e.stopPropagation();
	return false;

} // end handleButtonMouseDown();

/**
* Function handleButtonMouseUp() is a member function to process button mouseup events
*
* @param (e object) e is the event object associated with the event
*
* @param ($id object) $id is the jQuery object for the element firing the event
*
* @return (boolean)  returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseUp = function($id,  e) {

	// reset button image
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down-hl.png');

	e.stopPropagation();
	return false;

} // end handleButtonMouseUp();

/**
* @method handleOptionKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for
* the combobox
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false if consuming; true if not processing
*/

OAA_EXAMPLES.combobox.prototype.handleOptionKeyDown = function($id,  e) {

	var curNdx = this.$options.index($id);

	if (e.ctrlKey) {
		// do not process
		return true;
	}

	switch(e.keyCode) {
		case this.keys.tab: {
			// update and close the combobox

			if ($id.text() != this.$selected.text()) {

				// store the new selection
				this.selectOption($id);
			}

			// Close the option list
			this.closeList(false);

			// allow tab to propagate
			return true;
		}
		case this.keys.esc: {
			// Do not change combobox value

			// Close the option list
			this.closeList(true);

			e.stopPropagation();
			return false;
		}
		case this.keys.enter: {
			// change the combobox value

			if ($id.text() != this.$selected.text()) {

				// store the new selection
				this.selectOption($id);
			}

			// Close the option list
			this.closeList(false);

			e.stopPropagation();
			return false;
		}
		case this.keys.up: {
			
			if (e.altKey) {
				// alt+up toggles the list
				this.toggleList(true);

			}
			else {
				// move to the previous item in the list
			
				if (curNdx > 0) {
					var $prev = this.$options.eq(curNdx - 1);

					// remove the selected class from the current selection
					$id.removeClass('selected');

					// Add the selected class to the new selection
					$prev.addClass('selected');

					// scroll the list window to the new option
					this.$list.scrollTop(this.calcOffset($prev));

					// Set focus on the new item
					$prev.focus();
				}
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.down: {

			if (e.altKey) {
				// alt+up toggles the list
				this.toggleList(true);
			}
			else {
				// move to the next item in the list
			
				if (curNdx < this.$options.length - 1) {
					var $next = this.$options.eq(curNdx + 1);

					// remove the selected from the current selection
					$id.removeClass('selected');

					// Add the selected class to the new selection
					$next.addClass('selected');

					// scroll the list window to the new option
					this.$list.scrollTop(this.calcOffset($next));

					// Set focus on the new item
					$next.focus();
				}
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.home: {
			// select the first list item

			var $first = this.$options.first();

			// remove the selected class from the current selection
			this.$options.eq(curNdx).removeClass('selected');

			// Add the selected class to the new selection
			$first.addClass('selected');

			// scroll the list window to the new option
			this.$list.scrollTop(0);

			// set focus on the first item
			$first.focus();

			e.stopPropagation();
			return false;
		}
		case this.keys.end: {
			// select the last list item

			var $last = this.$options.last();

			// remove the selected class from the current selection
			this.$options.eq(curNdx).removeClass('selected');

			// Add the selected class to the new selection
			$last.addClass('selected');

			// scroll the list window to the new option
			this.$list.scrollTop(this.calcOffset($last));

			// set focus on last item
			$last.focus();

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleOptionKeyDown()

/**
* @method handleOptionKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for
* the combobox. Needed for browsers that use keypress to manipulate the window
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false if consuming; true if not processing
*/

OAA_EXAMPLES.combobox.prototype.handleOptionKeyPress = function($id,  e) {

	var curNdx = this.$options.index($id);

	if (e.altKey || e.ctrlKey || e.shiftKey) {
		// do not process
		return true;
	}

	switch(e.keyCode) {
		case this.keys.esc:
		case this.keys.enter:
		case this.keys.up:
		case this.keys.down:
		case this.keys.home:
		case this.keys.end: {
			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleOptionKeyPress()

/**
* @method handleEditKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for
* the edit box.
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @param {object} e - the event object associated with the event
*
* @return {boolean} Returns false if consuming; true if not processing
*/

OAA_EXAMPLES.combobox.prototype.handleEditKeyDown = function($id,  e) {

	var curNdx = this.$options.index(this.$selected);

	if (e.altKey && (e.keyCode == this.keys.up || e.keyCode == this.keys.down)) {

		this.toggleList(true);

		e.stopPropagation();
		return false;
	}

	switch (e.keyCode) {
		case this.keys.backspace:
		case this.keys.del: {
			this.$edit.val(this.$selected.text());

			e.stopPropagation();
			return false;
		}
		case this.keys.enter: {

			// toggle the option list
			this.toggleList(false);

			e.stopPropagation();
			return false;
		}
		case this.keys.up: {
			
			// move to the previous item in the list
			
			if (curNdx > 0) {
				var $prev = this.$options.eq(curNdx - 1);

				this.selectOption($prev);
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.down: {

			// move to the next item in the list
			
			if (curNdx < this.$options.length - 1) {
				var $next = this.$options.eq(curNdx + 1);

				this.selectOption($next);
			}

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleEditKeyDown()

/**
* Function handleEditKeyPress() is a member function to process keypress events for
* the edit box. Needed for browsers that use keypress events to manipulate the window.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false if consuming; true if not processing
*/

OAA_EXAMPLES.combobox.prototype.handleEditKeyPress = function($id,  e) {

	var curNdx = this.$options.index($id);

	if (e.altKey && (e.keyCode == this.keys.up || e.keyCode == this.keys.down)) {
		e.stopPropagation();
		return false;
	}

	switch(e.keyCode) {
		case this.keys.esc:
		case this.keys.enter: {

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleOptionKeyPress()

/**
* @method handleOptionClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events for the combobox.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false
*/

OAA_EXAMPLES.combobox.prototype.handleOptionClick = function($id, e) {

	// select the clicked item
	this.selectOption($id);

	// close the list
	this.closeList(false);

	e.stopPropagation();
	return false;	

} // end handleOptionClick()

/**
* Function handleComboFocus() is a member function to process focus events for
* the list box
*
* @param (e object) e is the event object associated with the event
*
* @param ($id object) $id is the jQuery object for the element firing the event
*
* @return (boolean) Returns true
*/

OAA_EXAMPLES.combobox.prototype.handleComboFocus = function($id,  e) {

	if (this.timer != null) {
		window.clearTimeout(this.timer);
		this.timer = null;
	}

	return true;

} // end handleComboFocus()

/**
* @method handleComboBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process blur events for the combobox
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns true
*/

OAA_EXAMPLES.combobox.prototype.handleComboBlur = function($id,  e) {

	// store the currently selected value
	this.selectOption(this.$options.filter('.selected'));

	// close the list box
	if (this.isOpen() == true) {
		this.timer = window.setTimeout(function() {g_cb1.closeList(false);}, 40);
	}

	return true;

} // end handleComboBlur()
"""

example_obj.style       = """
* {
	font-family: "Times New Roman,Georgia,Serif"; 
}
.hidden {
	position: absolute;
	top: -20em;
	left: -200em;
}

.wrapper {
	height: 24px;
	overflow: auto;
}
.cb {
	margin: 20px;
	padding: 0;
	height: 24px;
	display: block;
	overflow: visible;
}

.cb_label {
	margin: 0;
	padding: 2px;
	width: 45px;
	font-weight: bold;
	float: left;
	display: inline;
}
.cb_edit {
	margin: 0;
	padding: 2px 3px;
	width: 240px;
	height: 18px;
	border: 1px solid black;
	font-size: 1em;
	float: left;
	display: inline;
}
.cb_button {
	margin: 0;
	padding: 0;
	height: 24px;
	width: 24px;
	border: 1px solid black;
	background-color: #999;
	float: left;
	display: inline;
	text-align: center;
}

button.cb_button img {
	margin: 0;
	padding: 0;
	height: 22px;
	width: 22px;
	position: relative;
	top: -1px;
	left: -3px;
}

.cb_list {
	clear: both;
	list-style: none;
	padding: 0;
	margin: 0;
	margin-left: 49px;
	border: 1px solid black;
	width: 246px;
	height: 200px;
	overflow: auto;
	background-color: #fff;
	position: relative;
	z-index: 300;
}

.cb_option {
	margin: 0 1px 0 0;
	padding: 2px 5px;
}
.selected {
	border-top: 1px solid #44e;
	border-bottom: 1px solid #44e;
	padding: 1px 5px;
	background-color: #77a;
	color: #fff;
}
.cb_option:hover {
	border-top: 1px solid #44e;
	border-bottom: 1px solid #44e;
	padding: 1px 5px;
	font-weight: bold;
	background-color: #77f;
	color: #fff;
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
example_obj.title       = 'Combobox with aria-autocomplete="inline"'
example_obj.permanent_slug = 'combobox2'

example_obj.a11y_features = """
This example implements a combobox widget with aria-autocomplete="inline". Focus will remain on the edit box while the user manipulates the list box.
"""
example_obj.keyboard    = """
<ul>
    <li>Alt + Up Arrow/Down Arrow: Open or close the list box. Focus moves to selected option in list.<br>Note: Opera does not propagate alt key modifer events to the web page. Alt+Arrow key combinations will not work in Opera.</li>
    <li>Up Arrow: Select the previous option. If the list box is expanded, move upward in list and update the edit box but do not select a new option.</li>
    <li>Down Arrow: Select the next option. If the list box is expanded, move downward in list and update the edit box but do not select a new option.</li>
    <li>Home: Select the first option. If the list box is expanded, move to first list option and update the edit box but do not select.</li>
    <li>End: Select the last option. If the list box is expanded, move to last list and update the edit box but do not select.</li>
    <li>Enter: Select the highlighted list option and collapse the list box. If the list box is collapsed, expand it.</li>
    <li>Escape: Close list box without changing the combobox value (e.g. no selection is made).</li>
    <li>Tab: Select highlighted option and close list box (if it is expanded). Focus moves to the next focusable element in page.</li>
    <li>Shift+Tab: Same as tab key except focus moves to previous focusable item in page.</li>
</ul>
"""

example_obj.markup = [m1,m2,m3,m4,m5,m6]

example_obj.html       = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<div role="application" tabindex="-1">

<form autocomplete="off">
<div id="cb1" class="cb">
	<div class="cb_label"><label id="cb1-label" for="cb1-edit">State</label>:</div>
	<input id="cb1-edit" class="cb_edit" type="text" tabindex="0"
      role="combobox"
		aria-labelledby="cb1-label"
		aria-autocomplete="inline"
		aria-owns="cb1-list"/>
	<div id="cb1-button-label" class="hidden">Open list of states</div>
	<button id="cb1-button" class="cb_button" aria-labelledby="cb1-button-label" aria-controls="cb1-list" tabindex="-1">
		<img src="{{EXAMPLE_MEDIA}}images/button-arrow-down.png" alt="Open or close the list box" />
	</button>

	<ul id="cb1-list" class="cb_list" tabindex="-1" role="listbox" aria-expanded="true">
		<li id="cb1-opt1" role="option" class="cb_option">Alabama</li>
		<li id="cb1-opt2" role="option" class="cb_option">Alaska</li>
		<li id="cb1-opt3" role="option" class="cb_option">American Samoa</li>
		<li id="cb1-opt4" role="option" class="cb_option">Arizona</li>
		<li id="cb1-opt5" role="option" class="cb_option">Arkansas</li>
		<li id="cb1-opt6" role="option" class="cb_option">California</li>
		<li id="cb1-opt7" role="option" class="cb_option">Colorado</li>
		<li id="cb1-opt8" role="option" class="cb_option">Connecticut</li>
		<li id="cb1-opt9" role="option" class="cb_option">Delaware</li>
		<li id="cb1-opt10" role="option" class="cb_option">District of Columbia</li>
		<li id="cb1-opt11" role="option" class="cb_option">Florida</li>
		<li id="cb1-opt12" role="option" class="cb_option">Georgia</li>
		<li id="cb1-opt13" role="option" class="cb_option">Guam</li>
		<li id="cb1-opt14" role="option" class="cb_option">Hawaii</li>
		<li id="cb1-opt15" role="option" class="cb_option">Idaho</li>
		<li id="cb1-opt16" role="option" class="cb_option selected">Illinois</li>
		<li id="cb1-opt17" role="option" class="cb_option">Indiana</li>
		<li id="cb1-opt18" role="option" class="cb_option">Iowa</li>
		<li id="cb1-opt19" role="option" class="cb_option">Kansas</li>
		<li id="cb1-opt20" role="option" class="cb_option">Kentucky</li>
		<li id="cb1-opt21" role="option" class="cb_option">Louisiana</li>
		<li id="cb1-opt22" role="option" class="cb_option">Maine</li>
		<li id="cb1-opt23" role="option" class="cb_option">Maryland</li>
		<li id="cb1-opt24" role="option" class="cb_option">Massachusetts</li>
		<li id="cb1-opt25" role="option" class="cb_option">Michigan</li>
		<li id="cb1-opt26" role="option" class="cb_option">Minnesota</li>
		<li id="cb1-opt27" role="option" class="cb_option">Mississippi</li>
		<li id="cb1-opt28" role="option" class="cb_option">Missouri</li>
		<li id="cb1-opt29" role="option" class="cb_option">Montana</li>
		<li id="cb1-opt30" role="option" class="cb_option">Nebraska</li>
		<li id="cb1-opt31" role="option" class="cb_option">Nevada</li>
		<li id="cb1-opt32" role="option" class="cb_option">New Hampshire</li>
		<li id="cb1-opt33" role="option" class="cb_option">New Jersey</li>
		<li id="cb1-opt34" role="option" class="cb_option">New Mexico</li>
		<li id="cb1-opt35" role="option" class="cb_option">New York</li>
		<li id="cb1-opt36" role="option" class="cb_option">North Carolina</li>
		<li id="cb1-opt37" role="option" class="cb_option">North Dakota</li>
		<li id="cb1-opt38" role="option" class="cb_option">Northern Marianas Islands</li>
		<li id="cb1-opt39" role="option" class="cb_option">Ohio</li>
		<li id="cb1-opt40" role="option" class="cb_option">Oklahoma</li>
		<li id="cb1-opt41" role="option" class="cb_option">Oregon</li>
		<li id="cb1-opt42" role="option" class="cb_option">Pennsylvania</li>
		<li id="cb1-opt43" role="option" class="cb_option">Puerto Rico</li>
		<li id="cb1-opt44" role="option" class="cb_option">Rhode Island</li>
		<li id="cb1-opt45" role="option" class="cb_option">South Carolina</li>
		<li id="cb1-opt47" role="option" class="cb_option">South Dakota</li>
		<li id="cb1-opt48" role="option" class="cb_option">Tennessee</li>
		<li id="cb1-opt49" role="option" class="cb_option">Texas</li>
		<li id="cb1-opt50" role="option" class="cb_option">Utah</li>
		<li id="cb1-opt51" role="option" class="cb_option">Vermont</li>
		<li id="cb1-opt52" role="option" class="cb_option">Virginia</li>
		<li id="cb1-opt53" role="option" class="cb_option">Virgin Islands</li>
		<li id="cb1-opt54" role="option" class="cb_option">Washington</li>
		<li id="cb1-opt55" role="option" class="cb_option">West Virginia</li>
		<li id="cb1-opt56" role="option" class="cb_option">Wisconsin</li>
		<li id="cb1-opt57" role="option" class="cb_option">Wyoming</li>
	</ul>
</div>
</form>
</div>
"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};
var g_cb1 = null;  // variable for the combobox instantiation

$(document).ready(function() {

	g_cb1 = new OAA_EXAMPLES.combobox('cb1', true);
}); // end ready

/**
* keyCodes() is an object to contain keycodes needed for the application
*/
function keyCodes() {
	// Define values for keycodes
	this.backspace  = 8;
	this.tab        = 9;
	this.enter      = 13;
	this.shift      = 16; // defined for keyUp event handler - firefox browser fix
	this.ctrl       = 17; // defined for keyUp event handler - firefox browser fix
	this.alt        = 18; // defined for keyUp event handler - firefox browser fix
	this.esc        = 27;

	this.space      = 32;
	this.pageup     = 33;
	this.pagedown   = 34;
	this.end        = 35;
	this.home       = 36;

	this.left       = 37;
	this.up         = 38;
	this.right      = 39; 
	this.down       = 40; 

} // end keyCodes

/**
* @constructor combobox
*
* @memberOf OAA_EXAMPLES
*
* @desc a class for an ARIA-enabled combobox widget
*
* @param {string} id - the id of the div containing the combobox. Text input must have role="combobox".
*
* @param {boolean} editable is true if the edit box should be editable; false if read-only.
*
* @return {N/A}
*/

/**
* @private
* @constructor Internal Properties
*
* @property {object} $id - The jQuery object of the div containing the combobox
* @property {boolean} editable - True if the edit box is editable
*
* @property {object} $edit - The jQuery object of the edit box
* @property {object} $button - The jQuery object of the button
* @property {object} $list - The jQuery object of the option list
* @property {object} $options - An array of jQuery objects for the combobox options
*
* @property {boolean} $selected  - the current value of the combobox
* @property {boolean} $focused - the currently selected option in the combo list
* @property {object} timer - stores the close list timer that is set when combo looses focus
*/

OAA_EXAMPLES.combobox = function(id, editable) {

	// Define the object properties

	this.$id = $('#' + id); 
	this.editable = editable; 
	this.keys = new keyCodes();

	// Store jQuery objects for the elements of the combobox
	this.$edit = $('#' + id + '-edit');  
	this.$button = $('#' + id + '-button'); 
	this.$list = $('#' + id + '-list');  
	this.$options = this.$list.find('li'); 

	this.$selected;
	this.$focused; 
	this.timer = null;
	// Initalize the combobox
	this.init();

	// bind event handlers for the widget
	this.bindHandlers();

} // end combobox constructor


/**
* @method init
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to initialize the combobox elements. Hides the list
* and sets ARIA attributes
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.init = function() {

	// Hide the list of options
	this.closeList(false);

	// If the edit box is to be readonly, aria-readonly must be defined as true
	if (this.editable == false) {
		this.$edit.attr('aria-readonly', 'false');
	}

	// Set initial value for the edit box
	this.$selected = this.$options.filter('.selected');

	if (this.$selected.length > 0) {
		this.$edit.val(this.$selected.text());
	}

} // end initCombo()

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers for the combobox elements
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.bindHandlers = function() {

	var thisObj = this;

	///////////////// bind editbox handlers /////////////////////////

	this.$edit.keydown(function(e) {
		return thisObj.handleEditKeyDown($(this), e);
	});

	this.$edit.keyup(function(e) {
		return thisObj.handleEditKeyUp($(this), e);
	});

	this.$edit.keypress(function(e) {
		return thisObj.handleEditKeyPress($(this), e);
	});

	this.$edit.blur(function(e) {
		return thisObj.handleComboBlur($(this), e);
	});

	///////////////// bind handlers for the button /////////////////////////
	
	this.$button.click(function(e) {
		return thisObj.handleButtonClick($(this), e);
	});

	this.$button.mouseover(function(e) {
		return thisObj.handleButtonMouseOver($(this), e);
	});

	this.$button.mouseout(function(e) {
		return thisObj.handleButtonMouseOut($(this), e);
	});

	this.$button.mousedown(function(e) {
		return thisObj.handleButtonMouseDown($(this), e);
	});

	this.$button.mouseup(function(e) {
		return thisObj.handleButtonMouseUp($(this), e);
	});

	///////////////// bind listbox handlers /////////////////////////

	this.$list.focus(function(e) {
		return thisObj.handleComboFocus($(this), e);
	});

	this.$list.blur(function(e) {
		return thisObj.handleComboBlur($(this), e);
	});

	///////////////// bind list option handlers /////////////////////////

	this.$options.click(function(e) {
		return thisObj.handleOptionClick($(this), e);
	});

} // end bindHandlers()

/**
* @method isOpen
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to get the current state of the list box
*
* @return {boolean} returns true if list box is open; false if it is not
*/

OAA_EXAMPLES.combobox.prototype.isOpen = function() {

	if (this.$list.attr('aria-expanded') == 'true') {
		return true;
	}
	else {
		return false;
	}

} // end isOpen

/**
* @method closeList
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to close the list box if it is open
*
* @param {boolean} restore is true if function should restore higlight to stored list selection
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.closeList = function(restore) {

	var $curOption = this.$options.filter('.selected');

	if (restore == true) {
		$curOption = this.$selected;

		// remove the selected class from the other list items
		this.$options.removeClass('selected');

		// add selected class to the stored selection
		$curOption.addClass('selected');
	}

	this.$list.hide().attr('aria-expanded', 'false');

} // end closeList()

/**
* @method openList
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to open the list box if it is closed
*
* @param {boolean} restore is true if function should restore higlight to stored list selection
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.openList = function(restore) {

	var $curOption = this.$options.filter('.selected');


	if (restore == true) {
		$curOption = this.$selected;

		// remove the selected class from the other list items
		this.$options.removeClass('selected');

		// add selected class to the stored selection
		$curOption.addClass('selected');
	}

	this.$list.show().attr('aria-expanded', 'true');

	if (this.$selected.length == 0) {

		// select the first item
		this.selectOption(this.$options.first());
		$curOption = this.$selected;
	}

	// scroll to the currently selected option
	this.$list.scrollTop(this.calcOffset($curOption));

} // end openList();

/**
* @method toggleList
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to toggle the display of the combobox options.
*
* @param {boolean} restore is true if toggle should restore higlight to stored list selection
*
* Return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.toggleList = function(restore) {

	if (this.isOpen() == true) {

		this.closeList(restore);
	}
	else {
		this.openList(restore);
	}

} // end toggleList()

/**
* @method selectOption
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to select a new combobox option.
* The jQuery object for the new option is stored and the selected class is added
*
* @param {object} $id - the jQuery object of the new option to select
*
* @return N/A
*/

OAA_EXAMPLES.combobox.prototype.selectOption = function($id) {

	// remove the selected class from the list
	this.$options.removeClass('selected');
	
	// add the selected class to the new option
	$id.addClass('selected');

	// store the newly selected option
	this.$selected = $id;

	// update the edit box
	this.$edit.val($id.text());

	//move cursor to the end
	this.selectText(this.$edit.val().length, this.$edit.val().length);

	// reset the option list
	this.$options = this.$list.find('li').removeClass('hidden');
	
} // end selectOption

/**
* @method calcOffset
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to calculate the pixel offset of a list option from the top of the list
*
* @param {object} $id - the jQuery object of the option to scroll to
*
* @return {integer} returns the pixel offset of the option
*/

OAA_EXAMPLES.combobox.prototype.calcOffset = function($id) {
	var offset = 0;
	var selectedNdx = this.$options.index($id);

	for (var ndx = 0; ndx < selectedNdx; ndx++) {
		if (this.$options.eq(ndx).not('[class=hidden]')) {
			offset += this.$options.eq(ndx).outerHeight();
		}
	}

	return offset;

} // end calcOffset

/**
* @method handleButtonClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to consume button click events. This handler prevents
* clicks on the button from reloading the page. This could also be done by adding 'onclick="false";' to the
* button HTML markup.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonClick = function($id,  e) {

	e.stopPropagation();
	return false;

} // end handleButtonClick();

/**
* @method handleButtonMouseOver
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mouseover events
*
* @param (e object) e is the event object associated with the event
*
* @param ($id object) $id is the jQuery object for the element firing the event
*
* @return (boolean)  returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseOver = function($id,  e) {

	// change the button image to reflect the highlight state
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down-hl.png');

	e.stopPropagation();
	return false;

} // end handleButtonMouseOver();

/**
* @method handleButtonMouseOut
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mouseout events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean}  returns false
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseOut = function($id,  e) {

	// reset image to normal state
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down.png');

	e.stopPropagation();
	return false;

} // end handleButtonMouseOut();

/**
* @method handleButtonMouseDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mousedown events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean}  returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseDown = function($id, e) {

	// change the button image to reflect the pressed state
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down-pressed-hl.png');

	// toggle the display of the option list
	this.toggleList(true);

	// Set focus on the edit box
	this.$edit.focus();

	e.stopPropagation();
	return false;

} // end handleButtonMouseDown();

/**
* @method handleButtonMouseUp - a member function to process button mouseup events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean}  returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseUp = function($id,  e) {

	// reset button image
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down-hl.png');

	e.stopPropagation();
	return false;

} // end handleButtonMouseUp();

/**
* @method handleEditKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for the edit box.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false if consuming; true if not processing
*/

OAA_EXAMPLES.combobox.prototype.handleEditKeyDown = function($id,  e) {

	var $curOption = this.$options.filter('.selected');
	var curNdx = this.$options.index($curOption);

	switch(e.keyCode) {
		case this.keys.tab: {
			// store the current selection
			this.selectOption($curOption);

			if (this.isOpen() == true) {
				// Close the option list
				this.closeList(false);
			}

			// allow tab to propagate
			return true;
		}
		case this.keys.esc: {
			// Do not change combobox value

			// Restore the edit box to the selected value
			this.$edit.val(this.$selected.text());

			// Select the text
			this.$edit.select();

			if (this.isOpen() == true) {

				// Close the option list
				this.closeList(true);
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.enter: {
			if (e.shiftKey || e.altKey || e.ctrlKey) {
				// do nothing
				return true;
			}

			if (this.isOpen() == false) {
				// open the option list
				this.openList(false);
			}
			else {
				// store the new selection
				this.selectOption($curOption);

				// Close the option list
				this.closeList(false);
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.up: {
			
			var $curOption = this.$options.filter('.selected');

			if (e.shiftKey || e.ctrlKey) {
				// do nothing
				return true;
			}

			if (e.altKey) {
				// alt+up toggles the list

				if (this.isOpen() == true) {

					this.selectOption($curOption);
				}
				
				// toggle the list
				this.toggleList(false);
			}
			else {
				// move to the previous item in the list
			
				if (curNdx > 0) {
					var $prev = this.$options.eq(curNdx - 1);

					// remove the selected class from the current selection
					$curOption.removeClass('selected');

					// Add the selected class to the new selection
					$prev.addClass('selected');

					// Change the text in the edit box
					this.$edit.val($prev.text());

					// Select the text
					this.$edit.select();

					if (this.isOpen() == true) {
						// scroll the list window to the new option
						this.$list.scrollTop(this.calcOffset($prev));
					}
				}
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.down: {
			if (e.shiftKey || e.ctrlKey) {
				// do nothing
				return true;
			}

			if (e.altKey) {
				// alt+up toggles the list

				if (this.isOpen() == true) {
					// Restore the edit box to the selected value
					this.$edit.val(this.$selected.text());

					// Select the text
					this.$edit.select();

					// alt+up toggles the list
					this.closeList(true);
				}
				else {
					// alt+up toggles the list
					this.openList(false);
				}
			}
			else {
				// move to the next item in the list

				if (curNdx != this.$options.length - 1) {
					var $prev = this.$options.eq(curNdx + 1);

					// remove the selected class from the current selection
					this.$options.eq(curNdx).removeClass('selected');

					// Add the selected class to the new selection
					$prev.addClass('selected');

					// Change the text in the edit box
					this.$edit.val($prev.text());

					// Select the text
					this.$edit.select();

					if (this.isOpen() == true) {
						// scroll the list window to the new option
						this.$list.scrollTop(this.calcOffset($prev));
					}
				}
			}

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleEditKeyDown()

/**
* @method handleEditKeyUp
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keyup events for the edit box.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id  the jQuery object for the element firing the event
*
* @return {boolean} Returns false if consuming; true if not processing
*/

OAA_EXAMPLES.combobox.prototype.handleEditKeyUp = function($id,  e) {

	var thisObj = this;
	var val = this.$edit.val();
	var re = new RegExp('^' + val, 'i');

	if (e.shiftKey || e.ctrlKey || e.altKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
		case this.keys.shift:
		case this.keys.ctrl:
		case this.keys.alt:
		case this.keys.esc: 
		case this.keys.tab:
		case this.keys.enter:
		case this.keys.left:
		case this.keys.right:
		case this.keys.up:
		case this.keys.down:
		case this.keys.home:
		case this.keys.end: {
			// do nothing
			return true;
		}
	}

	// repopulate the list make all items visible and remove the selection highlighting
	this.$options = this.$list.find('li').removeClass('hidden').removeClass('selected');

	if (val.length == 0) {
		// if the list box is visible, scroll to the top
		if (this.isOpen() == true) {
			this.$list.scrollTop(0);
		}
	}
	else {
		// recreate the list including only options that match
		// what the user typed
		this.$options = this.$options.filter(function(index) {

			if (re.test($(this).text()) == true) {
				return true;
			}
			else {
				// hide those entries that do not match
				$(this).addClass('hidden');

				return false;
			}
		});
	}
	
	if (this.$options.length > 0) {
		var $newOption = this.$options.first();
		var newVal = $newOption.text();
		var start = val.length;
		var end = newVal.length;
		var editNode = this.$edit.get(0);

		if (e.keyCode != this.keys.backspace) {
			// if the user isn't backspacing, fill in the
			// suggested value.
			this.$edit.val(newVal);
		}

		// Select the auto-complete text
		this.selectText(start, end);

		// Reset the highlighting for the list
		this.$options.removeClass('selected');

		$newOption.addClass('selected');
	}

	// Show the list if it is hidden
	if (this.isOpen() == false) {
		this.openList(false);
	}

	e.stopPropagation();
	return false;
} // end handleEditKeyUp()

/**
* @method handleEditKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for
* the edit box. Needed for browsers that use keypress events to manipulate the window.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false if consuming; true if not processing
*/

OAA_EXAMPLES.combobox.prototype.handleEditKeyPress = function($id,  e) {

	var curNdx = this.$options.index($id);

	if (e.altKey && (e.keyCode == this.keys.up || e.keyCode == this.keys.down)) {
		e.stopPropagation();
		return false;
	}

	switch(e.keyCode) {
		case this.keys.enter:
		case this.keys.up:
		case this.keys.down: {
			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleOptionKeyPress()

/**
* @method handleOptionClick - a member function to process click events for
* the combobox.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false
*/

OAA_EXAMPLES.combobox.prototype.handleOptionClick = function($id,  e) {

	// select the clicked item
	this.selectOption($id);

	// set focus on the edit box
	this.$edit.focus();

	// close the list
	this.closeList(false);

	e.stopPropagation();
	return false;	

} // end handleOptionClick()

/**
* @method handleComboFocus - a member function to process focus events for
* the combobox
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns true
*/

OAA_EXAMPLES.combobox.prototype.handleComboFocus = function($id,  e) {

	window.clearTimeout(g_cb1.timer);

	// set focus on the edit box
	this.$edit.focus();

	e.stopPropagation();
	return false;

} // end handleComboFocus()

/**
* @method handleComboBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process blur events for the combobox
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns true
*/

OAA_EXAMPLES.combobox.prototype.handleComboBlur = function($id,  e) {

	// store the currently selected value
	this.selectOption(this.$options.filter('.selected'));

	// close the list box
	if (this.isOpen() == true) {
		this.timer = window.setTimeout(function() {g_cb1.closeList(false);}, 40);
	}

	e.stopPropagation();
	return false;

} // end handleComboBlur()

/**
* @method selectText
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to select some of the text in the edit box.
* If start and end are the same value, the function moves the cursor to that position.
*
* @param {object} start - the character position for the start of the selection
*
* @param {object} end is the character position for the end of the selection
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.selectText = function(start, end) {

	var editNode = this.$edit.get(0);

	if (editNode.setSelectionRange) {
		// Firefox and other gecko based browsers
		editNode.setSelectionRange(start, end);
	}
	else if (editNode.createTextRange) {
		// Internet Explorer
		var range = editNode.createTextRange();
		range.collapse(true);
		range.moveEnd('character', start);
		range.moveStart('character', end);
		range.select();
	}
	else if (editNode.selectionStart) {
		// Other browsers
		editNode.selectionStart = start;
		editNode.selectionEnd = end;
	}

} // end selectText()
"""

example_obj.style       = """
* {
	font-family: "Times New Roman,Georgia,Serif"; 
}
.hidden {
	position: absolute;
	top: -20em;
	left: -200em;
}

.wrapper {
	height: 24px;
	overflow: auto;
}
.cb {
	margin: 20px;
	padding: 0;
	height: 24px;
	display: block;
	overflow: visible;
}

.cb_label {
	margin: 0;
	padding: 2px;
	width: 45px;
	font-weight: bold;
	float: left;
	display: inline;
}
.cb_edit {
	margin: 0;
	padding: 2px 3px;
	width: 240px;
	height: 18px;
	border: 1px solid black;
	font-size: 1em;
	float: left;
	display: inline;
}
.cb_button {
	margin: 0;
	padding: 0;
	height: 24px;
	width: 24px;
	border: 1px solid black;
	background-color: #999;
	float: left;
	display: inline;
	text-align: center;
}

button.cb_button img {
	margin: 0;
	padding: 0;
	height: 22px;
	width: 22px;
	position: relative;
	top: -1px;
	left: -3px;
}
.cb_list {
	clear: both;
	list-style: none;
	padding: 0;
	margin: 0;
	margin-left: 49px;
	border: 1px solid black;
	width: 246px;
	height: 200px;
	overflow: auto;
	background-color: #fff;
	position: relative;
	z-index: 300;
}

.cb_option {
	margin: 0 1px 0 0;
	padding: 2px 5px;
}
.selected {
	border-top: 1px solid #44e;
	border-bottom: 1px solid #44e;
	padding: 1px 5px;
	background-color: #77a;
	color: #fff;
}
.cb_option:hover {
	border-top: 1px solid #44e;
	border-bottom: 1px solid #44e;
	padding: 1px 5px;
	font-weight: bold;
	background-color: #77f;
	color: #fff;
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
example_obj.title       = 'Combobox with aria-autocomplete="list"'
example_obj.permanent_slug = 'combobox3'

example_obj.a11y_features = """
This is example implements a combobox widget with aria-autocomplete="list". Focus remains on the edit box while the user manipulates the list. activedescendant is used to tell assistive technologies which list option is currently selected. For clarity, this example was designed not to update the edit box until the user makes a choice from the list.
"""
example_obj.keyboard    = """

* Enter: Select highlighted option and close the list box. If list box is closed, opens the list box.</li>
* Escape: Close list box without changing the combobox value (e.g. no selection is made).</li>
* Up Arrow: Moves upward in list. If the list box is closed, this does not select the highlighted list option.</li>
* Down Arrow: Moves downward in list. If the list box is closed, this does not select the highlighted list option.</li>
* Home: If the list box is open, moves to first option in list.</li>
* End: If the list box is open, moves to last option in list.</li>
* Tab: Select highlighted option and close list box. Focus moves to the next focusable element in page.</li>
* Shift+Tab: Same as tab key except focus moves to previous focusable item in page.</li>
* Alt + Up Arrow/Down Arrow: Open or close the list box.<br>Note: Opera does not propagate alt key modifer events to the web page. Alt+Arrow key combinations will not work in Opera.

"""

example_obj.markup = [m1,m2,m3,m4,m5,m6]

example_obj.html       = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<div role="application" tabindex="-1">

<form autocomplete="off">
<div id="cb1" class="cb">
	<div class="cb_label"><label id="cb1-label" for="cb1-edit">State</label>:</div>
	<input id="cb1-edit" class="cb_edit" type="text"
		tabindex="0"
      role="combobox"
		aria-labelledby="cb1-label"
		aria-autocomplete="list"
		aria-owns="cb1-list"
		aria-readonly="true"
		aria-activedescendant="cb1-opt16"/>
	<div id="cb1-button-label" class="hidden">Open list of states</div>
	<button id="cb1-button" class="cb_button" aria-labelledby="cb1-button-label" aria-controls="cb1-list" tabindex="-1">
		<img src="{{EXAMPLE_MEDIA}}images/button-arrow-down.png" alt="Open or close the list box" />
	</button>

	<ul id="cb1-list" class="cb_list" tabindex="-1" role="listbox" aria-expanded="true">
		<li id="cb1-opt1" role="option" class="cb_option" role="listitem" tabindex="-1">Alabama</li>
		<li id="cb1-opt2" role="option" class="cb_option" role="listitem" tabindex="-1">Alaska</li>
		<li id="cb1-opt3" role="option" class="cb_option" role="listitem" tabindex="-1">American Samoa</li>
		<li id="cb1-opt4" role="option" class="cb_option" role="listitem" tabindex="-1">Arizona</li>
		<li id="cb1-opt5" role="option" class="cb_option" role="listitem" tabindex="-1">Arkansas</li>
		<li id="cb1-opt6" role="option" class="cb_option" role="listitem" tabindex="-1">California</li>
		<li id="cb1-opt7" role="option" class="cb_option" role="listitem" tabindex="-1">Colorado</li>
		<li id="cb1-opt8" role="option" class="cb_option" role="listitem" tabindex="-1">Connecticut</li>
		<li id="cb1-opt9" role="option" class="cb_option" role="listitem" tabindex="-1">Delaware</li>
		<li id="cb1-opt10" role="option" class="cb_option" role="listitem" tabindex="-1">District of Columbia</li>
		<li id="cb1-opt11" role="option" class="cb_option" role="listitem" tabindex="-1">Florida</li>
		<li id="cb1-opt12" role="option" class="cb_option" role="listitem" tabindex="-1">Georgia</li>
		<li id="cb1-opt13" role="option" class="cb_option" role="listitem" tabindex="-1">Guam</li>
		<li id="cb1-opt14" role="option" class="cb_option" role="listitem" tabindex="-1">Hawaii</li>
		<li id="cb1-opt15" role="option" class="cb_option" role="listitem" tabindex="-1">Idaho</li>
		<li id="cb1-opt16" role="option" class="cb_option selected" role="listitem" tabindex="-1">Illinois</li>
		<li id="cb1-opt17" role="option" class="cb_option" role="listitem" tabindex="-1">Indiana</li>
		<li id="cb1-opt18" role="option" class="cb_option" role="listitem" tabindex="-1">Iowa</li>
		<li id="cb1-opt19" role="option" class="cb_option" role="listitem" tabindex="-1">Kansas</li>
		<li id="cb1-opt20" role="option" class="cb_option" role="listitem" tabindex="-1">Kentucky</li>
		<li id="cb1-opt21" role="option" class="cb_option" role="listitem" tabindex="-1">Louisiana</li>
		<li id="cb1-opt22" role="option" class="cb_option" role="listitem" tabindex="-1">Maine</li>
		<li id="cb1-opt23" role="option" class="cb_option" role="listitem" tabindex="-1">Maryland</li>
		<li id="cb1-opt24" role="option" class="cb_option" role="listitem" tabindex="-1">Massachusetts</li>
		<li id="cb1-opt25" role="option" class="cb_option" role="listitem" tabindex="-1">Michigan</li>
		<li id="cb1-opt26" role="option" class="cb_option" role="listitem" tabindex="-1">Minnesota</li>
		<li id="cb1-opt27" role="option" class="cb_option" role="listitem" tabindex="-1">Mississippi</li>
		<li id="cb1-opt28" role="option" class="cb_option" role="listitem" tabindex="-1">Missouri</li>
		<li id="cb1-opt29" role="option" class="cb_option" role="listitem" tabindex="-1">Montana</li>
		<li id="cb1-opt30" role="option" class="cb_option" role="listitem" tabindex="-1">Nebraska</li>
		<li id="cb1-opt31" role="option" class="cb_option" role="listitem" tabindex="-1">Nevada</li>
		<li id="cb1-opt32" role="option" class="cb_option" role="listitem" tabindex="-1">New Hampshire</li>
		<li id="cb1-opt33" role="option" class="cb_option" role="listitem" tabindex="-1">New Jersey</li>
		<li id="cb1-opt34" role="option" class="cb_option" role="listitem" tabindex="-1">New Mexico</li>
		<li id="cb1-opt35" role="option" class="cb_option" role="listitem" tabindex="-1">New York</li>
		<li id="cb1-opt36" role="option" class="cb_option" role="listitem" tabindex="-1">North Carolina</li>
		<li id="cb1-opt37" role="option" class="cb_option" role="listitem" tabindex="-1">North Dakota</li>
		<li id="cb1-opt38" role="option" class="cb_option" role="listitem" tabindex="-1">Northern Marianas Islands</li>
		<li id="cb1-opt39" role="option" class="cb_option" role="listitem" tabindex="-1">Ohio</li>
		<li id="cb1-opt40" role="option" class="cb_option" role="listitem" tabindex="-1">Oklahoma</li>
		<li id="cb1-opt41" role="option" class="cb_option" role="listitem" tabindex="-1">Oregon</li>
		<li id="cb1-opt42" role="option" class="cb_option" role="listitem" tabindex="-1">Pennsylvania</li>
		<li id="cb1-opt43" role="option" class="cb_option" role="listitem" tabindex="-1">Puerto Rico</li>
		<li id="cb1-opt44" role="option" class="cb_option" role="listitem" tabindex="-1">Rhode Island</li>
		<li id="cb1-opt45" role="option" class="cb_option" role="listitem" tabindex="-1">South Carolina</li>
		<li id="cb1-opt47" role="option" class="cb_option" role="listitem" tabindex="-1">South Dakota</li>
		<li id="cb1-opt48" role="option" class="cb_option" role="listitem" tabindex="-1">Tennessee</li>
		<li id="cb1-opt49" role="option" class="cb_option" role="listitem" tabindex="-1">Texas</li>
		<li id="cb1-opt50" role="option" class="cb_option" role="listitem" tabindex="-1">Utah</li>
		<li id="cb1-opt51" role="option" class="cb_option" role="listitem" tabindex="-1">Vermont</li>
		<li id="cb1-opt52" role="option" class="cb_option" role="listitem" tabindex="-1">Virginia</li>
		<li id="cb1-opt53" role="option" class="cb_option" role="listitem" tabindex="-1">Virgin Islands</li>
		<li id="cb1-opt54" role="option" class="cb_option" role="listitem" tabindex="-1">Washington</li>
		<li id="cb1-opt55" role="option" class="cb_option" role="listitem" tabindex="-1">West Virginia</li>
		<li id="cb1-opt56" role="option" class="cb_option" role="listitem" tabindex="-1">Wisconsin</li>
		<li id="cb1-opt57" role="option" class="cb_option" role="listitem" tabindex="-1">Wyoming</li>
	</ul>
</div>
</form>
</div>
"""
example_obj.script      = """
var g_combo = null;  // set to active combobox for blur function
var OAA_EXAMPLES = OAA_EXAMPLES || {};
$(document).ready(function() {

	var cb1 = new OAA_EXAMPLES.combobox('cb1', false);
}); // end ready

//
// keyCodes() is an object to contain keycodes needed for the application
//
function keyCodes() {
	// Define values for keycodes
	this.backspace  = 8;
	this.tab        = 9;
	this.enter      = 13;
	this.esc        = 27;

	this.space      = 32;
	this.pageup     = 33;
	this.pagedown   = 34;
	this.end        = 35;
	this.home       = 36;

	this.up         = 38;
	this.down       = 40; 
	
	this.del        = 46;

} // end keyCodes

/**
* @constructor combobox
*
* @memberOf OAA_EXAMPLES
*
* @desc a class for an ARIA-enabled combobox widget
*
* @param {string} id - the id of the div containing the combobox. Text input must have role="combobox".
*
* @param {boolean} editable is true if the edit box should be editable; false if read-only.
*
* @return {N/A}
*/

/**
* @private
* @constructor Internal Properties
*
* @property {object} $id - The jQuery object of the div containing the combobox
* @property {boolean} editable - True if the edit box is editable
*
* @property {object} $edit - The jQuery object of the edit box
* @property {object} $button - The jQuery object of the button
* @property {object} $list - The jQuery object of the option list
* @property {object} $options - An array of jQuery objects for the combobox options
*
* @property {boolean} $selected - the current value of the combobox
* @property {boolean} $focused - the currently selected option in the combo list
* @property {object} timer - stores the close list timer that is set when combo looses focus
*/

OAA_EXAMPLES.combobox = function(id, editable) {

	// Define the object properties

	this.$id = $('#' + id);
	this.editable = editable;  
	this.keys = new keyCodes();

	// Store jQuery objects for the elements of the combobox
	this.$edit = $('#' + id + '-edit'); 
	this.$button = $('#' + id + '-button'); 
	this.$list = $('#' + id + '-list'); 
	this.$options = this.$list.find('li');

	this.$selected;
	this.$focused;
	this.timer = null;

	// Initalize the combobox
	this.init();

	// bind event handlers for the widget
	this.bindHandlers();

} // end combobox constructor


/**
* @method init
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to initialize the combobox elements. Hides the list and sets ARIA attributes
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.init = function() {

	// Hide the list of options
	this.$list.hide().attr('aria-expanded', 'false');

	// If the edit box is to be readonly, aria-readonly must be defined as true
	if (this.editable == false) {
		this.$edit.attr('aria-readonly', 'true');
	}

	// Set initial value for the edit box
	this.$selected = this.$options.filter('.selected');

	if (this.$selected.length > 0) {
		this.$edit.val(this.$selected.text());
	}

} // end initCombo()

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers for the combobox elements
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.bindHandlers = function() {

	var thisObj = this;

	///////////////// bind handlers for the button /////////////////////////
	
	this.$button.click(function(e) {
		return thisObj.handleButtonClick($(this), e);
	});

	this.$button.mouseover(function(e) {
		return thisObj.handleButtonMouseOver($(this), e);
	});

	this.$button.mouseout(function(e) {
		return thisObj.handleButtonMouseOut($(this), e);
	});

	this.$button.mousedown(function(e) {
		return thisObj.handleButtonMouseDown($(this), e);
	});

	this.$button.mouseup(function(e) {
		return thisObj.handleButtonMouseUp($(this), e);
	});

	///////////////// bind listbox handlers /////////////////////////

	this.$options.click(function(e) {
		return thisObj.handleOptionClick($(this), e);
	});

	this.$list.focus(function(e) {
		return thisObj.handleComboFocus($(this), e);
	});

	this.$list.blur(function(e) {
		return thisObj.handleComboBlur($(this), e);
	});

	this.$options.focus(function(e) {
		return thisObj.handleComboFocus($(this), e);
	});

	this.$options.blur(function(e) {
		return thisObj.handleComboBlur($(this), e);
	});

	///////////////// bind editbox handlers /////////////////////////

	this.$edit.keydown(function(e) {
		return thisObj.handleEditKeyDown($(this), e);
	});

	this.$edit.keypress(function(e) {
		return thisObj.handleEditKeyPress($(this), e);
	});

	this.$edit.blur(function(e) {
		return thisObj.handleComboBlur($(this), e);
	});

} // end bindHandlers()

/**
* @method isOpen
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to get the current state of the list box
*
* @return {boolean} returns true if list box is open; false if it is not
*/

OAA_EXAMPLES.combobox.prototype.isOpen = function() {

	if (this.$list.attr('aria-expanded') == 'true') {
		return true;
	}
	else {
		return false;
	}

} // end isOpen

/**
* @method closeList
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to close the list box if it is open
*
* @param {boolean} restore is true if function should restore higlight to stored list selection
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.closeList = function(restore) {

	var $curOption = this.$options.filter('.selected');

	if (restore == true) {
		$curOption = this.$selected;

		// remove the selected class from the other list items
		this.$options.removeClass('selected');

		// add selected class to the stored selection
		$curOption.addClass('selected');
	}

	this.$list.hide().attr('aria-expanded', 'false');

} // end closeList()

/**
* @method openList
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to open the list box if it is closed
*
* @param {boolean} restore is true if function should restore higlight to stored list selection
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.openList = function(restore) {

	var $curOption = this.$options.filter('.selected');

	if (restore == true) {

		if (this.$selected.length == 0) {
			// select the first item
			this.selectOption(this.$options.first());
			$curOption = this.$selected;
		}
		else {
			$curOption = this.$selected;
		}

		// remove the selected class from the other list items
		this.$options.removeClass('selected');

		// add selected class to the stored selection
		$curOption.addClass('selected');
	}

	this.$list.show().attr('aria-expanded', 'true');

	// scroll to the currently selected option
	this.$list.scrollTop(this.calcOffset($curOption));

} // end openList();

/**
* @method toggleList
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to toggle the display of the combobox options.
*
* @param {boolean} restore is true if toggle should restore higlight to stored list selection
*
* Return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.toggleList = function(restore) {

	if (this.isOpen() == true) {

		this.closeList(restore);
	}
	else {
		this.openList(restore);
	}

} // end toggleList()

/**
* Function selectOption() is a member function to select a new combobox option.
* The jQuery object for the new option is stored and the selected class is added
*
* @param ($id object) $id is the jQuery object of the new option to select
*
* @return N/A
*/
 
OAA_EXAMPLES.combobox.prototype.selectOption = function($id) {

	// If there is a selected option, remove the selected class from it
	if (this.$selected.length > 0) {
		this.$selected.removeClass('selected');
	}
	
	// add the selected class to the new option
	$id.addClass('selected');

	// set active descendant for the new option
	this.$edit.attr('aria-activedescendant', $id.attr('id'));

	// store the newly selected option
	this.$selected = $id;

	// update the edit box
	this.$edit.val($id.text());
	
} // end selectOption

/**
* @method calcOffset
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to calculate the pixel offset of a list option from the top of the list
*
* @param {object} $id - the jQuery object of the option to scroll to
*
* @return {integer} returns the pixel offset of the option
*/

OAA_EXAMPLES.combobox.prototype.calcOffset = function($id) {
	var offset = 0;
	var selectedNdx = this.$options.index($id);

	for (var ndx = 0; ndx < selectedNdx; ndx++) {
		offset += this.$options.eq(ndx).outerHeight();
	}

	return offset;

} // end calcOffset

/**
* @method handleButtonClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to consume button click events. This handler prevents
* clicks on the button from reloading the page. This could also be done by adding 'onclick="false";' to the
* button HTML markup.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} - returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonClick = function($id,  e) {

	e.stopPropagation();
	return false;

} // end handleButtonClick();

/**
* @method handleButtonMouseOver
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mouseover events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseOver = function($id,  e) {

	// change the button image to reflect the highlight state
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down-hl.png');

	e.stopPropagation();
	return false;

} // end handleButtonMouseOver();

/**
* @method handleButtonMouseOut
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mouseout events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseOut = function($id,  e) {

	// reset image to normal state
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down.png');

	e.stopPropagation();
	return false;

} // end handleButtonMouseOut();

/**
* @method handleButtonMouseDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mousedown events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseDown = function($id,  e) {

	// change the button image to reflect the pressed state
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down-pressed-hl.png');

	// toggle the display of the option list
	this.toggleList(true);

	// Set focus on the edit box
	this.$edit.focus();

	e.stopPropagation();
	return false;

} // end handleButtonMouseDown();

/**
* @method handleButtonMouseUp
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mouseup events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseUp = function($id,  e) {

	// reset button image
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down-hl.png');

	e.stopPropagation();
	return false;

} // end handleButtonMouseUp();


/**
* @method handleEditKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for the edit box.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false if consuming; true if not processing
*/

OAA_EXAMPLES.combobox.prototype.handleEditKeyDown = function($id,  e) {

	var $curOption = this.$options.filter('.selected');
	var curNdx = this.$options.index($curOption);

	if (e.altKey && (e.keyCode == this.keys.up || e.keyCode == this.keys.down)) {

		this.toggleList(true);

		e.stopPropagation();
		return false;
	}

	switch (e.keyCode) {
		case this.keys.backspace:
		case this.keys.del: {
			// prevent the edit box from being changed
			this.$edit.val(this.$selected.text());

			e.stopPropagation();
			return false;
		}
		case this.keys.tab: {

			// store the current selection
			this.selectOption($curOption);


			if (this.isOpen() == true) {
				// Close the option list
				this.closeList(false);
			}

			// allow tab to propagate
			return true;
		}
		case this.keys.esc: {
			// Do not change combobox value

			if (this.isOpen() == true) {
				// Close the option list
				this.closeList(true);
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.enter: {

			if (this.isOpen() == true) {
				// store the current selection
				this.selectOption($curOption);

				// Close the option list
				this.closeList(false);
			}
			else {
				this.openList(false);
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.up: {
			
			// move to the previous item in the list
			
			// if the list is expanded and this isn't the first item
			// move to the next item in the list
			
			if (curNdx > 0) {

				var $prev = this.$options.eq(curNdx - 1);

				if (this.isOpen() == true) {
					// remove the selected class from the current selection
					$curOption.removeClass('selected');

					// Add the selected class to the new selection
					$prev.addClass('selected');

					// Set activedescendent for new option
					this.$edit.attr('aria-activedescendant', $prev.attr('id'));

					// scroll the list window to the new option
					this.$list.scrollTop(this.calcOffset($prev));
				}
				else {
					// store the new selection
					this.selectOption($prev);
				}

			}

			e.stopPropagation();
			return false;
		}
		case this.keys.down: {

			// if the list is expanded and there are more items,
			// move to the next item in the list
			
			if (curNdx < this.$options.length - 1) {

				var $next = this.$options.eq(curNdx + 1);

				if (this.isOpen() == true) {
					// remove the selected class from the current selection
					$curOption.removeClass('selected');

					// Add the selected class to the new selection
					$next.addClass('selected');

					// Set activedescendent for new option
					this.$edit.attr('aria-activedescendant', $next.attr('id'));

					// scroll the list window to the new option
					this.$list.scrollTop(this.calcOffset($next));
				}
				else {
					// store the new selection
					this.selectOption($next);
				}
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.home: {
			// select the first list item if the list is open

			if (this.isOpen() == true) {
			
				var $first = this.$options.first();

				// remove the selected class from the current selection
				$curOption.removeClass('selected');

				// Add the selected class to the new selection
				$first.addClass('selected');

				// scroll the list window to the new option
				this.$list.scrollTop(0);

				// Set activedescendent for new option
				this.$edit.attr('aria-activedescendant', $first.attr('id'));
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.end: {
			// select the last list item if the list is open

			if (this.isOpen() == true) {

				var $last = this.$options.last();

				// remove the selected class from the current selection
				$curOption.removeClass('selected');

				// Add the selected class to the new selection
				$last.addClass('selected');

				// scroll the list window to the new option
				this.$list.scrollTop(this.calcOffset($last));

				// Set activedescendent for new option
				this.$edit.attr('aria-activedescendant', $last.attr('id'));
			}

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleEditKeyDown()

/**
* @method handleEditKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for the edit box.
* Needed for browsers that use keypress events to manipulate the window.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false if consuming; true if not processing
*/

OAA_EXAMPLES.combobox.prototype.handleEditKeyPress = function($id,  e) {

	var curNdx = this.$options.index($id);

	if (e.altKey && (e.keyCode == this.keys.up || e.keyCode == this.keys.down)) {
		e.stopPropagation();
		return false;
	}

	switch(e.keyCode) {
		case this.keys.esc:
		case this.keys.enter: {

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleOptionKeyPress()

/**
* @method handleOptionClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events for the combobox.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false
*/

OAA_EXAMPLES.combobox.prototype.handleOptionClick = function($id,  e) {

	// select the clicked item
	this.selectOption($id);

	// set focus on the edit box
	//this.$edit.focus();

	// close the list
	this.closeList(false);

	e.stopPropagation();
	return false;	

} // end handleOptionClick()

/**
* @method handleComboFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process focus events for the list box
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns true
*/

OAA_EXAMPLES.combobox.prototype.handleComboFocus = function($id,  e) {

	if (g_combo != null) {
		window.clearTimeout(g_combo.timer);
	}

	// Set focus on the edit box
	this.$edit.focus();

	return true;

} // end handleComboFocus()

/**
* @method handleComboBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process blur events for the combobox
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns true
*/

OAA_EXAMPLES.combobox.prototype.handleComboBlur = function($id,  e) {

	// store the currently selected value
	this.$selected = this.$options.filter('.selected');

	// update the edit box
	this.$edit.val(this.$selected.text());

	g_combo = this;

	// close the list box
	if (this.isOpen() == true) {
		this.timer = window.setTimeout(function() {g_combo.closeList(false);}, 40);
	}

	return true;

} // end handleComboBlur()
"""

example_obj.style       = """
* {
	font-family: "Times New Roman,Georgia,Serif"; 
}
.hidden {
	position: absolute;
	top: -20em;
	left: -200em;
}

.wrapper {
	height: 24px;
	overflow: auto;
}
.cb {
	margin: 20px;
	padding: 0;
	height: 24px;
	display: block;
	overflow: visible;
}

.cb_label {
	margin: 0;
	padding: 2px;
	width: 45px;
	font-weight: bold;
	float: left;
	display: inline;
}
.cb_edit {
	margin: 0;
	padding: 2px 3px;
	width: 240px;
	height: 18px;
	border: 1px solid black;
	font-size: 1em;
	float: left;
	display: inline;
}
.cb_button {
	margin: 0;
	padding: 0;
	height: 24px;
	width: 24px;
	border: 1px solid black;
	background-color: #999;
	float: left;
	display: inline;
	text-align: center;
}

button.cb_button img {
	margin: 0;
	padding: 0;
	height: 22px;
	width: 22px;
	position: relative;
	top: -1px;
	left: -3px;
}
.cb_list {
	clear: both;
	list-style: none;
	padding: 0;
	margin: 0;
	margin-left: 49px;
	border: 1px solid black;
	width: 246px;
	height: 200px;
	overflow: auto;
	background-color: #fff;
	position: relative;
	z-index: 300;
}

.cb_option {
	margin: 0 1px 0 0;
	padding: 2px 5px;
}
.selected {
	border-top: 1px solid #44e;
	border-bottom: 1px solid #44e;
	padding: 1px 5px;
	background-color: #77a;
	color: #fff;
}
.cb_option:hover {
	border-top: 1px solid #44e;
	border-bottom: 1px solid #44e;
	padding: 1px 5px;
	font-weight: bold;
	background-color: #77f;
	color: #fff;
}
"""
example3 = create_example(example_obj)


# =============================
# Example 4
# =============================

order += 1

example_obj             = example_object()
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order          = order
example_obj.title       = 'Combobox with aria-autocomplete="none" and role="combobox" on wrapping div'
example_obj.permanent_slug = 'combobox4'

example_obj.a11y_features = """
This is example implements a combobox widget with aria-autocomplete="none". The edit box is readonly. The application is required to manage focus for the list box so assistive technologies can follow the currently selected option. For clarity, this example was designed not to update the edit box until the user makes a choice from the list.
"""
example_obj.keyboard    = """
<p>If focus is on the edit box:</p>
<ul>
    <li>Up Arrow: Move upward in list, even if the list box is closed.</li>
    <li>Down Arrow: Move downward in list, even if the list box is closed.</li>
    <li>Alt + Up Arrow/Down Arrow: Open or close the list box. Focus moves to selected option in list.<br>Note: Opera does not propagate alt key modifer events to the web page. Alt+Arrow key combinations will not work in Opera.</li>
</ul>

<p>If focus is on the list box:</p>
<ul>
    <li>Enter: Select highlighted option and close the list box. Focus moves to the edit box.</li>
    <li>Escape: Close list box without changing the combobox value (e.g. no selection is made). Focus moves to the edit box.</li>
    <li>Up Arrow: Move upward in list.</li>
    <li>Down Arrow: Move downward in list.</li>
    <li>Home: Move to first option in list.</li>
    <li>End: Move to last option in list.</li>
    <li>Tab: Select highlighted option and close list box. Focus moves to the next focusable element in page.</li>
    <li>Shift+Tab: Same as tab key except focus moves to previous focusable item in page.</li>
</ul>
"""

example_obj.markup = [m1,m2,m3,m4,m5]

example_obj.html       = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<div role="application" tabindex="-1">

<form autocomplete="off">
<div id="cb1" class="cb" role="combobox">
	<div class="cb_label"><label id="cb1-label" for="cb1-edit">State</label>:</div>
	<input id="cb1-edit" class="cb_edit" type="text"
		aria-labelledby="cb1-label"
		aria-autocomplete="none"
		aria-readonly="true"
		tabindex="0" />
	<div id="cb1-button-label" class="hidden">Open list of states</div>
	<button id="cb1-button" class="cb_button" aria-labelledby="cb1-button-label" aria-controls="cb1-list" tabindex="-1">
		<img src="{{EXAMPLE_MEDIA}}images/button-arrow-down.png" alt="Open or close the list box" />
	</button>

	<ul id="cb1-list" class="cb_list" tabindex="-1" aria-expanded="true" role="listbox">
		<li id="cb1-opt1" role="option" class="cb_option" tabindex="-1">Alabama</li>
		<li id="cb1-opt2" role="option" class="cb_option" tabindex="-1">Alaska</li>
		<li id="cb1-opt3" role="option" class="cb_option" tabindex="-1">American Samoa</li>
		<li id="cb1-opt4" role="option" class="cb_option" tabindex="-1">Arizona</li>
		<li id="cb1-opt5" role="option" class="cb_option" tabindex="-1">Arkansas</li>
		<li id="cb1-opt6" role="option" class="cb_option" tabindex="-1">California</li>
		<li id="cb1-opt7" role="option" class="cb_option" tabindex="-1">Colorado</li>
		<li id="cb1-opt8" role="option" class="cb_option" tabindex="-1">Connecticut</li>
		<li id="cb1-opt9" role="option" class="cb_option" tabindex="-1">Delaware</li>
		<li id="cb1-opt10" role="option" class="cb_option" tabindex="-1">District of Columbia</li>
		<li id="cb1-opt11" role="option" class="cb_option" tabindex="-1">Florida</li>
		<li id="cb1-opt12" role="option" class="cb_option" tabindex="-1">Georgia</li>
		<li id="cb1-opt13" role="option" class="cb_option" tabindex="-1">Guam</li>
		<li id="cb1-opt14" role="option" class="cb_option" tabindex="-1">Hawaii</li>
		<li id="cb1-opt15" role="option" class="cb_option" tabindex="-1">Idaho</li>
		<li id="cb1-opt16" role="option" class="cb_option selected" tabindex="-1">Illinois</li>
		<li id="cb1-opt17" role="option" class="cb_option" tabindex="-1">Indiana</li>
		<li id="cb1-opt18" role="option" class="cb_option" tabindex="-1">Iowa</li>
		<li id="cb1-opt19" role="option" class="cb_option" tabindex="-1">Kansas</li>
		<li id="cb1-opt20" role="option" class="cb_option" tabindex="-1">Kentucky</li>
		<li id="cb1-opt21" role="option" class="cb_option" tabindex="-1">Louisiana</li>
		<li id="cb1-opt22" role="option" class="cb_option" tabindex="-1">Maine</li>
		<li id="cb1-opt23" role="option" class="cb_option" tabindex="-1">Maryland</li>
		<li id="cb1-opt24" role="option" class="cb_option" tabindex="-1">Massachusetts</li>
		<li id="cb1-opt25" role="option" class="cb_option" tabindex="-1">Michigan</li>
		<li id="cb1-opt26" role="option" class="cb_option" tabindex="-1">Minnesota</li>
		<li id="cb1-opt27" role="option" class="cb_option" tabindex="-1">Mississippi</li>
		<li id="cb1-opt28" role="option" class="cb_option" tabindex="-1">Missouri</li>
		<li id="cb1-opt29" role="option" class="cb_option" tabindex="-1">Montana</li>
		<li id="cb1-opt30" role="option" class="cb_option" tabindex="-1">Nebraska</li>
		<li id="cb1-opt31" role="option" class="cb_option" tabindex="-1">Nevada</li>
		<li id="cb1-opt32" role="option" class="cb_option" tabindex="-1">New Hampshire</li>
		<li id="cb1-opt33" role="option" class="cb_option" tabindex="-1">New Jersey</li>
		<li id="cb1-opt34" role="option" class="cb_option" tabindex="-1">New Mexico</li>
		<li id="cb1-opt35" role="option" class="cb_option" tabindex="-1">New York</li>
		<li id="cb1-opt36" role="option" class="cb_option" tabindex="-1">North Carolina</li>
		<li id="cb1-opt37" role="option" class="cb_option" tabindex="-1">North Dakota</li>
		<li id="cb1-opt38" role="option" class="cb_option" tabindex="-1">Northern Marianas Islands</li>
		<li id="cb1-opt39" role="option" class="cb_option" tabindex="-1">Ohio</li>
		<li id="cb1-opt40" role="option" class="cb_option" tabindex="-1">Oklahoma</li>
		<li id="cb1-opt41" role="option" class="cb_option" tabindex="-1">Oregon</li>
		<li id="cb1-opt42" role="option" class="cb_option" tabindex="-1">Pennsylvania</li>
		<li id="cb1-opt43" role="option" class="cb_option" tabindex="-1">Puerto Rico</li>
		<li id="cb1-opt44" role="option" class="cb_option" tabindex="-1">Rhode Island</li>
		<li id="cb1-opt45" role="option" class="cb_option" tabindex="-1">South Carolina</li>
		<li id="cb1-opt47" role="option" class="cb_option" tabindex="-1">South Dakota</li>
		<li id="cb1-opt48" role="option" class="cb_option" tabindex="-1">Tennessee</li>
		<li id="cb1-opt49" role="option" class="cb_option" tabindex="-1">Texas</li>
		<li id="cb1-opt50" role="option" class="cb_option" tabindex="-1">Utah</li>
		<li id="cb1-opt51" role="option" class="cb_option" tabindex="-1">Vermont</li>
		<li id="cb1-opt52" role="option" class="cb_option" tabindex="-1">Virginia</li>
		<li id="cb1-opt53" role="option" class="cb_option" tabindex="-1">Virgin Islands</li>
		<li id="cb1-opt54" role="option" class="cb_option" tabindex="-1">Washington</li>
		<li id="cb1-opt55" role="option" class="cb_option" tabindex="-1">West Virginia</li>
		<li id="cb1-opt56" role="option" class="cb_option" tabindex="-1">Wisconsin</li>
		<li id="cb1-opt57" role="option" class="cb_option" tabindex="-1">Wyoming</li>
	</ul>
</div>
</form>
</div>
"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};
var g_cb1 = null;  // set to active combobox for blur function

$(document).ready(function() {

	g_cb1 = new OAA_EXAMPLES.combobox('cb1', false);
}); // end ready

/**
* keyCodes() is an object to contain keycodes needed for the application
*/
function keyCodes() {
	// Define values for keycodes
	this.backspace  = 8;
	this.tab        = 9;
	this.enter      = 13;
	this.esc        = 27;

	this.space      = 32;
	this.pageup     = 33;
	this.pagedown   = 34;
	this.end        = 35;
	this.home       = 36;

	this.up         = 38;
	this.down       = 40; 
	
	this.del        = 46;

} // end keyCodes

/**
* @constructor combobox
*
* @memberOf OAA_EXAMPLES
*
* @desc a class for an ARIA-enabled combobox widget
*
* @param {string} id - the id of the div containing the combobox. Text input must have role="combobox".
*
* @param {boolean} editable - true if the edit box should be editable; false if read-only.
*
* @return {N/A}
*/

/**
* @private
* @constructor Internal Properties
*
* @property {object} $id - The jQuery object of the div containing the combobox
* @property {boolean} editable - True if the edit box is editable

* @property {object} $edit - The jQuery object of the edit box
* @property {object} $button - The jQuery object of the button
* @property {object} $buttonImg - The jQuery object of the button image
* @property {object} $list - The jQuery object of the option list
* @property {object} $options - An array of jQuery objects for the combobox options

* @property {boolean} $selected - the current value of the combobox
* @property {boolean} $focused - the currently selected option in the combo list
* @property {object} timer - stores the close list timer that is set when combo looses focus 
*/

OAA_EXAMPLES.combobox = function(id, editable) {

	// Define the object properties

	this.$id = $('#' + id);
	this.editable = editable;
	this.keys = new keyCodes();

	// Store jQuery objects for the elements of the combobox
	this.$edit = $('#' + id + '-edit');
	this.$button = $('#' + id + '-button'); 
	this.$buttonImg = $('#' + id).find('img');
	this.$list = $('#' + id + '-list'); 
	this.$options = this.$list.find('li'); 

	this.$selected; 
	this.$focused; 
	this.timer = null;

	// Initalize the combobox
	this.init();

	// bind event handlers for the widget
	this.bindHandlers();

} // end combobox constructor


/**
* @method init
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to initialize the combobox elements. Hides the list
* and sets ARIA attributes
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.init = function() {

	// Hide the list of options
	this.$list.hide().attr('aria-expanded', 'false');

	// If the edit box is to be readonly, aria-readonly must be defined as true
	if (this.editable == false) {
		this.$edit.attr('aria-readonly', 'true');
	}

	// Set initial value for the edit box
	this.$selected = this.$options.filter('.selected');

	if (this.$selected.length > 0) {
		this.$edit.val(this.$selected.text());
	}

} // end initCombo()

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers for the combobox elements
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.bindHandlers = function() {

	var thisObj = this;

	///////////////// bind editbox handlers /////////////////////////

	this.$edit.keydown(function(e) {
		return thisObj.handleEditKeyDown($(this), e);
	});

	this.$edit.keypress(function(e) {
		return thisObj.handleEditKeyPress($(this), e);
	});

	this.$edit.blur(function(e) {
		return thisObj.handleComboBlur($(this), e);
	});

	///////////////// bind handlers for the button /////////////////////////
	
	this.$button.click(function(e) {
		return thisObj.handleButtonClick($(this), e);
	});

	this.$button.mouseover(function(e) {
		return thisObj.handleButtonMouseOver($(this), e);
	});

	this.$button.mouseout(function(e) {
		return thisObj.handleButtonMouseOut($(this), e);
	});

	this.$button.mousedown(function(e) {
		return thisObj.handleButtonMouseDown($(this), e);
	});

	this.$button.mouseup(function(e) {
		return thisObj.handleButtonMouseUp($(this), e);
	});

	///////////////// bind listbox handlers /////////////////////////

	this.$list.focus(function(e) {
		return thisObj.handleComboFocus($(this), e);
	});

	this.$list.blur(function(e) {
		return thisObj.handleComboBlur($(this), e);
	});

	///////////////// bind list option handlers /////////////////////////

	this.$options.keydown(function(e) {
		return thisObj.handleOptionKeyDown($(this), e);
	});

	this.$options.keypress(function(e) {
		return thisObj.handleOptionKeyPress($(this), e);
	});

	this.$options.click(function(e) {
		return thisObj.handleOptionClick($(this), e);
	});

	this.$options.focus(function(e) {
		return thisObj.handleComboFocus($(this), e);
	});

	this.$options.blur(function(e) {
		return thisObj.handleComboBlur($(this), e);
	});

} // end bindHandlers()

/**
* @method isOpen
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to get the current state of the list box
*
* @return {boolean} returns true if list box is open; false if it is not
*/

OAA_EXAMPLES.combobox.prototype.isOpen = function() {

	if (this.$list.attr('aria-expanded') == 'true') {
		return true;
	}
	else {
		return false;
	}

} // end isOpen

/**
* @method closeList
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to close the list box if it is open
*
* @param {boolean} restore - true if function should restore higlight to stored list selection
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.closeList = function(restore) {

	var $curOption = this.$options.filter('.selected');

	if (restore == true) {
		$curOption = this.$selected;

		// remove the selected class from the other list items
		this.$options.removeClass('selected');

		// add selected class to the stored selection
		$curOption.addClass('selected');
	}

	this.$list.hide().attr('aria-expanded', 'false');

	// set focus on the edit box
	this.$edit.focus();

} // end closeList()

/**
* @method openList
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to open the list box if it is closed
*
* @param {boolean} restore - true if function should restore higlight to stored list selection
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.openList = function(restore) {

	var $curOption = this.$options.filter('.selected');


	if (restore == true) {

		if (this.$selected.length == 0) {
			// select the first item
			this.selectOption(this.$options.first());
		}

		$curOption = this.$selected;

		// remove the selected class from the other list items
		this.$options.removeClass('selected');

		// add selected class to the stored selection
		$curOption.addClass('selected');
	}

	this.$list.show().attr('aria-expanded', 'true');

	// scroll to the currently selected option
	this.$list.scrollTop(this.calcOffset($curOption));

	// set focus on the selected item
	this.$selected.focus();

} // end openList();

/**
* @method toggleList
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to toggle the display of the combobox options.
*
* @param {boolean} restore - true if toggle should restore higlight to stored list selection
*
* Return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.toggleList = function(restore) {

	if (this.isOpen() == true) {

		this.closeList(restore);
	}
	else {
		this.openList(restore);
	}

} // end toggleList()

/**
* @method selectOption
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to select a new combobox option.
* The jQuery object for the new option is stored and the selected class is added
*
* @param {object} $id - the jQuery object of the new option to select
*
* @return {N/A}
*/
 
OAA_EXAMPLES.combobox.prototype.selectOption = function($id) {

	// If there is a selected option, remove the selected class from it
	if (this.$selected.length > 0) {
		this.$selected.removeClass('selected');
	}
	
	// add the selected class to the new option
	$id.addClass('selected');

	// store the newly selected option
	this.$selected = $id;

	// update the edit box
	this.$edit.val($id.text());
	
} // end selectOption

/**
* @method calcOffset
*
* @memberOf OAA_EXAMPLES
*
* @desc member function to calculate the pixel offset of a list option from the top of the list
*
* @param {obj} $id - the jQuery object of the option to scroll to
*
* @return {integer} returns the pixel offset of the option
*/

OAA_EXAMPLES.combobox.prototype.calcOffset = function($id) {
	var offset = 0;
	var selectedNdx = this.$options.index($id);

	for (var ndx = 0; ndx < selectedNdx; ndx++) {
		offset += this.$options.eq(ndx).outerHeight();
	}

	return offset;

} // end calcOffset

/**
* @method handleButtonClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to consume button click events. This handler prevents
* clicks on the button from reloading the page. This could also be done by adding 'onclick="false";' to the button HTML markup.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonClick = function($id,  e) {

	e.stopPropagation();
	return false;

} // end handleButtonClick();

/**
* @method handleButtonMouseOver
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mouseover events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseOver = function($id,  e) {

	// change the button image to reflect the highlight state
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down-hl.png');

	e.stopPropagation();
	return false;

} // end handleButtonMouseOver();

/**
* @method handleButtonMouseOut
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mouseout events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseOut = function($id,  e) {

	// reset image to normal state
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down.png');

	e.stopPropagation();
	return false;

} // end handleButtonMouseOut();

/**
* @method handleButtonMouseDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mousedown events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseDown = function($id,  e) {

	// change the button image to reflect the pressed state
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down-pressed-hl.png');

	// toggle the display of the option list
	this.toggleList(true);

	e.stopPropagation();
	return false;

} // end handleButtonMouseDown();

/**
* @method handleButtonMouseUp
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mouseup events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseUp = function($id,  e) {

	// reset button image
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down-hl.png');

	e.stopPropagation();
	return false;

} // end handleButtonMouseUp();

/**
* @method handleOptionKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for the combobox
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false if consuming; true if not processing
*/

OAA_EXAMPLES.combobox.prototype.handleOptionKeyDown = function($id,  e) {

	var curNdx = this.$options.index($id);

	if (e.ctrlKey) {
		// do not process
		return true;
	}

	switch(e.keyCode) {
		case this.keys.tab: {
			// update and close the combobox

			if ($id.text() != this.$selected.text()) {

				// store the new selection
				this.selectOption($id);
			}

			// Close the option list
			this.closeList(false);

			// allow tab to propagate
			return true;
		}
		case this.keys.esc: {
			// Do not change combobox value

			// Close the option list
			this.closeList(true);

			e.stopPropagation();
			return false;
		}
		case this.keys.enter: {
			// change the combobox value

			if ($id.text() != this.$selected.text()) {

				// store the new selection
				this.selectOption($id);
			}

			// Close the option list
			this.closeList(false);

			e.stopPropagation();
			return false;
		}
		case this.keys.up: {
			
			if (e.altKey) {
				// alt+up toggles the list
				this.toggleList(true);

			}
			else {
				// move to the previous item in the list
			
				if (curNdx > 0) {
					var $prev = this.$options.eq(curNdx - 1);

					// remove the selected class from the current selection
					$id.removeClass('selected');

					// Add the selected class to the new selection
					$prev.addClass('selected');

					// scroll the list window to the new option
					this.$list.scrollTop(this.calcOffset($prev));

					// Set focus on the new item
					$prev.focus();
				}
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.down: {

			if (e.altKey) {
				// alt+up toggles the list
				this.toggleList(true);
			}
			else {
				// move to the next item in the list
			
				if (curNdx < this.$options.length - 1) {
					var $next = this.$options.eq(curNdx + 1);

					// remove the selected from the current selection
					$id.removeClass('selected');

					// Add the selected class to the new selection
					$next.addClass('selected');

					// scroll the list window to the new option
					this.$list.scrollTop(this.calcOffset($next));

					// Set focus on the new item
					$next.focus();
				}
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.home: {
			// select the first list item

			var $first = this.$options.first();

			// remove the selected class from the current selection
			this.$options.eq(curNdx).removeClass('selected');

			// Add the selected class to the new selection
			$first.addClass('selected');

			// scroll the list window to the new option
			this.$list.scrollTop(0);

			// set focus on the first item
			$first.focus();

			e.stopPropagation();
			return false;
		}
		case this.keys.end: {
			// select the last list item

			var $last = this.$options.last();

			// remove the selected class from the current selection
			this.$options.eq(curNdx).removeClass('selected');

			// Add the selected class to the new selection
			$last.addClass('selected');

			// scroll the list window to the new option
			this.$list.scrollTop(this.calcOffset($last));

			// set focus on last item
			$last.focus();

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleOptionKeyDown()

/**
* @method handleOptionKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for
* the combobox. Needed for browsers that use keypress to manipulate the window
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false if consuming; true if not processing
*/

OAA_EXAMPLES.combobox.prototype.handleOptionKeyPress = function($id,  e) {

	var curNdx = this.$options.index($id);

	if (e.altKey || e.ctrlKey || e.shiftKey) {
		// do not process
		return true;
	}

	switch(e.keyCode) {
		case this.keys.esc:
		case this.keys.enter:
		case this.keys.up:
		case this.keys.down:
		case this.keys.home:
		case this.keys.end: {
			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleOptionKeyPress()

/**
* @method handleEditKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for the edit box.
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @param {object} e - the event object associated with the event
*
* @return {boolean} Returns false if consuming; true if not processing
*/

OAA_EXAMPLES.combobox.prototype.handleEditKeyDown = function($id,  e) {

	var curNdx = this.$options.index(this.$selected);

	if (e.altKey && (e.keyCode == this.keys.up || e.keyCode == this.keys.down)) {

		this.toggleList(true);

		e.stopPropagation();
		return false;
	}

	switch (e.keyCode) {
		case this.keys.backspace:
		case this.keys.del: {
			this.$edit.val(this.$selected.text());

			e.stopPropagation();
			return false;
		}
		case this.keys.enter: {

			// toggle the option list
			this.toggleList(false);

			e.stopPropagation();
			return false;
		}
		case this.keys.up: {
			
			// move to the previous item in the list
			
			if (curNdx > 0) {
				var $prev = this.$options.eq(curNdx - 1);

				this.selectOption($prev);
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.down: {

			// move to the next item in the list
			
			if (curNdx < this.$options.length - 1) {
				var $next = this.$options.eq(curNdx + 1);

				this.selectOption($next);
			}

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleEditKeyDown()

/**
* @method handleEditKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for the edit box.
* Needed for browsers that use keypress events to manipulate the window.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false if consuming; true if not processing
*/

OAA_EXAMPLES.combobox.prototype.handleEditKeyPress = function($id,  e) {

	var curNdx = this.$options.index($id);

	if (e.altKey && (e.keyCode == this.keys.up || e.keyCode == this.keys.down)) {
		e.stopPropagation();
		return false;
	}

	switch(e.keyCode) {
		case this.keys.esc:
		case this.keys.enter: {

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleOptionKeyPress()

/**
* @method handleOptionClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events for the combobox.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false
*/

OAA_EXAMPLES.combobox.prototype.handleOptionClick = function($id, e) {

	// select the clicked item
	this.selectOption($id);

	// close the list
	this.closeList(false);

	e.stopPropagation();
	return false;	

} // end handleOptionClick()

/**
* @method handleComboFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process focus events for the list box
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns true
*/

OAA_EXAMPLES.combobox.prototype.handleComboFocus = function($id,  e) {

	if (this.timer != null) {
		window.clearTimeout(this.timer);
		this.timer = null;
	}

	return true;

} // end handleComboFocus()

/**
* @method handleComboBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process blur events for the combobox
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns true
*/

OAA_EXAMPLES.combobox.prototype.handleComboBlur = function($id,  e) {

	// store the currently selected value
	this.selectOption(this.$options.filter('.selected'));

	// close the list box
	if (this.isOpen() == true) {
		this.timer = window.setTimeout(function() {g_cb1.closeList(false);}, 40);
	}

	return true;

} // end handleComboBlur()
"""

example_obj.style       = """
* {
	font-family: "Times New Roman,Georgia,Serif"; 
}
.hidden {
	position: absolute;
	top: -20em;
	left: -200em;
}

.wrapper {
	height: 24px;
	overflow: auto;
}
.cb {
	margin: 20px;
	padding: 0;
	height: 24px;
	display: block;
	overflow: visible;
}

.cb_label {
	margin: 0;
	padding: 2px;
	width: 45px;
	font-weight: bold;
	float: left;
	display: inline;
}
.cb_edit {
	margin: 0;
	padding: 2px 3px;
	width: 240px;
	height: 18px;
	border: 1px solid black;
	font-size: 1em;
	float: left;
	display: inline;
}
.cb_button {
	margin: 0;
	padding: 0;
	height: 24px;
	width: 24px;
	border: 1px solid black;
	background-color: #999;
	float: left;
	display: inline;
	text-align: center;
}

button.cb_button img {
	margin: 0;
	padding: 0;
	height: 22px;
	width: 22px;
	position: relative;
	top: -1px;
	left: -3px;
}

.cb_list {
	clear: both;
	list-style: none;
	padding: 0;
	margin: 0;
	margin-left: 49px;
	border: 1px solid black;
	width: 246px;
	height: 200px;
	overflow: auto;
	background-color: #fff;
	position: relative;
	z-index: 300;
}

.cb_option {
	margin: 0 1px 0 0;
	padding: 2px 5px;
}
.selected {
	border-top: 1px solid #44e;
	border-bottom: 1px solid #44e;
	padding: 1px 5px;
	background-color: #77a;
	color: #fff;
}
.cb_option:hover {
	border-top: 1px solid #44e;
	border-bottom: 1px solid #44e;
	padding: 1px 5px;
	font-weight: bold;
	background-color: #77f;
	color: #fff;
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
example_obj.title       = 'Combobox with aria-autocomplete="inline" and role="combobox" on wrapping div'
example_obj.permanent_slug = 'combobox5'

example_obj.a11y_features = """
This example implements a combobox widget with aria-autocomplete="inline". Focus will remain on the edit box while the user manipulates the list box.
"""
example_obj.keyboard    = """
<ul>
    <li>Alt + Up Arrow/Down Arrow: Open or close the list box. Focus moves to selected option in list.<br>Note: Opera does not propagate alt key modifer events to the web page. Alt+Arrow key combinations will not work in Opera.</li>
    <li>Up Arrow: Select the previous option. If the list box is expanded, move upward in list and update the edit box but do not select a new option.</li>
    <li>Down Arrow: Select the next option. If the list box is expanded, move downward in list and update the edit box but do not select a new option.</li>
    <li>Home: Select the first option. If the list box is expanded, move to first list option and update the edit box but do not select.</li>
    <li>End: Select the last option. If the list box is expanded, move to last list and update the edit box but do not select.</li>
    <li>Enter: Select the highlighted list option and collapse the list box. If the list box is collapsed, expand it.</li>
    <li>Escape: Close list box without changing the combobox value (e.g. no selection is made).</li>
    <li>Tab: Select highlighted option and close list box (if it is expanded). Focus moves to the next focusable element in page.</li>
    <li>Shift+Tab: Same as tab key except focus moves to previous focusable item in page.</li>
</ul>
"""

example_obj.markup = [m1,m2,m3,m4,m5]

example_obj.html       = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<div role="application" tabindex="-1">

<form autocomplete="off">
<div id="cb1" class="cb" role="combobox">
	<div class="cb_label"><label id="cb1-label" for="cb1-edit">State</label>:</div>
	<input id="cb1-edit" class="cb_edit" type="text" tabindex="0"
		aria-labelledby="cb1-label"
		aria-autocomplete="inline"
		aria-owns="cb1-list"/>
	<div id="cb1-button-label" class="hidden">Open list of states</div>
	<button id="cb1-button" class="cb_button" aria-labelledby="cb1-button-label" aria-controls="cb1-list" tabindex="-1">
		<img src="{{EXAMPLE_MEDIA}}images/button-arrow-down.png" alt="Open or close the list box" />
	</button>

	<ul id="cb1-list" class="cb_list" tabindex="-1" role="listbox" aria-expanded="true">
		<li id="cb1-opt1" role="option" class="cb_option">Alabama</li>
		<li id="cb1-opt2" role="option" class="cb_option">Alaska</li>
		<li id="cb1-opt3" role="option" class="cb_option">American Samoa</li>
		<li id="cb1-opt4" role="option" class="cb_option">Arizona</li>
		<li id="cb1-opt5" role="option" class="cb_option">Arkansas</li>
		<li id="cb1-opt6" role="option" class="cb_option">California</li>
		<li id="cb1-opt7" role="option" class="cb_option">Colorado</li>
		<li id="cb1-opt8" role="option" class="cb_option">Connecticut</li>
		<li id="cb1-opt9" role="option" class="cb_option">Delaware</li>
		<li id="cb1-opt10" role="option" class="cb_option">District of Columbia</li>
		<li id="cb1-opt11" role="option" class="cb_option">Florida</li>
		<li id="cb1-opt12" role="option" class="cb_option">Georgia</li>
		<li id="cb1-opt13" role="option" class="cb_option">Guam</li>
		<li id="cb1-opt14" role="option" class="cb_option">Hawaii</li>
		<li id="cb1-opt15" role="option" class="cb_option">Idaho</li>
		<li id="cb1-opt16" role="option" class="cb_option selected">Illinois</li>
		<li id="cb1-opt17" role="option" class="cb_option">Indiana</li>
		<li id="cb1-opt18" role="option" class="cb_option">Iowa</li>
		<li id="cb1-opt19" role="option" class="cb_option">Kansas</li>
		<li id="cb1-opt20" role="option" class="cb_option">Kentucky</li>
		<li id="cb1-opt21" role="option" class="cb_option">Louisiana</li>
		<li id="cb1-opt22" role="option" class="cb_option">Maine</li>
		<li id="cb1-opt23" role="option" class="cb_option">Maryland</li>
		<li id="cb1-opt24" role="option" class="cb_option">Massachusetts</li>
		<li id="cb1-opt25" role="option" class="cb_option">Michigan</li>
		<li id="cb1-opt26" role="option" class="cb_option">Minnesota</li>
		<li id="cb1-opt27" role="option" class="cb_option">Mississippi</li>
		<li id="cb1-opt28" role="option" class="cb_option">Missouri</li>
		<li id="cb1-opt29" role="option" class="cb_option">Montana</li>
		<li id="cb1-opt30" role="option" class="cb_option">Nebraska</li>
		<li id="cb1-opt31" role="option" class="cb_option">Nevada</li>
		<li id="cb1-opt32" role="option" class="cb_option">New Hampshire</li>
		<li id="cb1-opt33" role="option" class="cb_option">New Jersey</li>
		<li id="cb1-opt34" role="option" class="cb_option">New Mexico</li>
		<li id="cb1-opt35" role="option" class="cb_option">New York</li>
		<li id="cb1-opt36" role="option" class="cb_option">North Carolina</li>
		<li id="cb1-opt37" role="option" class="cb_option">North Dakota</li>
		<li id="cb1-opt38" role="option" class="cb_option">Northern Marianas Islands</li>
		<li id="cb1-opt39" role="option" class="cb_option">Ohio</li>
		<li id="cb1-opt40" role="option" class="cb_option">Oklahoma</li>
		<li id="cb1-opt41" role="option" class="cb_option">Oregon</li>
		<li id="cb1-opt42" role="option" class="cb_option">Pennsylvania</li>
		<li id="cb1-opt43" role="option" class="cb_option">Puerto Rico</li>
		<li id="cb1-opt44" role="option" class="cb_option">Rhode Island</li>
		<li id="cb1-opt45" role="option" class="cb_option">South Carolina</li>
		<li id="cb1-opt47" role="option" class="cb_option">South Dakota</li>
		<li id="cb1-opt48" role="option" class="cb_option">Tennessee</li>
		<li id="cb1-opt49" role="option" class="cb_option">Texas</li>
		<li id="cb1-opt50" role="option" class="cb_option">Utah</li>
		<li id="cb1-opt51" role="option" class="cb_option">Vermont</li>
		<li id="cb1-opt52" role="option" class="cb_option">Virginia</li>
		<li id="cb1-opt53" role="option" class="cb_option">Virgin Islands</li>
		<li id="cb1-opt54" role="option" class="cb_option">Washington</li>
		<li id="cb1-opt55" role="option" class="cb_option">West Virginia</li>
		<li id="cb1-opt56" role="option" class="cb_option">Wisconsin</li>
		<li id="cb1-opt57" role="option" class="cb_option">Wyoming</li>
	</ul>
</div>
</form>
</div>
"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};
var g_cb1 = null;  // variable for the combobox instantiation

$(document).ready(function() {

	g_cb1 = new OAA_EXAMPLES.combobox('cb1', true);
}); // end ready

/**
* keyCodes() is an object to contain keycodes needed for the application
*/

function keyCodes() {
	// Define values for keycodes
	this.backspace  = 8;
	this.tab        = 9;
	this.enter      = 13;
	this.shift      = 16; // defined for keyUp event handler - firefox browser fix
	this.ctrl       = 17; // defined for keyUp event handler - firefox browser fix
	this.alt        = 18; // defined for keyUp event handler - firefox browser fix
	this.esc        = 27;

	this.space      = 32;
	this.pageup     = 33;
	this.pagedown   = 34;
	this.end        = 35;
	this.home       = 36;

	this.left       = 37;
	this.up         = 38;
	this.right      = 39; 
	this.down       = 40; 

} // end keyCodes

/**
* @constructor combobox
*
* @memberOf OAA_EXAMPLES
*
* @desc a class for an ARIA-enabled combobox widget
*
* @param {string} id - the id of the div containing the combobox. Text input must have role="combobox".
*
* @param {boolean} editable - true if the edit box should be editable; false if read-only.
*
* @return {N/A}
*/

/**
* @private
* @constructor Internal Properties
*
* @property {object} $id - The jQuery object of the div containing the combobox
* @property {boolean} editable - True if the edit box is editable

*
* @property {object} $edit - The jQuery object of the edit box
* @property {object} $button - The jQuery object of the button
* @property {object} $list - The jQuery object of the option list
* @property {object} $options - An array of jQuery objects for the combobox options
*
* @property {boolean} $selected  - the current value of the combobox
* @property {boolean} $focused - the currently selected option in the combo list

* @property {object} timer - stores the close list timer that is set when combo looses focus
*/

OAA_EXAMPLES.combobox = function(id, editable) {

	// Define the object properties

	this.$id = $('#' + id); 
	this.editable = editable; 
	this.keys = new keyCodes();

	// Store jQuery objects for the elements of the combobox
	this.$edit = $('#' + id + '-edit');  
	this.$button = $('#' + id + '-button'); 
	this.$list = $('#' + id + '-list'); 
	this.$options = this.$list.find('li');

	this.$selected;
	this.$focused; 
	this.timer = null;

	// Initalize the combobox
	this.init();

	// bind event handlers for the widget
	this.bindHandlers();

} // end combobox constructor


/**
* @method init
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to initialize the combobox elements. Hides the list
* and sets ARIA attributes
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.init = function() {

	// Hide the list of options
	this.closeList(false);

	// If the edit box is to be readonly, aria-readonly must be defined as true
	if (this.editable == false) {
		this.$edit.attr('aria-readonly', 'false');
	}

	// Set initial value for the edit box
	this.$selected = this.$options.filter('.selected');

	if (this.$selected.length > 0) {
		this.$edit.val(this.$selected.text());
	}

} // end initCombo()

/**
* @method bindHandlers
*
* @desc a member function to bind event handlers for the combobox elements
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.bindHandlers = function() {

	var thisObj = this;

	///////////////// bind editbox handlers /////////////////////////

	this.$edit.keydown(function(e) {
		return thisObj.handleEditKeyDown($(this), e);
	});

	this.$edit.keyup(function(e) {
		return thisObj.handleEditKeyUp($(this), e);
	});

	this.$edit.keypress(function(e) {
		return thisObj.handleEditKeyPress($(this), e);
	});

	this.$edit.blur(function(e) {
		return thisObj.handleComboBlur($(this), e);
	});

	///////////////// bind handlers for the button /////////////////////////
	
	this.$button.click(function(e) {
		return thisObj.handleButtonClick($(this), e);
	});

	this.$button.mouseover(function(e) {
		return thisObj.handleButtonMouseOver($(this), e);
	});

	this.$button.mouseout(function(e) {
		return thisObj.handleButtonMouseOut($(this), e);
	});

	this.$button.mousedown(function(e) {
		return thisObj.handleButtonMouseDown($(this), e);
	});

	this.$button.mouseup(function(e) {
		return thisObj.handleButtonMouseUp($(this), e);
	});

	///////////////// bind listbox handlers /////////////////////////

	this.$list.focus(function(e) {
		return thisObj.handleComboFocus($(this), e);
	});

	this.$list.blur(function(e) {
		return thisObj.handleComboBlur($(this), e);
	});

	///////////////// bind list option handlers /////////////////////////

	this.$options.click(function(e) {
		return thisObj.handleOptionClick($(this), e);
	});

} // end bindHandlers()

/**
* @method isOpen
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to get the current state of the list box
*
* @return {boolean} returns true if list box is open; false if it is not
*/

OAA_EXAMPLES.combobox.prototype.isOpen = function() {

   if (this.$list.attr('aria-expanded') == 'true') {
      return true;
   }
   else {
      return false;
   }

} // end isOpen

/**
* @method closeList
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to close the list box if it is open
*
* @param {boolean} restore - true if function should restore higlight to stored list selection
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.closeList = function(restore) {

	var $curOption = this.$options.filter('.selected');

	if (restore == true) {
		$curOption = this.$selected;

		// remove the selected class from the other list items
		this.$options.removeClass('selected');

		// add selected class to the stored selection
		$curOption.addClass('selected');
	}

	this.$list.hide().attr('aria-expanded', 'false');

} // end closeList()

/**
* @method openList
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to open the list box if it is closed
*
* @param {boolean} restore - true if function should restore higlight to stored list selection
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.openList = function(restore) {

	var $curOption = this.$options.filter('.selected');


	if (restore == true) {
		$curOption = this.$selected;

		// remove the selected class from the other list items
		this.$options.removeClass('selected');

		// add selected class to the stored selection
		$curOption.addClass('selected');
	}

	this.$list.show().attr('aria-expanded', 'true');

	if (this.$selected.length == 0) {

		// select the first item
		this.selectOption(this.$options.first());
		$curOption = this.$selected;
	}

	// scroll to the currently selected option
	this.$list.scrollTop(this.calcOffset($curOption));

} // end openList();

/**
* @method toggleList() - a member function to toggle the display of the combobox options.
*
* @param {boolean} restore - true if toggle should restore higlight to stored list selection
*
* return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.toggleList = function(restore) {

	if (this.isOpen() == true) {

		this.closeList(restore);
	}
	else {
		this.openList(restore);
	}

} // end toggleList()

/**
* @method selectOption
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to select a new combobox option.
* The jQuery object for the new option is stored and the selected class is added
*
* @param {object} $id - the jQuery object of the new option to select
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.selectOption = function($id) {

	// remove the selected class from the list
	this.$options.removeClass('selected');
	
	// add the selected class to the new option
	$id.addClass('selected');

	// store the newly selected option
	this.$selected = $id;

	// update the edit box
	this.$edit.val($id.text());

	//move cursor to the end
	this.selectText(this.$edit.val().length, this.$edit.val().length);

	// reset the option list
	this.$options = this.$list.find('li').removeClass('hidden');
	
} // end selectOption

/**
* @method calcOffset
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to calculate the pixel offset of a list option
* from the top of the list
*
* @param {object} $id - the jQuery object of the option to scroll to
*
* @return {integer} returns the pixel offset of the option
*/

OAA_EXAMPLES.combobox.prototype.calcOffset = function($id) {
	var offset = 0;
	var selectedNdx = this.$options.index($id);

	for (var ndx = 0; ndx < selectedNdx; ndx++) {
		if (this.$options.eq(ndx).not('[class=hidden]')) {
			offset += this.$options.eq(ndx).outerHeight();
		}
	}

	return offset;

} // end calcOffset

/**
* @method handleButtonClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to consume button click events. This handler prevents
* clicks on the button from reloading the page. This could also be done by adding 'onclick="false";' to the
* button HTML markup.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonClick = function($id,  e) {

	e.stopPropagation();
	return false;

} // end handleButtonClick();

/**
* @method handleButtonMouseOver
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mouseover events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseOver = function($id,  e) {

	// change the button image to reflect the highlight state
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down-hl.png');

	e.stopPropagation();
	return false;

} // end handleButtonMouseOver();

/**
* @method handleButtonMouseOut
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mouseout events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseOut = function($id,  e) {

	// reset image to normal state
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down.png');

	e.stopPropagation();
	return false;

} // end handleButtonMouseOut();

/**
* @method handleButtonMouseDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mousedown events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseDown = function($id,  e) {

	// change the button image to reflect the pressed state
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down-pressed-hl.png');

	// toggle the display of the option list
	this.toggleList(true);

	// Set focus on the edit box
	this.$edit.focus();

	e.stopPropagation();
	return false;

} // end handleButtonMouseDown();

/**
* @method handleButtonMouseUp
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mouseup events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseUp = function($id,  e) {

	// reset button image
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down-hl.png');

	e.stopPropagation();
	return false;

} // end handleButtonMouseUp();

/**
* @method handleEditKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for the edit box.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false if consuming; true if not processing
*/

OAA_EXAMPLES.combobox.prototype.handleEditKeyDown = function($id,  e) {

	var $curOption = this.$options.filter('.selected');
	var curNdx = this.$options.index($curOption);

	switch(e.keyCode) {
		case this.keys.tab: {
			// store the current selection
			this.selectOption($curOption);

			if (this.isOpen() == true) {
				// Close the option list
				this.closeList(false);
			}

			// allow tab to propagate
			return true;
		}
		case this.keys.esc: {
			// Do not change combobox value

			// Restore the edit box to the selected value
			this.$edit.val(this.$selected.text());

			// Select the text
			this.$edit.select();

			if (this.isOpen() == true) {

				// Close the option list
				this.closeList(true);
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.enter: {
			if (e.shiftKey || e.altKey || e.ctrlKey) {
				// do nothing
				return true;
			}

			if (this.isOpen() == false) {
				// open the option list
				this.openList(false);
			}
			else {
				// store the new selection
				this.selectOption($curOption);

				// Close the option list
				this.closeList(false);
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.up: {
			
			var $curOption = this.$options.filter('.selected');

			if (e.shiftKey || e.ctrlKey) {
				// do nothing
				return true;
			}

			if (e.altKey) {
				// alt+up toggles the list

				if (this.isOpen() == true) {

					this.selectOption($curOption);
				}
				
				// toggle the list
				this.toggleList(false);
			}
			else {
				// move to the previous item in the list
			
				if (curNdx > 0) {
					var $prev = this.$options.eq(curNdx - 1);

					// remove the selected class from the current selection
					$curOption.removeClass('selected');

					// Add the selected class to the new selection
					$prev.addClass('selected');

					// Change the text in the edit box
					this.$edit.val($prev.text());

					// Select the text
					this.$edit.select();

					if (this.isOpen() == true) {
						// scroll the list window to the new option
						this.$list.scrollTop(this.calcOffset($prev));
					}
				}
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.down: {
			if (e.shiftKey || e.ctrlKey) {
				// do nothing
				return true;
			}

			if (e.altKey) {
				// alt+up toggles the list

				if (this.isOpen() == true) {
					// Restore the edit box to the selected value
					this.$edit.val(this.$selected.text());

					// Select the text
					this.$edit.select();

					// alt+up toggles the list
					this.closeList(true);
				}
				else {
					// alt+up toggles the list
					this.openList(false);
				}
			}
			else {
				// move to the next item in the list

				if (curNdx != this.$options.length - 1) {
					var $prev = this.$options.eq(curNdx + 1);

					// remove the selected class from the current selection
					this.$options.eq(curNdx).removeClass('selected');

					// Add the selected class to the new selection
					$prev.addClass('selected');

					// Change the text in the edit box
					this.$edit.val($prev.text());

					// Select the text
					this.$edit.select();

					if (this.isOpen() == true) {
						// scroll the list window to the new option
						this.$list.scrollTop(this.calcOffset($prev));
					}
				}
			}

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleEditKeyDown()

/**
* @method handleEditKeyUp
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keyup events for
* the edit box.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false if consuming; true if not processing
*/

OAA_EXAMPLES.combobox.prototype.handleEditKeyUp = function($id,  e) {

	var thisObj = this;
	var val = this.$edit.val();
	var re = new RegExp('^' + val, 'i');

	if (e.shiftKey || e.ctrlKey || e.altKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
		case this.keys.shift:
		case this.keys.ctrl:
		case this.keys.alt:
		case this.keys.esc: 
		case this.keys.tab:
		case this.keys.enter:
		case this.keys.left:
		case this.keys.right:
		case this.keys.up:
		case this.keys.down:
		case this.keys.home:
		case this.keys.end: {
			// do nothing
			return true;
		}
	}

	// repopulate the list make all items visible and remove the selection highlighting
	this.$options = this.$list.find('li').removeClass('hidden').removeClass('selected');

	if (val.length == 0) {
		// if the list box is visible, scroll to the top
		if (this.isOpen() == true) {
			this.$list.scrollTop(0);
		}
	}
	else {
		// recreate the list including only options that match
		// what the user typed
		this.$options = this.$options.filter(function(index) {

			if (re.test($(this).text()) == true) {
				return true;
			}
			else {
				// hide those entries that do not match
				$(this).addClass('hidden');

				return false;
			}
		});
	}
	
	if (this.$options.length > 0) {
		var $newOption = this.$options.first();
		var newVal = $newOption.text();
		var start = val.length;
		var end = newVal.length;
		var editNode = this.$edit.get(0);

		if (e.keyCode != this.keys.backspace) {
			// if the user isn't backspacing, fill in the
			// suggested value.
			this.$edit.val(newVal);
		}

		// Select the auto-complete text
		this.selectText(start, end);

		// Reset the highlighting for the list
		this.$options.removeClass('selected');

		$newOption.addClass('selected');
	}

	// Show the list if it is hidden
	if (this.isOpen() == false) {
		this.openList(false);
	}

	e.stopPropagation();
	return false;
} // end handleEditKeyUp()

/**
* @method handleEditKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for the edit box.
* Needed for browsers that use keypress events to manipulate the window.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false if consuming; true if not processing
*/

OAA_EXAMPLES.combobox.prototype.handleEditKeyPress = function($id,  e) {

	var curNdx = this.$options.index($id);

	if (e.altKey && (e.keyCode == this.keys.up || e.keyCode == this.keys.down)) {
		e.stopPropagation();
		return false;
	}

	switch(e.keyCode) {
		case this.keys.enter:
		case this.keys.up:
		case this.keys.down: {
			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleOptionKeyPress()

/**
* @method handleOptionClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events for the combobox.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false
*/

OAA_EXAMPLES.combobox.prototype.handleOptionClick = function($id,  e) {

	// select the clicked item
	this.selectOption($id);

	// set focus on the edit box
	this.$edit.focus();

	// close the list
	this.closeList(false);

	e.stopPropagation();
	return false;	

} // end handleOptionClick()

/**
* @method handleComboFocus
*
* @memberOf OAA_EXAMPLES
*
* @desca member function to process focus events for the combobox
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns true
*/

OAA_EXAMPLES.combobox.prototype.handleComboFocus = function($id,  e) {

	window.clearTimeout(g_cb1.timer);

	// set focus on the edit box
	this.$edit.focus();

	e.stopPropagation();
	return false;

} // end handleComboFocus()

/**
* @method handleComboBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process blur events for the combobox
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns true
*/

OAA_EXAMPLES.combobox.prototype.handleComboBlur = function($id,  e) {

	// store the currently selected value
	this.selectOption(this.$options.filter('.selected'));

	// close the list box
	if (this.isOpen() == true) {
		this.timer = window.setTimeout(function() {g_cb1.closeList(false);}, 40);
	}

	e.stopPropagation();
	return false;

} // end handleComboBlur()

/**
* @method selectText
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to select some of the text in the edit box.
* If start and end are the same value, the function moves the cursor to that position.
*
* @param {object} start - the character position for the start of the selection
*
* @param {object} end - the character position for the end of the selection
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.selectText = function(start, end) {

	var editNode = this.$edit.get(0);

	if (editNode.setSelectionRange) {
		// Firefox and other gecko based browsers
		editNode.setSelectionRange(start, end);
	}
	else if (editNode.createTextRange) {
		// Internet Explorer
		var range = editNode.createTextRange();
		range.collapse(true);
		range.moveEnd('character', start);
		range.moveStart('character', end);
		range.select();
	}
	else if (editNode.selectionStart) {
		// Other browsers
		editNode.selectionStart = start;
		editNode.selectionEnd = end;
	}

} // end selectText()
"""

example_obj.style       = """
* {
	font-family: "Times New Roman,Georgia,Serif"; 
}
.hidden {
	position: absolute;
	top: -20em;
	left: -200em;
}

.wrapper {
	height: 24px;
	overflow: auto;
}
.cb {
	margin: 20px;
	padding: 0;
	height: 24px;
	display: block;
	overflow: visible;
}

.cb_label {
	margin: 0;
	padding: 2px;
	width: 45px;
	font-weight: bold;
	float: left;
	display: inline;
}
.cb_edit {
	margin: 0;
	padding: 2px 3px;
	width: 240px;
	height: 18px;
	border: 1px solid black;
	font-size: 1em;
	float: left;
	display: inline;
}
.cb_button {
	margin: 0;
	padding: 0;
	height: 24px;
	width: 24px;
	border: 1px solid black;
	background-color: #999;
	float: left;
	display: inline;
	text-align: center;
}

button.cb_button img {
	margin: 0;
	padding: 0;
	height: 22px;
	width: 22px;
	position: relative;
	top: -1px;
	left: -3px;
}
.cb_list {
	clear: both;
	list-style: none;
	padding: 0;
	margin: 0;
	margin-left: 49px;
	border: 1px solid black;
	width: 246px;
	height: 200px;
	overflow: auto;
	background-color: #fff;
	position: relative;
	z-index: 300;
}

.cb_option {
	margin: 0 1px 0 0;
	padding: 2px 5px;
}
.selected {
	border-top: 1px solid #44e;
	border-bottom: 1px solid #44e;
	padding: 1px 5px;
	background-color: #77a;
	color: #fff;
}
.cb_option:hover {
	border-top: 1px solid #44e;
	border-bottom: 1px solid #44e;
	padding: 1px 5px;
	font-weight: bold;
	background-color: #77f;
	color: #fff;
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
example_obj.title       = 'Combobox with aria-autocomplete="list" and role="combobox" on wrapping div'
example_obj.permanent_slug = 'combobox6'

example_obj.a11y_features = """
This is example implements a combobox widget with aria-autocomplete="list". Focus remains on the edit box while the user manipulates the list. activedescendant is used to tell assistive technologies which list option is currently selected. For clarity, this example was designed not to update the edit box until the user makes a choice from the list.
"""
example_obj.keyboard    = """
<ul>
    <li>Enter: Select highlighted option and close the list box. If list box is closed, opens the list box.</li>
    <li>Escape: Close list box without changing the combobox value (e.g. no selection is made).</li>
    <li>Up Arrow: Moves upward in list. If the list box is closed, this does not select the highlighted list option.</li>
    <li>Down Arrow: Moves downward in list. If the list box is closed, this does not select the highlighted list option.</li>
    <li>Home: If the list box is open, moves to first option in list.</li>
    <li>End: If the list box is open, moves to last option in list.</li>
    <li>Tab: Select highlighted option and close list box. Focus moves to the next focusable element in page.</li>
    <li>Shift+Tab: Same as tab key except focus moves to previous focusable item in page.</li>
    <li>Alt + Up Arrow/Down Arrow: Open or close the list box.<br>Note: Opera does not propagate alt key modifer events to the web page. Alt+Arrow key combinations will not work in Opera.</li></li>
</ul>
"""

example_obj.markup = [m1,m2,m3,m4,m5,m6]

example_obj.html       = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<div role="application" tabindex="-1">

<form autocomplete="off">
<div id="cb1" class="cb" role="combobox" aria-activedescendant="cb1-opt16">
	<div class="cb_label"><label id="cb1-label" for="cb1-edit">State</label>:</div>
	<input id="cb1-edit" class="cb_edit" type="text"
		tabindex="0"
		aria-labelledby="cb1-label"
		aria-autocomplete="list"
		aria-owns="cb1-list"
		aria-readonly="true"/>
	<div id="cb1-button-label" class="hidden">Open list of states</div>
	<button id="cb1-button" class="cb_button" aria-labelledby="cb1-button-label" aria-controls="cb1-list" tabindex="-1">
		<img src="{{EXAMPLE_MEDIA}}images/button-arrow-down.png" alt="Open or close the list box" />
	</button>

	<ul id="cb1-list" class="cb_list" tabindex="-1" role="listbox" aria-expanded="true">
		<li id="cb1-opt1" role="option" class="cb_option" role="listitem" tabindex="-1">Alabama</li>
		<li id="cb1-opt2" role="option" class="cb_option" role="listitem" tabindex="-1">Alaska</li>
		<li id="cb1-opt3" role="option" class="cb_option" role="listitem" tabindex="-1">American Samoa</li>
		<li id="cb1-opt4" role="option" class="cb_option" role="listitem" tabindex="-1">Arizona</li>
		<li id="cb1-opt5" role="option" class="cb_option" role="listitem" tabindex="-1">Arkansas</li>
		<li id="cb1-opt6" role="option" class="cb_option" role="listitem" tabindex="-1">California</li>
		<li id="cb1-opt7" role="option" class="cb_option" role="listitem" tabindex="-1">Colorado</li>
		<li id="cb1-opt8" role="option" class="cb_option" role="listitem" tabindex="-1">Connecticut</li>
		<li id="cb1-opt9" role="option" class="cb_option" role="listitem" tabindex="-1">Delaware</li>
		<li id="cb1-opt10" role="option" class="cb_option" role="listitem" tabindex="-1">District of Columbia</li>
		<li id="cb1-opt11" role="option" class="cb_option" role="listitem" tabindex="-1">Florida</li>
		<li id="cb1-opt12" role="option" class="cb_option" role="listitem" tabindex="-1">Georgia</li>
		<li id="cb1-opt13" role="option" class="cb_option" role="listitem" tabindex="-1">Guam</li>
		<li id="cb1-opt14" role="option" class="cb_option" role="listitem" tabindex="-1">Hawaii</li>
		<li id="cb1-opt15" role="option" class="cb_option" role="listitem" tabindex="-1">Idaho</li>
		<li id="cb1-opt16" role="option" class="cb_option selected" role="listitem" tabindex="-1">Illinois</li>
		<li id="cb1-opt17" role="option" class="cb_option" role="listitem" tabindex="-1">Indiana</li>
		<li id="cb1-opt18" role="option" class="cb_option" role="listitem" tabindex="-1">Iowa</li>
		<li id="cb1-opt19" role="option" class="cb_option" role="listitem" tabindex="-1">Kansas</li>
		<li id="cb1-opt20" role="option" class="cb_option" role="listitem" tabindex="-1">Kentucky</li>
		<li id="cb1-opt21" role="option" class="cb_option" role="listitem" tabindex="-1">Louisiana</li>
		<li id="cb1-opt22" role="option" class="cb_option" role="listitem" tabindex="-1">Maine</li>
		<li id="cb1-opt23" role="option" class="cb_option" role="listitem" tabindex="-1">Maryland</li>
		<li id="cb1-opt24" role="option" class="cb_option" role="listitem" tabindex="-1">Massachusetts</li>
		<li id="cb1-opt25" role="option" class="cb_option" role="listitem" tabindex="-1">Michigan</li>
		<li id="cb1-opt26" role="option" class="cb_option" role="listitem" tabindex="-1">Minnesota</li>
		<li id="cb1-opt27" role="option" class="cb_option" role="listitem" tabindex="-1">Mississippi</li>
		<li id="cb1-opt28" role="option" class="cb_option" role="listitem" tabindex="-1">Missouri</li>
		<li id="cb1-opt29" role="option" class="cb_option" role="listitem" tabindex="-1">Montana</li>
		<li id="cb1-opt30" role="option" class="cb_option" role="listitem" tabindex="-1">Nebraska</li>
		<li id="cb1-opt31" role="option" class="cb_option" role="listitem" tabindex="-1">Nevada</li>
		<li id="cb1-opt32" role="option" class="cb_option" role="listitem" tabindex="-1">New Hampshire</li>
		<li id="cb1-opt33" role="option" class="cb_option" role="listitem" tabindex="-1">New Jersey</li>
		<li id="cb1-opt34" role="option" class="cb_option" role="listitem" tabindex="-1">New Mexico</li>
		<li id="cb1-opt35" role="option" class="cb_option" role="listitem" tabindex="-1">New York</li>
		<li id="cb1-opt36" role="option" class="cb_option" role="listitem" tabindex="-1">North Carolina</li>
		<li id="cb1-opt37" role="option" class="cb_option" role="listitem" tabindex="-1">North Dakota</li>
		<li id="cb1-opt38" role="option" class="cb_option" role="listitem" tabindex="-1">Northern Marianas Islands</li>
		<li id="cb1-opt39" role="option" class="cb_option" role="listitem" tabindex="-1">Ohio</li>
		<li id="cb1-opt40" role="option" class="cb_option" role="listitem" tabindex="-1">Oklahoma</li>
		<li id="cb1-opt41" role="option" class="cb_option" role="listitem" tabindex="-1">Oregon</li>
		<li id="cb1-opt42" role="option" class="cb_option" role="listitem" tabindex="-1">Pennsylvania</li>
		<li id="cb1-opt43" role="option" class="cb_option" role="listitem" tabindex="-1">Puerto Rico</li>
		<li id="cb1-opt44" role="option" class="cb_option" role="listitem" tabindex="-1">Rhode Island</li>
		<li id="cb1-opt45" role="option" class="cb_option" role="listitem" tabindex="-1">South Carolina</li>
		<li id="cb1-opt47" role="option" class="cb_option" role="listitem" tabindex="-1">South Dakota</li>
		<li id="cb1-opt48" role="option" class="cb_option" role="listitem" tabindex="-1">Tennessee</li>
		<li id="cb1-opt49" role="option" class="cb_option" role="listitem" tabindex="-1">Texas</li>
		<li id="cb1-opt50" role="option" class="cb_option" role="listitem" tabindex="-1">Utah</li>
		<li id="cb1-opt51" role="option" class="cb_option" role="listitem" tabindex="-1">Vermont</li>
		<li id="cb1-opt52" role="option" class="cb_option" role="listitem" tabindex="-1">Virginia</li>
		<li id="cb1-opt53" role="option" class="cb_option" role="listitem" tabindex="-1">Virgin Islands</li>
		<li id="cb1-opt54" role="option" class="cb_option" role="listitem" tabindex="-1">Washington</li>
		<li id="cb1-opt55" role="option" class="cb_option" role="listitem" tabindex="-1">West Virginia</li>
		<li id="cb1-opt56" role="option" class="cb_option" role="listitem" tabindex="-1">Wisconsin</li>
		<li id="cb1-opt57" role="option" class="cb_option" role="listitem" tabindex="-1">Wyoming</li>
	</ul>
</div>
</form>
</div>
"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};

var g_combo = null;  // set to active combobox for blur function

$(document).ready(function() {

	var cb1 = new OAA_EXAMPLES.combobox('cb1', false);
}); // end ready

/**
* keyCodes() is an object to contain keycodes needed for the application
*/

function keyCodes() {
	// Define values for keycodes
	this.backspace  = 8;
	this.tab        = 9;
	this.enter      = 13;
	this.esc        = 27;

	this.space      = 32;
	this.pageup     = 33;
	this.pagedown   = 34;
	this.end        = 35;
	this.home       = 36;

	this.up         = 38;
	this.down       = 40; 
	
	this.del        = 46;

} // end keyCodes

/**
* @constructor combobox
*
* @memberOf OAA_EXAMPLES
*
* @desc a class for an ARIA-enabled combobox widget
*
* @param {string} id - the id of the div containing the combobox. Text input must have role="combobox".
*
* @param {boolean} editable - true if the edit box should be editable; false if read-only.
*
* @return {N/A}
*/

/**
* @private
* @constructor Internal Properties
*
* @property {object} $id - The jQuery object of the div containing the combobox
* @property {boolean} editable - True if the edit box is editable
*
* @property {object} $edit - The jQuery object of the edit box
* @property {object} $button - The jQuery object of the button
* @property {object} $list - The jQuery object of the option list
* @property {object} $options - An array of jQuery objects for the combobox options
*
* @property {boolean} $selected  - the current value of the combobox
* @property {boolean} $focused - the currently selected option in the combo list
* @property {object} timer - stores the close list timer that is set when combo looses focus
*/

OAA_EXAMPLES.combobox = function(id, editable) {

	// Define the object properties

	this.$id = $('#' + id); 
	this.editable = editable; 
	this.keys = new keyCodes();

	// Store jQuery objects for the elements of the combobox
	this.$edit = $('#' + id + '-edit');  
	this.$button = $('#' + id + '-button'); 
	this.$list = $('#' + id + '-list');  
	this.$options = this.$list.find('li');
	this.$selected; 
	this.$focused; 
	this.timer = null;

	// Initalize the combobox
	this.init();

	// bind event handlers for the widget
	this.bindHandlers();

} // end combobox constructor


/**
* @method init
*
* @membreOf OAA_EXAMPLES
*
* @desc a member function to initialize the combobox elements. Hides the list
* and sets ARIA attributes
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.init = function() {

	// Hide the list of options
	this.$list.hide().attr('aria-expanded', 'false');

	// If the edit box is to be readonly, aria-readonly must be defined as true
	if (this.editable == false) {
		this.$edit.attr('aria-readonly', 'true');
	}

	// Set initial value for the edit box
	this.$selected = this.$options.filter('.selected');

	if (this.$selected.length > 0) {
		this.$edit.val(this.$selected.text());
	}

} // end initCombo()

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers for the combobox elements
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.bindHandlers = function() {

	var thisObj = this;

	///////////////// bind handlers for the button /////////////////////////
	
	this.$button.click(function(e) {
		return thisObj.handleButtonClick($(this), e);
	});

	this.$button.mouseover(function(e) {
		return thisObj.handleButtonMouseOver($(this), e);
	});

	this.$button.mouseout(function(e) {
		return thisObj.handleButtonMouseOut($(this), e);
	});

	this.$button.mousedown(function(e) {
		return thisObj.handleButtonMouseDown($(this), e);
	});

	this.$button.mouseup(function(e) {
		return thisObj.handleButtonMouseUp($(this), e);
	});

	///////////////// bind listbox handlers /////////////////////////

	this.$options.click(function(e) {
		return thisObj.handleOptionClick($(this), e);
	});

	this.$list.focus(function(e) {
		return thisObj.handleComboFocus($(this), e);
	});

	this.$list.blur(function(e) {
		return thisObj.handleComboBlur($(this), e);
	});

	this.$options.focus(function(e) {
		return thisObj.handleComboFocus($(this), e);
	});

	this.$options.blur(function(e) {
		return thisObj.handleComboBlur($(this), e);
	});

	///////////////// bind editbox handlers /////////////////////////

	this.$edit.keydown(function(e) {
		return thisObj.handleEditKeyDown($(this), e);
	});

	this.$edit.keypress(function(e) {
		return thisObj.handleEditKeyPress($(this), e);
	});

	this.$edit.blur(function(e) {
		return thisObj.handleComboBlur($(this), e);
	});

} // end bindHandlers()

/**
* @method isOpen
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to get the current state of the list box
*
* @return {boolean} returns true if list box is open; false if it is not
*/

OAA_EXAMPLES.combobox.prototype.isOpen = function() {

	if (this.$list.attr('aria-expanded') == 'true') {
		return true;
	}
	else {
		return false;
	}

} // end isOpen

/**
* @method closeList
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to close the list box if it is open
*
* @param {boolean} restore - true if function should restore higlight to stored list selection
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.closeList = function(restore) {

	var $curOption = this.$options.filter('.selected');

	if (restore == true) {
		$curOption = this.$selected;

		// remove the selected class from the other list items
		this.$options.removeClass('selected');

		// add selected class to the stored selection
		$curOption.addClass('selected');
	}

	this.$list.hide().attr('aria-expanded', 'false');

} // end closeList()

/**
* @method openList
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to open the list box if it is closed
*
* @param {boolean} restore - true if function should restore higlight to stored list selection
*
* @return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.openList = function(restore) {

	var $curOption = this.$options.filter('.selected');

	if (restore == true) {

		if (this.$selected.length == 0) {
			// select the first item
			this.selectOption(this.$options.first());
			$curOption = this.$selected;
		}
		else {
			$curOption = this.$selected;
		}

		// remove the selected class from the other list items
		this.$options.removeClass('selected');

		// add selected class to the stored selection
		$curOption.addClass('selected');
	}

	this.$list.show().attr('aria-expanded', 'true');

	// scroll to the currently selected option
	this.$list.scrollTop(this.calcOffset($curOption));

} // end openList();

/*
* @method toggleList
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to toggle the display of the combobox options.
*
* @param {booleam} restore - true if toggle should restore higlight to stored list selection
*
* Return {N/A}
*/

OAA_EXAMPLES.combobox.prototype.toggleList = function(restore) {

	if (this.isOpen() == true) {

		this.closeList(restore);
	}
	else {
		this.openList(restore);
	}

} // end toggleList()

/**
* @method selectOption
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to select a new combobox option.
* The jQuery object for the new option is stored and the selected class is added
*
* @param {object} $id - the jQuery object of the new option to select
*
* @return {N/A}
*/
OAA_EXAMPLES.combobox.prototype.selectOption = function($id) {

	// If there is a selected option, remove the selected class from it
	if (this.$selected.length > 0) {
		this.$selected.removeClass('selected');
	}
	
	// add the selected class to the new option
	$id.addClass('selected');

	// set active descendant for the new option
	this.$id.attr('aria-activedescendant', $id.attr('id'));

	// store the newly selected option
	this.$selected = $id;

	// update the edit box
	this.$edit.val($id.text());
	
} // end selectOption

/**
* @methodFunction calcOffset
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to calculate the pixel offset of a list option from the top of the list
*
* @param {$id} $id - the jQuery object of the option to scroll to
*
* @return {integer} returns the pixel offset of the option
*/

OAA_EXAMPLES.combobox.prototype.calcOffset = function($id) {
	var offset = 0;
	var selectedNdx = this.$options.index($id);

	for (var ndx = 0; ndx < selectedNdx; ndx++) {
		offset += this.$options.eq(ndx).outerHeight();
	}

	return offset;

} // end calcOffset

/**
* @method handleButtonClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to consume button click events. This handler prevents
* clicks on the button from reloading the page. This could also be done by adding
* 'onclick="false";' to the button HTML markup.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonClick = function($id,  e) {

	e.stopPropagation();
	return false;

} // end handleButtonClick();

/**
* @method handleButtonMouseOver
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mouseover events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseOver = function($id,  e) {

	// change the button image to reflect the highlight state
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down-hl.png');

	e.stopPropagation();
	return false;

} // end handleButtonMouseOver();

/**
* @method handleButtonMouseOut
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mouseout events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseOut = function($id,  e) {

	// reset image to normal state
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down.png');

	e.stopPropagation();
	return false;

} // end handleButtonMouseOut();

/**
* @method handleButtonMouseDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process button mousedown events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseDown = function($id,  e) {

	// change the button image to reflect the pressed state
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down-pressed-hl.png');

	// toggle the display of the option list
	this.toggleList(true);

	// Set focus on the edit box
	this.$edit.focus();

	e.stopPropagation();
	return false;

} // end handleButtonMouseDown();

/**
* Function handleButtonMouseUp() is a member function to process button mouseup events
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.combobox.prototype.handleButtonMouseUp = function($id,  e) {

	// reset button image
	$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/button-arrow-down-hl.png');

	e.stopPropagation();
	return false;

} // end handleButtonMouseUp();


/**
* @method handleEditKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for the edit box.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false if consuming; true if not processing
*/

OAA_EXAMPLES.combobox.prototype.handleEditKeyDown = function($id,  e) {

	var $curOption = this.$options.filter('.selected');
	var curNdx = this.$options.index($curOption);

	if (e.altKey && (e.keyCode == this.keys.up || e.keyCode == this.keys.down)) {

		this.toggleList(true);

		e.stopPropagation();
		return false;
	}

	switch (e.keyCode) {
		case this.keys.backspace:
		case this.keys.del: {
			// prevent the edit box from being changed
			this.$edit.val(this.$selected.text());

			e.stopPropagation();
			return false;
		}
		case this.keys.tab: {

			// store the current selection
			this.selectOption($curOption);


			if (this.isOpen() == true) {
				// Close the option list
				this.closeList(false);
			}

			// allow tab to propagate
			return true;
		}
		case this.keys.esc: {
			// Do not change combobox value

			if (this.isOpen() == true) {
				// Close the option list
				this.closeList(true);
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.enter: {

			if (this.isOpen() == true) {
				// store the current selection
				this.selectOption($curOption);

				// Close the option list
				this.closeList(false);
			}
			else {
				this.openList(false);
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.up: {
			
			// move to the previous item in the list
			
			// if the list is expanded and this isn't the first item
			// move to the next item in the list
			
			if (curNdx > 0) {

				var $prev = this.$options.eq(curNdx - 1);

				if (this.isOpen() == true) {
					// remove the selected class from the current selection
					$curOption.removeClass('selected');

					// Add the selected class to the new selection
					$prev.addClass('selected');

					// Set activedescendent for new option
					this.$id.attr('aria-activedescendant', $prev.attr('id'));

					// scroll the list window to the new option
					this.$list.scrollTop(this.calcOffset($prev));
				}
				else {
					// store the new selection
					this.selectOption($prev);
				}

			}

			e.stopPropagation();
			return false;
		}
		case this.keys.down: {

			// if the list is expanded and there are more items,
			// move to the next item in the list
			
			if (curNdx < this.$options.length - 1) {

				var $next = this.$options.eq(curNdx + 1);

				if (this.isOpen() == true) {
					// remove the selected class from the current selection
					$curOption.removeClass('selected');

					// Add the selected class to the new selection
					$next.addClass('selected');

					// Set activedescendent for new option
					this.$id.attr('aria-activedescendant', $next.attr('id'));

					// scroll the list window to the new option
					this.$list.scrollTop(this.calcOffset($next));
				}
				else {
					// store the new selection
					this.selectOption($next);
				}
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.home: {
			// select the first list item if the list is open

			if (this.isOpen() == true) {
			
				var $first = this.$options.first();

				// remove the selected class from the current selection
				$curOption.removeClass('selected');

				// Add the selected class to the new selection
				$first.addClass('selected');

				// scroll the list window to the new option
				this.$list.scrollTop(0);

				// Set activedescendent for new option
				this.$id.attr('aria-activedescendant', $first.attr('id'));
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.end: {
			// select the last list item if the list is open

			if (this.isOpen() == true) {

				var $last = this.$options.last();

				// remove the selected class from the current selection
				$curOption.removeClass('selected');

				// Add the selected class to the new selection
				$last.addClass('selected');

				// scroll the list window to the new option
				this.$list.scrollTop(this.calcOffset($last));

				// Set activedescendent for new option
				this.$id.attr('aria-activedescendant', $last.attr('id'));
			}

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleEditKeyDown()

/**
* @method handleEditKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for the edit box.
* Needed for browsers that use keypress events to manipulate the window.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false if consuming; true if not processing
*/

OAA_EXAMPLES.combobox.prototype.handleEditKeyPress = function($id,  e) {

	var curNdx = this.$options.index($id);

	if (e.altKey && (e.keyCode == this.keys.up || e.keyCode == this.keys.down)) {
		e.stopPropagation();
		return false;
	}

	switch(e.keyCode) {
		case this.keys.esc:
		case this.keys.enter: {

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleOptionKeyPress()

/**
* @method handleOptionClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events for the combobox.
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns false
*/

OAA_EXAMPLES.combobox.prototype.handleOptionClick = function($id,  e) {

	// select the clicked item
	this.selectOption($id);

	// set focus on the edit box
	//this.$edit.focus();

	// close the list
	this.closeList(false);

	e.stopPropagation();
	return false;	

} // end handleOptionClick()

/**
* @method handleComboFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process focus events for the list box
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns true
*/

OAA_EXAMPLES.combobox.prototype.handleComboFocus = function($id,  e) {

	if (g_combo != null) {
		window.clearTimeout(g_combo.timer);
	}

	// Set focus on the edit box
	this.$edit.focus();

	return true;

} // end handleComboFocus()

/**
* @method handleComboBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process blur events for the combobox
*
* @param {object} e - the event object associated with the event
*
* @param {object} $id - the jQuery object for the element firing the event
*
* @return {boolean} Returns true
*/

OAA_EXAMPLES.combobox.prototype.handleComboBlur = function($id,  e) {

	// store the currently selected value
	this.$selected = this.$options.filter('.selected');

	// update the edit box
	this.$edit.val(this.$selected.text());

	g_combo = this;

	// close the list box
	if (this.isOpen() == true) {
		this.timer = window.setTimeout(function() {g_combo.closeList(false);}, 40);
	}

	return true;

} // end handleComboBlur()
"""

example_obj.style       = """
* {
	font-family: "Times New Roman,Georgia,Serif"; 
}
.hidden {
	position: absolute;
	top: -20em;
	left: -200em;
}

.wrapper {
	height: 24px;
	overflow: auto;
}
.cb {
	margin: 20px;
	padding: 0;
	height: 24px;
	display: block;
	overflow: visible;
}

.cb_label {
	margin: 0;
	padding: 2px;
	width: 45px;
	font-weight: bold;
	float: left;
	display: inline;
}
.cb_edit {
	margin: 0;
	padding: 2px 3px;
	width: 240px;
	height: 18px;
	border: 1px solid black;
	font-size: 1em;
	float: left;
	display: inline;
}
.cb_button {
	margin: 0;
	padding: 0;
	height: 24px;
	width: 24px;
	border: 1px solid black;
	background-color: #999;
	float: left;
	display: inline;
	text-align: center;
}

button.cb_button img {
	margin: 0;
	padding: 0;
	height: 22px;
	width: 22px;
	position: relative;
	top: -1px;
	left: -3px;
}
.cb_list {
	clear: both;
	list-style: none;
	padding: 0;
	margin: 0;
	margin-left: 49px;
	border: 1px solid black;
	width: 246px;
	height: 200px;
	overflow: auto;
	background-color: #fff;
	position: relative;
	z-index: 300;
}

.cb_option {
	margin: 0 1px 0 0;
	padding: 2px 5px;
}
.selected {
	border-top: 1px solid #44e;
	border-bottom: 1px solid #44e;
	padding: 1px 5px;
	background-color: #77a;
	color: #fff;
}
.cb_option:hover {
	border-top: 1px solid #44e;
	border-bottom: 1px solid #44e;
	padding: 1px 5px;
	font-weight: bold;
	background-color: #77f;
	color: #fff;
}
"""

example6 = create_example(example_obj)