"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples import *

order = 1

spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='checkbox')
m2 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='presentation')
m3 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-checked')
m4 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-describedby')
m5 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-hidden')

# =============================
# Example 1
# =============================

example_obj             = example_object()
example_obj.order          = order
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.title       = 'Alert role example using an ARIA alert box'
example_obj.permanent_slug = 'alert1'

example_obj.a11y_features = """
Simple number guessing game that displays the results of each guess in an ARIA alert box.
"""
example_obj.keyboard    = """
* Tab: Move between guess box and buttons.
* Enter: Submit guess or push button.
"""

example_obj.aria_labelledby = True
example_obj.html_label = True

example_obj.markup = [m1,m2,m3,m4]

example_obj.html        = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>

<div id="guess1" class="guess">
  <h2>Number Guessing Game</h2>
       <p><strong>Instructions:</strong> In this game you guess a number between 1 an 10 and then press the "Check My Guess" button to check your responses.  
	  An <abbr title="Accessible Rich Internet Application">ARIA</abbr> dialog box will display the results of your guess.  To start over again to press the "Play Again" button.</p>

       <p class="input">
         <label for="id_guess1_text">Guess a number between 1 and 10</label>
           <input type="text" id="id_guess1_text" size="3" aria-labelledby="guess1_label" aria-invalid="false"/>
       </p>

       <p id="id_guess1_alert" class="feedback"></p>

       <p class="input">  	
         <input class="button" id="id_guess1_check" type="button" value="Check My Guess"/>
         <input class="button" id="id_guess1_again" type="button" value="Play Again"/>
       </p>
</div>

"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};

$(document).ready(function () {
	var guess1 = new OAA_EXAMPLES.guess(1, 10, 'id_guess1_text', 'id_guess1_check', 'id_guess1_again', 'id_guess1_alert');
	
});

/**
* @constructor guess
*
* @memberOf OAA_EXAMPLES
*
* @param {integer} max - the maximum number to guess.
*
* @param {integer} min - the minimum number to guess.
*
* @param {String} text_id - the id of the text box where player enters a guess.
*
* @param {String} check_id - the id of the check guess button.
*
* @param {String} again_id - the id of the play again button.
*
* @param {String} alert_id - the id of the alert element where game messages will
*                          be printed.
*
* @return {N/A}
*/

/**
* @private
* @constructor Internal Properties
*
* @property {integer} min - the minimum number to guess
* @property {integer} max - the maximum number to guess
*
* @property {object} $text - the jQuery object pointer to the text box
* @property {object} $check - the jQuery object pointer to the check guess button
* @property {object} $again - the jQuery object pointer to the play again button
* @property {object} $alert - the jQuery object pointer to the alert area
*
* @property {integer} - guessVal - the number for the player to guess
* @property {integer} - guessCount - the number of atempts the player has made
* @property {integer} - enterkey - the key code for the enter key
*/

OAA_EXAMPLES.guess = function(min, max, text_id, check_id, again_id, alert_id) {
	
	this.minGuess = min;         
	this.maxGuess = max;         
	this.$text = $('#' + text_id);
	this.$check = $('#' + check_id);
	this.$again = $('#' + again_id);
	this.$alert = $('#' + alert_id);

	this.guessVal = -1;
	this.guessCount = 0;     
	this.enterKey = 13;        

	// bind event handlers
	this.bindHandlers();

	// initialize the game
	this.newGame();

} // end guess object constructor

/**
* @method newGame
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set up a new game. The function chooses a number
* between 1 and the max number specified at instantiation, sets the guess count to 0, and show the user a message to make a guess.
*
* @return {N/A}
*/

OAA_EXAMPLES.guess.prototype.newGame = function () {

	// get a new random number for the player to guess
	this.guessVal = Math.floor(Math.random()*(this.maxGuess - this.minGuess + 1)) + this.minGuess;
	
	// reset the guess count
	this.guessCount = 0;

	// reset the guess text box
	this.$text.val('');
	this.$text.attr('aria-invalid', 'false');

	// Re-enable the buttons
	this.$text.removeAttr('disabled');
	this.$check.removeAttr('disabled');

	// invite the user to make a guess
	this.$alert.text('Make a guess.');

	// set focus on the guest text box
	this.$text.focus();

} // end newGame

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a function to bind the event handlers for the game controls
*
* @return {N/A}
*/

OAA_EXAMPLES.guess.prototype.bindHandlers = function () {

	var thisObj = this; // Store the this pointer

	// bind a focus handler for the guess text box
	this.$text.focus(function (e) {
		thisObj.handleTextFocus(e);
		return true;
	});

	// bind a keydown handler for the guess text box
	this.$text.keydown(function (e) {
		return thisObj.handleTextKeyDown(e);
	});

	// bind a keypress handler for the guess text box
	this.$text.keypress(function (e) {
		return thisObj.handleTextKeyPress(e);
	});

	// bind a click handler for the check guess button
	this.$check.click(function (e) {
		return thisObj.handleCheckClick(e);
	});

	// bind a click handler for the play again button
	this.$again.click(function (e) {
		return thisObj.handleAgainClick(e);
	});

} // end bindHandlers()

/**
* @method handleTextFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process focus events for the guess text box
*
* @input {obj} evt - the event object associated with the keydown event
*
* @return {N/A}
*/

OAA_EXAMPLES.guess.prototype.handleTextFocus = function(evt) {

	// Select any text in the text box
	this.$text.select();

} // end handleTextFocus()

/**
* @method handleTextKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for the guess text box
*
* @input {obj} evt - the event object associated with the keydown event
*
* @return {boolean} false if consuming event, true if propagating
*/

OAA_EXAMPLES.guess.prototype.handleTextKeyDown = function(evt) {

	// do nothing if shift, alt, or ctrl key pressed.
	if (evt.shiftKey || evt.altKey || evt.ctrlKey) {
		return true;
	}

	if (evt.keyCode == this.enterKey) {

		// validate the guess
		if (this.validateGuess() == true) {

			// increment the guess count
			this.guessCount++;

			// see if the player has won
			if (this.checkGuess() == true) {
				// disable the guess text box and the check guess button
				this.$text.attr('disabled', 'true');
				this.$check.attr('disabled', 'true');

				// Set the focus on the play again button
				this.$again.focus();
			}
			else {
				// Game is still in progress. Set focus on the guess text box
				this.$text.focus();
			}
		}
		else {
			// not a valid guess
			this.$text.focus();
		}

		evt.stopPropagation;
		return false;
	}

	return true;

} // end handleTextKeyDown()

/**
* @method handleTextKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for the guess text box. This function
* is included to handle browsers that perform window scrolling, etc. on keypress rather than keydown.
*
* @input {obj} evt - the event object associated with the keypress event
*
* @return {boolean} false if consuming event, true if propagating
*/

OAA_EXAMPLES.guess.prototype.handleTextKeyPress = function(evt) {

	// do nothing if shift, alt, or ctrl key pressed.
	if (evt.shiftKey || evt.altKey || evt.ctrlKey) {
		return true;
	}

	if (evt.keyCode == this.enterKey) {

		// consume the event
		evt.stopPropagation;
		return false;
	}

	return true;

} // end handleTextKeyPress()

/**
* @method handleCheckClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events for the check guess button
*
* @input {obj} evt - the event object associated with the click event
*
* @return {boolean} false if consuming event, true if propagating
*/

OAA_EXAMPLES.guess.prototype.handleCheckClick = function(evt) {
	// do nothing if shift, alt, or ctrl key pressed.
	if (evt.shiftKey || evt.altKey || evt.ctrlKey) {
		return true;
	}

	// validate the guess
	if (this.validateGuess() == true) {

		// increment the guess count
		this.guessCount++;

		// see if the player has won
		if (this.checkGuess() == true) {
			// disable the guess text box and the check guess button
			this.$text.attr('disabled', 'true');
			this.$check.attr('disabled', 'true');

			// Set the focus on the play again button
			this.$again.focus();
		}
		else {
			// Game is still in progress. Set focus on the guess text box
			this.$text.focus();
		}
	}
	else {
		// not a valid guess
		this.$text.focus();
	}
		
	evt.stopPropagation;
	return false;

} // end handleCheckClick()

/**
* @method handleAgainClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events for the play again button
*
* @input {obj} evt - the event object associated with the click event
*
* @return {boolean} false if consuming event, true if propagating
*/

OAA_EXAMPLES.guess.prototype.handleAgainClick = function(evt) {

	// do nothing if shift, alt, or ctrl key pressed.
	if (evt.shiftKey || evt.altKey || evt.ctrlKey) {
		return true;
	}

	// Setup a new game
	this.newGame();

	// Set focus to the guess text box
	this.$text.focus();
		
	evt.stopPropagation;
	return false;

} // end handleTextKeyDown()

/**
* @method validateGuess
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to validate a player's guess. If the guess is not a number, is less than
* the minimum allowed guess, or is greater than the maximum allowed guess, the user is warned that the guess is invalid
*
* @return {boolean} true if guess is valid; false if guess is invalid
*/

OAA_EXAMPLES.guess.prototype.validateGuess = function() {
	var val = this.$text.val();

	if (this.$text.val() == '') {
		// guess is empty
		this.$text.attr('aria-invalid', 'true');
		this.$alert.html('You must enter a number!');

		return false;
	}
	else if (isNaN(val) == true) {

		// guess is not a number
		this.$text.attr('aria-invalid', 'true');
		this.$alert.html('\\'' + this.$text.val() + '\\' is not a number!');

		return false;
	}
	else if (val < this.minGuess || val > this.maxGuess) {

		// guess is out of range
		this.$text.attr('aria-invalid', 'true');
		this.$alert.html('You must choose a number between ' + this.minGuess + ' and ' + this.maxGuess + '!');

		return false;
	}
	
	this.$text.attr('aria-invalid', 'false');

	return true;

} // end validateGuess()

/**
* @method checkGuess
* 
* @memberOf OAA_EXAMPLES
*
* @desc a member function to check the player's guess to see if he or she has won the game
*
* @return {boolean} true if the player has won; false if not
*/

OAA_EXAMPLES.guess.prototype.checkGuess = function() {

	var guess = this.$text.val();

	if (guess == this.guessVal) {

		// The player has won. Tell the player how many tries it took

		if (this.guessCount == 1) {
			this.$alert.html('\\'' + guess + '\\' is right. You got it on your first try!');
		}
		else {
			this.$alert.html('\\'' + guess + '\\' is right. It only took you ' + this.guessCount + ' tries!');
		}
		return true;
	}

	// Player did not guess the correct number. Tell the player if he or she is too high or too low
	if (guess < this.guessVal) {
		this.$alert.html('\\'' + guess + '\\' is too low. Try a higher number.');
	}
	else {
		this.$alert.html('\\'' + guess + '\\' is too high. Try a lower number.');
	}

	return false;

} // end checkGuess()
"""

example_obj.style       = """

div.guess {
  border: thick double black;
  padding: 1em;
  width: 65%;
  font-family: Arial, Helvetica, sans-serif;
}

div.guess h2 {
  margin: 0;
  padding: 0;
  text-align: center;
  margin-left: 1em;
  margin-right: 1em;
}

div.guess input {
  font-size: 100%;
}

div.guess p.input {
  margin: 0;
  padding: 0;
  font-size: 150%;
  margin-top: .5em;
  margin-bottom: .5em;
  text-align: center;
  margin-left: 1em;
  margin-right: 1em;
}

div.guess input.button {
  margin: 0;
  padding: 0;
  display: inline;
  padding-left: .5em;
  padding-right: .5em;
  padding-top: .25em;
  padding-bottom: .25em;
}


div.guess p.feedback {
  margin: 0;
  padding: .25em;
  border: 2px solid black;
  text-align: center;
  margin-top: .5em;
  margin-bottom: .5em;
  font-weight: bold;
}
"""

example1 = create_example(example_obj)

# =============================
# Example 2
# =============================

order += 1

example_obj             = example_object()
example_obj.order          = order
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.title       = 'Alert example using a modal ARIA dialog box'
example_obj.permanent_slug = 'alertdialog1'

example_obj.a11y_features = """
Simple number guessing game that displays the results of each guess in a modal ARIA dialog box.
"""
example_obj.keyboard    = """
* Tab: Move between guess box and buttons.
* Enter: Submit guess or push button.
"""
example_obj.aria_labelledby = True
example_obj.html_label = True

example_obj.markup = [m1,m2,m3,m4,m5]

example_obj.html        = """
//reference to JQuery
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>

<div role="application">

<div id="id_guess1" class="guess">

  <h2>Number Guessing Game</h2>
	
	<p><strong>Instructions:</strong> In this game you guess a number between 1 an 10 and then press the "Check My Guess" button to check your responses.  
	  An <abbr title="Accessible Rich Internet Application">ARIA</abbr> dialog box will display the results of your guess.  To start over again to press the "Play Again" button.</p>

  <p class="input">
    <label for="id_guess1_text">Guess a number between 1 and 10</label>
    <input type="text" id="id_guess1_text" size="3" aria-labelledby="guess1_label" aria-invalid="false">
  </p>

  <p class="input">  	
    <input class="button" id="id_guess1_check" type="button" value="Check My Guess"/>
    <input class="button" id="id_guess1_again" type="button" value="Play Again"/>
  </p>
</div>

</div>
"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};

$(document).ready(function () {
	var guess1 = new OAA_EXAMPLES.guess(1, 10, 'id_guess1', 'id_guess1_text', 'id_guess1_check', 'id_guess1_again', 'alert1');
	
});

/**
* keyCodes is an object that defines keycodes for the key handlers
*/
function keyCodes () {
	// Define values for keycodes
	this.tab        = 9;
	this.enter      = 13;
	this.esc        = 27;
	this.space      = 32;
}

/**
* @constructor alertDlg
*
* @memberOf OAA_EXAMPLES
*
* @desc a class to implement a modal alert dialog
*
* @param {String} alert_id - the id of the dialog to create
*
* @param {String} game_id - the id to attach the dialog to
*
* @return {N/A}
*/

/**
* @private
* @constructor Internal Properties
*
* @property {obj} $dlg - the object pointer of the dialog
* @property {obj} $game - the object pointer of the dialog of the containing div for the game
* @property {obj} $msg - the object pointer of the alert message area
* @property {obj} $button - the object pointer of the alert close button
* @property {obj} $focus - the object pointer of a page element to give focus to on dialog dismissal
* @property {obj} keys - defines keycodes for the key handlers
*/

OAA_EXAMPLES.alertDlg = function(alert_id, game_id) {
	var dlg = '<div id="' + alert_id + '" role="alertdialog" tabindex="-1" aria-hidden="true" aria-labelledby="' +
		alert_id + '_title"><p id="' + alert_id + '_title" class="title">Alert Box</p><p id="' + 
		alert_id + '_message">No Message</p><input id="' +
		alert_id + '_close" type="button" value="Close" /></div>';

	// append the dialog to the document
	$('div#' + game_id).append(dlg);

	// Define the object properties
	this.$dlg  = $('#' + alert_id); 
	this.$game = $('#' + game_id); 
	this.$msg = $('#' + alert_id + '_message');
	this.$button = $('#' + alert_id + '_close');
	this.$focus;

	this.keys = new keyCodes();

	// bind handlers
	this.bindHandlers();

} // end alertDlg constructor

/**
* @method showMsg
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the message text of the alertDlg
*
* @param {String} msg - the message to display in the dialog box.
*
* @param {String} focusId - the id of the element to give focus to when the dialog is dismissed.
*
* @return {N/A}
*/

OAA_EXAMPLES.alertDlg.prototype.showMsg = function(msg, $focus) {

	// Store the focus ID
	this.$focus = $focus;

	// Set the message text
	this.$msg.html(msg);

	// Show the dialog
	this.showDlg();

} // end showMsg()

/**
* @method bindHandlers - a member function to bind event handlers to the modal alert dialog
*
* @memberOf OAA_EXAMPLES
*
* @return {N/A}
*/

OAA_EXAMPLES.alertDlg.prototype.bindHandlers = function () {

	var thisObj = this; // store the this pointer

	// bind a keydown handler
	this.$dlg.keydown(function(e) {
		return thisObj.handleDlgKeyDown(e);
	});

	// bind a keypress handler
	this.$dlg.keypress(function(e) {
		return thisObj.handleDlgKeyPress(e);
	});

	// bind a click handler
	this.$button.click(function(e) {
		return thisObj.handleCloseClick(e);
	});

} // end bindhandlers()

/**
* @method handleDlgKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for the alert dialog
*
* @param {obj} evt - the event object associated with the keydown event
*
* @return {boolean} true if propagating; false if consuming event
*/

OAA_EXAMPLES.alertDlg.prototype.handleDlgKeyDown = function(evt) {

	if (evt.ctrlKey || evt.AltKey) {
		// do nothing
		return true;
	}

	switch (evt.keyCode) {
		case this.keys.tab: {
			// Consume the tab event and do nothing
			evt.stopPropagation;
			return false;
		}
		case this.keys.enter:
		case this.keys.esc:
		case this.keys.space: {

			// hide the dialog
			this.hideDlg();

			evt.stopPropagation;
			return false;

			break;
		}
	} // end switch

	return true;

} // end handleDlgKeyDown()

/**
* @method handleDlgKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to consume keypress events for the alert dialog
*
* @param {obj} evt - the event object associated with the keydown event
*
* @return {boolean} true if propagating; false if consuming event
*/

OAA_EXAMPLES.alertDlg.prototype.handleDlgKeyPress = function(evt) {

	if (evt.ctrlKey || evt.AltKey) {
		// do nothing
		return true;
	}

	switch (evt.keyCode) {
		case this.keys.tab:
		case this.keys.enter:
		case this.keys.esc:
		case this.keys.space: {

			evt.stopPropagation;
			return false;

			break;
		}
	} // end switch

	return true;

} // end handleDlgKeyPress()

/**
* @method handleCloseClick
*
* @memberOf OAA_EXAMPLES
*
* @param {obj} evt - the event object associated with the click event
*
* @return {boolean} true if propagating; false if consuming event
*/

OAA_EXAMPLES.alertDlg.prototype.handleCloseClick = function(evt) {

	if (evt.shiftKey || evt.ctrlKey || evt.AltKey) {
		// do nothing
		return true;
	}

	// Hide the dialog
	this.hideDlg();

	evt.stopPropagation;
	return false;

} // end handleCloseClick()

/**
* @method showDlg
*
* @memberOf OAA_EXAMPLES
* 
* @desc a member function to show the alert dialog and give it focus
*
* @return {N/A}
*/

OAA_EXAMPLES.alertDlg.prototype.showDlg = function() {

	var thisObj = this;

	// Bind an event listener to the document to capture all mouse events to make dialog modal
	$(document).bind('click mousedown mouseup mousemove mouseover', function(e) {

		//ensure focus remains on the dialog
		thisObj.$dlg.focus();

		// Consume all mouse events and do nothing
		e.stopPropagation;
		return false;
	});

	// Position the dialog centered in the containing div
	this.$dlg.css('left', (this.$game.width() - this.$dlg.width()) / 2 + this.$game.offset().left + 'px');
	this.$dlg.css('top', (this.$game.height() - this.$dlg.height()) / 2 + this.$game.offset().top + 'px');

	// Display the dialog
	this.$dlg.show();
	this.$dlg.attr('aria-hidden', 'false');

	// Give the dialog focus
	this.$dlg.attr('tabindex', '0');
	this.$dlg.focus();

} // end showDlg()

/**
* @method hideDlg
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to hide the alert dialog and return focus to the page
*
* @return {N/A}
*/

OAA_EXAMPLES.alertDlg.prototype.hideDlg = function() {

	// set aria hidden attribute and remove dialog from tab order
	this.$dlg.attr('aria-hidden', 'true');
	this.$dlg.attr('tabindex', '-1');

	// hide the dialog
	this.$dlg.hide();

	// Unbind the document mouse event listeners
	$(document).unbind('click mousedown mouseup mousemove');

	// return focus to the specified page element
	if (this.$focus) {
		this.$focus.focus();
	}

} // end hideDlg()


/**
* @constructor guess
*
* @memberOf OAA_EXAMPLES
*
* @desc a class to implement a simple number guessing game
*
* @param {String} game_id - the id to attach the instance of the game to.
*
* @param {integer} min - the minimum number to guess.
*
* @param {integer} max - the maximum number to guess.
*
* @param {String} text_id - the id of the text box where player enters a guess.
*
* @param {String} check_id - the id of the check guess button.
*
* @param {String} again_id - the id of the play again button.
*
* @param {obj} alertObj - the modal dialog object where game messages will be printed.
*
* @return {N/A}
*/

/**
* @private
* @constructor Internal Properties
*
* @property {integer} min - the minimum number to guess
* @property {integer} max - the maximum number to guess
*
* @property {obj} $text - the jQuery object pointer to the text box
* @property {obj} $check - the jQuery object pointer to the check guess button
* @property {obj} $again - the jQuery object pointer to the play again button
* @property {obj} alertDlg - the modal alert dialog to be displayed during the game
*/

OAA_EXAMPLES.guess = function(min, max, game_id, text_id, check_id, again_id, alert_id) {
	
	// define class properties
	this.minGuess = min;   
	this.maxGuess = max;       
	this.$text = $('#' + text_id); 
	this.$check = $('#' + check_id);
	this.$again = $('#' + again_id); 
	this.alertDlg = new OAA_EXAMPLES.alertDlg('alert1', game_id);
	this.guessVal = -1;        
	this.guessCount = 0;      

	this.keys = new keyCodes();

	// bind event handlers
	this.bindHandlers();

	// initialize the game
	this.newGame();

} // end guess object constructor

/**
* @method newGame
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set up a new game. The function chooses a number
* between 1 and the max number specified at instantiation, sets the guess count to 0, and
* show the user a message to make a guess.
*
* @return {N/A}
*/

OAA_EXAMPLES.guess.prototype.newGame = function () {

	// get a new random number for the player to guess
	this.guessVal = Math.floor(Math.random()*(this.maxGuess - this.minGuess + 1)) + this.minGuess;
	
	// reset the guess count
	this.guessCount = 0;

	// reset the guess text box
	this.$text.val('');
	this.$text.attr('aria-invalid', 'false');

	// Re-enable the buttons
	this.$text.removeAttr('disabled');
	this.$check.removeAttr('disabled');

	// Set focus on the guess text box
	this.$text.focus();

} // end newGame

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a function to bind the event handlers for the game controls
*
* @return {N/A}
*/

OAA_EXAMPLES.guess.prototype.bindHandlers = function () {

	var thisObj = this; // Store the this pointer

	// bind a focus handler for the guess text box
	this.$text.focus(function (e) {
		thisObj.handleTextFocus(e);
		return true;
	});

	// bind a keydown handler for the guess text box
	this.$text.keydown(function (e) {
		return thisObj.handleTextKeyDown(e);
	});

	// bind a keypress handler for the guess text box
	this.$text.keypress(function (e) {
		return thisObj.handleTextKeyPress(e);
	});

	// bind a click handler for the check guess button
	this.$check.click(function (e) {
		return thisObj.handleCheckClick(e);
	});

	// bind a click handler for the play again button
	this.$again.click(function (e) {
		return thisObj.handleAgainClick(e);
	});

} // end bindHandlers()

/**
* @method handleTextFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process focus events for the guess text box
*
* @input {obj} evt - the event object associated with the keydown event
*
* @return {N/A}
*/

OAA_EXAMPLES.guess.prototype.handleTextFocus = function(evt) {

	// Select any text in the text box
	this.$text.select();

} // end handleTextFocus()

/**
* @method handleTextKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for the guess text box
*
* @input {obj} evt - the event object associated with the keydown event
*
* @return {boolean} false if consuming event, true if propagating
*/

OAA_EXAMPLES.guess.prototype.handleTextKeyDown = function(evt) {

	// do nothing if shift, alt, or ctrl key pressed.
	if (evt.shiftKey || evt.altKey || evt.ctrlKey) {
		return true;
	}

	if (evt.keyCode == this.keys.enter) {

		// validate the guess
		if (this.validateGuess() == true) {

			// increment the guess count
			this.guessCount++;

			// see if the player has won
			if (this.checkGuess() == true) {
				// disable the guess text box and the check guess button
				this.$text.attr('disabled', 'true');
				this.$check.attr('disabled', 'true');
			}
		}

		evt.stopPropagation;
		return false;
	}

	return true;

} // end handleTextKeyDown()

/**
* @method handleTextKeyPress
* 
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for the guess text box. This function
* is included to handle browsers that perform window scrolling, etc. on keypress rather than keydown.
*
* @input {obj} evt - the event object associated with the keypress event
*
* @return {boolean} false if consuming event, true if propagating
*/

OAA_EXAMPLES.guess.prototype.handleTextKeyPress = function(evt) {

	// do nothing if shift, alt, or ctrl key pressed.
	if (evt.shiftKey || evt.altKey || evt.ctrlKey) {
		return true;
	}

	if (evt.keyCode == this.enterKey) {

		// consume the event
		evt.stopPropagation;
		return false;
	}

	return true;

} // end handleTextKeyPress()

/**
* @method handleCheckClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events for the check guess button
*
* @input {obj} evt - the event object associated with the click event
*
* @return {boolean} false if consuming event, true if propagating
*/

OAA_EXAMPLES.guess.prototype.handleCheckClick = function(evt) {

	// do nothing if shift, alt, or ctrl key pressed.
	if (evt.shiftKey || evt.altKey || evt.ctrlKey) {
		return true;
	}

	// validate the guess
	if (this.validateGuess() == true) {

		// increment the guess count
		this.guessCount++;

		// see if the player has won
		if (this.checkGuess() == true) {
			// disable the guess text box and the check guess button
			this.$text.attr('disabled', 'true');
			this.$check.attr('disabled', 'true');
		}
	}
		
	evt.stopPropagation;
	return false;

} // end handleCheckClick()

/**
* @method handleAgainClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events for the play again button
*
* @input {obj} evt - the event object associated with the click event
*
* @return {boolean} false if consuming event, true if propagating
*/

OAA_EXAMPLES.guess.prototype.handleAgainClick = function(evt) {

	// do nothing if shift, alt, or ctrl key pressed.
	if (evt.shiftKey || evt.altKey || evt.ctrlKey) {
		return true;
	}

	// Setup a new game
	this.newGame();

	evt.stopPropagation;
	return false;

} // end handleTextKeyDown()

/**
* @method validateGuess
*
* @memberOf OAA_EXAMPLES
* 
* @desc a member function to validate a player's guess. If the guess is not a number, is less than
* the minimum allowed guess, or is greater than the maximum allowed guess, the user is warned that the guess is invalid
*
* @return {boolean} true if guess is valid; false if guess is invalid
*/

OAA_EXAMPLES.guess.prototype.validateGuess = function() {
	var val = this.$text.val();

	if (this.$text.val() == '') {
		// guess is empty
		this.$text.attr('aria-invalid', 'true');
		this.alertDlg.showMsg('You must enter a number!', this.$text);

		return false;
	}
	else if (isNaN(val) == true) {

		// guess is not a number
		this.$text.attr('aria-invalid', 'true');
		this.alertDlg.showMsg('\\'' + this.$text.val() + '\\' is not a number!', this.$text);

		return false;
	}
	else if (val < this.minGuess || val > this.maxGuess) {

		// guess is out of range
		this.$text.attr('aria-invalid', 'true');
		this.alertDlg.showMsg('You must choose a number between ' + this.minGuess + ' and ' + this.maxGuess + '!', this.$text);

		return false;
	}
	
	this.$text.attr('aria-invalid', 'false');

	return true;

} // end validateGuess()

/**
* @method checkGuess
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to check the player's guess to see if he or she has won the game
*
* @return {boolean} true if the player has won; false if not
*/

OAA_EXAMPLES.guess.prototype.checkGuess = function() {

	var guess = this.$text.val();

	if (guess == this.guessVal) {

		// The player has won. Tell the player how many tries it took

		if (this.guessCount == 1) {
			this.alertDlg.showMsg('\\'' + guess + '\\' is right. You got it on your first try!', this.$again);
		}
		else {
			this.alertDlg.showMsg('\\'' + guess + '\\' is right. It only took you ' + this.guessCount + ' tries!', this.$again);
		}
		return true;
	}

	// Player did not guess the correct number. Tell the player if he or she is too high or too low
	if (guess < this.guessVal) {
		this.alertDlg.showMsg('\\'' + guess + '\\' is too low. Try a higher number.', this.$text);
	}
	else {
		this.alertDlg.showMsg('\\'' + guess + '\\' is too high. Try a lower number.', this.$text);
	}

	return false;

} // end checkGuess()
"""

example_obj.style       = """

div.guess {
  border: thick double black;
  padding: 1em;
  width: 50%;
  font-family: Arial, Helvetica, sans-serif;
}

div.guess h2 {
  margin: 0;
  padding: 0;
  text-align: center;
  margin-left: 1em;
  margin-right: 1em;
}

div.guess input {
  font-size: 100%;
}

div.guess p.input {
  margin: 0;
  padding: 0;
  font-size: 150%;
  margin-top: .5em;
  margin-bottom: .5em;
  text-align: center;
  margin-left: 1em;
  margin-right: 1em;
}

div.guess input.button {
  margin: 0;
  padding: 0;
  display: inline;
  padding-left: .5em;
  padding-right: .5em;
  padding-top: .25em;
  padding-bottom: .25em;
}


div#alert1 {
  position: absolute;
  width: 25%;
  border:medium solid black;
  display: none;
  background-color: white;
  color: black;
  text-align: center;
  padding-bottom: 1em;
  font-family: Arial, Helvetica, sans-serif;
}

div#alert1 p.title {
  margin: 0;
  padding: 0;
  color: white;
  background-color: black;
  text-align: center;
  font-weight: bold;
  border-top: thin solid white;
  border-left: thin solid white;
  border-right: thin solid white;
}
"""

example2 = create_example(example_obj)