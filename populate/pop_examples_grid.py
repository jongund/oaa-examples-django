"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples import *

order = 1

spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='alert')
m2 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='application')
m3 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='button')
m4 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='grid')
m5 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='gridcell')
m6 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='row')
m7 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-disabled')
m8 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-hidden')
m9 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-label')
m10 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-labelledby')
m11 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-live')
m12 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-pressed')
m13 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-selected')
m14 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='presentation')
m15 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-readonly')
m16 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-sort')

# =============================
# Example 1
# =============================

example_obj             = example_object()
example_obj.example_id = 18
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order       = order
example_obj.title       = 'Grid: Reimbursement Form'
example_obj.permanent_slug = 'grid1'

example_obj.a11y_features = """
Simple example of a grid widget to implement a travel reimbursement form.
"""
example_obj.keyboard    = """
<p><a href="http://dev.aol.com/dhtml_style_guide#grid">Based on the keyboard shortcuts defined in the AOL DHTML Style guide for grid</a></p>
* Tab (standard mode): Move focus between grid, links and form controls.
* Tab (actionable mode): Move focus.
* ENTER or F2 (standard mode): Edit contents of gridcell.
* ENTER or F2 (Actionable mode): Update the contents of the gridcell.
* ESC (Actionable mode): Move to standard mode, do not update the contents of the gridcell.
* Up Arrow: Move focus to gridcell in previous row
* Down Arrow: Move focus to gridcell in next row
* Left Arrow: Move focus one gridcell to the left.
* Right Arrow: Move focus one gridcell to the right.
* Home: Move focus to first gridcell in the row.
* End: Move focus to the last gridcell to the row.
* Page Up: Move focus to the first gridcell in the columm.
* Page Down: Move focus to the last gridcell in the column.
"""
example_obj.aria_labelledby = True

example_obj.markup = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13]

example_obj.html        = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<div role="application">

    <table id="expenses" role="grid" summary="ARIA Enabled Travel Reimbursement Form Example">
        <caption>ARIA Enabled Travel Reimbursement Form Example</caption>
        <thead>
        <tr>
            <th id="date" rowspan="2">Date</th>
            <th id="from" colspan="2">Departed From</th>
            <th id="to" colspan="2">Arrived At</th>
            <th id="miles" rowspan="2">Automobile<br/> Miles</th>
            <th id="mileage" rowspan="2">Mileage <br/>Reimbursement</th>
            <th id="trans" colspan="3">Other Transportation Cost</th>
            <th id="lodging" rowspan="2">Lodging</th>
            <th id="meals" rowspan="2">Meals</th>
            <th id="misc" rowspan="2">Miscellaneous</th>
            <th id="total" rowspan="2">Daily<br/>Total</th>
        </tr>
        <tr>
            <th id="location1">Location</th>
            <th id="time1">Time</th>
            <th id="location2">Location</th>
            <th id="time2">Time</th>
            <th id="trans-other">Air, Rails, etc..</th>
            <th id="trans-rental">Car Rental</th>
            <th id="trans-misc">Taxi, Parking, Tolls, etc..</th>
        </tr>
        </thead>
        <tbody id="data">
        <tr id="totals" role="row">
            <th id="total-expenses-lbl" class="calc" role="gridcell" colspan="6">
               <div id="addRow" role="button" class="addButton" tabindex="0" title="Add new row" aria-pressed="false" aria-disabled="false">+</div>
               Total Travel Expenses
            </td>
            <td id="calc-total-mileage" class="calc" role="gridcell" headers="total-expenses-lbl mileage" aria-label="Total Mileage">-</td>
            <td id="calc-total-trans-other" class="calc" role="gridcell" headers="total-expenses-lbl trans-other" aria-label="Total air or rail transportation">-</td>
            <td id="calc-total-trans-rental" class="calc" role="gridcell" headers="total-expenses-lbl trans-rental" aria-label="Total car rental">-</td>
            <td id="calc-total-trans-misc" class="calc" role="gridcell" headers="total-expenses-lbl trans-misc" aria-label="Total taxi, parking and tolls">-</td>
            <td id="calc-total-lodging" class="calc" role="gridcell" headers="total-expenses-lbl lodging" aria-label="Total lodging">-</td>
            <td id="calc-total-meals" class="calc" role="gridcell" headers="total-expenses-lbl meals" aria-label="Total meals">-</td>
            <td id="calc-total-misc" class="calc" role="gridcell" headers="total-expenses-lbl misc" aria-label="Total miscellaneous">-</td>
            <td id="calc-total-reimbursement" class="reimbursement" role="gridcell" headers="total-expenses-lbl total" aria-label="Total reimbursement" aria-live="polite">-</td>
        </tr>
        <tr>
            <th id="msg">Messages: </th><td headers="msg" colspan="13" id="alert" role="alert">&nbsp;</td>
        </tr>  
        </tbody>
    </table>

    <div id="debug"></div>  
    
    <div id="row_numbers" class="offscreen"></div>  
</div>
"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};
$(document).ready(function () {

	// Create an instance of the travel Calculator. Parameters are the table to use,
	// the per-mile reimbursement, the maximum number of data rows, and the initial
	// number of rows to create.
	var app = new OAA_EXAMPLES.travelCalc('table#expenses', 0.15, 5, 1);

}); // end ready function

function keyCodes () {
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

	this.left       = 37;
	this.up         = 38;
	this.right      = 39;
	this.down       = 40; 

	this.insert     = 45; 
	this.del        = 46; 

	this.f2         = 113; 
}

/**
* @constructor travelCalc
*
* @memberOf OAA_EXAMPLES
*
* @desc a class to implement a simple travel reimbusement calculator
*
* @param {string} table - the id of the table to operate on
*
* @param {integer} maxRows - the maximum number of rows an instance of
* travelCalc may have
*
* @param {integer} initNum - the number of rows to add during object instantiation
*
* @return {N/A}
*/

/**
* @private
* @constructor Internal Properties
*
* @property {integer} maxRows - maximum number of rows allowed this instance
* @property {integer} numRows - The current number of rows belonging to instance
* @property {integer} curRow - The currently selected row
* @property {integer} curCol - The currently selected column
*
* @property {object} $tbody - Store the tbody object
* @property {object} $addButton - Store the add row button object
*
* @property {boolean} editMode - True if in edit mode
*/

OAA_EXAMPLES.travelCalc = function(table, reimbursement, maxRows, initNum) {

	var thisObj = this; // Store the this pointer

	// Define class properties
	this.reimbursement = reimbursement;
	this.maxRows = maxRows;
	this.numRows = 0;	
	this.curRow = 0;	
	this.curCol = 0;	
	this.$tbody = $(table).find('tbody#data'); 
   this.$addButton = $(table).find('.addButton'); 
	this.editMode = false;

	this.keys = new keyCodes();

	// Bind handlers
	this.bindHandlers();

	// Add rows
	for (var ndx = 0; ndx < initNum; ndx += 1) {
		this.addRow();
	}

	// Store the collection of editable table cells in an object property
	// this property must be updated when adding new rows.
	this.$editableCells = this.$tbody.find('td.editable,th.editable');

	// Make first row navigable
	$('#row1-date').attr('tabindex', '0');

} // end travelCalc constructor

/**
* @method addRow
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to add a row to the data grid. Function builds a string containing
* the elements to add, and appends the string to the table. addRow() will not add a new row if
* maxRows has been reached
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.addRow = function() {
	var thisObj = this;	// store a pointer to this object

	// Do not add a new row if maxRows has been reached
	if (this.numRows < this.maxRows) { 
		var label;

		// Increment the number of rows
		this.numRows += 1;

		var row = '<tr role=\"row\" id=\"row' + (this.numRows) + '\">';

		// date cell
		label = 'aria-labelledby=\"date r' + this.numRows + '\"';
		row += '<th id=\"row' + this.numRows + '-date\" role=\"gridcell\" ' +
			'class=\"date editable\" ' + label + 'aria-selected="false" tabindex=\"-1\">' +
			'<span id=\"row' + this.numRows + '-date-dta\" class=\"data\" aria-hidden=\"false\"></span>' +
			'<input id=\"row' + this.numRows + '-date-edt\" class=\"edt\" type=\"text\" aria-hidden=\"true\" size=\"6\" title=\"Enter travel date of trip ' + this.numRows + '\" />' +
			'</th>';

		// Departure location cell
		headers = 'headers=\"location1 row' + this.numRows + '-date\"';
		row += '<td id=\"row' + this.numRows + '-location1\" role=\"gridcell\" ' +
			'class=\"location editable\" ' + headers + 'aria-selected="false" tabindex=\"-1\">' +
			'<span id=\"row' + this.numRows + '-location1-dta\" class=\"data\" aria-hidden=\"false\"></span>' +
			'<input id=\"row' + this.numRows + '-location1-edt\" class=\"edt\" type=\"text\" aria-hidden=\"true\" size=\"12\" title=\"Enter departure location for trip ' + this.numRows + '\" />' +
			'</td>';

		// Departure time cell
		headers = 'headers=\"time1 row' + this.numRows + '-date\"';
		row += '<td id=\"row' + this.numRows + '-time1\" role=\"gridcell\" ' +
			'class=\"time editable\" ' + headers + 'aria-selected="false" tabindex=\"-1\">' +
			'<span id=\"row' + this.numRows + '-time1-dta\" class=\"data\" aria-hidden=\"false\"></span>' +
			'<input id=\"row' + this.numRows + '-time1-edt\" class=\"edt\" type=\"text\" aria-hidden=\"true\" size=\"6\" title=\"Enter departure time for trip ' + this.numRows + '\" />' +
			'</td>';

		// Arrived at cell
		headers = 'headers=\"location2 row' + this.numRows + '-date\"';
		row += '<td id=\"row' + this.numRows + '-location2\" role=\"gridcell\" ' +
			'class=\"location editable\" ' + headers + 'aria-selected="false" tabindex=\"-1\">' +
			'<span id=\"row' + this.numRows + '-location2-dta\" class=\"data\" aria-hidden=\"false\"></span>' +
			'<input id=\"row' + this.numRows + '-location2-edt\" class=\"edt\" type=\"text\" aria-hidden=\"true\" size=\"12\" title=\"Enter destination for trip ' + this.numRows + '\" />' +
			'</td>';

		// Arrival time cell
		headers = 'headers=\"time2 row' + this.numRows + '-date\"';
		row += '<td id=\"row' + this.numRows + '-time2\" role=\"gridcell\" ' +
			'class=\"time editable\" ' + headers + 'aria-selected="false" tabindex=\"-1\">' +
			'<span id=\"row' + this.numRows + '-time2-dta\" class=\"data\" aria-hidden=\"false\"></span>' +
			'<input id=\"row' + this.numRows + '-time2-edt\" class=\"edt\" type=\"text\" aria-hidden=\"true\" size=\"6\" title=\"Enter arrival time for trip ' + this.numRows + '\" />' +
			'</td>';

		// Automobile miles cell
		headers = 'headers=\"miles row' + this.numRows + '-date\"';
		row += '<td id=\"row' + this.numRows + '-miles\" role=\"gridcell\" ' +
			'class=\"miles editable\" ' + headers + 'aria-selected="false" tabindex=\"-1\">' +
			'<span id=\"row' + this.numRows + '-miles-dta\" class=\"data\" aria-hidden=\"false\"></span>' +
			'<input id=\"row' + this.numRows + '-miles-edt\" class=\"edt\" type=\"text\" aria-hidden=\"true\" size=\"6\" title=\"Enter miles driven for trip ' + this.numRows + '\" />' +
			'</td>';

		// Mileage reimbursement cell
		headers = 'headers=\"mileage row' + this.numRows + '-date\"';
		row += '<td id=\"row' + this.numRows + '-mileage\" role=\"gridcell\" ' +
			'class=\"calc\" ' + headers + 'tabindex=\"-1\">-</td>';

		// Air et al. transportation cost cell
		headers = 'headers=\"trans-other row' + this.numRows + '-date\"';
		row += '<td id=\"row' + this.numRows + '-trans-other\" role=\"gridcell\" ' +
			'class=\"expense editable\" ' + headers + 'aria-selected="false" tabindex=\"-1\">' +
			'<span id=\"row' + this.numRows + '-trans-other-dta\" class=\"data\" aria-hidden=\"false\"></span>' +
			'<input id=\"row' + this.numRows + '-trans-other-edt\" class=\"edt\" type=\"text\" aria-hidden=\"true\" size=\"6\" title=\"Enter air, rail, or other major travel expense for trip ' +
         this.numRows + '\" />' +
			'</td>';

		// Car rental transportation cost cell
		headers = 'headers=\"trans-rental row' + this.numRows + '-date\"';
		row += '<td id=\"row' + this.numRows + '-trans-rental\" role=\"gridcell\" ' +
			'class=\"expense editable\" ' + headers + 'aria-selected="false" tabindex=\"-1\">' +
			'<span id=\"row' + this.numRows + '-trans-rental-dta\" class=\"data\" aria-hidden=\"false\"></span>' +
			'<input id=\"row' + this.numRows + '-trans-rental-edt\" class=\"edt\" type=\"text\" aria-hidden=\"true\" size=\"6\" title=\"Enter car rental expense for trip ' + this.numRows + '\" />' +
			'</td>';

		// Misc. transportation cost cell
		headers = 'headers=\"trans-misc row' + this.numRows + '-date\"';
		row += '<td id=\"row' + this.numRows + '-trans-misc\" role=\"gridcell\" ' +
			'class=\"expense editable\" ' + headers + 'aria-selected="false" tabindex=\"-1\">' +
			'<span id=\"row' + this.numRows + '-trans-misc-dta\" class=\"data\" aria-hidden=\"false\"></span>' +
			'<input id=\"row' + this.numRows + '-trans-misc-edt\" class=\"edt\" type=\"text\" aria-hidden=\"true\" size=\"6\" title=\"Enter miscellaneous expenses, such as parking, tolls, or taxi, for trip ' +
         this.numRows + '\" />' +
			'</td>';

		// Lodging cost cell
		headers = 'headers=\"lodging row' + this.numRows + '-date\"';
		row += '<td id=\"row' + this.numRows + '-lodging\" role=\"gridcell\" ' +
			'class=\"expense editable\" ' + headers + 'aria-selected="false" tabindex=\"-1\">' +
			'<span id=\"row' + this.numRows + '-lodging-dta\" class=\"data\" aria-hidden=\"false\"></span>' +
			'<input id=\"row' + this.numRows + '-lodging-edt\" class=\"edt\" type=\"text\" aria-hidden=\"true\" size=\"6\" title=\"Enter lodging expense for trip ' + this.numRows + '\" />' +
			'</td>';

		// Meals cost cell
		headers = 'headers=\"meals row' + this.numRows + '-date\"';
		row += '<td id=\"row' + this.numRows + '-meals\" role=\"gridcell\" ' +
			'class=\"expense editable\" ' + headers + 'aria-selected="false" tabindex=\"-1\">' +
			'<span id=\"row' + this.numRows + '-meals-dta\" class=\"data\" aria-hidden=\"false\"></span>' +
			'<input id=\"row' + this.numRows + '-meals-edt\" class=\"edt\" type=\"text\" aria-hidden=\"true\" size=\"6\" title=\"Enter meal expense for trip ' + this.numRows + '\" />' +
			'</td>';

		// Misc. cost cell
		headers = 'headers=\"misc row' + this.numRows + '-date\"';
		row += '<td id=\"row' + this.numRows + '-misc\" role=\"gridcell\" ' +
			'class=\"expense editable\" ' + headers + 'aria-selected="false" tabindex=\"-1\">' +
			'<span id=\"row' + this.numRows + '-misc-dta\" class=\"data\" aria-hidden=\"false\"></span>' +
			'<input id=\"row' + this.numRows + '-misc-edt\" class=\"edt\" type=\"text\" aria-hidden=\"true\" size=\"6\" title=\"Enter other miscellaneous expenses for trip ' + this.numRows + '\" />' +
			'</td>';

		// Row total cell and closing tr
		headers = 'headers=\"total row' + this.numRows + '-date\"';
		row += '<td id=\"row' + this.numRows + '-total\" class=\"calc\" ' + headers + '>-</td></tr>'

		// Append the new row to the grid
		$('tbody').find('tr#totals').before(row);

		// Add an entry for this row in the list of rows
		$('#row_numbers').append('<div id=\"r' + this.numRows + '\">Row ' + this.numRows + '</div>');
	}
   else {
			$('td#alert').text('Maximum number of rows (' + this.maxRows + ') reached.');
         this.$addButton.unbind('mousedown mouseup keydown keyup');
         this.$addButton.addClass('disabled');
         this.$addButton.attr('aria-disabled', 'true');
         this.$addButton.removeClass('pressed');
         this.$addButton.attr('aria-pressed', 'false');
   }

} //end addRow()

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers to the tbody of the data table. This uses event* 
* delegation to manage events for the children cells. Event delegation is much faster than binding to each cell,
* and it also allows new table rows to be handled.
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.bindHandlers = function() {
	var thisObj = this;	// store a pointer to this object
	var $tbody = this.$tbody; // store a pointer to the table body property (saves a dereference)
	var $button = this.$addButton; // store a pointer to the add row button property (saves a dereference)

	/************ Bind the handlers for the editable grid cells  in the data table **********/
	//

	// bind a click handler
	$tbody.delegate('.editable', 'click', function (e) {
			return thisObj.handleCellClick(this, e);
	}); // end click handler

	// bind a double click handler
	$tbody.delegate('.editable', 'dblclick', function (e) {
			return thisObj.handleCellDblclick(this, e);
	}); // end double click handler

	// bind a keydown handler
	$tbody.delegate('.editable', 'keydown', function (e) {
			return thisObj.handleCellKeyDown(this, e);
	}); // end keydown handler

	// bind a keypress handler - consume events for Opera
	$tbody.delegate('.editable', 'keypress', function (e) {
			return thisObj.handleCellKeyPress(this, e);
	}); // end keyup handler

	// bind a focus handler
	$tbody.delegate('.editable', 'focus', function (e) {
			return thisObj.handleCellFocus(this, e);
	}); // end focus handler

	// bind a blur handler
	$tbody.delegate('.editable', 'blur', function (e) {
			return thisObj.handleCellBlur(this, e);
	}); // end blur handler


	/************ Bind the handlers for the edit boxes in the editable cells **********/
	
	// bind a keydown handler
	$tbody.delegate('input.edt', 'keydown', function (e) {
			return thisObj.handleEditKeyDown(this, e);
	}); // end edit box keydown handler

	// bind a keypress handler - consume events for Opera
	$tbody.delegate('input.edt', 'keypress', function (e) {
			return thisObj.handleEditKeyPress(this, e);
	}); // end edit box keyup handler

	// bind a focus handler
	$tbody.delegate('input.edt', 'focus', function (e) {
			return thisObj.handleEditFocus(this, e);
	}); // end edit box focus handler

	// bind a blur handler
	$tbody.delegate('input.edt', 'blur', function (e) {
			return thisObj.handleEditBlur(this, e);
	}); // end edit box blurhandler

	/************ Bind the handlers for the add row button **********/
	
	// bind a mousedown handler
	$button.mousedown(function (e) {
			return thisObj.handleAddMouseDown(this, e);
	}); // end add button mousedown handler

	// bind a mouseup handler
	$button.mouseup(function (e) {
			return thisObj.handleAddMouseUp(this, e);
	}); // end add button mouseup handler

	// bind a keydown handler
	$button.keydown(function (e) {
			return thisObj.handleAddKeyDown(this, e);
	}); // end add button keydown handler

	// bind a keyup handler
	$button.keyup(function (e) {
			return thisObj.handleAddKeyUp(this, e);
	}); // end add button keyup handler

	// bind a focus handler
	$button.focus(function (e) {
			return thisObj.handleAddFocus(this, e);
	}); // end add button focus handler

	// bind a blur handler
	$button.blur(function (e) {
			return thisObj.handleAddBlur(this, e);
	}); // end add button blur handler

} // end bindHandlers()


/**
* @method enterEditMode
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to enter the edit mode of an editable cell
*
* @param {object} id - the jQuery object of the cell to operate on
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.enterEditMode = function($id) {

	var $edt = $id.find('.edt');
	var $data = $id.find('.data');
	
	// Clear any old alert messages
	$('td#alert').text('');

	// Set the editMode flag to true -- make edit mode modal
	// This is faster than unbinding edit cell event handlers
	this.editMode = true;

	// Copy the data from the cell's data span into the edit box
	$edt.val($data.text());

	// hide the data and show the edit box
	$data.hide();
   $data.attr('aria-hidden', 'true');
	$edt.show();
   $edt.attr('aria-hidden', 'false');

	// give the edit box focus
	$edt.focus();

} // end enterEditMode()

/**
* @methodleaveEditMode
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to exit the edit mode of an editable cell
*
* @param {object} id - the jQuery object of the cell to operate on
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.leaveEditMode = function(id) {

	var $cell = $(id);
	var $edt = $cell.find('.edt');
	var $data = $cell.find('.data');
	var thisObj = this;
	var validEntry = true;


	// Make sure we are actually in edit mode
	if (this.editMode == false) {
		return;
	}

	// Validate the input
	if ($cell.hasClass('date')) {

		if (this.validateDate($edt) == true) {

			// Store the changes
			$data.text($edt.val());
		}
	}
	else if ($cell.hasClass('time')) {

		if (this.validateTime($edt) == true) {

			// Store the changes
			$data.text($edt.val());
		}
	}
	else if ($cell.hasClass('miles')) {

		if (this.validateMiles($edt) == true) {

			var $reimbursementCell = $cell.next(); 

			// Store the changes
			$data.text($edt.val());

			// Calculate the mileage reimbursement
			$reimbursementCell.text( this.calcMileAmount($edt.val()) );

			// recalculate the daily total
			this.calcDaily($cell.attr('id').split('-')[0])

			// recalculate the mileage reimbursement total
			this.calcMileageTotal();

			// recalculate the total reimbursement
			this.calcTotalReimbursement();
		}
	}
	else if ($cell.hasClass('expense')) {

		if (this.validateExpense($edt) == true) {

			// Store the changes
			$data.text($edt.val());

			// recalculate the daily total
			this.calcDaily($cell.attr('id').split('-')[0])

			// recalculate the column total
			this.calcExpenseTotal($cell.attr('id'))

			// recalculate the total reimbursement
			this.calcTotalReimbursement();
		}
	}
	else {
		// Don't validate; just store the changes
		$data.text($edt.val());
	}

	// Set the editMode flag to false
	this.editMode = false;

	// Hide the edit box and show the data
	$edt.hide();
   $edt.attr('aria-hidden', 'true');
	$data.show();
   $data.attr('aria-hidden', 'false');

	// Give the parent focus
	$cell.focus();


} // end leaveEditMode()

/**
* @method validateDate
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to validate data entered in the date column
*
* @param {object} id - the jQuery object of the edit box the user modified
*
* @return {boolean} true if valid entry; false if invalid
*/

OAA_EXAMPLES.travelCalc.prototype.validateDate = function($edt) {

	var curDate = new Date();

	if ($edt.val() != "") {
		// try parsing as date using JavaScript Date constructor
		var dateValue = new Date($edt.val().replace(/-/g, '/'));


		if (isFinite(dateValue)) {

			// If user entered 2-digit year, the date will be approximately 100 years off. Check for this and correct
			if (curDate.getFullYear() - dateValue.getFullYear() >= 99) {
				dateValue.setFullYear(dateValue.getFullYear() + 100);
			}

			// Check if date entered is in the future
			if (dateValue > curDate) {
				$('td#alert').text('Date must be before the current date');
				return false;
			}

			// Set date to 60 days in the past
			curDate.setDate(curDate.getDate() - 60);

			// Check if date entered is older than 60 days ago
			if (dateValue < curDate) {
				$('td#alert').text('Date must be within the last 60 days');
				return false;
			}

			// format as mm/dd/yyyy
			$edt.val( (dateValue.getMonth() + 1) + '/' + dateValue.getDate() + '/' + dateValue.getFullYear() );
			return true;
		}
		else {
			$('td#alert').text('Date needs to be in date format, such as 1/31/2001.');
			return false;
		}
	}

	return false;

} // end validateDate()

/**
* @method validateTime
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to validate data entered in the time columns
*
* @param {object} id - the jQuery object of the edit box the user modified
*
* @return true if valid entry; false if invalid
*/

OAA_EXAMPLES.travelCalc.prototype.validateTime = function($edt) {

	if ($edt.val() != "") {
		var str = $.trim($edt.val());

		if (/^(0?[1-9]|1[0-2]):[0-5]\\d ?([ap]m?)?$/.test(str) == false) {

			$('td#alert').text('Time must be in valid time format, such as h:mm [am|pm]');
			return false;
		}
	}

	return true;

} // end validateTime()

/**
* @method validateMiles
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to validate data entered in the Automobile Miles column
*
* @param {object} id - the jQuery object of the edit box the user modified
*
* @return true if valid entry; false if invalid
*/

OAA_EXAMPLES.travelCalc.prototype.validateMiles = function($edt) {

	if ($edt.val() != "") {
		var str = $.trim($edt.val());

		if (/^\\d*$/.test(str) == false) {

			$('td#alert').text('Automobile Miles must be a number');
			return "Invalid";
		}
	}

	return true;

} // end validateMiles()

/**
* @method validateExpense
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to validate data entered in the expense columns
*
* @param {object} id - the jQuery object of the edit box the user modified
*
* @return {boolean} true if valid entry; false if invalid
*/

OAA_EXAMPLES.travelCalc.prototype.validateExpense = function($edt) {

	if ($edt.val() != "") {
		var str = $.trim($edt.val());

		if (/^\\$?[1-9]\\d{0,2}(,\\d{3})*(\\.\\d{0,2})?$/.test(str) ) {

			if (str.charAt(0) != '$') {
				str = '$' + str;
			}//spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')
			
			if (/\\.\\d$/.test(str)) {
				str += "0";
			}
			else if (/\\.$/.test(str) ) {
				str += "00";
			}
			else if (!/\\.\\d{2}$/.test(str) ) {
				str += ".00";
			}
			$edt.val(str);
			return true;
		}
		else {
			$('td#alert').text('Expense must be in valid US money format, such as $1,000.00');
			return "Invalid";
		}
	}

	return true;

} // end validateExpense()

/**
* @method calcMileAmount
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to calculate the automobile mileage reimbursement for a trip
*
* @param {integer} miles - the total miles entered in the Automobile Miles column
*
* @return {string} The calculated reimbursement, in U.S. currency format
*/

OAA_EXAMPLES.travelCalc.prototype.calcMileAmount = function(miles) {

	var amount = '$' + (miles * this.reimbursement); 
	var tmp = amount.split('.');

	// If cents is defined, round to the nearest cent
	if (tmp[1] != undefined) {
		var rounded = Math.round(tmp[1].substr(0,2) + '.' + tmp[1].substr(2));
		amount = tmp[0] + '.' + rounded;
	}

	// Add cents
	if (/\\.\\d$/.test(amount)) {
		amount += "0";
	}
	else if (/\\.$/.test(amount) ) {
		amount += "00";
	}
	else if (!/\\.\\d{2}$/.test(amount) ) {
		amount += ".00";
	}

	return amount;
}

/**
* @method calcDaily
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to calculate the daily total cost of a trip
*
* @param {string} row - the id of the current row the user modified
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.calcDaily = function(row) {
	var total = $('#' + row + '-mileage').text().substr(1); // Strip the '$'

	if (total.length) {
		// remove any ',' from the value and convert to a float
		total = parseFloat(total.replace(/,/g, ''));
	}
	else {
		total = 0;
	}

	// Add the total for each expense
	$('#' + row).find('td.expense').each(function() {
		var expense = $(this).find('.data').text().substr(1);

		if (expense.length) {
			// remove any ',' from the value
			expense = expense.replace(/,/g, '');
				
			total += parseFloat(expense);
		}
	});

	// Add cents
	if (/\\.\\d$/.test(total)) {
		total += "0";
	}
	else if (/\\.$/.test(total) ) {
		total += "00";
	}
	else if (!/\\.\\d{2}$/.test(total) ) {
		total += ".00";
	}
	
	$('#' + row + '-total').text('$' + total);
}

/**
* @method calcMileageTotal
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to calculate the total mileage Reimbursement amount
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.calcMileageTotal = function() {

	var total = 0;

	// Iterate through the column, adding the expense to the total.
	for (var row = 1; row <= this.numRows ; row++) {
		var expense = $('#row' + row + '-mileage').text().substr(1); // strip the'$' from the expense

		if (expense.length) {
			// remove any ',' from the value
			expense = expense.replace(/,/g, '');
				
			total += parseFloat(expense);
		}
	}

	// Add cents
	if (/\\.\\d$/.test(total)) {
		total += "0";
	}
	else if (/\\.$/.test(total) ) {
		total += "00";
	}
	else if (!/\\.\\d{2}$/.test(total) ) {
		total += ".00";
	}

	$('#calc-total-mileage').text('$' + total);
}

/**
* @method calcExpenseTotal
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to calculate the total expense for a column
*
* @param {string} id - the id of the column to update
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.calcExpenseTotal = function(id) {

	var total = 0;
	var col = id.substr(id.indexOf('-'));

	// Iterate through the column, adding the expense to the total.
	for (var row = 1; row <= this.numRows ; row++) {
		var expense = $('#row' + row + col).find('span').text().substr(1); // strip the'$' from the expense

		if (expense.length) {
			// remove any ',' from the value
			expense = expense.replace(/,/g, '');
				
			total += parseFloat(expense);
		}
	}

	// Add cents
	if (/\\.\\d$/.test(total)) {
		total += "0";
	}
	else if (/\\.$/.test(total) ) {
		total += "00";
	}
	else if (!/\\.\\d{2}$/.test(total) ) {
		total += ".00";
	}

	$('#calc-total' + col).text('$' + total);
}

/**
* @method calcTotalReimbursement
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to calculate the total expense reimbursement
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.calcTotalReimbursement = function() {

	var total = 0;

	// Iterate through the column, adding the expense to the total.
	$('th#total-expenses-lbl').siblings().not('td#calc-total-reimbursement').each(function() {
		var expense = $(this).text().substr(1); // strip the'$' from the expense

		if (expense.length) {
			// remove any ',' from the value
			expense = expense.replace(/,/g, '');
				
			total += parseFloat(expense);
		}
	});

	// Add cents
	if (/\\.\\d$/.test(total)) {
		total += "0";//spec_aria10 = LanguageSpec.objects.get(url_slug='aria10');
	}
	else if (/\\.$/.test(total) ) {
		total += "00";
	}
	else if (!/\\.\\d{2}$/.test(total) ) {
		total += ".00";
	}

	$('#calc-total-reimbursement').text('$' + total);
}

/**
* @method handleCellClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback for the click event. It is bound to the editable grid cells
*
* @param {object} id - the element generating the event
*
* @param {object} e - the event object associated with the event
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.handleCellClick = function(id, e) {

	$(id).focus();

	e.stopPropagation();
	return false;

} // end handleCellClick()

/**
* @method handleCellDblclick
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback for the dblclick event. It is bound to the editable grid cells
*
* @param {object} id - the element generating the event
*
* @param {object} e - the event object associated with the event
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.handleCellDblclick = function(id, e) {

	// do nothing if we are in editMode
	if (this.editMode == false) {

		// enter the edit mode for the cell
		this.enterEditMode($(id));
	}

	e.stopPropagation();
	return false;

} //end handleCellDblclick()

/**
* @method handleCellKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback for the keydown event. It is bound to the editable grid cells
*
* @param {object} id - the element generating the event
*
* @param {object} e - the event object associated with the event
*
* @return {boolean} False if specified key is pressed, true if other keypress
*/

OAA_EXAMPLES.travelCalc.prototype.handleCellKeyDown = function(id, e) {

	var $curCell = $(id); // Store the current cell object to prevent repeated DOM traversals

	// do nothing if the shift, alt, or ctrl key is pressed or we are in editMode
	if (e.ctrlKey == true || e.altKey == true || e.shiftKey == true || this.editMode == true) {
		return true;
	}

	switch (e.keyCode) {
		case this.keys.enter:
		case this.keys.f2: {
			// enter the edit mode for the cell
			this.enterEditMode($curCell);

			e.stopPropagation();
			return false;
			break;
		}
		case this.keys.left: {
			var $newCell = $curCell.prev();

			// If there is another editable cell to the right, select it
			if ($newCell.length) {

				if ($newCell.attr('id').search('mileage') > 0) {
					// skip this column
					$newCell = $newCell.prev();
				}

				if ($newCell.hasClass('editable')) {

					// Make the new cell navigable and give it focus
					// Use jQuery chaining for optimization
					$newCell.attr('tabindex', '0').focus();
				}
			}

			e.stopPropagation();
			return false;
			break;
		}
		case this.keys.right: {
			var $newCell = $curCell.next();

			// If there is another editable cell to the right, select it
			if ($newCell.length) {

				if ($newCell.attr('id').search('mileage') > 0) {
					// skip this column
					$newCell = $newCell.next();
				}

				if ($newCell.hasClass('editable')) {

					// Make the new cell navigable and give it focus
					// Use jQuery chaining for optimization
					$newCell.attr('tabindex', '0').focus();
				}
			}

			e.stopPropagation();
			return false;
			break;
		}
		case this.keys.up: {
			// Cell id's are of the form "row#-colName". We need to isolate the row number and
			// column name
			var curRow = $curCell.attr('id');
			var len = curRow.indexOf('-');
			var rowNum = curRow.substr(3, len - 3) - 1;

			if (rowNum > 0)
			{
				// build the id string of the new cell
				var newCell = '#row' + rowNum + '-' + curRow.substr(len + 1);

				// Make the new cell navigable and give it focus
				// Use jQuery chaining for optimization
				$(newCell).attr('tabindex', '0').focus();
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.down: {
			// Cell id's are of the form "row#-colName". We need to isolate the row number and
			// column name
			var curRow = $curCell.attr('id');
			var len = curRow.indexOf('-');
			var rowNum = parseInt(curRow.substr(3, len - 3)) + 1;

			if (rowNum <= this.numRows)
			{
				// build the id string of the new cell
				var newCell = '#row' + rowNum + '-' + curRow.substr(len + 1);

				// Make the new cell navigable and give it focus
				// Use jQuery chaining for optimization
				$(newCell).attr('tabindex', '0').focus();
			}
			e.stopPropagation();
			return false;
		}
		case this.keys.pageup: {
			// Cell id's are of the form "row#-colName". We need to isolate the row number and
			// column name
			var curRow = $curCell.attr('id');
			var len = curRow.indexOf('-');
			var rowNum = parseInt(curRow.substr(3, len - 3)) - 1;

			if (rowNum > 0)
			{
				// build the id string of the new cell
				var newCell = '#row1-' + curRow.substr(len + 1);

				// Make the new cell navigable and give it focus
				// Use jQuery chaining for optimization
				$(newCell).attr('tabindex', '0').focus();
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.pagedown: {
			// Cell id's are of the form "row#-colName". We need to isolate the row number and
			// column name
			var curRow = $curCell.attr('id');
			var len = curRow.indexOf('-');
			var rowNum = parseInt(curRow.substr(3, len - 3)) + 1;

			if (rowNum <= this.numRows)
			{
				// build the id string of the new cell
				var newCell = '#row' + this.numRows + '-' + curRow.substr(len + 1);

				// Make the new cell navigable and give it focus
				// Use jQuery chaining for optimization
				$(newCell).attr('tabindex', '0').focus();
			}
			e.stopPropagation();
			return false;
		}
		case this.keys.home: {
			var row = $curCell.attr('id').split('-')[0];

			// Make the new cell navigable and give it focus
			// Use jQuery chaining for optimization
			$('#' + row + '-date').attr('tabindex', '0').focus();

			e.stopPropagation();
			return false;
			break;
		}
		case this.keys.end: {
			var row = $curCell.attr('id').split('-')[0];

			// Make the new cell navigable and give it focus
			// Use jQuery chaining for optimization
			$('#' + row + '-misc').attr('tabindex', '0').focus();

			e.stopPropagation();
			return false;
			break;
		}

	}

	return true;

} // end handleCellKeyDown

/**
* @method handleCellKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback for the keypress event. It is bound to the editable grid cells
*
* @param {object} id - the element generating the event
*
* @param {object} e - the event object associated with the event
*
* @return {boolean} False if specified key is released, true if other key released
*/

OAA_EXAMPLES.travelCalc.prototype.handleCellKeyPress = function(id, e) {

	// do nothing if the shift, alt, or ctrl key is pressed or we are in editMode
	if (e.ctrlKey == true || e.altKey == true || e.shiftKey == true || this.editMode == true) {
		return true;
	}
	
	switch (e.keyCode) {
		case this.keys.enter:
		case this.keys.f2:
		case this.keys.left:
		case this.keys.right:
		case this.keys.up:
		case this.keys.down:
		case this.keys.pageup:
		case this.keys.pagedown:
		case this.keys.home:
		case this.keys.end: {

			e.stopPropagation();
			return false;
			break;
		}
	}

	return true;

} // end handleCellKeyPress

/**
* @method handleCellFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback for the focus event. It is bound to the editable grid cells
*
* @param {object} id - the element generating the event
*
* @param {object} e - the event object associated with the event
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.handleCellFocus = function(id, e) {

	// Remove the highlighting from the table cells and remove them from the tab order.
	// Use jQuery chaining for optimization
	this.$editableCells.attr('tabindex', '-1').removeClass('focus').attr('aria-selected', 'false');

	// Add the highlighting for the focused cell and make it navigable
	// Use jQuery Chaining for optimization
	$(id).addClass('focus').attr('tabindex', '0').attr('aria-selected', 'true');

	return true;

} // end handleCellFocus()

/**
* @method handleCellBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback for the blur event. It is bound to the editable grid cells
*
* @param {object} id - the element generating the event
*
* @param {object} e - the event object associated with the event
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.handleCellBlur = function(id, e) {

	var $cell = $(id);
	// do nothing if we are in editMode
	if (this.editMode == false) {
		$cell.removeClass('focus').attr('aria-selected', 'false');
	}
	return true;

} // end handleCellBlur()

/**
* @method handleEditKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback for the keydown event. It is bound to the edit boxes in the editable grid cells
*
* @param {object} id - the element generating the event
*
* @param {object} e - the event object associated with the event
*
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.handleEditKeyDown = function(id, e) {

	var $parentNode = $(id).parent();
	var $newNode;
	
	// do nothing if the ctrl or alt key is pressed
	if (e.ctrlKey == true || e.altKey == true) {
		return true;
	}

	switch (e.keyCode) {
		case this.keys.tab: {
			var haveNewCell = false;

			if (e.shiftKey) {
				//shift-tabspec_aria10 = LanguageSpec.objects.get(url_slug='aria10');
				$newNode = $parentNode.prev();
				if ($newNode.length) {
					if ($newNode.attr('id').search('mileage') > 0) {
						$newNode = $newNode.prev();
					}

					haveNewCell = true;
				}
			}
			else {
				$newNode = $parentNode.next();
				if ($newNode.length) {
					if ($newNode.attr('id').search('mileage') > 0) {
						$newNode = $newNode.next();
					}

					haveNewCell = true;
				}
			}
			// leave edit mode
			this.leaveEditMode($parentNode);

			// Select the next editable cell (if possible)
			if (haveNewCell == true && $newNode.is('.editable')) {
				$newNode.focus();
			}

			e.stopPropagation();
			return false;
			break;
		}
		case this.keys.enter:
		case this.keys.f2:
		case this.keys.esc: {
			// leave edit mode
			this.leaveEditMode($parentNode);
			e.stopPropagation();
			return false;
			break;
		}
	}

	return true;

} // end handleEditKeyDown()

/**
* @method handleEditKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback for the keypress event. It is bound to the edit boxes in the editable grid cells
*
* @param {object} id - the element generating the event
*
* @param {object} e - the event object associated with the event
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.handleEditKeyPress = function(id, e) {

	// do nothing if the ctrl or alt key is pressed
	if (e.ctrlKey == true || e.altKey == true) {
		return true;
	}
	switch (e.keyCode) {
		case this.keys.tab:
		case this.keys.enter:
		case this.keys.f2:
		case this.keys.esc: {
			e.stopPropagation();
			return false;
			break;
		}
	}
	return true;
} // end handleEditKeyPress()

/**
* @method handleEditFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback for the focus event. It is bound to the edit boxes in the editable grid cells
*
* @param {object} id - the element generating the event
*
* @param {object} e - the event object associated with the event
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.handleEditFocus = function(id, e) {
	
	var $parentNode = $(id).parent();
	
	return true;
}

/**
* @method handleEditBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback for the blur event. It is bound to the edit boxes in the editable grid cells
*
* @param {object} id - the element generating the event
*
* @param {object} e - the event object associated with the event
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.handleEditBlur = function(id, e) {

	var $parentNode = $(id).parent();
	
	// leave edit mode
	this.leaveEditMode($parentNode);

	e.stopPropagation();
	return false;
}

/**
* @method handleAddMouseDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback for the mousedown event. It is bound to the add row butto
*
* @param {object} id - the element generating the event
*
* @param [object] e - the event object associated with the event
*
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.handleAddMouseDown = function(id, e) {

   $(id).addClass('pressed');
   $(id).attr('aria-pressed', 'true')
   this.addRow();
   $(id).removeClass('pressed');
   $(id).attr('aria-pressed', 'false')
   $(id).focus();

	e.stopPropagation();
	return false;

} // end handleAddMouseDown()

/**
* @method handleAddMouseUp
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback for the mouseup event. It is bound to the add row button
*
* @param {object} id - the element generating the event
*
* @param {object} e - the event object associated with the event
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.handleAddMouseUp = function(id, e) {

   $(id).removeClass('pressed');
   $(id).attr('aria-pressed', 'false')

	e.stopPropagation();
	return false;

} // end handleAddMouseUp()

/**
* @method handleAddKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback for the keydown event. It is bound to the add row button
*
* @param {object} id - the element generating the event
*
* @param {object} e - the event object associated with the event
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.handleAddKeyDown = function(id, e) {

	// do nothing if the ctrl or alt key is pressed
	if (e.ctrlKey == true || e.altKey == true) {
		return true;
	}
	switch (e.keyCode) {
		case this.keys.enter:
		case this.keys.space: {
         $(id).addClass('pressed');
         $(id).attr('aria-pressed', 'true')
         this.addRow();
			e.stopPropagation();
			return false;
			break;
		}
	}
	return true;
} // end handleAddKeyDown()

/**
* @method handleAddKeyUp
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback for the keyup event. It is bound to the add row button
*
* @param {object} id - the element generating the event
*
* @param {object} e - the event object associated with the event
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.handleAddKeyUp = function(id, e) {

	// do nothing if the ctrl or alt key is pressed
	if (e.ctrlKey == true || e.altKey == true) {
		return true;
	}
	switch (e.keyCode) {
		case this.keys.enter:
		case this.keys.space: {
         $(id).removeClass('pressed');
         $(id).attr('aria-pressed', 'false')
			e.stopPropagation();
			return false;
			break;
		}
	}
	return true;
} // end handleAddKeyDown()

/**
* @method handleAddFocus()
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback for the focus event. It is bound to the add row button
*
* @param {object} id - the element generating the event
*
* @param {object} e - the event object associated with the event
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.handleAddFocus = function(id, e) {
	
	$(id).addClass('buttonFocus');
	return true;
}

/**
* @method handleAddBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback for the blur event. It is bound to the add row button
*
* @param {object} id - the element generating the event
*
* @param {object} e - the event object associated with the event
*
* @return {N/A}
*/

OAA_EXAMPLES.travelCalc.prototype.handleAddBlur = function(id, e) {

	$(id).removeClass('buttonFocus pressed');
   $(id).attr('aria-pressed', 'false')
	return false;
}
"""

example_obj.style       = """
table#expenses {
	margin: 0;
	padding: 0;
	border: 1px solid black;
	border-spacing: 0;
}

caption {
	margin: 0;
	padding: 5px;
	border: 2px solid black;
	font-weight: bold;
	font-size: 1.25em;
	color: #027;
	background-color: #eee;
}

table#expenses th {
	margin: 0;
	padding: 5px;
	border: 1px solid black;
	background-color: #eee;
	color: #027;
}
table#expenses th.date {
background-color: #fff;
font-weight: normal;
}

table#expenses td {
	margin: 0;
	padding: 2px;
   background-color: #fff;
	border: 1px solid black;
	border: 1px solid black;
}

.expense, .miles {
	text-align: right;
}
.calc, .reimbursement {
	background-color: #ffe !important;
	font-weight: bold;
	text-align: right;
	color: #027;
}

#msg, #alert {
	border-top: 3px solid black !important;
}

.offscreen {
	position: absolute;
	top: -30em;
	left: -300em;
}

.edt {
	margin: 1px;
	padding: 0;
	width: 100%;
	border: none;
	background-color: white;
	display: none;
}
.data {
	margin: 0;
	padding: 0;
	width: 100%;
}
div.addButton {
   float: left;
   display: inline;
   width: 1.5em;
   text-align: center;
   font-weight: bold;
   color: #800;
   background-color: #eee;
   border-top: 1px solid #777;
   border-left: 1px solid #777;
   border-right: 2px solid #000;
   border-bottom: 2px solid #000;
}
div.pressed {
   background-color: #fff;
   border-top: 2px solid #000;
   border-left: 2px solid #000;
   border-bottom: 1px solid #777;
   border-right: 1px solid #777;
}
div.disabled {
   background-color: #eee;
   color: #444;
   border-top: 1px solid #777;
   border-left: 1px solid #777;
   border-bottom: 2px solid #000;
   border-right: 2px solid #000;
}
.focus {
	background-color: #79e !important;
}
"""

example1 = create_example(example_obj)

# =============================
# Example 2
# =============================
order += 1

example_obj             = example_object()
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order       = order
example_obj.example_id = 19
example_obj.title       = 'Grid: Email Application'
example_obj.permanent_slug = 'grid2'

example_obj.a11y_features = """
Simple example of a grid widget to implement an email application. Inline images are used to display the visual state of the sort order of the cells.
"""
example_obj.keyboard    = """
<ul>
    <li>Tab: Move focus between web 2.0 widgets, links and form controls.</li>
    <li>Up Arrow: Move focus to previous message</li>
    <li>Down Arrow: Move focus to next message</li>
    <li>Left Arrow: Move focus one column to the left.</li>
    <li>Right Arrow: Move focus one column to the right.</li>
	<li>Space Bar: When in message list, it selects or unselects the current message.</li>
	<li>Space Bar: When the headers, it reorders the list of messages based on that column data.</li>
</ul>
"""

example_obj.markup = [m3, m4, m5, m6, m10, m13, m14, m15, m16]

example_obj.html        = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<div role="application">

<table id="grid1" class="email" role="grid" aria-labelledby="grid1_label" aria-readonly="true">
	   
  <caption id="grid1_label">Inbox</caption>
  
  <thead>
    <tr>
      <th id="grid1_sel" tabindex="-1"><abbr title="Selected">Sel</abbr></th>
      <th id="grid1_msg" tabindex="-1"><abbr title="Message">Msg</abbr></th>
      <th id="grid1_stat" tabindex="-1">Status</th>
      <th id="grid1_att" tabindex="-1"><abbr title="Attachment">Att</abbr></th>
      <th id="grid1_pri" tabindex="-1"><abbr title="Priority">Pri</abbr></th>
      <th id="grid1_from" tabindex="-1">From</th>
      <th id="grid1_sub" tabindex="-1">Subject</th>
      <th id="grid1_date" tabindex="-1">Date</th>
      <th id="grid1_size" tabindex="-1">Size</th>
  </tr>
  </thead>
  
  <tbody id="data">
  </tbody>
</table>
</div>
"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};

var g_data = {
 'emails' :[
  { 'id': 1, 'stat': 1, 'pri': 1, 'from': 'John Smith', 'sub': 'Trip to Florida', 'date': 'Mar 10', 'att': true, 'siz': '2K' },
  { 'id': 2, 'stat': 0, 'pri': 2, 'from': 'Fred Jones', 'sub': 'Lunch on Friday', 'date': 'Mar 12', 'att': false, 'siz': '1K' },
  { 'id': 3, 'stat': 2, 'pri': 3, 'from': 'Jane Johnson', 'sub': 'Proposal for you to review', 'date': 'Mar 13', 'att': true, 'siz': '12K' },
  { 'id': 4, 'stat': 1, 'pri': 4, 'from': 'Bill Smith', 'sub': 'Information on Weekend', 'date': 'Mar 19', 'att': false, 'siz': '122K' },
  { 'id': 5, 'stat': 0, 'pri': 5, 'from': 'Skip Roland', 'sub': 'Opportunity to participate', 'date': 'Mar 20', 'att': true, 'siz': '4K' }
 ] };

$(document).ready(function() {

	var emailApp = new OAA_EXAMPLES.email('grid1');
}); // end ready

//
// keyCodes() is an object to contain keycodes needed for the application
//
function keyCodes() {
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
* @constructor email
*
* @memberOf OAA_EXAMPLES
*
* @desc a class to implement an email application. email() loads example email
* into a simple data table, making the table columns sortable.
* email() must be passed the id of the html table to attach to.
* It assumes that the email data is in a format like g_data
*/

/**
* @constructor Internal Properties
*
* @property {object} $id - the jquery object for the table to attach to.
*
* @property {array} $headers - an array of jquery objects for the header cells
*
* @property {object} $data - the jquery object for the table
*
* @property {array} $cells - an array of jquery objects for the table cells - including the header column
*
* @property {array} labels - human readable labels to columns and cells
*
* @property {priorities} - array of priority levels, from lowest to highest
*
* @property {stat} - status of each label (either unread, read, or reply}
*
* @property {boolean} isSortable - Set to true if data loads correctly and table has sortable columns
*/

OAA_EXAMPLES.email = function(id){

	var thisObj = this;

	this.$id = $('#' + id);
	this.$headers = $('#' + id + ' thead').find('th'); 
	this.$data = this.$id.find('#data'); 
	this.$cells; 

	// create arrays to give human-readable labels to the columns and grid cells
	this.labels = new Array('Selected', 'Message Number', 'Status', 'Attachment', 'Priority', 'From', 'Subject', 'Date', 'Size');
	this.priorities = new Array('lowest', 'low', 'none', 'high', 'highest');
	this.stat = new Array('unread', 'read', 'reply');

	this.keys = new keyCodes();
	this.isSortable = false;

	// Parse the email data structure.
	// This could be from any data source that yields a data structure like g_data
	thisObj.loadData(g_data);

	// make the table sortable
	thisObj.makeSortable(thisObj.$data);

	thisObj.$cells = thisObj.$data.find('th,td');

	// bind event handlers to the application table
	thisObj.bindHandlers();


} // end email() constructor

/**
* @method loadData
*
* @memberOf OAA_EXAMPLES
*
* @desc loads the email data from the data source
*
* @return {N/A}
*/

OAA_EXAMPLES.email.prototype.loadData = function(data) {

	var thisObj = this;
	var row;
	var tmpStr;
	var count = 1;
	var id = thisObj.$id.attr('id');
	var label;

	$.each(data.emails, function(ndx, record) {

		var msgID = id + '_msg' + count;

		row = '<tr id="' + msgID + '" role="row" aria-selected="false">';

		label = msgID + ' ' + id + '_sel"';
		row += '<th id="' + msgID + '_sel" role="gridcell" aria-labelledby="' + label
			+ '" tabindex="0"><input name="email_' + count
			+ '" type="checkbox" tabindex="-1"/></th>';

		row += '<td id="' + msgID + '_msg" role="gridcell" headers="' + msgID + '_sel ' + id + '_msg" tabindex="-1">' + count + '</td>';

		// set tmpstr to be the value of the message status (unread, read, reply)
		tmpStr = thisObj.stat[record.stat];

		row += '<td id="' + msgID + '_stat" role="gridcell" headers="' + msgID + '_sel ' + id + '_stat" tabindex="-1">'
			+ '<span class="hidden">' + tmpStr + '</span><img src="{{EXAMPLE_MEDIA}}images/' + tmpStr
			+ '.gif" alt="' + tmpStr + '" role="presentation"></td>';

		// set tmpstr to indicate an attachment or no attachment
		tmpStr = (record.att == true ? 'attachment': 'no attachment'); 

		row += '<td id="' + msgID + '_att" role="gridcell" headers="' + msgID + '_sel ' + id + '_att" tabindex="-1">'
			+ '<span class="hidden">' + tmpStr + '</span><img src="{{EXAMPLE_MEDIA}}images/'
			+ (record.att == true ? 'attach': 'noattach') + '.gif" alt="' + tmpStr + '" role="presentation"></td>';

		// set tmpStr to be the value of the message priority
		tmpStr = thisObj.priorities[record.pri - 1];

		row += '<td id="' + msgID + '_pri" role="gridcell" headers="' + msgID + '_sel ' + id + '_pri" tabindex="-1">'
			+'<span class="hidden">Priority ' + record.pri + '</span><img src="{{EXAMPLE_MEDIA}}images/priority_'
			+ tmpStr + '.gif" alt="' + tmpStr + '" role="presentation"></td>';

		row += '<td id="' + msgID + '_from" role="gridcell" headers="' + msgID + '_sel ' + id + '_from" tabindex="-1">'
			+ record.from + '</td>';

		row += '<td id="' + msgID + '_sub" role="gridcell" headers="' + msgID + '_sel ' + id + '_sub" tabindex="-1">'
			+ record.sub + '</td>';

		row += '<td id="' + msgID + '_date" role="gridcell" headers="' + msgID + '_sel ' + id + '_date" tabindex="-1">'
			+ record.date + '</td>';

		row += '<td id="' + msgID + '_size" role="gridcell" headers="' + msgID + '_sel ' + id + '_size" tabindex="-1">'
			+ record.siz + '</td></tr>';

		thisObj.$data.append(row);

		count++;
	});

} // end loadData()

/**
* @method makeSortable
*
* @memberOf OAA_EXAMPLES
*
* @desc applies properties to a table necessary to allow for alpha-numeric sorting
*
* @return {N/A}
*/

OAA_EXAMPLES.email.prototype.makeSortable = function() {

	var thisObj = this;

	// iterate through the table elements
	this.$id.each(function () {

		thisObj.$id.alternateRowColors();

		// iterate through the table header
		thisObj.$headers.each(function(column) {

			var $header = $(this);
			var findSortKey;

			// Add the sort-alpha class
			$header.addClass('sort-alpha');

			// find the sort keys
			findSortKey = function ($cell) {
				return $cell.find('.sort-key').text().toUpperCase()
					+ ' ' + $cell.text().toUpperCase();
			};

			if (findSortKey) {
				// Define the header highlighting handler
				$header.find('.sort-button').addClass('clickable');

				$header.append('<button class="sort-button" role="button" type="button" tabindex="-1">'
						+ '<img class="sort-image" src="{{EXAMPLE_MEDIA}}images/sortable.png" title="Sort column" role="presentation">'
						+ '<span class="hidden">Sort ' + $header.text() + ' column</span>'
						+ '</button>');

				thisObj.isSortable = true;


			} // end if
		}); // end each
	}); // end each
} // end makeSortable();

/**
* @method sortTable
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to sort the table rows alpha-numerically based on the active column
*
* @param{object} $id - the jQuery object of the header cell of the column to sort by
*
* return {N/A}
*/

OAA_EXAMPLES.email.prototype.sortTable = function($id) {

	var thisObj = this;
	var colNdx = this.$headers.index($id);
	var sortDirection = 1;

	// if the table is sorted in ascending order, reverse
	// the sort order flag
	if ($id.is('.sorted-asc')) {
		sortDirection = -1;
	}

	// create an array of the table rows
	var rows = this.$data.find('tr').get();

	// iterate through the table rows and store the sort keys for each
	// in an attached expando
	$.each(rows, function (index, row) {
		var $cell;

		// The first column is marked as a header row for screen readers
		// Need to treat it seperately
		if (colNdx == 0) {
			$cell = $(row).children('th').eq(colNdx);
			row.sortKey = $cell.find('.sort-key') + ' '
					+ $cell.find('input').attr('checked');
		}
		else {
			$cell = $(row).children('td').eq(colNdx - 1);

			row.sortKey = $cell.find('.sort-key').text().toUpperCase()
					+ ' ' + $cell.text().toUpperCase();
		}
	});

	// sort the rows
	rows.sort(function(a, b) {

		if (a.sortKey < b.sortKey) {
			// move row a before row b
			// (according to the sort direction)
			return -sortDirection;
		}
		else if (a.sortKey > b.sortKey) {
			// move row a after row b
			return sortDirection;
		}

		// the rows are equal--do nothing
		return 0;
	});

	// iterate through the rows array and reinsert them into the table
	// according to the new sort order
	$.each(rows, function(index, row) {

		// insert the row
		thisObj.$data.append(row);

		// remove the expando
		row.sortKey = null;
	});


	// remove the previous sorted class and reset the button images
	this.$headers
		.removeClass('sorted-asc')
		.removeClass('sorted-desc') 
      .removeAttr('aria-sorted')
      .not($id).find('img').attr('src', '{{EXAMPLE_MEDIA}}images/sortable.png');

	if (sortDirection == 1) {
		$id.addClass('sorted-asc');
      $id.attr('aria-sort', 'ascending');
		$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/sorted-asc.png');
	}
	else {
		$id.addClass('sorted-desc');
      $id.attr('aria-sort', 'descending');
		$id.find('img').attr('src', '{{EXAMPLE_MEDIA}}images/sorted-desc.png');
	}

	// reapply the sorted class
	// the first column is th for screen readers
	if (this.$headers.index($id) == 0) {
		// remove the sorted class from the other columns
		this.$data.find('td').removeClass('sorted')

		// apply the class to the browser column
		this.$data.find('th').addClass('sorted');
	}
	else {
		// remove the class from the browser column
		this.$data.find('th').removeClass('sorted');

		// apply the class to the appropriate column
		this.$data.find('td').removeClass('sorted')
			.filter(':nth-child(' + (colNdx + 1) + ')')
			.addClass('sorted');
	}

	// Modify the table caption to reflect the new sort column
	this.$id.find('caption').html('Inbox sorted by '
		+ this.labels[colNdx] + ': '
		+ ($id.is('.sorted-asc') ? 'Ascending' : 'Descending') + ' order');
		
	// reapply the row striping
	this.$id.alternateRowColors();

} // end sortTable()
//
// function bindHandlers() is a member function to bind event handlers to the application table
//
// return N/A
//
OAA_EXAMPLES.email.prototype.bindHandlers = function() {

	var thisObj = this;

	////////////////// bind header handlers ////////////////////
	
	this.$headers.keydown(function(e) {
		return thisObj.handleHeaderKeyDown($(this), e);
	});
	
	this.$headers.keypress(function(e) {
		return thisObj.handleHeaderKeyPress($(this), e);
	});
	
	this.$headers.click(function(e) {
		return thisObj.handleHeaderClick($(this), e);
	});

	this.$headers.hover(function() {
		$(this).addClass('hover');
	}, function() {
		$(this).removeClass('hover');
	});

	this.$headers.focus(function(e) {
		return thisObj.handleHeaderFocus($(this), e);
	});

	this.$headers.blur(function(e) {
		return thisObj.handleHeaderBlur($(this), e);
	});

	////////////////// bind tbody handlers ////////////////////
	
	// bind a keydown handler
	this.$data.delegate('th,td', 'keydown', function (e) {
			return thisObj.handleCellKeyDown($(this), e);
	}); // end edit box keydown handler

	// bind a keypress handler - consume events for Opera
	this.$data.delegate('th,td', 'keypress', function (e) {
			return thisObj.handleCellKeyPress($(this), e);
	}); // end edit box keyup handler

	// bind a click handler
	this.$data.delegate('th,td', 'click', function (e) {
			return thisObj.handleCellClick($(this), e);
	}); // end edit box keyup handler

	// bind a focus handler
	this.$data.delegate('th,td', 'focus', function (e) {
			return thisObj.handleCellFocus($(this), e);
	}); // end edit box focus handler

	// bind a blur handler
	this.$data.delegate('th,td', 'blur', function (e) {
			return thisObj.handleCellBlur($(this), e);
	}); // end edit box blurhandler

	////////////////// bind checkbox click handler ////////////////////
	
	// bind a click handler
	this.$data.delegate('input', 'mousedown', function (e) {
			return thisObj.handleCheckboxMouseDown($(this), e);
	}); // end edit box keydown handler

} // end bindHandlers();

/**
* @method handleHeaderKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for the table header cells
*
* @param {object} $id - the jquery object of the cell generating the event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false if consuming event; true of not processing
*/

OAA_EXAMPLES.email.prototype.handleHeaderKeyDown = function($id, e) {

	var curNdx = this.$headers.index($id);

	if (e.altKey || e.ctrlKey || e.shiftKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
		case this.keys.space: {
			$id.focus();

			this.sortTable($id);

			e.stopPropagation();
			return false;
		}
		case this.keys.left: {
			if (curNdx > 0) {
				var $prev = this.$headers.eq(curNdx - 1);

				$prev.focus();
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.right: {
			if (curNdx < this.$headers.length - 1) {
				var $next = this.$headers.eq(curNdx + 1);

				$next.focus();
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.down: {

			// set focus on the cell in this columen of the first table row
			this.$data.find('tr').first().children().eq(curNdx).focus();

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleHeaderKeyDown()

/**
* @method handleHeaderKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for the table header
*
* @param {object} $id - the jquery object of the cell generating the event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false if consuming event; true of not processing
*/

OAA_EXAMPLES.email.prototype.handleHeaderKeyPress = function($id, e) {

	if (e.altKey || e.ctrlKey || e.shiftKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
		case this.keys.space:
		case this.keys.down: {
			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleHeaderKeyPress()

/**
* @method OAA_EXAMPLES handleHeaderClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events for the table header cells
*
* @param {object} $id - the jquery object of the cell generating the event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false if consuming event; true of not processing
*/

OAA_EXAMPLES.email.prototype.handleHeaderClick = function($id, e) {

	$id.focus();

	this.sortTable($id);

	e.stopPropagation();
	return false;

} // end handleHeaderClick()

/**
* @method handleHeaderFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process blur events for the table header cells
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.email.prototype.handleHeaderFocus = function($id, e) {

	// remove the other headers from the tab order and remove the focus highlighting
	this.$headers.attr('tabindex', '-1').removeClass('focus');

	// remove the cells from the tab order and remove the focus highlighting
	this.$cells.attr('tabindex', '-1').removeClass('focus');

	// add the focus class and make the current header navigable
	$id.addClass('focus').attr('tabindex', '0');

	return true;
} // end handleHeaderFocus()

/**
* @method handleHeaderBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process blur events for the table header cells
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.email.prototype.handleHeaderBlur = function($id, e) {

	// remove the focus class
	$id.removeClass('focus');

	return true;
} // end handleHeaderBlur()

/**
* @method handleCellKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for the table cells
*
* @param {object} $id - the jquery object of the cell generating the event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false if consuming event; true of not processing
*/

OAA_EXAMPLES.email.prototype.handleCellKeyDown = function($id, e) {

	var $curRow = $id.parent();
	var $rows = this.$data.find('tr');
	var rowNdx = $rows.index($curRow);

	if (e.altKey || e.ctrlKey || e.shiftKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
		case this.keys.space: {
			var $input = $curRow.find('input');

			if ($input.attr('checked') == true) {
				$input.attr('checked', false);
				$curRow.removeClass('selected').attr('aria-selected', 'false');
			}
			else {
				$input.attr('checked', true);
				$curRow.addClass('selected').attr('aria-selected', 'true');
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.left: {
			// move left one cell

			var $prev = $id.prev();

			if ($prev.length > 0) {
				$prev.focus();
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.right: {
			// move right one cell

			var $next = $id.next();

			if ($next.length > 0) {
				$next.focus();
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.up: {
			// move up one row

			var colNdx = $curRow.children().filter($id).index();

			if (rowNdx > 0) {
				var $newCell = $rows.eq(rowNdx-1).children().eq(colNdx);

				$newCell.focus();
			}
			else {
				// move to the table header
				this.$headers.eq(colNdx).focus();

				// remove the cells from the tab order
				this.$cells.attr('tabindex', '-1');
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.down: {
			// move down one row

			if (rowNdx < $rows.length-1) {
				var colNdx = $curRow.children().filter($id).index();
				var $newCell = $rows.eq(rowNdx+1).children().eq(colNdx);

				$newCell.focus();
			}

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleCellKeyDown()

/**
* @method handleCellKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for the table cells
*
* @param {object} $id - the jquery object of the cell generating the event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false if consuming event; true of not processing
*/

OAA_EXAMPLES.email.prototype.handleCellKeyPress = function($id, e) {

	if (e.altKey || e.ctrlKey || e.shiftKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
		case this.keys.space:
		case this.keys.left:
		case this.keys.up:
		case this.keys.right:
		case this.keys.down: {
			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleCellKeyPress()

/**
* @method handleCellClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events for the table cells
*
* @param {object} $id - the jquery object of the cell generating the event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false if consuming event; true of not processing
*/

OAA_EXAMPLES.email.prototype.handleCellClick = function($id, e) {

	$id.focus()

	e.stopPropagation();
	return false;

} // end handleCellClick()

/**
* @method handleCellFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process blur events for the table cells
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.email.prototype.handleCellFocus = function($id, e) {

	// remove the headers from the tab order and remove the focus highlighting
	this.$headers.attr('tabindex', '-1').removeClass('focus');

	// remove the other cells from the tab order and remove the focus highlighting
	this.$cells.attr('tabindex', '-1').removeClass('focus');


	// add the focus class and make the current cell navigable
	$id.addClass('focus').attr('tabindex', '0');

	return true;
} // end handleCellFocus()

/**
* @method handleCellBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process blur events for the table cells
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.email.prototype.handleCellBlur = function($id, e) {

	// remove the focus class
	$id.removeClass('focus');

	return true;
} // end handleCellBlur()

/**
* @method handleCheckboxMouseDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process mousedown for the checkboxes
*
* @param {object} $id - the jquery object of the cell generating the event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false;
*/

OAA_EXAMPLES.email.prototype.handleCheckboxMouseDown = function($id, e) {

	var $curRow = $id.parent().parent();

	if ($id.attr('checked') == true) {
		$id.attr('checked', false);
		$curRow.removeClass('selected').attr('aria-selected', 'false');
	}
	else {
		$id.attr('checked', true);
		$curRow.addClass('selected').attr('aria-selected', 'true');
	}

	this.$cells.removeClass('focus');
	$id.parent().focus().addClass('focus');

	e.stopPropagation();
	return false;

} // end handleCheckboxMouseDown()

// Define a small jQuery extension to alternate table row colors
jQuery.fn.alternateRowColors = function() {
	$('tbody tr:odd', this).removeClass('even').addClass('odd');
	$('tbody tr:even', this).removeClass('odd').addClass('even');

	return this;
};
"""

example_obj.style       = """
body {
  font-size: medium;
  font-family: sans-serif;
  }
  
.warning {
  color: red;
  font-weight: bold;
}

#grid1 {
	padding: 0;
	text-align: center;
	border-collapse: collapse;
	border: 2px solid black;
}

thead th {
	padding: 2px 8px;
	background-color: #eef;
	border: 1px solid black;
}

th.hover {
	border: 2px solid black;
	background-color: #9bf;
}

tbody th, td {
	padding: 2px 5px;
	border: 1px solid black;
}

button.sort-button {
	margin: 5px;
	padding: 0px;
	width: 18px;
	height: 19px;
	border: none;
	background-color: transparent;
}

img.sort-image {
	margin: 0;
	padding: 0;
	width: 14px;
	height: 15px;
	position: relative;
	top: 0px;
	left: -1px;
}

.focus {
	border: 2px solid black;
	background-color: #79e;
}

.selected {
	color: #fff;
	background-color: #800 !important;
}

.odd {
	background-color: #fcfcec;
}
.even {
	background-color: transparent;
}

.hidden {
  position: absolute;
  top: -30em;
  left: -300em;
}
"""

example2 = create_example(example_obj)