"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples import *

order = 1

spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='application')
m2 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='button')
m3 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='toolbar')
m4 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-checked')
m5 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-describedby')
m6 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-labelledby')
m7 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-pressed')

# =============================
# Example 1
# =============================

example_obj             = example_object()
example_obj.example_id = 38
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order          = order
example_obj.title       = 'Toolbar using inline images for visual state'
example_obj.permanent_slug = 'toolbar1'

example_obj.a11y_features = """
Simple example of a toolbar widget using inline images to display the visual state of the buttons.
"""

example_obj.keyboard    = """

    * Tab: move between toolbar items.
    * Left and Right Arrows: move between button items.
    * Space: toggle <code>aria-pressed</code> state of currently focused button until key is released.

"""

example_obj.markup = [m1,m2,m3,m4,m5,m6,m7]

example_obj.code        = """
<div role="application">

<h3>Text Sample 1</h3>

<ul class="toolbar" title="Text Formatting Controls 1" role="toolbar" id="toolbar1">

	<li id="bigger1"  
		role="button"
		tabindex="0"
		aria-pressed="false"
		aria-labelledby="bigger_label"
		aria-controls="text1"
			><img src="{{EXAMPLE_MEDIA}}images/button-bigger.png" alt="incease font size" align="middle"></li>
		    
	<li id="smaller1"  
		role="button"
		tabindex="-1"
		aria-pressed="false"
		aria-labelledby="smaller_label"
		aria-controls="text1"
			><img src="{{EXAMPLE_MEDIA}}images/button-smaller.png" alt="decrease font size" align="middle"></li>
		   
	<li id="italic1"  
		class="toggleButton"
		role="button"
		tabindex="-1"
		aria-pressed="true"
		aria-labelledby="italic_label"
		aria-controls="text1"
			><img src="{{EXAMPLE_MEDIA}}images/button-italicPressed.png" alt="italicize text" align="middle"></li>
		
	<li id="bold1"  
		class="toggleButton"
		role="button"
		tabindex="0"
		aria-pressed="false"
		aria-labelledby="bold_label"
		aria-controls="text1"
			><img src="{{EXAMPLE_MEDIA}}images/button-bold.png" alt="bold text" align="middle"></li>
		
</ul>

<ul class="toolbar" title="Paragraph Formatting Controls 1"  role="toolbar" id="toolbar2">
	
	<li id="left1" 
		class="radioButton"
		role="button"
		tabindex="0"
		aria-pressed="true"
		aria-labelledby="left_label"
		aria-controls="text1"
			><img src="{{EXAMPLE_MEDIA}}images/button-leftPressed.png" alt="align text left" align="middle"></li>
		    
	<li id="center1"
		class="radioButton"
		role="button"
		tabindex="-1"
		aria-pressed="false"
		aria-labelledby="center_label"
		aria-controls="text1"
			><img src="{{EXAMPLE_MEDIA}}images/button-center.png" alt="align text center" align="middle"></li>
		   
	<li id="right1"
		class="radioButton"
		role="button"
		tabindex="-1"
		aria-pressed="false"
		aria-labelledby="right_label"
		aria-controls="text1"
			><img src="{{EXAMPLE_MEDIA}}images/button-right.png" alt="align text right" align="middle"></li>
		
	<li id="justify1"
		class="radioButton"
		role="button"
		tabindex="0"
		aria-pressed="false"
		aria-labelledby="justify_label"
		aria-controls="text1"
			><img src="{{EXAMPLE_MEDIA}}images/button-justify.png" alt="justify text" align="middle"></li>
		
</ul>

<p style="clear: both; height: 1px">&nbsp;</p>

<label for="text1">Example Text 1</label>
<textarea id="text1" name="text1" class="example italic"> 
Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation, so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.
</textarea>	
<p>&nbsp;</p>

<h3>Text Sample 2</h3>

<ul class="toolbar" title="Text Formatting Controls 2"  role="toolbar" id="toolbar3">

	<li id="bigger2"  
		role="button"
		tabindex="0"
		aria-pressed="false"
		aria-labelledby="bigger_label"
		aria-controls="text2"
			><img src="{{EXAMPLE_MEDIA}}images/button-bigger.png" alt="increase font size" align="middle"></li>
		    
	<li id="smaller2" 
		role="button"
		tabindex="-1"
		aria-pressed="false"
		aria-labelledby="smaller_label"
		aria-controls="text2"
			><img src="{{EXAMPLE_MEDIA}}images/button-smaller.png" alt="decrease font size" align="middle"></li>
		   
	<li id="italic2"  
		class="toggleButton"
		role="button"
		tabindex="-1"
		aria-pressed="false"
		aria-controls="text2"
		aria-labelledby="italic_label"
			><img src="{{EXAMPLE_MEDIA}}images/button-italic.png" alt="italicize text" align="middle"></li>
		
	<li id="bold2"  
		class="toggleButton"
		role="button"
		tabindex="0"
		aria-pressed="true"
		aria-labelledby="bold_label"
		aria-controls="text2"
			><img src="{{EXAMPLE_MEDIA}}images/button-boldPressed.png" alt="bold text" align="middle"></li>
		
</ul>

<ul class="toolbar" title="Paragraph Formatting Controls 2"  role="toolbar" id="toolbar4">

	<li id="left2"
		class="radioButton"
		role="button"
		tabindex="0"
		aria-pressed="true"
		aria-labelledby="left_label"
		aria-controls="text2"
			><img src="{{EXAMPLE_MEDIA}}images/button-leftPressed.png" alt="align text left" align="middle"></li>
		    
	<li id="center2"
		class="radioButton"
		role="button"
		tabindex="-1"
		aria-pressed="false"
		aria-labelledby="center_label"
		aria-controls="text2"
			><img src="{{EXAMPLE_MEDIA}}images/button-center.png" alt="align text center" align="middle"></li>
		   
	<li id="right2"
		class="radioButton"
		role="button"
		tabindex="-1"
		aria-pressed="false"
		aria-labelledby="right_label"
		aria-controls="text2"
			><img src="{{EXAMPLE_MEDIA}}images/button-right.png" alt="align text right" align="middle"></li>
		
	<li id="justify2"
		class="radioButton"
		role="button"
		tabindex="-1"
		aria-pressed="false"
		aria-labelledby="justify_label"
		aria-controls="text2"
			><img src="{{EXAMPLE_MEDIA}}images/button-justify.png" alt="justify text" align="middle"></li>

</ul>

<p style="clear: both; height: 1px">&nbsp;</p>

<label for="text2">Example Text 2</label>
<textarea id="text2" name="text2" class="example bold">
But, in a larger sense, we can not dedicate - we can not consecrate - we can not hallow - this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us - that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion - that we here highly resolve that these dead shall not have died in vain - that this nation, under God, shall have a new birth of freedom - and that government of the people, by the people, for the people, shall not perish from the earth. 
</textarea>

<p class="hide" id="bold_label">Bold</p>

<p class="hide" id="italic_label">Italic</p>

<p class="hide" id="bigger_label">Font Larger</p>

<p class="hide" id="smaller_label">Font Smaller</p>

</div>

"""
example_obj.script      = """
var KEY_ENTER = 13;
var KEY_SPACE = 32;
var KEY_LEFT  = 37;
var KEY_UP    = 38;
var KEY_RIGHT = 39;
var KEY_DOWN  = 40;

$(document).ready(function() {

	$('ul.toolbar li').mousedown(function(event) {

		var ariaControls = '#' + $(this).attr('aria-controls');
		var button = $(this).attr('aria-labelledby');

		// remove "_label" from the button string
		button = button.substr(0, button.length - 6);

		// trigger the blur event to reset the button images to the unfocused state.
		// this is necessary because blur is not triggered for li elements when using the mouse
		$('ul.toolbar li').trigger('blur');

		$(this).siblings().attr('tabindex', "-1");
		$(this).attr('tabindex', "0");

		switch(button) {
			case 'bigger': {
				increaseFontSize(ariaControls);
				$(this).children('img').attr('src', "{{EXAMPLE_MEDIA}}images/button-biggerPressed-focus.png");
				break;
			}
			case 'smaller': {
				decreaseFontSize(ariaControls);
				$(this).children('img').attr('src', "{{EXAMPLE_MEDIA}}images/button-smallerPressed-focus.png");
				break;
			}
			case 'italic':
			case 'bold': {
				$(ariaControls).toggleClass(button);

				if ($(ariaControls).hasClass(button) == true) {
					$(this).children('img').attr('src', "{{EXAMPLE_MEDIA}}images/button-" + button + "Pressed-focus.png");
				}
				else
				{
					$(this).children('img').attr('src', "{{EXAMPLE_MEDIA}}images/button-" + button + "-focus.png");
				}
				break;
			}
			case 'left':
			case 'center':
			case 'right':
			case 'justify': {

				// Set the pressed-focus button state
				$(this).children('img').attr('src', "{{EXAMPLE_MEDIA}}images/button-" + button + "Pressed-focus.png");
				$(this).attr('aria-pressed', "true");

				setAlignment(button, ariaControls);

				// clear the other alignment buttons
				$(this).siblings().each(function(index) {
					var sib = $(this).attr('id');
					sib = sib.substr(0, sib.length - 1);
					$(this).children('img').attr('src', "{{EXAMPLE_MEDIA}}images/button-" + sib + ".png");
					$(this).attr('aria-pressed', "false");
				});

				break;
			}
		} // end switch

		if ($(this).hasClass('toggleButton') == true) {

			// This is a toggle button: toggle aria-pressed state
			togglePressed(this);
		}
		else if ($(this).hasClass('radioButton') == false) {

			// This is a momentary pushbutton: Set aria-pressed to true
			$(this).attr('aria-pressed', 'true');
		}

		// Give the current button focus
		$(this).focus();

		event.stopPropagation();
		return false;
	}); // end button click handler

	// bind a mouseup handler to the buttons to enable momentary pushbuttons
	// to return to unpressed state and toggle buttons to remain pressed
	// 
	$('ul.toolbar li').mouseup(function(event) {

		if ($(this).hasClass('toggleButton') == false && $(this).hasClass('radioButton') == false) {

			// Set aria-pressed to false
			$(this).attr('aria-pressed', 'false');

			// change button image to reflect unpressed state
			switch ($(this).attr('aria-labelledby')) {
				case 'bigger_label': {
					$(this).children('img').attr('src', "{{EXAMPLE_MEDIA}}images/button-bigger-focus.png");
					break;
				}
				case 'smaller_label': {
					$(this).children('img').attr('src', "{{EXAMPLE_MEDIA}}images/button-smaller-focus.png");
					break;
				}
			} // end switch
		}

		event.stopPropagation();
		return false;
	}); // end mouseup handler

	 // keypress handler
	 //
	 // The Opera browser performs some window commands from the keypress event,
	 // not keydown like Firefox, Safari, and IE. This event handler consumes
	 // keypresses for relevant keys so that Opera behaves when the user is
	 // manipulating the buttons with the keyboard.
	 //
	$('ul.toolbar li').keypress(function(event) {
		switch (event.keyCode) {
			case KEY_UP:
			case KEY_DOWN:
			case KEY_ENTER:
			case KEY_SPACE: {
				event.stopPropagation;
				return false;
				break;
			} // end case
		} //end switch

		return true;
	}); //end keypress event

	$('ul.toolbar li').keydown(function(event) {

		var ariaControls = '#' + $(this).attr('aria-controls');

		$(this).siblings().attr('tabindex', "-1");
		$(this).attr('tabindex', "0");


		switch (event.keyCode) {
			case KEY_UP:
			case KEY_LEFT: {
				selectedButton = $(this).prev();
				if (!$(selectedButton).length) {
					selectedButton = $(this).parent().children('li:last');
				}

				// Blur the other buttons in the toolbar
				$(selectedButton).siblings().trigger('blur');

				// Set focus to the selected button
				$(selectedButton).focus();

				event.stopPropagation();
				return false;

			} // end case
			case KEY_DOWN:
			case KEY_RIGHT: {
				selectedButton = $(this).next();
				if (!$(selectedButton).length) {
					selectedButton = $(this).parent().children('li:first');
				}

				// Blur the other buttons in the toolbar
				$(selectedButton).siblings().trigger('blur');

				// Set focus to the selected button
				$(selectedButton).focus();

				event.stopPropagation();
				return false;
				
			} // end case
			case KEY_ENTER:
			case KEY_SPACE: {
				var button = $(this).attr('aria-labelledby');

				// remove "_label" from the button string
				button = button.substr(0, button.length - 6);

					switch(button) {
					case 'bigger': {
						increaseFontSize(ariaControls);
						$(this).children('img').attr('src', "{{EXAMPLE_MEDIA}}images/button-biggerPressed-focus.png");
						break;
					}
					case 'smaller': {
						decreaseFontSize(ariaControls);
						$(this).children('img').attr('src', "{{EXAMPLE_MEDIA}}images/button-smallerPressed-focus.png");
						break;
					}
					case 'italic':
					case 'bold': {
						$(ariaControls).toggleClass(button);
		
						if ($(ariaControls).hasClass(button) == true) {
							$(this).children('img').attr('src', "{{EXAMPLE_MEDIA}}images/button-" + button + "Pressed-focus.png");
						}
						else
						{
							$(this).children('img').attr('src', "{{EXAMPLE_MEDIA}}images/button-" + button + "-focus.png");
						}
						break;
					}
					case 'left':
					case 'center':
					case 'right':
					case 'justify': {
		
						// Set the pressed-focus button state
						$(this).children('img').attr('src', "{{EXAMPLE_MEDIA}}images/button-" + button + "Pressed-focus.png");
						$(this).attr('aria-pressed', "true");
		
						setAlignment(button, ariaControls);
		
						// clear the other alignment buttons
						$(this).siblings().each(function(index) {
							var sib = $(this).attr('id');
							sib = sib.substr(0, sib.length - 1);
							$(this).children('img').attr('src', "{{EXAMPLE_MEDIA}}images/button-" + sib + ".png");
							$(this).attr('aria-pressed', "false");
						});
		
						break;
					}
				} // end switch	

				if ($(this).hasClass('toggleButton') == true) {

						// This is a toggle button: toggle aria-pressed state
						togglePressed(this);
				}
				else if ($(this).hasClass('radioButton') == false) {
						// This is a momentary pushbutton: Set aria-pressed to true
						$(this).attr('aria-pressed', 'true');
				}

				event.stopPropagation();
				return false;

			} // end case
			
		} // end switch

		return true;
	}); // end button click handler

	// bind a keyup handler to the buttons to enable momentary pushbuttons
	// to return to unpressed state and toggle buttons to remain pressed
	// 
	$('ul.toolbar li').keyup(function(event) {
		
		var id = this;
		var selectedButton;

		switch (event.keyCode) {
			case KEY_ENTER:
			case KEY_SPACE: {
				if ($(this).hasClass('toggleButton') == false && $(this).hasClass('radioButton') == false) {
				
					// set aria-pressed to false
					$(id).attr('aria-pressed', 'false');

					// change button image to reflect unpressed state
					switch ($(this).attr('aria-labelledby')) {
						case 'bigger_label': {
							$(this).children('img').attr('src', "{{EXAMPLE_MEDIA}}images/button-bigger-focus.png");
							break;
						}
						case 'smaller_label': {
							$(this).children('img').attr('src', "{{EXAMPLE_MEDIA}}images/button-smaller-focus.png");
							break;
						}
					} // end switch
				}

				event.stopPropagation();
				return false;

			} // end case
		} // end switch

		return true;
	}); // end mouseup handler

	// bind a focus handler to set button image to show focus
	// 
	$('ul.toolbar li').focus(function(event) {

		var pressed = "Pressed";
		var button = $(this).attr('aria-labelledby');

		// Remove "_label" from the button string
		button = button.substr(0, button.length - 6);

		// If aria-pressed is false, set pressed to be an empty string
		if ($(this).attr('aria-pressed') == 'false') {
			pressed = '';
		}

		$(this).children('img').attr('src', "{{EXAMPLE_MEDIA}}images/button-" + button + pressed + "-focus.png");
		
	}); // end focus handler

	// bind a blur handler to set button image to show focus
	// 
	$('ul.toolbar li').blur(function(event) {

		var pressed = "Pressed";
		var button = $(this).attr('aria-labelledby');

		// Remove "_label" from the button string
		button = button.substr(0, button.length - 6);

		// If aria-pressed is false, set pressed to be an empty string
		if ($(this).attr('aria-pressed') == 'false') {
			pressed = '';
		}

		$(this).children('img').attr('src', "{{EXAMPLE_MEDIA}}images/button-" + button + pressed + ".png");

	}); // end blur handler

	/**
	 * increaseFontSize() increases the font size for the controlled area
	 *
	 * @param (ariaControls) id of text area to modify
	 *
	 * @return N/A
	 */
	function increaseFontSize(ariaControls) {
	
		var $text = $(ariaControls);
		var fontSize = parseFloat($text.css('fontSize'), 10);
	
		// increase the font size
		fontSize *= 1.4;
	
		if (fontSize > 120) {
			return;
		}
		// write the new value to the css 
		// note: 'px' must be appended for valid css
		$text.css('fontSize', fontSize+'px');
	} // end increaseFontSize()
	
	/**
	 * decreaseFontSize() decreases the font size for the controlled area
	 *
	 * @param (ariaControls) id of text area to modify
	 *
	 * @return N/A
	 */
	function decreaseFontSize(ariaControls) {
	
		var $text = $(ariaControls);
		var fontSize = parseFloat($text.css('fontSize'), 10);
	
		// increase the font size
		fontSize /= 1.4;
	
		if (fontSize < 4) {
			return;
		}
	
		// write the new value to the css property
		// note: 'px' must be appended for valid css
		$text.css('fontSize', fontSize+'px');
	
	} // end decreaseFontSize
	
	/**
	 * setAlignment() sets the aligment of text according to the values passed into the function
	 *
	 * @param (align) value of alignment to set
	 * @param (id) button to be operated on
	 *
	 * @return N/A
	 */
	function setAlignment(align, id) {
	
		// reverse the aria-pressed state
		$(id).css('text-align', align);
	}

	/**
	 * togglePressed() toggles the aria-pressed atribute between true or false
	 *
	 * @param ( id object) button to be operated on
	 *
	 * @return N/A
	 */
	function togglePressed(id) {
	
		// reverse the aria-pressed state
		if ($(id).attr('aria-pressed') == 'true') {
			$(id).attr('aria-pressed', 'false');
		}
		else {
			$(id).attr('aria-pressed', 'true');
		}
	}

}); // end ready
"""

example_obj.style       = """
ul.toolbar{
  float: left;
  display: inline;
  text-align: center;
  margin: 0 !important;
  padding: 0 1px !important;
  font-size: 100% !important;
  border: 1px solid black;
  background-color: #ccc;
}

ul.toolbar li{
  float: left;
  display: inline;
  text-align: center;
  margin: 0;
  padding: 3px;
  height: 36px;
  height: 34px;
}

ul div.italic{
   font-style: italic;
}

textarea.example {
  clear: both;
  margin: 0;
  padding: .25em;
  width: 60%;
  height: 200px;
  
}

.italic {
  font-style:italic;
}

.bold {
  font-weight:bold;
}

.hide {
position: absolute;
top: -20em;
left: -200em;
} 
"""

example1 = create_example(example_obj)