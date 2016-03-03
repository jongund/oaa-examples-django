"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples import *

order = 1

spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec = spec_aria10, attribute='role', value='tab')
m2 = ElementDefinition.objects.get(spec = spec_aria10, attribute='role', value='tablist')
m3 = ElementDefinition.objects.get(spec = spec_aria10, attribute='role', value='tabpanel')
m4 = ElementDefinition.objects.get(spec = spec_aria10, attribute='aria-controls')
m5 = ElementDefinition.objects.get(spec = spec_aria10, attribute='aria-hidden')
m6 = ElementDefinition.objects.get(spec = spec_aria10, attribute='aria-labelledby')
m7 = ElementDefinition.objects.get(spec = spec_aria10, attribute='aria-selected')
m8 = ElementDefinition.objects.get(spec = spec_aria10, attribute='aria-expanded')
m9 = ElementDefinition.objects.get(spec = spec_aria10, attribute='aria-multiselectable')

# =============================
# Example 1
# =============================

example_obj             = example_object()
example_obj.example_id = 34
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order       = order
example_obj.title       = 'Tab Panel'
example_obj.permanent_slug = 'tabpanel1'

example_obj.a11y_features = """
Simple example of a tab Panel widget.
"""
example_obj.keyboard    = """

The following keyboard shortcuts are implemented for this example (based on recommended shortcuts specified by the "DHTML Style Guide Working Group":http://dev.aol.com/dhtml_style_guide/


If focus is on a tab button:

    * Left / Up Arrow: Show the previous tab
    * Right / Down Arrow: Show the next tab
    * Home: Show the first tab
    * End: Show the last tab


If focus is on an element in a tab panel:

    * Control + Up Arrow/Left Arrow: Set focus on the tab button for the currently displayed tab.
    * Control + Page Up: Show the previous tab and set focus on its corresponding tab button. Shows the last tab in the panel if current tab is the first one.
    * Control + Page Down: Show the next tab and set focus on its corresponding tab button. Shows the first tab in the panel if current tab is the last one.


*NOTE:* Google Chrome does not propagate Control+ Page Up or Control+ Page Down to the web page when multiple tabs are open. This key combination will not function correctly in that case.
"""
example_obj.markup = [m1,m2,m3,m4,m5,m6,m7]

example_obj.html        = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<h2>Happy Time Pizza On-line Ordering System</h2>

<form>
<div id="tabpanel1" class="tabpanel">

	<ul class="tablist" role="tablist">
		<li id="tab1" class="tab selected" aria-controls="panel1" aria-selected="true" role="tab" tabindex="0">Crust</li>
		<li id="tab2" class="tab" aria-controls="panel2" role="tab" aria-selected="false" tabindex="-1">Veggies</li>
		<li id="tab3" class="tab" aria-controls="panel3" role="tab" aria-selected="false" tabindex="-1">Carnivore</li>
		<li id="tab4" class="tab" aria-controls="panel4" role="tab" aria-selected="false" tabindex="-1">Delivery</li>
	</ul>

	<div id="panel1" class="panel" aria-labelledby="tab1" role="tabpanel">
		<h3 tabindex="0">Select Crust</h3>
	   
        	<ul class="controlList">
	        	<li><input id="p1_opt1" type="radio" name="crust" value="crust1" /><label for="p1_opt1">Deep Dish</label></li>
	        	<li><input id="p1_opt2" type="radio" name="crust" value="crust2" checked="checked" /><label for="p1_opt2">Thick and cheesy</label></li>
	        	<li><input id="p1_opt3" type="radio" name="crust" value="crust3" /><label for="p1_opt3">Thick and spicy</label></li>
	        	<li><input id="p1_opt4" type="radio" name="crust" value="crust4" /><label for="p1_opt4">Thin</label></li>
	     	</ul>
	</div>

	<div id="panel2" class="panel" aria-labelledby="tab2" role="tabpanel">
		<h3 tabindex="0">Select Vegetables</h3>	
	   
	     	<ul class="controlList">
	        	<li><input id="p2_opt1" type="checkbox" name="veg" value="black olives" /><label for="p2_opt1">Black Olives</label></li>
	        	<li><input id="p2_opt2" type="checkbox" name="veg" value="green olives" /><label for="p2_opt2">Green Olives</label></li>
	        	<li><input id="p2_opt3" type="checkbox" name="veg" value="green peppers" /><label for="p2_opt3">Green Peppers</label></li>
	        	<li><input id="p2_opt4" type="checkbox" name="veg" value="mushrooms" /><label for="p2_opt4">Mushrooms</label></li>
	        	<li><input id="p2_opt5" type="checkbox" name="veg" value="onions" /><label for="p2_opt5">Onions</label></li>
	        	<li><input id="p2_opt6" type="checkbox" name="veg" value="pineapple" /><label for="p2_opt6">Pineapple</label></li>
	     	</ul>
	</div>

	<div id="panel3" class="panel" aria-labelledby="tab3" role="tabpanel">
		<h3 tabindex="0">Select Carnivore Options</h3>
	   
      		<ul class="controlList">
        		<li><input id="p3_opt1" type="checkbox" name="meat" value="pepperoni" /><label for="p3_opt1">Pepperoni</label></li>
        		<li><input id="p3_opt2" type="checkbox" name="meat" value="sausage" /><label for="p3_opt2">Italian Sausage</label></li>
        		<li><input id="p3_opt3" type="checkbox" name="meat" value="ham" /><label for="p3_opt3">Ham</label></li>
        		<li><input id="p3_opt4" type="checkbox" name="meat" value="hamburger" /><label for="p3_opt4">Hamburger</label></li>
      		</ul>
	</div>

	<div id="panel4" class="panel" aria-labelledby="tab4" role="tabpanel">
	 	<h3 tabindex="0">Select Delivery Method</h3>
	   
		<ul class="controlList">
			<li><input id="p4_opt1" type="radio" name="delivery" value="delivery1" checked="checked" /><label for="p4_opt1">Delivery</label></li>
			<li><input id="p4_opt2" type="radio" name="delivery" value="delivery2" /><label for="p4_opt2">Eat in</label></li>
			<li><input id="p4_opt3" type="radio" name="delivery" value="delivery3" /><label for="p4_opt3">Carry out</label></li>
			<li><input id="p4_opt4" type="radio" name="delivery" value="delivery4" /><label for="p4_opt4">Overnight mail</label></li>
		</ul>
	</div>
</div>
</form>


"""
example_obj.script      = """

var OAA_EXAMPLES = OAA_EXAMPLES || {} ;
$(document).ready(function() {

	var panel1 = new OAA_EXAMPLES.tabpanel("tabpanel1", false);
});



//
// keyCodes() is an object to contain keycodes needed for the application
//
OAA_EXAMPLES.keyCodes = function() {
	// Define values for keycodes
	this.tab        = 9;
	this.enter      = 13;
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

/*
* @constructor tabpanel
*
* @memberOf OAA_EXAMPLES
*
* @desc a class constructor to create a ARIA-enabled tab panel widget.
*
* @param {string} id - the id of the div containing the tab panel.
*
* @param {boolean} accordian - true if the tab panel should operate
*         as an accordian; false if a tab panel
*
* @return {N/A}
*
* Usage: Requires a div container and children as follows:
*
*         1. tabs/accordian headers have class 'tab'
*
*         2. panels are divs with class 'panel'
*/

/**
* @constructor Internal Properties
*
* @memberOf OAA_EXAMPLES
*
* @property {string} id - store the id of the containing div
*
* @property {boolean} accordian - true if this is an accordian control
*
* @property {object} $panel - store the jQuery object for the panel
*
* @property {object} keys - keycodes needed for event handlers
*
* @property {array} $tabs - Array of panel tabs.
*
* @property {array} $panels - Array of panel tabs.
*/

OAA_EXAMPLES.tabpanel = function(id, accordian) {

	// define the class properties
	
	this.panel_id = id;
	this.accordian = accordian;
	this.$panel = $('#' + id); 
	this.keys = new OAA_EXAMPLES.keyCodes(); 
	this.$tabs = this.$panel.find('.tab'); 
	this.$panels = this.$panel.children('.panel');
	// Bind event handlers
	this.bindHandlers();

	// Initialize the tab panel
	this.init();

} // end tabpanel() constructor

/**
* @method init
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to initialize the tab/accordian panel. Hides all panels. If a tab
* has the class 'selected', makes that panel visible; otherwise, makes first panel visible.
*
* @return {N/A}
*/

OAA_EXAMPLES.tabpanel.prototype.init = function() {
	var $tab; // the selected tab - if one is selected

	// add aria attributes to the panels
	this.$panels.attr('aria-hidden', 'true');

	// hide all the panels
	this.$panels.hide();

	// get the selected tab
	$tab = this.$tabs.filter('.selected');

	if ($tab == undefined) {
		$tab = this.$tabs.first();
		$tab.addClass('selected');
	}

	// show the panel that the selected tab controls and set aria-hidden to false
	this.$panel.find('#' + $tab.attr('aria-controls')).show().attr('aria-hidden', 'false');

} // end init()

/**
* @method switchTabs
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to give focus to a new tab or accordian header.
* If it's a tab panel, the currently displayed panel is hidden and the panel 
* associated with, the new tab is displayed.
*
* @param {object} $curTab - the jQuery object of the currently selected tab
*
* @param {obj} $newTab - the jQuery object of new tab to switch to
*
* @return {N/A}
*/

OAA_EXAMPLES.tabpanel.prototype.switchTabs = function($curTab, $newTab) {

	// Remove the highlighting from the current tab
	$curTab.removeClass('selected focus');

	// remove tab from the tab order and update its aria-selected attribute
	$curTab.attr('tabindex', '-1').attr('aria-selected', 'false');

	// update the aria attributes
	
	// Highlight the new tab and update its aria-selected attribute
	$newTab.addClass('selected').attr('aria-selected', 'true');

	// If this is a tab panel, swap displayed tabs
	if (this.accordian == false) {
		// hide the current tab panel and set aria-hidden to true
		this.$panel.find('#' + $curTab.attr('aria-controls')).hide().attr('aria-hidden', 'true');

		// show the new tab panel and set aria-hidden to false
		this.$panel.find('#' + $newTab.attr('aria-controls')).show().attr('aria-hidden', 'false');
	}

	// Make new tab navigable
	$newTab.attr('tabindex', '0');

	// give the new tab focus
	$newTab.focus();

} // end switchTabs()

/**
* @method togglePanel
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to display or hide the panel associated with an accordian header
*
* @param {object} $tab - the jQuery object of the currently selected tab
*
* @return {N/A}
*/

OAA_EXAMPLES.tabpanel.prototype.togglePanel = function($tab) {

	$panel = this.$panel.find('#' + $tab.attr('aria-controls'));

	if ($panel.attr('aria-hidden') == 'true') {
		$panel.slideDown(100);
		$panel.attr('aria-hidden', 'false');
	}
	else {
		$panel.slideUp(100);
		$panel.attr('aria-hidden', 'true');
	}
} // end togglePanel()

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers for the tabs
*
* @return {N/A}
*/

OAA_EXAMPLES.tabpanel.prototype.bindHandlers = function() {

	var thisObj = this; // Store the this pointer for reference

	//////////////////////////////
	// Bind handlers for the tabs / accordian headers

	// bind a tab keydown handler
	this.$tabs.keydown(function(e) {
		return thisObj.handleTabKeyDown($(this), e);
	});

	// bind a tab keypress handler
	this.$tabs.keypress(function(e) {
		return thisObj.handleTabKeyPress($(this), e);
	});

	// bind a tab click handler
	this.$tabs.click(function(e) {
		return thisObj.handleTabClick($(this), e);
	});

	// bind a tab focus handler
	this.$tabs.focus(function(e) {
		return thisObj.handleTabFocus($(this), e);
	});

	// bind a tab blur handler
	this.$tabs.blur(function(e) {
		return thisObj.handleTabBlur($(this), e);
	});

	/////////////////////////////
	// Bind handlers for the panels
	
	// bind a keydown handlers for the panel focusable elements
	this.$panels.keydown(function(e) {
		return thisObj.handlePanelKeyDown($(this), e);
	});

	// bind a keypress handler for the panel
	this.$panels.keypress(function(e) {
		return thisObj.handlePanelKeyPress($(this), e);
	});

} // end bindHandlers()

/**
* @method handleTabKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for a tab
*
* @param {object} $tab - the jquery object of the tab being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true if propagating; false if consuming event
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabKeyDown = function($tab, e) {

	if (e.altKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
		case this.keys.enter:
		case this.keys.space: {

			// Only process if this is an accordian widget
			if (this.accordian == true) {
				// display or collapse the panel
				this.togglePanel($tab);

				e.stopPropagation();
				return false;
			}

			return true;
		}
		case this.keys.left:
		case this.keys.up: {

			var thisObj = this;
			var $prevTab; // holds jQuery object of tab from previous pass
			var $newTab; // the new tab to switch to

			if (e.ctrlKey) {
				// Ctrl+arrow moves focus from panel content to the open
				// tab/accordian header.
			}
			else {
				var curNdx = this.$tabs.index($tab);

				if (curNdx == 0) {
					// tab is the first one:
					// set newTab to last tab
					$newTab = this.$tabs.last();
				}
				else {
					// set newTab to previous
					$newTab = this.$tabs.eq(curNdx - 1);
				}

				// switch to the new tab
				this.switchTabs($tab, $newTab);
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.right:
		case this.keys.down: {

			var thisObj = this;
			var foundTab = false; // set to true when current tab found in array
			var $newTab; // the new tab to switch to

			var curNdx = this.$tabs.index($tab);

			if (curNdx == this.$tabs.length-1) {
				// tab is the last one:
				// set newTab to first tab
				$newTab = this.$tabs.first();
			}
			else {
				// set newTab to next tab
				$newTab = this.$tabs.eq(curNdx + 1);
			}

			// switch to the new tab
			this.switchTabs($tab, $newTab);

			e.stopPropagation();
			return false;
		}
		case this.keys.home: {

			// switch to the first tab
			this.switchTabs($tab, this.$tabs.first());

			e.stopPropagation();
			return false;
		}
		case this.keys.end: {

			// switch to the last tab
			this.switchTabs($tab, this.$tabs.last());

			e.stopPropagation();
			return false;
		}
	}
} // end handleTabKeyDown()

/**
* @method handleTabKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for a tab.
*
* @param {object} $tab - the jquery object of the tab being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true if propagating; false if consuming event
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabKeyPress = function($tab, e) {

	if (e.altKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
		case this.keys.enter:
		case this.keys.space:
		case this.keys.left:
		case this.keys.up:
		case this.keys.right:
		case this.keys.down:
		case this.keys.home:
		case this.keys.end: {
			e.stopPropagation();
			return false;
		}
		case this.keys.pageup:
		case this.keys.pagedown: {

			// The tab keypress handler must consume pageup and pagedown
			// keypresses to prevent Firefox from switching tabs
			// on ctrl+pageup and ctrl+pagedown

			if (!e.ctrlKey) {
				return true;
			}

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleTabKeyPress()

/**
* Function handleTabClick() is a member function to process click events for tabs
*
* @param ($tab object) $tab is the jQuery object of the tab being processed
*
* @param (e object) e is the associated event object
*
* @return (boolean) returns true
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabClick = function($tab, e) {

	// Remove the highlighting from all tabs
	this.$tabs.removeClass('selected');

	// remove all tabs from the tab order and reset their aria-selected attribute
	this.$tabs.attr('tabindex', '-1').attr('aria-selected', 'false');

	// hide all tab panels
	this.$panels.hide();
	
	// Highlight the clicked tab and update its aria-selected attribute
	$tab.addClass('selected').attr('aria-selected', 'true');

	// show the clicked tab panel
	this.$panel.find('#' + $tab.attr('aria-controls')).show();

	// make clicked tab navigable
	$tab.attr('tabindex', '0');

	// give the tab focus
	$tab.focus();

	return true;

} // end handleTabClick()

/**
* @method handleTabFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process focus events for tabs
*
* @param {object} $tab - the jQuery object of the tab being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabFocus = function($tab, e) {

	// Add the focus class to the tab
	$tab.addClass('focus');

	return true;

} // end handleTabFocus()

/**
* @method handleTabBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process blur events for tabs
*
* @param {object} $tab - the jQuery object of the tab being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabBlur = function($tab, e) {

	// Remove the focus class to the tab
	$tab.removeClass('focus');

	return true;

} // end handleTabBlur()



// Panel Event handlers

/**
* @method handlePanelKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for a panel
*
* @param {object} $elem - the jquery object of the element being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true if propagating; false if consuming event
*/

OAA_EXAMPLES.tabpanel.prototype.handlePanelKeyDown = function($elem, e) {

	if (e.altKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
		case this.keys.esc: {
			e.stopPropagation();
			return false;
		}
		case this.keys.left:
		case this.keys.up: {

			if (!e.ctrlKey) {
				// do not process
				return true;
			}
	
			// get the jQuery object of the tab
			var $tab = $('#' + $elem.attr('aria-labelledby'));

			// Move focus to the tab
			$tab.focus();

			e.stopPropagation();
			return false;
		}
		case this.keys.pageup: {

			var $newTab;

			if (!e.ctrlKey) {
				// do not process
				return true;
			}

			// get the jQuery object of the tab
			var $tab = this.$tabs.filter('.selected');

			// get the index of the tab in the tab list
			var curNdx = this.$tabs.index($tab);

			if (curNdx == 0) {
				// this is the first tab, set focus on the last one
				$newTab = this.$tabs.last();
			}
			else {
				// set focus on the previous tab
				$newTab = this.$tabs.eq(curNdx - 1);
			}

			// switch to the new tab
			this.switchTabs($tab, $newTab);

			e.stopPropagation();
			e.preventDefault();
			return false;
		}
		case this.keys.pagedown: {

			var $newTab;

			if (!e.ctrlKey) {
				// do not process
				return true;
			}

			// get the jQuery object of the tab
			var $tab = $('#' + $elem.attr('aria-labelledby'));

			// get the index of the tab in the tab list
			var curNdx = this.$tabs.index($tab);

			if (curNdx == this.$tabs.length-1) {
				// this is the last tab, set focus on the first one
				$newTab = this.$tabs.first();
			}
			else {
				// set focus on the next tab
				$newTab = this.$tabs.eq(curNdx + 1);
			}

			// switch to the new tab
			this.switchTabs($tab, $newTab);

			e.stopPropagation();
			e.preventDefault();
			return false;
		}
	}

	return true;

} // end handlePanelKeyDown()

/**
* @method handlePanelKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for a panel
*
* @param {object} $elem - the jquery object of the element being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true if propagating; false if consuming event
*/

OAA_EXAMPLES.tabpanel.prototype.handlePanelKeyPress = function($elem, e) {

	if (e.altKey) {
		// do nothing
		return true;
	}

	if (e.ctrlKey && (e.keyCode == this.keys.pageup || e.keyCode == this.keys.pagedown)) {
			e.stopPropagation();
			e.preventDefault();
			return false;
	}

	switch (e.keyCode) {
		case this.keys.esc: {
			e.stopPropagation();
			e.preventDefault();
			return false;
		}
	}

	return true;

} // end handlePanelKeyPress()

/**
* focusable is a small jQuery extension to add a :focusable selector. It is used to
* get a list of all focusable elements in a panel. Credit to ajpiano on the jQuery forums.
*/

$.extend($.expr[':'], {
	focusable: function(element) {
		var nodeName = element.nodeName.toLowerCase();
		var tabIndex = $(element).attr('tabindex');

		// the element and all of its ancestors must be visible
		if (($(element)[nodeName == 'area' ? 'parents' : 'closest'](':hidden').length) == true) {
			return false;
		}

		// If tabindex is defined, its value must be greater than 0
		if (!isNaN(tabIndex) && tabIndex < 0) {
			return false;
		}

		// if the element is a standard form control, it must not be disabled
		if (/input|select|textarea|button|object/.test(nodeName) == true) {

	       		return !element.disabled;
		}

		// if the element is a link, href must be defined
		if ((nodeName == 'a' ||  nodeName == 'area') == true) {

			return (element.href.length > 0);
		}
		    	   
		// this is some other page element that is not normally focusable.
		return false;
	}
});
"""

example_obj.style       = """
.tabpanel {
	margin: 20px;
	padding: 0;
	height: 1%; /* IE fix for float bug */
}
.tablist {
	margin: 0 0px;
	padding: 0;
	list-style: none;
}

.tab {

	margin: .2em 1px 0 0;
	padding: 10px;
	height: 1em;
	font-weight: bold;
	background-color: #ec9;

	border: 1px solid black;
	-webkit-border-radius-topright: 5px;
	-webkit-border-radius-topleft: 5px;
	-moz-border-radius-topright: 5px;
	-moz-border-radius-topleft: 5px;
	border-radius-topright: 5px;
	border-radius-topleft: 5px;

	float: left;
	display: inline; /* IE float bug fix */
}

.panel {
	clear: both;
	display: block;
	margin: 0 0 0 0;
	padding: 10px;
	width: 600px;
	border: 1px solid black;

	-webkit-border-radius-topright: 10px;
	-webkit-border-radius-bottomleft: 10px;
	-webkit-border-radius-bottomright: 10px;
	-moz-border-radius-topright: 10px;
	-moz-border-radius-bottomleft: 10px;
	-moz-border-radius-bottomright: 10px;
	border-radius-topright: 10px;
	border-radius-bottomleft: 10px;
	border-radius-bottomright: 10px;
}

ul.controlList {
	list-style-type: none;
}

li.selected {
	color: black;
	background-color: #fff;
	border-bottom: 1px solid white;
}

.focus {
	margin-top: 0;
	height: 1.2em;
}

.accordian {
	margin: 0;
	float: none;
	-webkit-border-radius: 0;
	-moz-border-radius: 0;
	border-radius: 0;
	width: 600px;
}

.hidden {
	position: absolute;
	left: -300em;
	top: -30em;
}
"""

example1 = create_example(example_obj)

# =============================
# Example 2
# =============================

order += 1

example_obj             = example_object()
example_obj.example_id = 35
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order       = order
example_obj.title       = 'Tab Panel: Accordian1'
example_obj.permanent_slug = 'accordian1'

example_obj.a11y_features = """
Simple example of a tab panel accordian widget.
"""
example_obj.keyboard    = """

The following keyboard shortcuts are implemented for this example (based on recommended shortcuts specified by the "DHTML Style Guide Working Group":http://dev.aol.com/dhtml_style_guide/:


If focus is on a tab button:

    * Left / Up Arrow: Show the previous tab
    * Right / Down Arrow: Show the next tab
    * Home: Show the first tab
    * End: Show the last tab
    * Enter/Space: Expand / Collapse panel


If focus is on an element in a tab panel:

    * Control + Up Arrow/Left Arrow: Set focus on the tab button for the currently displayed tab.
    * Control + Page Up: Show the previous tab and set focus on its corresponding tab button. Shows the last tab in the panel if current tab is the first one.
    * Control + Page Down: Show the next tab and set focus on its corresponding tab button. Shows the first tab in the panel if current tab is the last one.
    * Tab: Move focus to next focusable element in panel. If focus is on last focusable element, move focus to first focusable element of next expanded panel or, if no more expanded panels or focusable elements, to first focusable element following tab panel in the page.
    * Shift+Tab: The reverse of Tab.


*NOTE:* Google Chrome does not propagate Control+ Page Up or Control+ Page Down to the web page when multiple tabs are open. This key combination will not function correctly in that case.
"""

example_obj.markup = [m1,m2,m3,m4,m5,m6,m7,m8,m9]

example_obj.html        = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<h2>Happy Time Pizza On-line Ordering System</h2>

<form>
<div id="accordian1" class="tabpanel" role="tablist" multiselectable="true">

	<h3 id="tab1" class="tab accordian selected" aria-selected="true" aria-controls="panel1" aria-expanded="true" role="tab" tabindex="0">
		<img src="{{EXAMPLE_MEDIA}}images/expanded.gif" alt="expanded" />
		Crust
	</h3>

	<div id="panel1" class="panel accordian" aria-labelledby="tab1" aria-hidden="false" role="tabpanel">
		<h3 tabindex="0">Select Crust</h3>
	   
        	<ul class="controlList">
	        	<li><input id="p1_opt1" type="radio" name="crust" value="crust1" /><label for="p1_opt1">Deep Dish</label></li>
	        	<li><input id="p1_opt2" type="radio" name="crust" value="crust2" checked="checked" /><label for="p1_opt2">Thick and cheesy</label></li>
	        	<li><input id="p1_opt3" type="radio" name="crust" value="crust3" /><label for="p1_opt3">Thick and spicy</label></li>
	        	<li><input id="p1_opt4" type="radio" name="crust" value="crust4" /><label for="p1_opt4">Thin</label></li>
	     	</ul>
	</div>

	<h3 id="tab2" class="tab accordian" aria-selected="false" aria-controls="panel2" aria-expanded="false" role="tab" tabindex="-1">
		<img src="{{EXAMPLE_MEDIA}}images/contracted.gif" alt="collapsed" />
		Veggies
	</h3>
	<div id="panel2" class="panel accordian" aria-labelledby="tab2" aria-hidden="true" role="tabpanel">
		<h3 tabindex="0">Select Vegetables</h3>	
	   
	     	<ul class="controlList">
	        	<li><input id="p2_opt1" type="checkbox" name="veg" value="black olives" /><label for="p2_opt1">Black Olives</label></li>
	        	<li><input id="p2_opt2" type="checkbox" name="veg" value="green olives" /><label for="p2_opt2">Green Olives</label></li>
	        	<li><input id="p2_opt3" type="checkbox" name="veg" value="green peppers" /><label for="p2_opt3">Green Peppers</label></li>
	        	<li><input id="p2_opt4" type="checkbox" name="veg" value="mushrooms" /><label for="p2_opt4">Mushrooms</label></li>
	        	<li><input id="p2_opt5" type="checkbox" name="veg" value="onions" /><label for="p2_opt5">Onions</label></li>
	        	<li><input id="p2_opt6" type="checkbox" name="veg" value="pineapple" /><label for="p2_opt6">Pineapple</label></li>
	     	</ul>
	</div>

	<h3 id="tab3" class="tab accordian" aria-selected="false" aria-controls="panel3" aria-expanded="false" role="tab" tabindex="-1">
		<img src="{{EXAMPLE_MEDIA}}images/contracted.gif" alt="collapsed" />
		Carnivore
	</h3>
	<div id="panel3" class="panel accordian" aria-labelledby="tab3" aria-hidden="true" role="tabpanel">
		<h3 tabindex="0">Select Carnivore Options</h3>
	   
      		<ul class="controlList">
        		<li><input id="p3_opt1" type="checkbox" name="meat" value="pepperoni" /><label for="p3_opt1">Pepperoni</label></li>
        		<li><input id="p3_opt2" type="checkbox" name="meat" value="sausage" /><label for="p3_opt2">Italian Sausage</label></li>
        		<li><input id="p3_opt3" type="checkbox" name="meat" value="ham" /><label for="p3_opt3">Ham</label></li>
        		<li><input id="p3_opt4" type="checkbox" name="meat" value="hamburger" /><label for="p3_opt4">Hamburger</label></li>
      		</ul>
	</div>

	<h3 id="tab4" class="tab accordian" aria-selected="false" aria-controls="panel4" aria-expanded="false" role="tab" tabindex="-1">
		<img src="{{EXAMPLE_MEDIA}}images/contracted.gif" alt="collapsed" />
		Delivery
	</h3>
	<div id="panel4" class="panel accordian" aria-labelledby="tab4" aria-hidden="true" role="tabpanel">
	 	<h3 tabindex="0">Select Delivery Method</h3>
	   
		<ul class="controlList">
			<li><input id="p4_opt1" type="radio" name="delivery" value="delivery1" checked="checked" /><label for="p4_opt1">Delivery</label></li>
			<li><input id="p4_opt2" type="radio" name="delivery" value="delivery2" /><label for="p4_opt2">Eat in</label></li>
			<li><input id="p4_opt3" type="radio" name="delivery" value="delivery3" /><label for="p4_opt3">Carry out</label></li>
			<li><input id="p4_opt4" type="radio" name="delivery" value="delivery4" /><label for="p4_opt4">Overnight mail</label></li>
		</ul>
	</div>
</div>
</form>

"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};
$(document).ready(function() {

	var panel1 = new OAA_EXAMPLES.tabpanel("accordian1", true);
});


// keyCodes() is an object to contain keycodes needed for the application

OAA_EXAMPLES.keyCodes = function() {
	// Define values for keycodes
	this.tab        = 9;
	this.enter      = 13;
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
* @constructor tabpanel
*
* @memberOf OAA_EXAMPLES
*
* @desc a class constructor to create a ARIA-enabled tab panel widget.
* 	  Usage: Requires a div container and children as follows:
*
*         1. tabs/accordian headers have class 'tab'
*
*         2. panels are divs with class 'panel'
*
* @param {string} id - the id of the div containing the tab panel.
*
* @param {boolean} accordian - true if the tab panel should operate
*         as an accordian; false if a tab panel
*
* @return {N/A}
*/

/**
* @constructor Internal Properties
*
* @property {string} id - store the id of the containing div
*
* @property {boolean} accordian - true if this is an accordian control
*
* @property {object} $panel - store the jQuery object for the panel
*
* @property {object} keys - keycodes needed for event handlers
*
* @property {array} $tabs - Array of panel tabs.
*
* @property {array} $panels - Array of panels.
*/



OAA_EXAMPLES.tabpanel = function(id, accordian) {

	// define the class properties
	
	this.panel_id = id;
	this.accordian = accordian; 
	this.$panel = $('#' + id); 
	this.keys = new OAA_EXAMPLES.keyCodes(); 
	this.$tabs = this.$panel.find('.tab');
	this.$panels = this.$panel.children('.panel');

	// Bind event handlers
	this.bindHandlers();

	// Initialize the tab panel
	this.init();

} // end tabpanel() constructor

/**
* @method init
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to initialize the tab/accordian panel. Hides all panels. If a tab
* has the class 'selected', makes that panel visible; otherwise, makes first panel visible.
*
* @return {N/A}
*/

OAA_EXAMPLES.tabpanel.prototype.init = function() {
	var $tab; // the selected tab - if one is selected

	// add aria attributes to the panels
	this.$panels.attr('aria-hidden', 'true');

	// hide all the panels
	this.$panels.hide();

	// get the selected tab
	$tab = this.$tabs.filter('.selected');

	if ($tab == undefined) {
		$tab = this.$tabs.first();
		$tab.addClass('selected');
	}

	// show the panel that the selected tab controls and set aria-hidden to false
	this.$panel.find('#' + $tab.attr('aria-controls')).show().attr('aria-hidden', 'false');

} // end init()

/**
* @method switchTabs
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to give focus to a new tab or accordian header. If it's
* a tab panel, the currently displayed panel is hidden and the panel
* associated with the new tab is displayed.
*
* @param {object} $curTab - the jQuery object of the currently selected tab
*
* @param {object} $newTab - the jQuery object of new tab to switch to
*
* @return {N/A}
*/

OAA_EXAMPLES.tabpanel.prototype.switchTabs = function($curTab, $newTab) {

	// Remove the highlighting from the current tab
	$curTab.removeClass('selected focus');

	// remove tab from the tab order and update its aria-selected attribute
	$curTab.attr('tabindex', '-1').attr('aria-selected', 'false');

	
	// Highlight the new tab and update its aria-selected attribute
	$newTab.addClass('selected').attr('aria-selected', 'true');

	// If this is a tab panel, swap displayed tabs
	if (this.accordian == false) {
		// hide the current tab panel and set aria-hidden to true
		this.$panel.find('#' + $curTab.attr('aria-controls')).hide().attr('aria-hidden', 'true');

      // update the aria-expanded attribute for the old tab
      $curTab.attr('aria-expanded', 'false');

		// show the new tab panel and set aria-hidden to false
		this.$panel.find('#' + $newTab.attr('aria-controls')).show().attr('aria-hidden', 'false');

      // update the aria-expanded attribute for the new tab
      $newTab.attr('aria-expanded', 'true');

		// get new list of focusable elements
		this.$focusable.length = 0;
        	this.$panels.find(':focusable');
	}

	// Make new tab navigable
	$newTab.attr('tabindex', '0');

	// give the new tab focus
	$newTab.focus();

} // end switchTabs()

/**
* @method togglePanel
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to display or hide the panel associated with an accordian
* header. Function also binds a keydown handler to the focusable items
* in the panel when expanding and unbinds the handlers when collapsing.
*
* @param {object} $tab - the jQuery object of the currently selected tab
*
* @return {N/A}
*/

OAA_EXAMPLES.tabpanel.prototype.togglePanel = function($tab) {

	$panel = this.$panel.find('#' + $tab.attr('aria-controls'));

	if ($panel.attr('aria-hidden') == 'true') {
		$panel.attr('aria-hidden', 'false');
		$panel.slideDown(100);
		$tab.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/expanded.gif').attr('alt', 'expanded');

      // update the aria-expanded attribute
      $tab.attr('aria-expanded', 'true');
	}
	else {
		$panel.attr('aria-hidden', 'true');
		$panel.slideUp(100);
		$tab.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/contracted.gif').attr('alt', 'collapsed');

      // update the aria-expanded attribute
      $tab.attr('aria-expanded', 'false');
	}

} // end togglePanel()

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers for the tabs
*
* @return {N/A}
*/

OAA_EXAMPLES.tabpanel.prototype.bindHandlers = function() {

	var thisObj = this; // Store the this pointer for reference

	//////////////////////////////
	// Bind handlers for the tabs / accordian headers

	// bind a tab keydown handler
	this.$tabs.keydown(function(e) {
		return thisObj.handleTabKeyDown($(this), e);
	});

	// bind a tab keypress handler
	this.$tabs.keypress(function(e) {
		return thisObj.handleTabKeyPress($(this), e);
	});

	// bind a tab click handler
	this.$tabs.click(function(e) {
		return thisObj.handleTabClick($(this), e);
	});

	// bind a tab focus handler
	this.$tabs.focus(function(e) {
		return thisObj.handleTabFocus($(this), e);
	});

	// bind a tab blur handler
	this.$tabs.blur(function(e) {
		return thisObj.handleTabBlur($(this), e);
	});

	/////////////////////////////
	// Bind handlers for the panels
	
	// bind a keydown handlers for the panel focusable elements
	this.$panels.keydown(function(e) {
		return thisObj.handlePanelKeyDown($(this), e);
	});

	// bind a keypress handler for the panel
	this.$panels.keypress(function(e) {
		return thisObj.handlePanelKeyPress($(this), e);
	});

   // bind a panel click handler
	this.$panels.click(function(e) {
		return thisObj.handlePanelClick($(this), e);
	});

} // end bindHandlers()

/**
* @method handleTabKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for a tab
*
* @param {object} $tab - the jquery object of the tab being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true if propagating; false if consuming event
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabKeyDown = function($tab, e) {

	if (e.altKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
		case this.keys.enter:
		case this.keys.space: {

			// Only process if this is an accordian widget
			if (this.accordian == true) {
				// display or collapse the panel
				this.togglePanel($tab);

				e.stopPropagation();
				return false;
			}

			return true;
		}
		case this.keys.left:
		case this.keys.up: {

			var thisObj = this;
			var $prevTab; // holds jQuery object of tab from previous pass
			var $newTab; // the new tab to switch to

			if (e.ctrlKey) {
				// Ctrl+arrow moves focus from panel content to the open
				// tab/accordian header.
			}
			else {
				var curNdx = this.$tabs.index($tab);

				if (curNdx == 0) {
					// tab is the first one:
					// set newTab to last tab
					$newTab = this.$tabs.last();
				}
				else {
					// set newTab to previous
					$newTab = this.$tabs.eq(curNdx - 1);
				}

				// switch to the new tab
				this.switchTabs($tab, $newTab);
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.right:
		case this.keys.down: {

			var thisObj = this;
			var foundTab = false; // set to true when current tab found in array
			var $newTab; // the new tab to switch to

			var curNdx = this.$tabs.index($tab);

			if (curNdx == this.$tabs.length-1) {
				// tab is the last one:
				// set newTab to first tab
				$newTab = this.$tabs.first();
			}
			else {
				// set newTab to next tab
				$newTab = this.$tabs.eq(curNdx + 1);
			}

			// switch to the new tab
			this.switchTabs($tab, $newTab);

			e.stopPropagation();
			return false;
		}
		case this.keys.home: {

			// switch to the first tab
			this.switchTabs($tab, this.$tabs.first());

			e.stopPropagation();
			return false;
		}
		case this.keys.end: {

			// switch to the last tab
			this.switchTabs($tab, this.$tabs.last());

			e.stopPropagation();
			return false;
		}
	}
} // end handleTabKeyDown()

/**
* @method handleTabKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for a tab.
*
* @param {object} $tab - the jquery object of the tab being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true if propagating; false if consuming event
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabKeyPress = function($tab, e) {

	if (e.altKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
		case this.keys.enter:
		case this.keys.space:
		case this.keys.left:
		case this.keys.up:
		case this.keys.right:
		case this.keys.down:
		case this.keys.home:
		case this.keys.end: {
			e.stopPropagation();
			return false;
		}
		case this.keys.pageup:
		case this.keys.pagedown: {

			// The tab keypress handler must consume pageup and pagedown
			// keypresses to prevent Firefox from switching tabs
			// on ctrl+pageup and ctrl+pagedown

			if (!e.ctrlKey) {
				return true;
			}

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleTabKeyPress()

/**
* @method handleTabClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events for tabs
*
* @param {object} $tab - the jQuery object of the tab being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabClick = function($tab, e) {

	// make clicked tab navigable
	$tab.attr('tabindex', '0').attr('aria-selected', 'true').addClass('selected');

	// remove all tabs from the tab order and update their aria-selected attribute
	this.$tabs.not($tab).attr('tabindex', '-1').attr('aria-selected', 'false').removeClass('selected');

	// Expand the new panel
	this.togglePanel($tab);

	e.stopPropagation();
	return false;

} // end handleTabClick()

/**
* @method handleTabFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process focus events for tabs
*
* @param {object} $tab - the jQuery object of the tab being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabFocus = function($tab, e) {

	// Add the focus class to the tab
	$tab.addClass('focus');

	return true;

} // end handleTabFocus()

/**
* @method handleTabBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process blur events for tabs
*
* @param {object} $tab - the jQuery object of the tab being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabBlur = function($tab, e) {

	// Remove the focus class to the tab
	$tab.removeClass('focus');

	return true;

} // end handleTabBlur()


// Panel Event handlers

/**
* @method handlePanelKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for a panel
*
* @param {object} $panel - the jquery object of the panel being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true if propagating; false if consuming event
*/

OAA_EXAMPLES.tabpanel.prototype.handlePanelKeyDown = function($panel, e) {

	if (e.altKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
		case this.keys.tab: {
			var $focusable = $panel.find(':focusable');
			var curNdx = $focusable.index($(e.target));
			var panelNdx = this.$panels.index($panel);
			var numPanels = this.$panels.length

			if (e.shiftKey) {
				// if this is the first focusable item in the panel
				// find the preceding expanded panel (if any) that has
				// focusable items and set focus to the last one in that
				// panel. If there is no preceding panel or no focusable items
				// do not process.
				if (curNdx == 0 && panelNdx > 0) {

					// Iterate through previous panels until we find one that
					// is expanded and has focusable elements
					//
					for (var ndx = panelNdx - 1; ndx >= 0; ndx--) {

						var $prevPanel = this.$panels.eq(ndx);
                  var $prevTab = $('#' + $prevPanel.attr('aria-labelledby'));

						// get the focusable items in the panel
						$focusable.length = 0;
						$focusable = $prevPanel.find(':focusable');

						if ($focusable.length > 0) {
							// there are focusable items in the panel.
							// Set focus to the last item.
							$focusable.last().focus();

                     // reset the aria-selected state of the tabs
                     this.$tabs.attr('aria-selected', 'false').removeClass('selected');

                     // set the associated tab's aria-selected state
                     $prevTab.attr('aria-selected', 'true').addClass('selected');

							e.stopPropagation;
							return false;
						}
					}
				}
			}
			else if (panelNdx < numPanels) {

				// if this is the last focusable item in the panel
				// find the nearest following expanded panel (if any) that has
				// focusable items and set focus to the first one in that
				// panel. If there is no preceding panel or no focusable items
				// do not process.
				if (curNdx == $focusable.length - 1) {

					// Iterate through following panels until we find one that
					// is expanded and has focusable elements
					//
					for (var ndx = panelNdx + 1; ndx < numPanels; ndx++) {

						var $nextPanel = this.$panels.eq(ndx);
                  var $nextTab = $('#' + $nextPanel.attr('aria-labelledby'));

						// get the focusable items in the panel
						$focusable.length = 0;
						$focusable = $nextPanel.find(':focusable');

						if ($focusable.length > 0) {
							// there are focusable items in the panel.
							// Set focus to the first item.
							$focusable.first().focus();

                     // reset the aria-selected state of the tabs
                     this.$tabs.attr('aria-selected', 'false').removeClass('selected');

                     // set the associated tab's aria-selected state
                     $nextTab.attr('aria-selected', 'true').addClass('selected');

							e.stopPropagation;
							return false;
						}
					}
				}
			}

			break;
		}
		case this.keys.left:
		case this.keys.up: {

			if (!e.ctrlKey) {
				// do not process
				return true;
			}
	
			// get the jQuery object of the tab
			var $tab = $('#' + $panel.attr('aria-labelledby'));

			// Move focus to the tab
			$tab.focus();

			e.stopPropagation();
			return false;
		}
		case this.keys.pageup: {

			var $newTab;

			if (!e.ctrlKey) {
				// do not process
				return true;
			}

			// get the jQuery object of the tab
			var $tab = this.$tabs.filter('.selected');

			// get the index of the tab in the tab list
			var curNdx = this.$tabs.index($tab);

			if (curNdx == 0) {
				// this is the first tab, set focus on the last one
				$newTab = this.$tabs.last();
			}
			else {
				// set focus on the previous tab
				$newTab = this.$tabs.eq(curNdx - 1);
			}

			// switch to the new tab
			this.switchTabs($tab, $newTab);

			e.stopPropagation();
			e.preventDefault();
			return false;
		}
		case this.keys.pagedown: {

			var $newTab;

			if (!e.ctrlKey) {
				// do not process
				return true;
			}

			// get the jQuery object of the tab
			var $tab = $('#' + $panel.attr('aria-labelledby'));

			// get the index of the tab in the tab list
			var curNdx = this.$tabs.index($tab);

			if (curNdx == this.$tabs.length-1) {
				// this is the last tab, set focus on the first one
				$newTab = this.$tabs.first();
			}
			else {
				// set focus on the next tab
				$newTab = this.$tabs.eq(curNdx + 1);
			}

			// switch to the new tab
			this.switchTabs($tab, $newTab);

			e.stopPropagation();
			e.preventDefault();
			return false;
		}
	}

	return true;

} // end handlePanelKeyDown()

/**
* @method handlePanelKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for a panel
*
* @param {object} $panel - the jquery object of the panel being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true if propagating; false if consuming event
*/

OAA_EXAMPLES.tabpanel.prototype.handlePanelKeyPress = function($panel, e) {

	if (e.altKey) {
		// do nothing
		return true;
	}

	if (e.ctrlKey && (e.keyCode == this.keys.pageup || e.keyCode == this.keys.pagedown)) {
			e.stopPropagation();
			e.preventDefault();
			return false;
	}

	switch (e.keyCode) {
		case this.keys.esc: {
			e.stopPropagation();
			e.preventDefault();
			return false;
		}
	}

	return true;

} // end handlePanelKeyPress()

/**
* @method handlePanelClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events for panels
*
* @param {object} $panel - the jQuery object of the panel being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.tabpanel.prototype.handlePanelClick = function($panel, e) {

   var $tab = $('#' + $panel.attr('aria-labelledby'));

	// make clicked panel's tab navigable
	$tab.attr('tabindex', '0').attr('aria-selected', 'true').addClass('selected');

	// remove all tabs from the tab order and update their aria-selected attribute
	this.$tabs.not($tab).attr('tabindex', '-1').attr('aria-selected', 'false').removeClass('selected');

	return true;

} // end handlePanelClick()

// focusable is a small jQuery extension to add a :focusable selector. It is used to
// get a list of all focusable elements in a panel. Credit to ajpiano on the jQuery forums.

$.extend($.expr[':'], {
	focusable: function(element) {
		var nodeName = element.nodeName.toLowerCase();
		var tabIndex = $(element).attr('tabindex');

		// the element and all of its ancestors must be visible
		if (($(element)[(nodeName == 'area' ? 'parents' : 'closest')](':hidden').length) == true) {
			return false;
		}

		// If tabindex is defined, its value must be greater than 0
		if (!isNaN(tabIndex) && tabIndex < 0) {
			return false;
		}

		// if the element is a standard form control, it must not be disabled
		if (/input|select|textarea|button|object/.test(nodeName) == true) {

	       		return !element.disabled;
		}

		// if the element is a link, href must be defined
		if ((nodeName == 'a' ||  nodeName == 'area') == true) {

			return (element.href.length > 0);
		}
		    	   
		// this is some other page element that is not normally focusable.
		return false;
	}
});
"""

example_obj.style       = """
.tabpanel {
	margin: 20px;
	padding: 0;
}
.tablist {
	margin: 0 0px;
	padding: 0;
	list-style: none;
}

.tab {
	margin: .2em 1px 0 0;
	padding: 10px;
	height: 1em;
	font-weight: bold;
	background-color: #ec9;

	border: 1px solid black;
	-webkit-border-radius-topright: 5px;
	-webkit-border-radius-topleft: 5px;
	-moz-border-radius-topright: 5px;
	-moz-border-radius-topleft: 5px;
	border-radius-topright: 5px;
	border-radius-topleft: 5px;

	float: left;
}

.panel {
	clear: both;
	margin: 0 0 0 0;
	padding: 10px;
	width: 600px;
	border: 1px solid black;

	-webkit-border-radius-topright: 10px;
	-webkit-border-radius-bottomleft: 10px;
	-webkit-border-radius-bottomright: 10px;
	-moz-border-radius-topright: 10px;
	-moz-border-radius-bottomleft: 10px;
	-moz-border-radius-bottomright: 10px;
	border-radius-topright: 10px;
	border-radius-bottomleft: 10px;
	border-radius-bottomright: 10px;
}

ul.controlList {
	list-style-type: none;
}

h3.selected {
	background-color: #fc5;
}

.focus {
	color: black;
	border-top: 2px solid black;
	border-bottom: 2px solid black;
	background-color: #fff !important;
	margin-top: 0;
}

.accordian {
	margin: 0;
	float: none;
	-webkit-border-radius: 0;
	-moz-border-radius: 0;
	border-radius: 0;
	width: 600px;
}

.hidden {
	position: absolute;
	left: -300em;
	top: -30em;
}
"""

example2 = create_example(example_obj)

# =============================
# Example 3
# =============================

order +=  1

example_obj             = example_object()
example_obj.example_id = 36
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order =order
example_obj.title       = 'Tab Panel: ARIA CSS Selectors'
example_obj.permanent_slug = 'tabpanel2'

example_obj.a11y_features = """
Simple example of a tab Panel widget which used ARIA css selectors.
"""
example_obj.keyboard    = """

The following keyboard shortcuts are implemented for this example (based on recommended shortcuts specified by the "DHTML Style Guide Working Group":http://dev.aol.com/dhtml_style_guide/:


If focus is on a tab button:

    * Left / Up Arrow: Show the previous tab
    * Right / Down Arrow: Show the next tab
    * Home: Show the first tab
    * End: Show the last tab


If focus is on an element in a tab panel:

    * Control + Up Arrow/Left Arrow: Set focus on the tab button for the currently displayed tab.
    * Control + Page Up: Show the previous tab and set focus on its corresponding tab button. Shows the last tab in the panel if current tab is the first one.
    * Control + Page Down: Show the next tab and set focus on its corresponding tab button. Shows the first tab in the panel if current tab is the last one.

*NOTE:* Google Chrome does not propagate Control+ Page Up or Control+ Page Down to the web page when multiple tabs are open. This key combination will not function correctly in that case.
"""

example_obj.markup = [m1,m2,m3,m4,m5,m6,m7]

example_obj.html        = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<h2>Happy Time Pizza On-line Ordering System</h2>

<form>
<div id="tabpanel1" class="tabpanel">

	<ul class="tablist" role="tablist">
		<li id="tab1" class="tab" aria-controls="panel1" aria-selected="true" role="tab" tabindex="0">Crust</li>
		<li id="tab2" class="tab" aria-controls="panel2" role="tab" aria-selected="false" tabindex="-1">Veggies</li>
		<li id="tab3" class="tab" aria-controls="panel3" role="tab" aria-selected="false" tabindex="-1">Carnivore</li>
		<li id="tab4" class="tab" aria-controls="panel4" role="tab" aria-selected="false" tabindex="-1">Delivery</li>
	</ul>

	<div id="panel1" class="panel" aria-labelledby="tab1" role="tabpanel">
		<h3 tabindex="0">Select Crust</h3>
	   
        	<ul class="controlList">
	        	<li><input id="p1_opt1" type="radio" name="crust" value="crust1" /><label for="p1_opt1">Deep Dish</label></li>
	        	<li><input id="p1_opt2" type="radio" name="crust" value="crust2" checked="checked" /><label for="p1_opt2">Thick and cheesy</label></li>
	        	<li><input id="p1_opt3" type="radio" name="crust" value="crust3" /><label for="p1_opt3">Thick and spicy</label></li>
	        	<li><input id="p1_opt4" type="radio" name="crust" value="crust4" /><label for="p1_opt4">Thin</label></li>
	     	</ul>
	</div>

	<div id="panel2" class="panel" aria-labelledby="tab2" role="tabpanel">
		<h3 tabindex="0">Select Vegetables</h3>	
	   
	     	<ul class="controlList">
	        	<li><input id="p2_opt1" type="checkbox" name="veg" value="black olives" /><label for="p2_opt1">Black Olives</label></li>
	        	<li><input id="p2_opt2" type="checkbox" name="veg" value="green olives" /><label for="p2_opt2">Green Olives</label></li>
	        	<li><input id="p2_opt3" type="checkbox" name="veg" value="green peppers" /><label for="p2_opt3">Green Peppers</label></li>
	        	<li><input id="p2_opt4" type="checkbox" name="veg" value="mushrooms" /><label for="p2_opt4">Mushrooms</label></li>
	        	<li><input id="p2_opt5" type="checkbox" name="veg" value="onions" /><label for="p2_opt5">Onions</label></li>
	        	<li><input id="p2_opt6" type="checkbox" name="veg" value="pineapple" /><label for="p2_opt6">Pineapple</label></li>
	     	</ul>
	</div>

	<div id="panel3" class="panel" aria-labelledby="tab3" role="tabpanel">
		<h3 tabindex="0">Select Carnivore Options</h3>
	   
      		<ul class="controlList">
        		<li><input id="p3_opt1" type="checkbox" name="meat" value="pepperoni" /><label for="p3_opt1">Pepperoni</label></li>
        		<li><input id="p3_opt2" type="checkbox" name="meat" value="sausage" /><label for="p3_opt2">Italian Sausage</label></li>
        		<li><input id="p3_opt3" type="checkbox" name="meat" value="ham" /><label for="p3_opt3">Ham</label></li>
        		<li><input id="p3_opt4" type="checkbox" name="meat" value="hamburger" /><label for="p3_opt4">Hamburger</label></li>
      		</ul>
	</div>

	<div id="panel4" class="panel" aria-labelledby="tab4" role="tabpanel">
	 	<h3 tabindex="0">Select Delivery Method</h3>
	   
		<ul class="controlList">
			<li><input id="p4_opt1" type="radio" name="delivery" value="delivery1" checked="checked" /><label for="p4_opt1">Delivery</label></li>
			<li><input id="p4_opt2" type="radio" name="delivery" value="delivery2" /><label for="p4_opt2">Eat in</label></li>
			<li><input id="p4_opt3" type="radio" name="delivery" value="delivery3" /><label for="p4_opt3">Carry out</label></li>
			<li><input id="p4_opt4" type="radio" name="delivery" value="delivery4" /><label for="p4_opt4">Overnight mail</label></li>
		</ul>
	</div>
</div>
</form>

"""
example_obj.script      = """

var OAA_EXAMPLES = OAA_EXAMPLES || {};
$(document).ready(function() {

	var panel1 = new tabpanel("tabpanel1", false);
});


// keyCodes() is an object to contain keycodes needed for the application

OAA_EXAMPLES.keyCodes = function() {
	// Define values for keycodes
	this.tab        = 9;
	this.enter      = 13;
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
* @constructor tabpanel
*
* @memberOf OAA_EXAMPLES
*
* @desc a class constructor to create a ARIA-enabled tab panel widget.
* Usage: Requires a div container and children as follows:
*
*         1. tabs/accordian headers have class 'tab'
*
*         2. panels are divs with class 'panel'
*
* @param {string} id - the id of the div containing the tab panel.
*
* @param {boolean} accordian - true if the tab panel should operate
*         as an accordian; false if a tab panel
*
* @return {N/A}
*/

/**
* @constructor Internal Properties
*
* @property {string} id - store the id of the containing div
*
* @property {boolean} accordian - true if this is an accordian control
*
* @property {object} $panel - store the jQuery object for the panel
*
* @property {object} keys - keycodes needed for event handlers
*
* @property {array} $tabs - Array of panel tabs.
*
* @property {array} $panels - Array of panels.
*/

OAA_EXAMPLES.tabpanel = function(id, accordian) {

	// define the class properties
	
	this.panel_id = id;
	this.accordian = accordian;
	this.$panel = $('#' + id);
	this.keys = new OAA_EXAMPLES.keyCodes();
	this.$tabs = this.$panel.find('.tab');
	this.$panels = this.$panel.children('.panel');

	// Bind event handlers
	this.bindHandlers();

	// Initialize the tab panel
	this.init();

} // end tabpanel() constructor

/**
* @method init
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to initialize the tab/accordian panel. Hides all panels. If a tab
* has the class 'selected', makes that panel visible; otherwise, makes first panel visible.
*
* @return {N/A}
*/

OAA_EXAMPLES.tabpanel.prototype.init = function() {
	var $tab; // the selected tab - if one is selected

	// add aria attributes to the panels
	this.$panels.attr('aria-hidden', 'true');

	// get the selected tab
	$tab = this.$tabs.filter('[aria-selected="true"]');

	if ($tab == undefined) {
		$tab = this.$tabs.first();
	}

	// show the panel that the selected tab controls and set aria-hidden to false
	this.$panel.find('#' + $tab.attr('aria-controls')).attr('aria-hidden', 'false');

} // end init()

/**
* @method switchTabs
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to give focus to a new tab or accordian header.
* If it's a tab panel, the currently displayed panel is hidden and the panel associated * with the new tab is displayed.
*
* @param {object} $curTab - the jQuery object of the currently selected tab
*
* @param {object} $newTab - the jQuery object of new tab to switch to
*
* @return {N/A}
*/

OAA_EXAMPLES.tabpanel.prototype.switchTabs = function($curTab, $newTab) {

	// Remove the highlighting from the current tab
	$curTab.removeClass('focus');

	// remove tab from the tab order and update its aria-selected attribute
	$curTab.attr('tabindex', '-1').attr('aria-selected', 'false');

	// update the aria attributes
	
	// Highlight the new tab and update its aria-selected attribute
	$newTab.attr('aria-selected', 'true');

	// If this is a tab panel, swap displayed tabs
	if (this.accordian == false) {
		// hide the current tab panel and set aria-hidden to true
		this.$panel.find('#' + $curTab.attr('aria-controls')).attr('aria-hidden', 'true');

		// show the new tab panel and set aria-hidden to false
		this.$panel.find('#' + $newTab.attr('aria-controls')).attr('aria-hidden', 'false');
	}

	// Make new tab navigable
	$newTab.attr('tabindex', '0');

	// give the new tab focus
	$newTab.focus();

} // end switchTabs()

/**
* @method togglePanel
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to display or hide the panel associated with an accordian header
*
* @param {object} $tab - the jQuery object of the currently selected tab
*
* @return {N/A}
*/

OAA_EXAMPLES.tabpanel.prototype.togglePanel = function($tab) {

	$panel = this.$panel.find('#' + $tab.attr('aria-controls'));

	if ($panel.attr('aria-hidden') == 'true') {
		$panel.slideDown(100);
		$panel.attr('aria-hidden', 'false');
	}
	else {
		$panel.slideUp(100);
		$panel.attr('aria-hidden', 'true');
	}
} // end togglePanel()

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers for the tabs
*
* @return {N/A}
*/

OAA_EXAMPLES.tabpanel.prototype.bindHandlers = function() {

	var thisObj = this; // Store the this pointer for reference

	//////////////////////////////
	// Bind handlers for the tabs / accordian headers

	// bind a tab keydown handler
	this.$tabs.keydown(function(e) {
		return thisObj.handleTabKeyDown($(this), e);
	});

	// bind a tab keypress handler
	this.$tabs.keypress(function(e) {
		return thisObj.handleTabKeyPress($(this), e);
	});

	// bind a tab click handler
	this.$tabs.click(function(e) {
		return thisObj.handleTabClick($(this), e);
	});

	// bind a tab focus handler
	this.$tabs.focus(function(e) {
		return thisObj.handleTabFocus($(this), e);
	});

	// bind a tab blur handler
	this.$tabs.blur(function(e) {
		return thisObj.handleTabBlur($(this), e);
	});

	/////////////////////////////
	// Bind handlers for the panels
	
	// bind a keydown handlers for the panel focusable elements
	this.$panels.keydown(function(e) {
		return thisObj.handlePanelKeyDown($(this), e);
	});

	// bind a keypress handler for the panel
	this.$panels.keypress(function(e) {
		return thisObj.handlePanelKeyPress($(this), e);
	});

} // end bindHandlers()

/**
* @method handleTabKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for a tab
*
* @param {object} $tab - the jquery object of the tab being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true if propagating; false if consuming event
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabKeyDown = function($tab, e) {

	if (e.altKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
		case this.keys.enter:
		case this.keys.space: {

			// Only process if this is an accordian widget
			if (this.accordian == true) {
				// display or collapse the panel
				this.togglePanel($tab);

				e.stopPropagation();
				return false;
			}

			return true;
		}
		case this.keys.left:
		case this.keys.up: {

			var thisObj = this;
			var $prevTab; // holds jQuery object of tab from previous pass
			var $newTab; // the new tab to switch to

			if (e.ctrlKey) {
				// Ctrl+arrow moves focus from panel content to the open
				// tab/accordian header.
			}
			else {
				var curNdx = this.$tabs.index($tab);

				if (curNdx == 0) {
					// tab is the first one:
					// set newTab to last tab
					$newTab = this.$tabs.last();
				}
				else {
					// set newTab to previous
					$newTab = this.$tabs.eq(curNdx - 1);
				}

				// switch to the new tab
				this.switchTabs($tab, $newTab);
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.right:
		case this.keys.down: {

			var thisObj = this;
			var foundTab = false; // set to true when current tab found in array
			var $newTab; // the new tab to switch to

			var curNdx = this.$tabs.index($tab);

			if (curNdx == this.$tabs.length-1) {
				// tab is the last one:
				// set newTab to first tab
				$newTab = this.$tabs.first();
			}
			else {
				// set newTab to next tab
				$newTab = this.$tabs.eq(curNdx + 1);
			}

			// switch to the new tab
			this.switchTabs($tab, $newTab);

			e.stopPropagation();
			return false;
		}
		case this.keys.home: {

			// switch to the first tab
			this.switchTabs($tab, this.$tabs.first());

			e.stopPropagation();
			return false;
		}
		case this.keys.end: {

			// switch to the last tab
			this.switchTabs($tab, this.$tabs.last());

			e.stopPropagation();
			return false;
		}
	}
} // end handleTabKeyDown()

/**
* @method handleTabKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for a tab.
*
* @param {object} $tab - the jquery object of the tab being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true if propagating; false if consuming event
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabKeyPress = function($tab, e) {

	if (e.altKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
		case this.keys.enter:
		case this.keys.space:
		case this.keys.left:
		case this.keys.up:
		case this.keys.right:
		case this.keys.down:
		case this.keys.home:
		case this.keys.end: {
			e.stopPropagation();
			return false;
		}
		case this.keys.pageup:
		case this.keys.pagedown: {

			// The tab keypress handler must consume pageup and pagedown
			// keypresses to prevent Firefox from switching tabs
			// on ctrl+pageup and ctrl+pagedown

			if (!e.ctrlKey) {
				return true;
			}

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleTabKeyPress()

/**
* @method handleTabClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events for tabs
*
* @param {object} $tab - the jQuery object of the tab being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabClick = function($tab, e) {

   // hide the panels
   this.$panels.attr('aria-hidden', 'true');

	// remove all tabs from the tab order and reset their aria-selected attribute
	this.$tabs.attr('tabindex', '-1').attr('aria-selected', 'false');

	// Update the selected tab's aria-selected attribute
	$tab.attr('aria-selected', 'true');

	// show the clicked tab panel
	this.$panel.find('#' + $tab.attr('aria-controls')).attr('aria-hidden', 'false');

	// make clicked tab navigable
	$tab.attr('tabindex', '0');

	// give the tab focus
	$tab.focus();

	return true;

} // end handleTabClick()

/**
* @method handleTabFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process focus events for tabs
*
* @param {object} $tab - the jQuery object of the tab being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabFocus = function($tab, e) {

	// Add the focus class to the tab
	$tab.addClass('focus');

	return true;

} // end handleTabFocus()

/**
* @method handleTabBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process blur events for tabs
*
* @param {object} $tab - the jQuery object of the tab being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabBlur = function($tab, e) {

	// Remove the focus class to the tab
	$tab.removeClass('focus');

	return true;

} // end handleTabBlur()


// Panel Event handlers

/**
* @method handlePanelKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for a panel
*
* @param {object} $elem - the jquery object of the element being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true if propagating; false if consuming event
*/

OAA_EXAMPLES.tabpanel.prototype.handlePanelKeyDown = function($elem, e) {

	if (e.altKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
		case this.keys.esc: {
			e.stopPropagation();
			return false;
		}
		case this.keys.left:
		case this.keys.up: {

			if (!e.ctrlKey) {
				// do not process
				return true;
			}
	
			// get the jQuery object of the tab
			var $tab = $('#' + $elem.attr('aria-labelledby'));

			// Move focus to the tab
			$tab.focus();

			e.stopPropagation();
			return false;
		}
		case this.keys.pageup: {

			var $newTab;

			if (!e.ctrlKey) {
				// do not process
				return true;
			}

			// get the jQuery object of the tab
			var $tab = this.$tabs.filter('[aria-selected="true"]');

			// get the index of the tab in the tab list
			var curNdx = this.$tabs.index($tab);

			if (curNdx == 0) {
				// this is the first tab, set focus on the last one
				$newTab = this.$tabs.last();
			}
			else {
				// set focus on the previous tab
				$newTab = this.$tabs.eq(curNdx - 1);
			}

			// switch to the new tab
			this.switchTabs($tab, $newTab);

			e.stopPropagation();
			e.preventDefault();
			return false;
		}
		case this.keys.pagedown: {

			var $newTab;

			if (!e.ctrlKey) {
				// do not process
				return true;
			}

			// get the jQuery object of the tab
			var $tab = $('#' + $elem.attr('aria-labelledby'));

			// get the index of the tab in the tab list
			var curNdx = this.$tabs.index($tab);

			if (curNdx == this.$tabs.length-1) {
				// this is the last tab, set focus on the first one
				$newTab = this.$tabs.first();
			}
			else {
				// set focus on the next tab
				$newTab = this.$tabs.eq(curNdx + 1);
			}

			// switch to the new tab
			this.switchTabs($tab, $newTab);

			e.stopPropagation();
			e.preventDefault();
			return false;
		}
	}

	return true;

} // end handlePanelKeyDown()

/**
* @method handlePanelKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for a panel
*
* @param {object} $elem - the jquery object of the element being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true if propagating; false if consuming event
*/

OAA_EXAMPLES.tabpanel.prototype.handlePanelKeyPress = function($elem, e) {

	if (e.altKey) {
		// do nothing
		return true;
	}

	if (e.ctrlKey && (e.keyCode == this.keys.pageup || e.keyCode == this.keys.pagedown)) {
			e.stopPropagation();
			e.preventDefault();
			return false;
	}

	switch (e.keyCode) {
		case this.keys.esc: {
			e.stopPropagation();
			e.preventDefault();
			return false;
		}
	}

	return true;

} // end handlePanelKeyPress()

// focusable is a small jQuery extension to add a :focusable selector. It is used to
// get a list of all focusable elements in a panel. Credit to ajpiano on the jQuery forums.

$.extend($.expr[':'], {
	focusable: function(element) {
		var nodeName = element.nodeName.toLowerCase();
		var tabIndex = $(element).attr('tabindex');

		// the element and all of its ancestors must be visible
		if (($(element)[nodeName == 'area' ? 'parents' : 'closest'](':hidden').length) == true) {
			return false;
		}

		// If tabindex is defined, its value must be greater than 0
		if (!isNaN(tabIndex) && tabIndex < 0) {
			return false;
		}

		// if the element is a standard form control, it must not be disabled
		if (/input|select|textarea|button|object/.test(nodeName) == true) {

	       		return !element.disabled;
		}

		// if the element is a link, href must be defined
		if ((nodeName == 'a' ||  nodeName == 'area') == true) {

			return (element.href.length > 0);
		}
		    	   
		// this is some other page element that is not normally focusable.
		return false;
	}
});
"""

example_obj.style       = """
.tabpanel {
	margin: 20px;
	padding: 0;
	height: 1%; /* IE fix for float bug */
}
.tablist {
	margin: 0 0px;
	padding: 0;
	list-style: none;
}

.tab {

	margin: .2em 1px 0 0;
	padding: 10px;
	height: 1em;
	font-weight: bold;
	background-color: #ec9;

	border: 1px solid black;
	-webkit-border-radius-topright: 5px;
	-webkit-border-radius-topleft: 5px;
	-moz-border-radius-topright: 5px;
	-moz-border-radius-topleft: 5px;
	border-radius-topright: 5px;
	border-radius-topleft: 5px;

	float: left;
	display: inline; /* IE float bug fix */
}

.panel {
	clear: both;
	display: block;
	margin: 0 0 0 0;
	padding: 10px;
	width: 600px;
	border: 1px solid black;

	-webkit-border-radius-topright: 10px;
	-webkit-border-radius-bottomleft: 10px;
	-webkit-border-radius-bottomright: 10px;
	-moz-border-radius-topright: 10px;
	-moz-border-radius-bottomleft: 10px;
	-moz-border-radius-bottomright: 10px;
	border-radius-topright: 10px;
	border-radius-bottomleft: 10px;
	border-radius-bottomright: 10px;
}

ul.controlList {
	list-style-type: none;
}

li[aria-selected='true'] {
	color: black;
	background-color: #fff;
	border-bottom: 1px solid white;
}

div[aria-hidden='true'] {
   display: none;
}

.focus {
	margin-top: 0;
	height: 1.2em;
}

.accordian {
	margin: 0;
	float: none;
	-webkit-border-radius: 0;
	-moz-border-radius: 0;
	border-radius: 0;
	width: 600px;
}

.hidden {
	position: absolute;
	left: -300em;
	top: -30em;
}
"""

example3 = create_example(example_obj)

# =============================
# Example 4
# =============================

order += 1

example_obj             = example_object()
example_obj.example_id = 37
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order       = order
example_obj.title       = 'Tab Panel: Accordian using ARIA CSS selectors'
example_obj.permanent_slug = 'accordian2'

example_obj.a11y_features = """
Simple example of a tab panel accordian widget using ARIA CSS selectors.
"""
example_obj.keyboard    = """

The following keyboard shortcuts are implemented for this example (based on recommended shortcuts specified by the "DHTML Style Guide Working Group":http://dev.aol.com/dhtml_style_guide/ :


If focus is on a tab button:

    * Left / Up Arrow: Show the previous tab
    * Right / Down Arrow: Show the next tab
    * Home: Show the first tab
    * End: Show the last tab
    * Enter/Space: Expand / Collapse panel


If focus is on an element in a tab panel:

    * Control + Up Arrow/Left Arrow: Set focus on the tab button for the currently displayed tab.
    * Control + Page Up: Show the previous tab and set focus on its corresponding tab button. Shows the last tab in the panel if current tab is the first one.
    * Control + Page Down: Show the next tab and set focus on its corresponding tab button. Shows the first tab in the panel if current tab is the last one.
    * Tab: Move focus to next focusable element in panel. If focus is on last focusable element, move focus to first focusable element of next expanded panel or, if no more expanded panels or focusable elements, to first focusable element following tab panel in the page.
    * Shift+Tab: The reverse of Tab.


*NOTE:* Google Chrome does not propagate Control+ Page Up or Control+ Page Down to the web page when multiple tabs are open. This key combination will not function correctly in that case.
"""

example_obj.markup = [m1,m2,m3,m4,m5,m6,m7,m8,m9]

example_obj.html        = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<h2>Happy Time Pizza On-line Ordering System</h2>

<form>
<div id="accordian1" class="tabpanel" role="tablist" multiselectable="true">

	<h3 id="tab1" class="tab accordian" aria-selected="true" aria-controls="panel1" aria-expanded="true" role="tab" tabindex="0">
		<img src="{{EXAMPLE_MEDIA}}images/expanded.gif" alt="expanded" />
		Crust
	</h3>

	<div id="panel1" class="panel accordian" aria-labelledby="tab1" aria-hidden="false" role="tabpanel">
		<h3 tabindex="0">Select Crust</h3>
	   
        	<ul class="controlList">
	        	<li><input id="p1_opt1" type="radio" name="crust" value="crust1" /><label for="p1_opt1">Deep Dish</label></li>
	        	<li><input id="p1_opt2" type="radio" name="crust" value="crust2" checked="checked" /><label for="p1_opt2">Thick and cheesy</label></li>
	        	<li><input id="p1_opt3" type="radio" name="crust" value="crust3" /><label for="p1_opt3">Thick and spicy</label></li>
	        	<li><input id="p1_opt4" type="radio" name="crust" value="crust4" /><label for="p1_opt4">Thin</label></li>
	     	</ul>
	</div>

	<h3 id="tab2" class="tab accordian" aria-selected="false" aria-controls="panel2" aria-expanded="false" role="tab" tabindex="-1">
		<img src="{{EXAMPLE_MEDIA}}images/contracted.gif" alt="collapsed" />
		Veggies
	</h3>
	<div id="panel2" class="panel accordian" aria-labelledby="tab2" aria-hidden="true" role="tabpanel">
		<h3 tabindex="0">Select Vegetables</h3>	
	   
	     	<ul class="controlList">
	        	<li><input id="p2_opt1" type="checkbox" name="veg" value="black olives" /><label for="p2_opt1">Black Olives</label></li>
	        	<li><input id="p2_opt2" type="checkbox" name="veg" value="green olives" /><label for="p2_opt2">Green Olives</label></li>
	        	<li><input id="p2_opt3" type="checkbox" name="veg" value="green peppers" /><label for="p2_opt3">Green Peppers</label></li>
	        	<li><input id="p2_opt4" type="checkbox" name="veg" value="mushrooms" /><label for="p2_opt4">Mushrooms</label></li>
	        	<li><input id="p2_opt5" type="checkbox" name="veg" value="onions" /><label for="p2_opt5">Onions</label></li>
	        	<li><input id="p2_opt6" type="checkbox" name="veg" value="pineapple" /><label for="p2_opt6">Pineapple</label></li>
	     	</ul>
	</div>

	<h3 id="tab3" class="tab accordian" aria-selected="false" aria-controls="panel3" aria-expanded="false" role="tab" tabindex="-1">
		<img src="{{EXAMPLE_MEDIA}}images/contracted.gif" alt="collapsed" />
		Carnivore
	</h3>
	<div id="panel3" class="panel accordian" aria-labelledby="tab3" aria-hidden="true" role="tabpanel">
		<h3 tabindex="0">Select Carnivore Options</h3>
	   
      		<ul class="controlList">
        		<li><input id="p3_opt1" type="checkbox" name="meat" value="pepperoni" /><label for="p3_opt1">Pepperoni</label></li>
        		<li><input id="p3_opt2" type="checkbox" name="meat" value="sausage" /><label for="p3_opt2">Italian Sausage</label></li>
        		<li><input id="p3_opt3" type="checkbox" name="meat" value="ham" /><label for="p3_opt3">Ham</label></li>
        		<li><input id="p3_opt4" type="checkbox" name="meat" value="hamburger" /><label for="p3_opt4">Hamburger</label></li>
      		</ul>
	</div>

	<h3 id="tab4" class="tab accordian" aria-selected="false" aria-controls="panel4" aria-expanded="false" role="tab" tabindex="-1">
		<img src="{{EXAMPLE_MEDIA}}images/contracted.gif" alt="collapsed" />
		Delivery
	</h3>
	<div id="panel4" class="panel accordian" aria-labelledby="tab4" aria-hidden="true" role="tabpanel">
	 	<h3 tabindex="0">Select Delivery Method</h3>
	   
		<ul class="controlList">
			<li><input id="p4_opt1" type="radio" name="delivery" value="delivery1" checked="checked" /><label for="p4_opt1">Delivery</label></li>
			<li><input id="p4_opt2" type="radio" name="delivery" value="delivery2" /><label for="p4_opt2">Eat in</label></li>
			<li><input id="p4_opt3" type="radio" name="delivery" value="delivery3" /><label for="p4_opt3">Carry out</label></li>
			<li><input id="p4_opt4" type="radio" name="delivery" value="delivery4" /><label for="p4_opt4">Overnight mail</label></li>
		</ul>
	</div>
</div>
</form>

"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};
$(document).ready(function() {

	var panel1 = new OAA_EXAMPLES.tabpanel("accordian1", true);
});


// keyCodes() is an object to contain keycodes needed for the application

OAA_EXAMPLES.keyCodes = function() {
	// Define values for keycodes
	this.tab        = 9;
	this.enter      = 13;
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
* @constructor tabpanel
*
* @memberOf OAA_EXAMPLES
*
* @desc a class constructor to create a ARIA-enabled tab panel widget.
*  	  Usage: Requires a div container and children as follows:
*
*         1. tabs/accordian headers have class 'tab'
*
*         2. panels are divs with class 'panel'
*
* @param {string} id - the id of the div containing the tab panel.
*
* @param {boolean} accordian - true if the tab panel should operate
*         as an accordian; false if a tab panel
*
* @return {N/A}
*/

/**
* @constructor Internal Properties
*
* @memberOf OAA_EXAMPLES
*
* @property {string} id - store the id of the containing div
*

* @property {boolean} accordian - true if this is an accordian control
*
* @property {object} $panel - store the jQuery object for the panel
*
* @property {object} keys - keycodes needed for event handlers
*
* @property {array} $tabs - Array of panel tabs.
*
* @property {array} $panels - Array of panel tabs.
*/

OAA_EXAMPLES.tabpanel = function(id, accordian) {

	// define the class properties
	
	this.panel_id = id; 
	this.accordian = accordian; 
	this.$panel = $('#' + id);  
	this.keys = new OAA_EXAMPLES.keyCodes();
	this.$tabs = this.$panel.find('.tab'); 
	this.$panels = this.$panel.children('.panel'); 

	// Bind event handlers
	this.bindHandlers();

	// Initialize the tab panel
	this.init();

} // end tabpanel() constructor

/**
* @method init
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to initialize the tab/accordian panel. Hides all panels. If a tab's
* aria-selected attribute is true, makes that panel visible; otherwise, makes first panel visible.
*
* @return {N/A}
*/

OAA_EXAMPLES.tabpanel.prototype.init = function() {
	var $tab; // the selected tab - if one is selected

	// add aria attributes to the panels
	this.$panels.attr('aria-hidden', 'true');

	// get the selected tab
	$tab = this.$tabs.filter('[aria-selected="true"]');

	if ($tab == undefined) {
		$tab = this.$tabs.first();
	}

	// show the panel that the selected tab controls and set aria-hidden to false
	this.$panel.find('#' + $tab.attr('aria-controls')).attr('aria-hidden', 'false');

} // end init()

/**
* @method switchTabs
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to give focus to a new tab or accordian header.
* If it's a tab panel, the currently displayed panel is hidden and the panel
* associated with the new tab is displayed.
*
* @param {object} $curTab - the jQuery object of the currently selected tab
*
* @param {object} $newTab - the jQuery object of new tab to switch to
*
* @return {N/A}
*/

OAA_EXAMPLES.tabpanel.prototype.switchTabs = function($curTab, $newTab) {

	// Remove the highlighting from the current tab
	$curTab.removeClass('focus');

	// remove tab from the tab order and update its aria-selected attribute
	$curTab.attr('tabindex', '-1').attr('aria-selected', 'false');

	
	// Highlight the new tab and update its aria-selected attribute
	$newTab.attr('aria-selected', 'true');

	// If activating new tab/panel, swap the displayed panels
	if (this.accordian == false) {
		// hide the current tab panel and set aria-hidden to true
		this.$panel.find('#' + $curTab.attr('aria-controls')).attr('aria-hidden', 'true');

      // update the aria-expanded attribute for the old tab
      $curTab.attr('aria-expanded', 'false');

      // show the new tab panel and set aria-hidden to false
      this.$panel.find('#' + $newTab.attr('aria-controls')).attr('aria-hidden', 'false');

      // update the aria-expanded attribute for the new tab
      $newTab.attr('aria-expanded', 'true');

   }

	// Make new tab navigable
	$newTab.attr('tabindex', '0');

	// give the new tab focus
	$newTab.focus();

} // end switchTabs()

/**
* @method togglePanel
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to display or hide the panel associated with an accordian
* header. Function also binds a keydown handler to the focusable items
* in the panel when expanding and unbinds the handlers when collapsing.
*
* @param {object} $tab - the jQuery object of the currently selected tab
*
* @return {N/A}
*/

OAA_EXAMPLES.tabpanel.prototype.togglePanel = function($tab) {

	$panel = this.$panel.find('#' + $tab.attr('aria-controls'));

	if ($panel.attr('aria-hidden') == 'true') {
		$panel.attr('aria-hidden', 'false');
		$tab.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/expanded.gif').attr('alt', 'expanded');

      // update the aria-expanded attribute
      $tab.attr('aria-expanded', 'true');
	}
	else {
		$panel.attr('aria-hidden', 'true');
		$panel.slideUp(100);
		$tab.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/contracted.gif').attr('alt', 'collapsed');

      // update the aria-expanded attribute
      $tab.attr('aria-expanded', 'false');
	}

} // end togglePanel()

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers for the tabs
*
* @return {N/A}
*/

OAA_EXAMPLES.tabpanel.prototype.bindHandlers = function() {

	var thisObj = this; // Store the this pointer for reference

	//////////////////////////////
	// Bind handlers for the tabs / accordian headers

	// bind a tab keydown handler
	this.$tabs.keydown(function(e) {
		return thisObj.handleTabKeyDown($(this), e);
	});

	// bind a tab keypress handler
	this.$tabs.keypress(function(e) {
		return thisObj.handleTabKeyPress($(this), e);
	});

	// bind a tab click handler
	this.$tabs.click(function(e) {
		return thisObj.handleTabClick($(this), e);
	});

	// bind a tab focus handler
	this.$tabs.focus(function(e) {
		return thisObj.handleTabFocus($(this), e);
	});

	// bind a tab blur handler
	this.$tabs.blur(function(e) {
		return thisObj.handleTabBlur($(this), e);
	});

	/////////////////////////////
	// Bind handlers for the panels
	
	// bind a keydown handlers for the panel focusable elements
	this.$panels.keydown(function(e) {
		return thisObj.handlePanelKeyDown($(this), e);
	});

	// bind a keypress handler for the panel
	this.$panels.keypress(function(e) {
		return thisObj.handlePanelKeyPress($(this), e);
	});

	// bind a panel click handler
	this.$panels.click(function(e) {
		return thisObj.handlePanelClick($(this), e);
	});

} // end bindHandlers()

/**
* @method handleTabKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for a tab
*
* @param {object} $tab - the jquery object of the tab being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true if propagating; false if consuming event
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabKeyDown = function($tab, e) {

	if (e.altKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
		case this.keys.enter:
		case this.keys.space: {

			// Only process if this is an accordian widget
			if (this.accordian == true) {
				// display or collapse the panel
				this.togglePanel($tab);

				e.stopPropagation();
				return false;
			}

			return true;
		}
		case this.keys.left:
		case this.keys.up: {

			var thisObj = this;
			var $prevTab; // holds jQuery object of tab from previous pass
			var $newTab; // the new tab to switch to

			if (e.ctrlKey) {
				// Ctrl+arrow moves focus from panel content to the open
				// tab/accordian header.
			}
			else {
				var curNdx = this.$tabs.index($tab);

				if (curNdx == 0) {
					// tab is the first one:
					// set newTab to last tab
					$newTab = this.$tabs.last();
				}
				else {
					// set newTab to previous
					$newTab = this.$tabs.eq(curNdx - 1);
				}

				// switch to the new tab
				this.switchTabs($tab, $newTab);
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.right:
		case this.keys.down: {

			var thisObj = this;
			var foundTab = false; // set to true when current tab found in array
			var $newTab; // the new tab to switch to

			var curNdx = this.$tabs.index($tab);

			if (curNdx == this.$tabs.length-1) {
				// tab is the last one:
				// set newTab to first tab
				$newTab = this.$tabs.first();
			}
			else {
				// set newTab to next tab
				$newTab = this.$tabs.eq(curNdx + 1);
			}

			// switch to the new tab
			this.switchTabs($tab, $newTab);

			e.stopPropagation();
			return false;
		}
		case this.keys.home: {

			// switch to the first tab
			this.switchTabs($tab, this.$tabs.first());

			e.stopPropagation();
			return false;
		}
		case this.keys.end: {

			// switch to the last tab
			this.switchTabs($tab, this.$tabs.last());

			e.stopPropagation();
			return false;
		}
	}
} // end handleTabKeyDown()

/**
* @method handleTabKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for a tab.
*
* @param {object} $tab - the jquery object of the tab being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true if propagating; false if consuming event
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabKeyPress = function($tab, e) {

	if (e.altKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
		case this.keys.enter:
		case this.keys.space:
		case this.keys.left:
		case this.keys.up:
		case this.keys.right:
		case this.keys.down:
		case this.keys.home:
		case this.keys.end: {
			e.stopPropagation();
			return false;
		}
		case this.keys.pageup:
		case this.keys.pagedown: {

			// The tab keypress handler must consume pageup and pagedown
			// keypresses to prevent Firefox from switching tabs
			// on ctrl+pageup and ctrl+pagedown

			if (!e.ctrlKey) {
				return true;
			}

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleTabKeyPress()

/**
* @method handleTabClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events for tabs
*
* @param {object} $tab - the jQuery object of the tab being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabClick = function($tab, e) {

	// make clicked tab navigable
	$tab.attr('tabindex', '0').attr('aria-selected', 'true');

	// remove all tabs from the tab order and update their aria-selected attribute
	this.$tabs.not($tab).attr('tabindex', '-1').attr('aria-selected', 'false');

	// Expand the new panel
	this.togglePanel($tab);

	e.stopPropagation();
	return false;

} // end handleTabClick()

/**
* @method handleTabFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process focus events for tabs
*
* @param {object} $tab - the jQuery object of the tab being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabFocus = function($tab, e) {

	// Add the focus class to the tab
	$tab.addClass('focus');

	return true;

} // end handleTabFocus()

/**
* @method handleTabBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process blur events for tabs
*
* @param {object} $tab - the jQuery object of the tab being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.tabpanel.prototype.handleTabBlur = function($tab, e) {

	// Remove the focus class to the tab
	$tab.removeClass('focus');

	return true;

} // end handleTabBlur()


// Panel Event handlers

/**
* @method handlePanelKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for a panel
*
* @param {object} $panel - the jquery object of the panel being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true if propagating; false if consuming event
*/

OAA_EXAMPLES.tabpanel.prototype.handlePanelKeyDown = function($panel, e) {

	if (e.altKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
		case this.keys.tab: {
			var $focusable = $panel.find(':focusable');
			var curNdx = $focusable.index($(e.target));
			var panelNdx = this.$panels.index($panel);
			var numPanels = this.$panels.length

			if (e.shiftKey) {
				// if this is the first focusable item in the panel
				// find the preceding expanded panel (if any) that has
				// focusable items and set focus to the last one in that
				// panel. If there is no preceding panel or no focusable items
				// do not process.
				if (curNdx == 0 && panelNdx > 0) {

					// Iterate through previous panels until we find one that
					// is expanded and has focusable elements
					//
					for (var ndx = panelNdx - 1; ndx >= 0; ndx--) {

						var $prevPanel = this.$panels.eq(ndx);
						var $prevTab = $('#' + $prevPanel.attr('aria-labelledby'));

						// get the focusable items in the panel
						$focusable.length = 0;
						$focusable = $prevPanel.find(':focusable');

						if ($focusable.length > 0) {
							// there are focusable items in the panel.
							// Set focus to the last item.
							$focusable.last().focus();

                     // Reset the aria-selected state of the tabs
                     this.$tabs.attr('aria-selected', 'false');

                     // Set that associated tab's aria-selected state to true
                     $prevTab.attr('aria-selected', 'true');

							e.stopPropagation;
							return false;
						}
					}
				}
			}
			else if (panelNdx < numPanels) {

				// if this is the last focusable item in the panel
				// find the nearest following expanded panel (if any) that has
				// focusable items and set focus to the first one in that
				// panel. If there is no preceding panel or no focusable items
				// do not process.
				if (curNdx == $focusable.length - 1) {

					// Iterate through following panels until we find one that
					// is expanded and has focusable elements
					//
					for (var ndx = panelNdx + 1; ndx < numPanels; ndx++) {

						var $nextPanel = this.$panels.eq(ndx);
						var $nextTab = $('#' + $nextPanel.attr('aria-labelledby'));

						// get the focusable items in the panel
						$focusable.length = 0;
						$focusable = $nextPanel.find(':focusable');

						if ($focusable.length > 0) {
							// there are focusable items in the panel.
							// Set focus to the first item.
							$focusable.first().focus();

                     // Reset the aria-selected state of the tabs
                     this.$tabs.attr('aria-selected', 'false');

                     // Set that associated tab's aria-selected state to true
                     $nextTab.attr('aria-selected', 'true');

							e.stopPropagation;
							return false;
						}
					}
				}
			}

			break;
		}
		case this.keys.left:
		case this.keys.up: {

			if (!e.ctrlKey) {
				// do not process
				return true;
			}
	
			// get the jQuery object of the tab
			var $tab = $('#' + $panel.attr('aria-labelledby'));

			// Move focus to the tab
			$tab.focus();

			e.stopPropagation();
			return false;
		}
		case this.keys.pageup: {

			var $newTab;

			if (!e.ctrlKey) {
				// do not process
				return true;
			}

			// get the jQuery object of the tab
			var $tab = this.$tabs.filter('[aria-selected="true"]');

			// get the index of the tab in the tab list
			var curNdx = this.$tabs.index($tab);

			if (curNdx == 0) {
				// this is the first tab, set focus on the last one
				$newTab = this.$tabs.last();
			}
			else {
				// set focus on the previous tab
				$newTab = this.$tabs.eq(curNdx - 1);
			}

			// switch to the new tab
			this.switchTabs($tab, $newTab);

			e.stopPropagation();
			e.preventDefault();
			return false;
		}
		case this.keys.pagedown: {

			var $newTab;

			if (!e.ctrlKey) {
				// do not process
				return true;
			}

			// get the jQuery object of the tab
			var $tab = $('#' + $panel.attr('aria-labelledby'));

			// get the index of the tab in the tab list
			var curNdx = this.$tabs.index($tab);

			if (curNdx == this.$tabs.length-1) {
				// this is the last tab, set focus on the first one
				$newTab = this.$tabs.first();
			}
			else {
				// set focus on the next tab
				$newTab = this.$tabs.eq(curNdx + 1);
			}

			// switch to the new tab
			this.switchTabs($tab, $newTab);

			e.stopPropagation();
			e.preventDefault();
			return false;
		}
	}

	return true;

} // end handlePanelKeyDown()

/**
* @method handlePanelKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for a panel
*
* @param {object} $panel - the jquery object of the panel being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true if propagating; false if consuming event
*/

OAA_EXAMPLES.tabpanel.prototype.handlePanelKeyPress = function($panel, e) {

	if (e.altKey) {
		// do nothing
		return true;
	}

	if (e.ctrlKey && (e.keyCode == this.keys.pageup || e.keyCode == this.keys.pagedown)) {
			e.stopPropagation();
			e.preventDefault();
			return false;
	}

	switch (e.keyCode) {
		case this.keys.esc: {
			e.stopPropagation();
			e.preventDefault();
			return false;
		}
	}

	return true;

} // end handlePanelKeyPress()

/**
* @method handlePanelClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events for panels
*
* @param {object} $panel - the jQuery object of the panel being processed
*
* @param {object} e - the associated event object
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.tabpanel.prototype.handlePanelClick = function($panel, e) {

   var $tab = $('#' + $panel.attr('aria-labelledby'));

	// make clicked panel's tab navigable
	$tab.attr('tabindex', '0').attr('aria-selected', 'true');

	// remove all tabs from the tab order and update their aria-selected attribute
	this.$tabs.not($tab).attr('tabindex', '-1').attr('aria-selected', 'false');

	return true;

} // end handlePanelClick()

// focusable is a small jQuery extension to add a :focusable selector. It is used to
// get a list of all focusable elements in a panel. Credit to ajpiano on the jQuery forums.
//
$.extend($.expr[':'], {
	focusable: function(element) {
		var nodeName = element.nodeName.toLowerCase();
		var tabIndex = $(element).attr('tabindex');

		// the element and all of its ancestors must be visible
		if (($(element)[(nodeName == 'area' ? 'parents' : 'closest')](':hidden').length) == true) {
			return false;
		}

		// If tabindex is defined, its value must be greater than 0
		if (!isNaN(tabIndex) && tabIndex < 0) {
			return false;
		}

		// if the element is a standard form control, it must not be disabled
		if (/input|select|textarea|button|object/.test(nodeName) == true) {

	       		return !element.disabled;
		}

		// if the element is a link, href must be defined
		if ((nodeName == 'a' ||  nodeName == 'area') == true) {

			return (element.href.length > 0);
		}
		    	   
		// this is some other page element that is not normally focusable.
		return false;
	}
});
"""

example_obj.style       = """
.tabpanel {
	margin: 20px;
	padding: 0;
}
.tablist {
	margin: 0 0px;
	padding: 0;
	list-style: none;
}

.tab {
	margin: .2em 1px 0 0;
	padding: 10px;
	height: 1em;
	font-weight: bold;
	background-color: #ec9;

	border: 1px solid black;
	-webkit-border-radius-topright: 5px;
	-webkit-border-radius-topleft: 5px;
	-moz-border-radius-topright: 5px;
	-moz-border-radius-topleft: 5px;
	border-radius-topright: 5px;
	border-radius-topleft: 5px;

	float: left;
}

.panel {
	clear: both;
	margin: 0 0 0 0;
	padding: 10px;
	width: 600px;
	border: 1px solid black;

	-webkit-border-radius-topright: 10px;
	-webkit-border-radius-bottomleft: 10px;
	-webkit-border-radius-bottomright: 10px;
	-moz-border-radius-topright: 10px;
	-moz-border-radius-bottomleft: 10px;
	-moz-border-radius-bottomright: 10px;
	border-radius-topright: 10px;
	border-radius-bottomleft: 10px;
	border-radius-bottomright: 10px;
}

ul.controlList {
	list-style-type: none;
}

h3[aria-selected="true"] {
	background-color: #fc5;
}

.focus {
	color: black;
	border-top: 2px solid black;
	border-bottom: 2px solid black;
	background-color: #fff !important;
	margin-top: 0;
}

div[aria-hidden="true"] {
   display: none;
}

.accordian {
	margin: 0;
	float: none;
	-webkit-border-radius: 0;
	-moz-border-radius: 0;
	border-radius: 0;
	width: 600px;
}

.hidden {
	position: absolute;
	left: -300em;
	top: -30em;
}
"""

example4 = create_example(example_obj)