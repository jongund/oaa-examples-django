"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples import *

order = 1

spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec = spec_aria10, attribute='role', value='menu')
m2 = ElementDefinition.objects.get(spec = spec_aria10, attribute='role', value='menubar')
m3 = ElementDefinition.objects.get(spec = spec_aria10, attribute='role', value='menuitem')
m4 = ElementDefinition.objects.get(spec = spec_aria10, attribute='role', value='menuitemcheckbox')
m5 = ElementDefinition.objects.get(spec = spec_aria10, attribute='role', value='menuitemradio')
m6 = ElementDefinition.objects.get(spec = spec_aria10, attribute='role', value='separator')
m7 = ElementDefinition.objects.get(spec = spec_aria10, attribute='aria-checked')
m8 = ElementDefinition.objects.get(spec = spec_aria10, attribute='aria-controls')
m9 = ElementDefinition.objects.get(spec = spec_aria10, attribute='aria-haspopup')

# =============================
# Example 1
# =============================

example_obj             = example_object()
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order          = order
example_obj.title       = 'Menubar'
example_obj.permanent_slug = 'menubar1'

example_obj.a11y_features = """
Simple example of a menubar widget.
"""
example_obj.keyboard    = """

The following keyboard shortcuts are implemented for this example (based on recommended shortcuts specified by the "DHTML Style Guide Working Group":http://dev.aol.com/dhtml_style_guide/ :
If focus is on the menubar:

    * Left arrow: Next menubar item
    * Right arrow: Previous menubar item
    * Up arrow: Open pull down menu and select first menu item
    * Down arrow: Open pull down menu and select first menu item
    * Enter: Open or close pull down menu. Select first menu item if opening
    * Space: Open or close pull down menu. Select first menu item if opening


If focus is on a menu item:

    * Left arrow: Open next pull down menu and select first item
    * Right arrow: Open previous pull menu and select first item
    * Up arrow: Select previous menu item
    * Down arrow: Select next menu item
    * Enter: Invoke selected item and dismiss menu
    * Space: Invoke selected item and dismiss menu
    * Esc: Close menu and return focus to menubar

"""

example_obj.markup = [m1,m2,m3,m4,m5,m6,m7,m8,m9]

example_obj.html        = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<ul id="mb1" class="menubar root-level" role="menubar" title="Styling Menu" aria-controls="st1">
  <li id="mb1_menu1" class="menu-parent" role="menuitem" tabindex="0" aria-haspopup="true">
    Font
    <ul id="fontMenu" class="menu" role="menu" aria-hidden="true">
      <li id="sans-serif"
        class="menu-item checked"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="true">Sans-serif</li>
      <li id="serif"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">Serif</li>
      <li id="monospace"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">Monospace</li>
      <li id="fantasy"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">Fantasy</li>
    </ul>
  </li>
  <li id="mb1_menu2" class="menu-parent" role="menuitem" tabindex="-1" aria-haspopup="true">
    Style
    <ul id="styleMenu" class="menu" role="menu" aria-hidden="true">
      <li id="italic"
        class="menu-item"
        role="menuitemcheckbox"
        aria-controls="st1"
        aria-checked="false"
        tabindex="-1">Italics</li>
      <li id="bold"
        class="menu-item"
        role="menuitemcheckbox"
        aria-controls="st1"
        aria-checked="false"
        tabindex="-1">Bold</li>
      <li id="underline"
        class="menu-item"
        role="menuitemcheckbox"
        aria-controls="st1"
        aria-checked="false"
        tabindex="-1">Underlined</li>
    </ul>
  </li>
  <li id="mb1_menu3" class="menu-parent" role="menuitem" tabindex="-1" aria-haspopup="true">
    Justification
    <ul id="justificationMenu" class="menu" role="menu" title="Justication" aria-hidden="true">
      <li id="left"
        class="menu-item checked"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="true">Left</li>
      <li id="center"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">Centered</li>
      <li id="right"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">Right</li>
      <li id="justify"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">Justify</li>
    </ul>
  </li>
  <li id="mb1_menu4" class="menu-parent" role="menuitem" tabindex="-1" aria-haspopup="true">
    Size
    <ul id="sizeMenu" class="menu" role="menu" title="Size" aria-hidden="true">
      <li id="larger"
        class="menu-item"
        role="menuitem"
        aria-controls="st1"
        tabindex="-1">Larger</li>
      <li id="smaller"
        class="menu-item"
        role="menuitem"
        aria-controls="st1"
        tabindex="-1">Smaller</li>
      <li id="fs_separator"
        class="menu-item separator"
        role="separator"
        tabindex="-1"></li>
      <li id="x-small"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">X-Small</li>
      <li id="small"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">Small</li>
      <li id="medium"
        class="menu-item checked"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="true">Medium</li>
      <li id="large"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">Large</li>
      <li id="x-large"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">X-Large</li>
    </ul>
  </li>
</ul>

<label for="st1" class="hidden">Text Sample 1</label>
<textarea id="st1" name="st1">
Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation, so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

But, in a larger sense, we can not dedicate, we can not consecrate, we can not hallow, this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us, that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion, that we here highly resolve that these dead shall not have died in vain, that this nation, under God, shall have a new birth of freedom, and that government of the people, by the people, for the people, shall not perish from the earth. 
</textarea>

<p><a href="http://en.wikipedia.org/wiki/Gettysburg,_Pennsylvania">More information on Gettysburg Address</a></p>
"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {} ;
$(document).ready(function() {
      var menu1 = new OAA_EXAMPLES.menubar('mb1', false);

}); // end ready()

/**
* @constructor textArea
*
* @memberOf OAA_EXAMPLES
*
* @desc is the constructor of a widget to manipulate the properties of a text area.
*
* @param {string} id - the HTML id of the text area to bind to
*
* @return {N/A}
*/

OAA_EXAMPLES.textArea = function(id) {

	// define widget properties
	this.$id = $('#' + id);

	this.fontSizes = new Array('x-small', 'small', 'medium', 'large', 'x-large');
	this.sizeNdx = 2; // index of current size setting

} // end textArea() constructor

/**
* @method setFont
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the font family of the text area.
*
* @param {string} fontFamily - name of family to set
*
* @return {N/A}
*/

OAA_EXAMPLES.textArea.prototype.setFont = function(fontFamily) {

	this.$id.css('font-family', fontFamily);

} // end setFont()

/**
* @method setStyle
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the font style of the text area.
*
* @param {string} style - name of style to set
*
* @return {N/A}
*/

OAA_EXAMPLES.textArea.prototype.setStyle = function(style) {

	this.$id.toggleClass(style);

} // end setStyle()

/**
* @method setAlignment
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the text alignment of the text area
*
* @param {string} justification - name of style to set
*
* @return {N/A}
*/

OAA_EXAMPLES.textArea.prototype.setAlignment = function(justification) {

	this.$id.css('text-align', justification);

} // end setAlignment()

/**
* @method getSize
*
* @memberOf OAA_EXAMPLES
*
* @desc returns the size of text in the text area.
*
* @return {N/A}
*/
 
OAA_EXAMPLES.textArea.prototype.getSize = function() {

	return this.fontSizes[this.sizeNdx];

} // end getSize()

/**
* @method setSize
*
* @memberOf OAA_EXAMPLES
*
* @desc sets the size of text in the text area.
*
* @param {string} size - size of text to set
*
* @return {N/A}
*/
 
OAA_EXAMPLES.textArea.prototype.setSize = function(size) {

	switch (size) {
	    case 'larger': {
	        this.sizeNdx += 1;
	        if (this.sizeNdx > 4) {
	            this.sizeNdx = 4;
	        }
	        break;
	    }
	    case 'smaller': {
	        this.sizeNdx -= 1;
	        if (this.sizeNdx < 0) {
	            this.sizeNdx = 0;
	        }
	        break;
	    }
	    case 'x-small': {
	        this.sizeNdx = 0;
	        break;
	    }
	    case 'small': {
	        this.sizeNdx = 1;
	        break;
	    }
	    case 'medium': {
	        this.sizeNdx = 2;
	        break;
	    }
	    case 'large': {
	        this.sizeNdx = 3;
	        break;
	    }
	    case 'x-large': {
	        this.sizeNdx = 4;
	        break;
	    }
	} // end switch

	// set the new size
	this.$id.css('font-size', this.fontSizes[this.sizeNdx]);

} // end setSize();



/**
* @constructor menubar
*
* @memberOf OAA_EXAMPLES
*
* @desc the constructor of a menu widget. The widget will bind to the ul passed to it.
*
* @param {string} id - the HTML id of the ul to bind to
*
* @param {boolean} vmenu - true if menu is vertical; false if horizontal
*
* @return {N/A}
*/

/**
* @constructor Internal Properties
*
* @memberOf OAA_EXAMPLES
*
* @property {array} $items - jQuery array of menu items
*
* @property {array} $rootItems - jQuery array of all root-level menu items
*
* @property {array} $items - jQuery array of all root-level menu items
*
* @property {array} $parents - jQuery array of menu items
*
* @property {array} $allItems - jQuery array of all menu items
*
* @property {object} $rootItems - jQuery object of the menu item with focus
*
* @property {boolean} $bCholdOpen - true if child menu is open
*/

OAA_EXAMPLES.menubar = function(id, vmenu) {

   // define widget properties
   this.$id = $('#' + id);

   this.$rootItems = this.$id.children('li'); 

   this.$items = this.$id.find('.menu-item').not('.separator'); 
   this.$parents = this.$id.find('.menu-parent'); 
   this.$allItems = this.$parents.add(this.$items); 
   this.$activeItem = null;

   this.vmenu = vmenu;
   this.bChildOpen = false; 

   this.keys = {
            tab:    9,
            enter:  13,
            esc:    27,
            space:  32,
            left:   37,
            up:     38,
            right:  39,
            down:   40 
   };

   // bind event handlers
   this.bindHandlers();

   // associate the menu with the textArea it controls
   this.textarea = new OAA_EXAMPLES.textArea(this.$id.attr('aria-controls'));
};

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers for the widget.
*
* @return {N/A}
*/

OAA_EXAMPLES.menubar.prototype.bindHandlers = function() {

   var thisObj = this;

   ///////// bind mouse event handlers //////////

   // bind a mouseenter handler for the menu items
   this.$items.mouseenter(function(e) {
      if ($(this).is('.checked')) {
         $(this).addClass('menu-hover-checked');
      }
      else {
         $(this).addClass('menu-hover');
      }
      return true;
   });

   // bind a mouseout handler for the menu items
   this.$items.mouseout(function(e) {
      $(this).removeClass('menu-hover menu-hover-checked');
      return true;
   });

   // bind a mouseenter handler for the menu parents
   this.$parents.mouseenter(function(e) {
      return thisObj.handleMouseEnter($(this), e);
   });

   // bind a mouseleave handler
   this.$parents.mouseleave(function(e) {
      return thisObj.handleMouseLeave($(this), e);
   });

   // bind a click handler
   this.$allItems.click(function(e) {
      return thisObj.handleClick($(this), e);
   });

   //////////// bind key event handlers //////////////////
  
   // bind a keydown handler
   this.$allItems.keydown(function(e) {
      return thisObj.handleKeyDown($(this), e);
   });

   // bind a keypress handler
   this.$allItems.keypress(function(e) {
      return thisObj.handleKeyPress($(this), e);
   });

   // bind a focus handler
   this.$allItems.focus(function(e) {
      return thisObj.handleFocus($(this), e);
   });

   // bind a blur handler
   this.$allItems.blur(function(e) {
      return thisObj.handleBlur($(this), e);
   });

   // bind a document click handler
   $(document).click(function(e) {
         return thisObj.handleDocumentClick(e);
   });

} // end bindHandlers()

/**
* @method handleMouseEnter
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process mouseover events for the top menus.
*
* @param {object} $item - the jquery object of the item firing the event
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns false;
*/

OAA_EXAMPLES.menubar.prototype.handleMouseEnter = function($item, e) {

   // add hover style
   if ($item.is('.checked')) {
      $item.addClass('menu-hover-checked');
   }
   else {
      $item.addClass('menu-hover');
   }

   // expand the first level submenu
   if ($item.attr('aria-haspopup') == 'true') {
      $item.children('ul').show().attr('aria-hidden', 'false');
      this.bChildOpen = true;
   }
   //e.stopPropagation();
   return true;

} // end handleMouseEnter()

/**
* @method handleMouseOut
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process mouseout events for the top menus.
*
* @param {object} $item - the jquery object of the item firing the event
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns false;
*/

OAA_EXAMPLES.menubar.prototype.handleMouseOut = function($item, e) {

   // Remover hover styles
   $item.removeClass('menu-hover menu-hover-checked');

   //e.stopPropagation();
   return true;

} // end handleMouseOut()

/**
* @method handleMouseLeave
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process mouseout events for the top menus.
*
* @param {object} $menu - the jquery object of the item firing the event
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns false;
*/

OAA_EXAMPLES.menubar.prototype.handleMouseLeave = function($menu, e) {

   var $active = $menu.find('.menu-focus-checked');

   $active = $active.add($menu.find('.menu-focus'));

   // Remove hover style
   $menu.removeClass('menu-hover menu-hover-checked');

   // if any item in the child menu has focus, move focus to the root item
   if ($active.length > 0) {

      this.bChildOpen = false;

      // remove the focus style from the active item
      $active.removeClass('menu-focus menu-focus-checked'); 

      // store the active item
      this.$activeItem = $menu;
 
      // cannot hide items with focus -- move focus to root item
      $menu.focus();
   }

   // hide the child menu
   $menu.children('ul').hide().attr('aria-hidden', 'true');

   //e.stopPropagation();
   return true;

} // end handleMouseLeave()

/**
* @method handleClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events for the top menus.
*
* @param {object} $item - the jquery object of the item firing the event
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns false;
*/

OAA_EXAMPLES.menubar.prototype.handleClick = function($item, e) {

   var $parentUL = $item.parent();

   if ($parentUL.is('.root-level')) {
         // open the child menu if it is closed
         $item.children('ul').first().show().attr('aria-hidden', 'false');
         this.bChildOpen = true;
   }
   else {
      // process the menu choice
      this.processMenuChoice($item);

      // remove hover and focus styling
      this.$allItems.removeClass('menu-hover menu-hover-checked menu-focus menu-focus-checked');

      // close the menu
      this.$id.find('ul').not('.root-level').hide().attr('aria-hidden','true');

      // move focus to the text area
      this.textarea.$id.focus();
   }

   e.stopPropagation();
   return false;

} // end handleClick()

/**
* @method handleFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process focus events for the menu.
*
* @param {object} $item - the jquery object of the item firing the event
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true;
*/

OAA_EXAMPLES.menubar.prototype.handleFocus = function($item, e) {

   // if activeItem is null, we are getting focus from outside the menu. Store
   // the item that triggered the event
   if (this.$activeItem == null) {
      this.$activeItem = $item;
   }
   else if ($item[0] != this.$activeItem[0]) {
      return true;
   }
   
   // get the set of jquery objects for all the parent items of the active item
   var $parentItems = this.$activeItem.parentsUntil('div').filter('li');

   // remove focus styling from all other menu items
   this.$allItems.removeClass('menu-focus menu-focus-checked');

   // add styling to the active item
   if (this.$activeItem.is('.checked')) {
      this.$activeItem.addClass('menu-focus-checked');
   }
   else {
      this.$activeItem.addClass('menu-focus');
   }

   // add styling to all parent items.
   // This assumes that parent items do not have a checked state
   $parentItems.addClass('menu-focus');

   if (this.vmenu == true) {
      // if the bChildOpen is true, open the active item's child menu (if applicable)
      if (this.bChildOpen == true) {

         var $itemUL = $item.parent();

         // if the itemUL is a root-level menu and item is a parent item,
         // show the child menu.
         if ($itemUL.is('.root-level') && ($item.attr('aria-haspopup') == 'true')) {
            $item.children('ul').show().attr('aria-hidden', 'false');
         }
      }
      else {
         this.vmenu = false;
      }
   }

   return true;

} // end handleFocus()

/**
* @method handleBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process blur events for the menu.
*
* @param {object} $item - the jquery object of the item firing the even
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true;
*/

OAA_EXAMPLES.menubar.prototype.handleBlur = function($item, e) {

   $item.removeClass('menu-focus menu-focus-checked');

   return true;

} // end handleBlur()

/**
* @method handleKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for the menus.
*
* @param {object} $item - the jquery object of the item firing the event
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns false if consuming; true if propagating
*/

OAA_EXAMPLES.menubar.prototype.handleKeyDown = function($item, e) {

   if (e.altKey || e.ctrlKey) {
       // Modifier key pressed: Do not process
       return true;
   }

   switch(e.keyCode) {
      case this.keys.tab: {

         // hide all menu items and update their aria attributes
         this.$id.find('ul').hide().attr('aria-hidden', 'true');

         // remove focus styling from all menu items
         this.$allItems.removeClass('menu-focus');

         this.$activeItem = null;
         this.bChildOpen == false;

         break;
      }
      case this.keys.esc: {
         var $itemUL = $item.parent();

         if ($itemUL.is('.root-level')) {
            // hide the child menu and update the aria attributes
            $item.children('ul').first().hide().attr('aria-hidden', 'true');
         }
         else {

            // move up one level
            this.$activeItem = $itemUL.parent();

            // reset the childOpen flag
            this.bChildOpen = false;

            // set focus on the new item
            this.$activeItem.focus();

            // hide the active menu and update the aria attributes
            $itemUL.hide().attr('aria-hidden', 'true');
         }

         e.stopPropagation();
         return false;
      }
      case this.keys.enter:
      case this.keys.space: {

         var $parentUL = $item.parent();

         if ($parentUL.is('.root-level')) {
            // open the child menu if it is closed
            $item.children('ul').first().show().attr('aria-hidden', 'false');
            this.bChildOpen = true;
         }
         else {
            // process the menu choice
            this.processMenuChoice($item);

            // remove hover styling
            this.$allItems.removeClass('menu-hover menu-hover-checked');
            this.$allItems.removeClass('menu-focus menu-focus-checked');

            // close the menu
            this.$id.find('ul').not('.root-level').hide().attr('aria-hidden','true');


            // clear the active item
            this.$activeItem = null;

            // move focus to the text area
            this.textarea.$id.focus();
         }

         e.stopPropagation();
         return false;
      }

      case this.keys.left: {

         if (this.vmenu == true && $itemUL.is('.root-level')) {
            // If this is a vertical menu and the root-level is active, move
            // to the previous item in the menu
            this.$activeItem = this.moveUp($item); 
         }
         else {
            this.$activeItem = this.moveToPrevious($item); 
         }

         this.$activeItem.focus();

         e.stopPropagation();
         return false;
      }
      case this.keys.right: {

         if (this.vmenu == true && $itemUL.is('.root-level')) {
            // If this is a vertical menu and the root-level is active, move
            // to the next item in the menu
            this.$activeItem = this.moveDown($item); 
         }
         else {
            this.$activeItem = this.moveToNext($item);
         }

         this.$activeItem.focus();

         e.stopPropagation();
         return false;
      }
      case this.keys.up: {

         if (this.vmenu == true && $itemUL.is('.root-level')) {
            // If this is a vertical menu and the root-level is active, move
            // to the previous root-level menu
            this.$activeItem = this.moveToPrevious($item); 
         }
         else {
            this.$activeItem = this.moveUp($item); 
         }

         this.$activeItem.focus();

         e.stopPropagation();
         return false;
      }
      case this.keys.down: {

         if (this.vmenu == true && $itemUL.is('.root-level')) {
            // If this is a vertical menu and the root-level is active, move
            // to the next root-level menu
            this.$activeItem = this.moveToNext($item); 
         }
         else {
            this.$activeItem = this.moveDown($item); 
         }

         this.$activeItem.focus();

         e.stopPropagation();
         return false;
      }
   } // end switch

   return true;

} // end handleMenuKeyDown()

/**
* @method moveToNext
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to move to the next menu level.
* This will be either the next root-level menu or the child of a menu parent. If
* at the root level and the active item is the last in the menu, this function will loop
* to the first menu item.
* If the menu is a horizontal menu, the first child element of the newly selected menu will
* be selected
*
* @param {object} $item - the active menu item
*
* @return {object} Returns the item to move to. Returns $item is no move is possible
*/

OAA_EXAMPLES.menubar.prototype.moveToNext = function($item) {

   var $itemUL = $item.parent(); // $item's containing menu 
   var $menuItems = $itemUL.children('li'); // the items in the currently active menu
   var menuNum = $menuItems.length; // the number of items in the active menu
   var menuIndex = $menuItems.index($item); // the items index in its menu
   var $newItem = null;
   var $newItemUL = null;

   if ($itemUL.is('.root-level')) {
      // this is the root level move to next sibling. This will require closing
      // the current child menu and opening the new one.
 
      if (menuIndex < menuNum-1) { // not the last root menu
         $newItem = $item.next();
      }
      else { // wrap to first item
         $newItem = $menuItems.first();
      }

      // close the current child menu (if applicable)
      if ($item.attr('aria-haspopup') == 'true') {

         var $childMenu = $item.children('ul').first();

         if ($childMenu.attr('aria-hidden') == 'false') {
            // hide the child and update aria attributes accordingly
            $childMenu.hide().attr('aria-hidden', 'true');
            this.bChildOpen = true;
         }
      }

      // remove the focus styling from the current menu
      $item.removeClass('menu-focus');

      // open the new child menu (if applicable)
      if (($newItem.attr('aria-haspopup') == 'true') && (this.bChildOpen == true)) {

         var $childMenu = $newItem.children('ul').first();

         // open the child and update aria attributes accordingly
         $childMenu.show().attr('aria-hidden', 'false');

         /*
          * Uncomment this section if the first item in the child menu should be
          * automatically selected
          *
         if (!this.vmenu) {
            // select the first item in the child menu
            $newItem = $childMenu.children('li').first();
         }
         */

      }
   }
   else {
      // this is not the root level. If there is a child menu to be moved into, do that;
      // otherwise, move to the next root-level menu if there is one
      if ($item.attr('aria-haspopup') == 'true') {
         
         var $childMenu = $item.children('ul').first();

         $newItem = $childMenu.children('li').first();

         // show the child menu and update its aria attributes
         $childMenu.show().attr('aria-hidden', 'false');
         this.bChildOpen = true;
      }
      else {
         // at deepest level, move to the next root-level menu
 
         if (this.vmenu == true) {
            // do nothing
            return $item;
         }

         var $parentMenus = null;
         var $rootItem = null;

         // get list of all parent menus for item, up to the root level
         $parentMenus = $item.parentsUntil('div').filter('ul').not('.root-level');

         // hide the current menu and update its aria attributes accordingly
         $parentMenus.hide().attr('aria-hidden', 'true');

         // remove the focus styling from the active menu
         $parentMenus.find('li').removeClass('menu-focus');
         $parentMenus.last().parent().removeClass('menu-focus');

         $rootItem = $parentMenus.last().parent(); // the containing root for the menu

         menuIndex = this.$rootItems.index($rootItem);

         // if this is not the last root menu item, move to the next one
         if (menuIndex < this.$rootItems.length-1) {
            $newItem = $rootItem.next();
         }
         else { // loop
            $newItem = this.$rootItems.first();
         }

         if ($newItem.attr('aria-haspopup') == 'true') {
            var $childMenu = $newItem.children('ul').first();

            $newItem = $childMenu.children('li').first();

            // show the child menu and update it's aria attributes
            $childMenu.show().attr('aria-hidden', 'false');
            this.bChildOpen = true;
         }
      }
   }

   return $newItem;
}

/**
* @method moveToPrevious
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to move to the previous menu level.
* This will be either the previous root-level menu or the child of a menu parent. If
* at the root level and the active item is the first in the menu, this function will loop
* to the last menu item.
*
* If the menu is a horizontal menu, the first child element of the newly selected menu will
* be selected
*
* @param {object} $item - the active menu item
*
* @return {object} Returns the item to move to. Returns $item is no move is possible
*/

OAA_EXAMPLES.menubar.prototype.moveToPrevious = function($item) {

   var $itemUL = $item.parent(); // $item's containing menu 
   var $menuItems = $itemUL.children('li'); // the items in the currently active menu
   var menuNum = $menuItems.length; // the number of items in the active menu
   var menuIndex = $menuItems.index($item); // the items index in its menu
   var $newItem = null;
   var $newItemUL = null;

   if ($itemUL.is('.root-level')) {
      // this is the root level move to previous sibling. This will require closing
      // the current child menu and opening the new one.
 
      if (menuIndex > 0) { // not the first root menu
         $newItem = $item.prev();
      }
      else { // wrap to last item
         $newItem = $menuItems.last();
      }

      // close the current child menu (if applicable)
      if ($item.attr('aria-haspopup') == 'true') {

         var $childMenu = $item.children('ul').first();

         if ($childMenu.attr('aria-hidden') == 'false') {
            // hide the child and update aria attributes accordingly
            $childMenu.hide().attr('aria-hidden', 'true');
            this.bChildOpen = true;
         }
      }

      // remove the focus styling from the current menu
      $item.removeClass('menu-focus');

      // open the new child menu (if applicable)
      if (($newItem.attr('aria-haspopup') == 'true') && this.bChildOpen == true) {

         var $childMenu = $newItem.children('ul').first();

         // open the child and update aria attributes accordingly
         $childMenu.show().attr('aria-hidden', 'false');

         /*
          * Uncomment this section if the first item in the child menu should be
          * automatically selected
          *
         if (!this.vmenu) {
            // select the first item in the child menu
            $newItem = $childMenu.children('li').first();
         }
         */

      }
   }
   else {
      // this is not the root level. If there is a parent menu that is not the
      // root menu, move up one level; otherwise, move to first item of the previous
      // root menu.
 
      var $parentLI = $itemUL.parent();
      var $parentUL = $parentLI.parent();

      var $parentMenus = null;
      var $rootItem = null;

      // if this is a vertical menu or is not the first child menu
      // of the root-level menu, move up one level.
      if (this.vmenu == true || !$parentUL.is('.root-level')) {

         $newItem = $itemUL.parent();

         // hide the active menu and update aria-hidden
         $itemUL.hide().attr('aria-hidden', 'true');

         // remove the focus highlight from the $item
         $item.removeClass('menu-focus');

         if (this.vmenu == true) {
            // set a flag so the focus handler does't reopen the menu
            this.bChildOpen = false;
         }

      }
      else { // move to previous root-level menu

         // hide the current menu and update the aria attributes accordingly
         $itemUL.hide().attr('aria-hidden', 'true');

         // remove the focus styling from the active menu
         $item.removeClass('menu-focus');
         $parentLI.removeClass('menu-focus');

         menuIndex = this.$rootItems.index($parentLI);

         if (menuIndex > 0) {
            // move to the previous root-level menu
            $newItem = $parentLI.prev();
         }
         else { // loop to last root-level menu
            $newItem = this.$rootItems.last();
         }

         // add the focus styling to the new menu
         $newItem.addClass('menu-focus');

         if ($newItem.attr('aria-haspopup') == 'true') {
            var $childMenu = $newItem.children('ul').first();

            // show the child menu and update it's aria attributes
            $childMenu.show().attr('aria-hidden', 'false');
            this.bChildOpen = true;

            $newItem = $childMenu.children('li').first();
         }
      }
   }

   return $newItem;
}

/**
* @method moveDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to select the next item in a menu.
* If the active item is the last in the menu, this function will loop to the
* first menu item.
*
* @param {object} $item - the active menu item
*
* @param {char} startChr - [optional] the character to attempt to match against the beginning of the
* menu item titles. If found, focus moves to the next menu item beginning with that character.
*
* @return {object} Returns the item to move to. Returns $item is no move is possible
*/

OAA_EXAMPLES.menubar.prototype.moveDown = function($item, startChr) {

   var $itemUL = $item.parent(); // $item's containing menu 
   var $menuItems = $itemUL.children('li').not('.separator'); // the items in the currently active menu
   var menuNum = $menuItems.length; // the number of items in the active menu
   var menuIndex = $menuItems.index($item); // the items index in its menu
   var $newItem = null;
   var $newItemUL = null;

   if ($itemUL.is('.root-level')) { // this is the root level menu

      if ($item.attr('aria-haspopup') != 'true') {
         // No child menu to move to
         return $item;
      }

      // Move to the first item in the child menu
      $newItemUL = $item.children('ul').first();
      $newItem = $newItemUL.children('li').first();

      // make sure the child menu is visible
      $newItemUL.show().attr('aria-hidden', 'false');
      this.bChildOpen = true;

      return $newItem;
   }

   // if $item is not the last item in its menu, move to the next item. If startChr is specified, move
   // to the next item with a title that begins with that character.
   //
   if (startChr) {
      var bMatch = false;
      var curNdx = menuIndex+1;

      // check if the active item was the last one on the list
      if (curNdx == menuNum) {
         curNdx = 0;
      }

      // Iterate through the menu items (starting from the current item and wrapping) until a match is found
      // or the loop returns to the current menu item 
      while (curNdx != menuIndex)  {

         var titleChr = $menuItems.eq(curNdx).html().charAt(0);

         if (titleChr.toLowerCase() == startChr) {
            bMatch = true;
            break;
         }

         curNdx = curNdx+1;

         if (curNdx == menuNum) {
            // reached the end of the list, start again at the beginning
            curNdx = 0;
         }
      }

      if (bMatch == true) {
         $newItem = $menuItems.eq(curNdx);

         // remove the focus styling from the current item
         $item.removeClass('menu-focus menu-focus-checked');

         return $newItem
      }
      else {
         return $item;
      }
   }
   else {
      if (menuIndex < menuNum-1) {
         $newItem = $menuItems.eq(menuIndex+1);
      }
      else {
         $newItem = $menuItems.first();
      }
   }

   // remove the focus styling from the current item
   $item.removeClass('menu-focus menu-focus-checked');

   return $newItem;
}

/**
* @method moveUp
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to select the previous item in a menu.
* If the active item is the first in the menu, this function will loop to the
* last menu item.
*
* @param {object} $item - the active menu item
*
* @return {object} Returns the item to move to. Returns $item is no move is possible
*/

OAA_EXAMPLES.menubar.prototype.moveUp = function($item) {

   var $itemUL = $item.parent(); // $item's containing menu 
   var $menuItems = $itemUL.children('li').not('.separator'); // the items in the currently active menu
   var menuNum = $menuItems.length; // the number of items in the active menu
   var menuIndex = $menuItems.index($item); // the items index in its menu
   var $newItem = null;
   var $newItemUL = null;

   if ($itemUL.is('.root-level')) { // this is the root level menu

      // nothing to do
      return $item;
   }

   // if $item is not the first item in its menu, move to the previous item
   if (menuIndex > 0) {

      $newItem = $menuItems.eq(menuIndex-1);
   }
   else {
      // loop to top of menu
      $newItem = $menuItems.last();
   }

   // remove the focus styling from the current item
   $item.removeClass('menu-focus menu-focus-checked');

   return $newItem;
}

/**
* @method handleKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for the menus.
* The Opera browser performs some window commands from the keypress event,
* not keydown like Firefox, Safari, and IE. This event handler consumes
* keypresses for relevant keys so that Opera behaves when the user is
* manipulating the menu with the keyboard.
*
* @param {object} $item is the jquery object of the item firing the event
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns false if consuming; true if propagating
*/

OAA_EXAMPLES.menubar.prototype.handleKeyPress = function($item, e) {

   if (e.altKey || e.ctrlKey || e.shiftKey) {
       // Modifier key pressed: Do not process
       return true;
   }

   switch(e.keyCode) {
      case this.keys.tab: {
         return true;
      }
      case this.keys.esc:
      case this.keys.enter:
      case this.keys.space:
      case this.keys.up:
      case this.keys.down:
      case this.keys.left:
      case this.keys.right: {

         e.stopPropagation();
         return false;
      }
      default : {
         var chr = String.fromCharCode(e.which);

         this.$activeItem = this.moveDown($item, chr);
         this.$activeItem.focus();

         e.stopPropagation();
         return false;
      }

   } // end switch

   return true;

} // end handleKeyPress()

/**
* @method handleDocumentClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events on the document.
* Needed to close an open menu if a user clicks outside the menu
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true;
*/

OAA_EXAMPLES.menubar.prototype.handleDocumentClick = function(e) {

   // get a list of all child menus
   var $childMenus = this.$id.find('ul').not('.root-level');

   // hide the child menus
   $childMenus.hide().attr('aria-hidden', 'true');

   this.$allItems.removeClass('menu-focus menu-focus-checked');

   this.$activeItem = null;

   // allow the event to propagate
   return true;

} // end handleDocumentClick()

/**
* @method processMenuChoice
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process the user's menu item choice.
* Since the menu will close after this, highlight styling is simply removed.
*
* @param {object} $item - the jquery object of the menu item firing the event
*
* @return {N/A}
*/

OAA_EXAMPLES.menubar.prototype.processMenuChoice = function($item) {

	// find the parent menu for this item
	var menuName = $item.parent().attr('id');
	var choice = $item.attr('id');

	// call the appropriate textarea function
	switch(menuName) {
		case 'fontMenu': {
			this.textarea.setFont(choice);

			// update the aria-checked state of the menu items and apply
			// appropriate styling
			$item.attr('aria-checked', 'true').addClass('checked');
			$item.siblings().attr('aria-checked', 'false').removeClass('checked');

			break;
		}
		case 'styleMenu': {
			this.textarea.setStyle(choice);

			// reverse the aria-checked state and update styling
			if ($item.attr('aria-checked') == 'true') {
				$item.attr('aria-checked', 'false').removeClass('checked');
			}
			else {
				$item.attr('aria-checked', 'true').addClass('checked');
			}

			break;
		}
		case 'justificationMenu': {
			this.textarea.setAlignment(choice);

			// update the aria-checked state of the menu items and apply
			// appropriate styling
			$item.attr('aria-checked', 'true').addClass('checked');
			$item.siblings().attr('aria-checked', 'false').removeClass('checked');

			break;
		}
		case 'sizeMenu': {
			var $menuItems = $item.siblings().andSelf();
			var $curItem;

			this.textarea.setSize(choice);

			////////////////////////
			// update the aria-checked state by first setting all items to false
			// and then setting the item that matches the currently selected font
			// size.
			
			// set aria-checked to false and removed checked styling
			$menuItems.attr('aria-checked', 'false').removeClass('checked');

			// determine which menu item matches the current font size
			$curItem = $menuItems.filter('[id=' + this.textarea.getSize() + ']');

			// Set aria-checked for the matching item and apply the checked styling
			$curItem.attr('aria-checked', 'true').addClass('checked');

			break;
		}
	} // end switch

} // end processMenuChoice()

/////////////// end menu widget definition /////////////////////
"""

example_obj.style       = """
#st1 {
	padding: .5em;
	border: 1px solid black;
	height: 400px;
	width: 70%;
	font-size: medium;
	font-family: sans-serif;
}
ul.menubar {
	margin: 0 !important;
	padding: 0 .25em !important;
	list-style: none !important;
   font-size: 100% !important;
	height: 1.85em;
	width: 20em;
	border: 1px solid black;
	background: #ccc;
}
ul.menubar li {
	float: left;
	display: inline; position: relative;
	margin: 0;
	padding: .25em .35em;
	height: 1.25em;
}
ul.menu {
	position: absolute;
	left: 0;
	top: 1.75em;
	display: none;
	list-style: none;
	margin: 0 !important;
	padding: 0 !important;
	font-weight: normal !important;
   font-size: 100% !important;
	border: 1px solid black;
	background-color: #ccc;
	width: 8.5em;
}
ul.menu li {
	float: none;
	display: block;
	white-space: nowrap;
	padding: 2px 1em;
	color: black;
}

li.separator {
	margin: 0;
	margin-bottom: 4px !important;
	height: 2px !important;
	border-bottom: 1px solid black;
}

li.checked {
	font-weight: bold;
	background-image: url('{{EXAMPLE_MEDIA}}images/dot.png');
	background-repeat: no-repeat;
	background-position: 5px 10px;
}

.menu-hover {
	background-color: #700 !important;
	color: white !important;
}

.menu-hover-checked {
	background-color: #700 !important;
	color: white !important;
	background-image: url('{{EXAMPLE_MEDIA}}images/dot-selected.png') !important;
}

.menu-focus {
	background-color: black;
	font-weight: bold;
	color: white !important;
}

li.menu-focus-checked {
	background-color: black;
	font-weight: bold;
	color: white !important;
	background-image: url('{{EXAMPLE_MEDIA}}images/dot-selected.png') !important;
}
.hidden {
   position: absolute;
   left: -200em;
   top: -20em;
}


/*
 * Text area styles
 */
.italic {
	font-style: italic;
}
.bold {
	font-weight: bold;
}
.underline {
	text-decoration: underline;
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
example_obj.title       = 'Menubar: ARIA CSS Selectors'
example_obj.permanent_slug = 'menubar2'

example_obj.a11y_features = """
Simple example of a menubar widget using ARIA CSS selectors.
"""
example_obj.keyboard    = """
The following keyboard shortcuts are implemented for this example (based on recommended shortcuts specified by the <a href="http://dev.aol.com/dhtml_style_guide">DHTML Style Guide Working Group</a>.):
If focus is on the menubar:

    * Left arrow: Next menubar item
    * Right arrow: Previous menubar item
    * Up arrow: Open pull down menu and select first menu item
    * Down arrow: Open pull down menu and select first menu item
    * Enter: Open or close pull down menu. Select first menu item if opening
    * Space: Open or close pull down menu. Select first menu item if opening


If focus is on a menu item:

    * Left arrow: Open next pull down menu and select first item
    * Right arrow: Open previous pull menu and select first item
    * Up arrow: Select previous menu item
    * Down arrow: Select next menu item
    * Enter: Invoke selected item and dismiss menu
    * Space: Invoke selected item and dismiss menu
    * Esc: Close menu and return focus to menubar
"""

example_obj.markup = [m1,m2,m3,m4,m5,m6,m7,m8,m9]

example_obj.html        = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<ul id="mb1" class="menubar root-level" role="menubar" title="Styling Menu" aria-controls="st1">
  <li id="mb1_menu1" class="menu-parent" role="menuitem" tabindex="0" aria-haspopup="true">
    Font
    <ul id="fontMenu" class="menu" role="menu" aria-hidden="true">
      <li id="sans-serif"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="true">Sans-serif</li>
      <li id="serif"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">Serif</li>
      <li id="monospace"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">Monospace</li>
      <li id="fantasy"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">Fantasy</li>
    </ul>
  </li>
  <li id="mb1_menu2" class="menu-parent" role="menuitem" tabindex="-1" aria-haspopup="true">
    Style
    <ul id="styleMenu" class="menu" role="menu" aria-hidden="true">
      <li id="italic"
        class="menu-item"
        role="menuitemcheckbox"
        aria-controls="st1"
        aria-checked="false"
        tabindex="-1">Italics</li>
      <li id="bold"
        class="menu-item"
        role="menuitemcheckbox"
        aria-controls="st1"
        aria-checked="false"
        tabindex="-1">Bold</li>
      <li id="underline"
        class="menu-item"
        role="menuitemcheckbox"
        aria-controls="st1"
        aria-checked="false"
        tabindex="-1">Underlined</li>
    </ul>
  </li>
  <li id="mb1_menu3" class="menu-parent" role="menuitem" tabindex="-1" aria-haspopup="true">
    Justification
    <ul id="justificationMenu" class="menu" role="menu" title="Justication" aria-hidden="true">
      <li id="left"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="true">Left</li>
      <li id="center"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">Centered</li>
      <li id="right"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">Right</li>
      <li id="justify"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">Justify</li>
    </ul>
  </li>
  <li id="mb1_menu4" class="menu-parent" role="menuitem" tabindex="-1" aria-haspopup="true">
    Size
    <ul id="sizeMenu" class="menu" role="menu" title="Size" aria-hidden="true">
      <li id="larger"
        class="menu-item"
        role="menuitem"
        aria-controls="st1"
        tabindex="-1">Larger</li>
      <li id="smaller"
        class="menu-item"
        role="menuitem"
        aria-controls="st1"
        tabindex="-1">Smaller</li>
      <li id="fs_separator"
        class="menu-item separator"
        role="separator"
        tabindex="-1"></li>
      <li id="x-small"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">X-Small</li>
      <li id="small"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">Small</li>
      <li id="medium"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="true">Medium</li>
      <li id="large"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">Large</li>
      <li id="x-large"
        class="menu-item"
        role="menuitemradio"
        tabindex="-1"
        aria-controls="st1"
        aria-checked="false">X-Large</li>
    </ul>
  </li>
</ul>

<label for="st1" class="hidden">Text Sample 1</label>
<textarea id="st1" name="st1">
Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation, so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

But, in a larger sense, we can not dedicate, we can not consecrate, we can not hallow, this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us, that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion, that we here highly resolve that these dead shall not have died in vain, that this nation, under God, shall have a new birth of freedom, and that government of the people, by the people, for the people, shall not perish from the earth. 
</textarea>

<p><a href="http://en.wikipedia.org/wiki/Gettysburg,_Pennsylvania">More information on Gettysburg Address</a></p>
"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};
$(document).ready(function() {
      var menu1 = new OAA_EXAMPLES.menubar('mb1', false);

}); // end ready()

/**
* constructor textArea
*
* @memberOf OAA_EXAMPLES
*
* @desc the constructor of a widget to manipulate the properties of a text area.
*
* @param {string} id - the HTML id of the text area to bind to
*
* @return {N/A}
*/

OAA_EXAMPLES.textArea = function(id) {

	// define widget properties
	this.$id = $('#' + id);

	this.fontSizes = new Array('x-small', 'small', 'medium', 'large', 'x-large');
	this.sizeNdx = 2; // index of current size setting

} // end textArea() constructor

/**
* @method setFont
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the font family of the text area.
*
* @param {string} fontFamily - name of family to set
*
* @return {N/A}
*/

OAA_EXAMPLES.textArea.prototype.setFont = function(fontFamily) {

	this.$id.css('font-family', fontFamily);

} // end setFont()

/**
* @methodsetStyle
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the font style of the text area.
*
* @param {string} style - name of style to set
*
* @return {N/A}
*/

OAA_EXAMPLES.textArea.prototype.setStyle = function(style) {

	this.$id.toggleClass(style);

} // end setStyle()

/**
* @method setAlignment
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the text alignment of the text area
*
* @param {string} justification - name of style to set
*
* @return {N/A}
*/

OAA_EXAMPLES.textArea.prototype.setAlignment = function(justification) {

	this.$id.css('text-align', justification);

} // end setAlignment()

/**
* @method getSize
*
* @memberOf OAA_EXAMPLES
*
* @desc returns the size of text in the text area.
*
* @return {N/A}
*/
 
OAA_EXAMPLES.textArea.prototype.getSize = function() {

	return this.fontSizes[this.sizeNdx];

} // end getSize()

/**
* @method setSize
*
* @memberOf OAA_EXAMPLES
*
* @desc sets the size of text in the text area.
*
* @param {string} size of text to set
*
* @return {N/A}
*/
 
OAA_EXAMPLES.textArea.prototype.setSize = function(size) {

	switch (size) {
	    case 'larger': {
	        this.sizeNdx += 1;
	        if (this.sizeNdx > 4) {
	            this.sizeNdx = 4;
	        }
	        break;
	    }
	    case 'smaller': {
	        this.sizeNdx -= 1;
	        if (this.sizeNdx < 0) {
	            this.sizeNdx = 0;
	        }
	        break;
	    }
	    case 'x-small': {
	        this.sizeNdx = 0;
	        break;
	    }
	    case 'small': {
	        this.sizeNdx = 1;
	        break;
	    }
	    case 'medium': {
	        this.sizeNdx = 2;
	        break;
	    }
	    case 'large': {
	        this.sizeNdx = 3;
	        break;
	    }
	    case 'x-large': {
	        this.sizeNdx = 4;
	        break;
	    }
	} // end switch

	// set the new size
	this.$id.css('font-size', this.fontSizes[this.sizeNdx]);

} // end setSize();



/**
* @constructor menubar
*
* @memberOf OAA_EXAMPLES
*
* @desc the constructor of a menu widget. The widget will bind to the ul passed to it.
*
* @param {string} id - the HTML id of the ul to bind to
*
* @param {boolean} vmenu - true if menu is vertical; false if horizontal
*
* @return {N/A}
*/

/**
* @constructor Internal Properties
*
* @property {array} $rootItems - jQuery array of all root-level menu items
*
* @property {array} $items - jQuery array of menu items
*
* @property {array} $parents - jQuery array of menu items
*
* @property {array} $allItems - jQuery array of all root-level menu items
*
* @property {object} $activeItem - jQuery object of the menu item with focus
*
* @property {boolean} $bChildOpen - true if child menu is open
*/

OAA_EXAMPLES.menubar = function(id, vmenu) {

   // define widget properties
   this.$id = $('#' + id);

   this.$rootItems = this.$id.children('li'); 

   this.$items = this.$id.find('.menu-item').not('.separator'); 
   this.$parents = this.$id.find('.menu-parent');
   this.$allItems = this.$parents.add(this.$items); 
   this.$activeItem = null; 

   this.vmenu = vmenu;
   this.bChildOpen = false; 

   this.keys = {
            tab:    9,
            enter:  13,
            esc:    27,
            space:  32,
            left:   37,
            up:     38,
            right:  39,
            down:   40 
   };

   // bind event handlers
   this.bindHandlers();

   // associate the menu with the textArea it controls
   this.textarea = new OAA_EXAMPLES.textArea(this.$id.attr('aria-controls'));
};

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers for the widget.
*
* @return {N/A}
*/

OAA_EXAMPLES.menubar.prototype.bindHandlers = function() {

   var thisObj = this;

   ///////// bind mouse event handlers //////////

   // bind a mouseenter handler for the menu items
   this.$items.mouseenter(function(e) {
      $(this).addClass('menu-hover');
      return true;
   });

   // bind a mouseout handler for the menu items
   this.$items.mouseout(function(e) {
      $(this).removeClass('menu-hover');
      return true;
   });

   // bind a mouseenter handler for the menu parents
   this.$parents.mouseenter(function(e) {
      return thisObj.handleMouseEnter($(this), e);
   });

   // bind a mouseleave handler
   this.$parents.mouseleave(function(e) {
      return thisObj.handleMouseLeave($(this), e);
   });

   // bind a click handler
   this.$allItems.click(function(e) {
      return thisObj.handleClick($(this), e);
   });

   //////////// bind key event handlers //////////////////
  
   // bind a keydown handler
   this.$allItems.keydown(function(e) {
      return thisObj.handleKeyDown($(this), e);
   });

   // bind a keypress handler
   this.$allItems.keypress(function(e) {
      return thisObj.handleKeyPress($(this), e);
   });

   // bind a focus handler
   this.$allItems.focus(function(e) {
      return thisObj.handleFocus($(this), e);
   });

   // bind a blur handler
   this.$allItems.blur(function(e) {
      return thisObj.handleBlur($(this), e);
   });

   // bind a document click handler
   $(document).click(function(e) {
         return thisObj.handleDocumentClick(e);
   });

} // end bindHandlers()

/**
* @method handleMouseEnter
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process mouseover events for the top menus.
*
* @param {object} $item - the jquery object of the item firing the event
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns false;
*/

OAA_EXAMPLES.menubar.prototype.handleMouseEnter = function($item, e) {

   // add hover style
   $item.addClass('menu-hover');

   // expand the first level submenu
   if ($item.attr('aria-haspopup') == 'true') {
      $item.children('ul').attr('aria-hidden', 'false');
   }
   //e.stopPropagation();
   return true;

} // end handleMouseEnter()

/**
* @method handleMouseOut
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process mouseout events for the top menus.
*
* @param {object} $item - the jquery object of the item firing the event
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns false;
*/

OAA_EXAMPLES.menubar.prototype.handleMouseOut = function($item, e) {

   // Remover hover styles
   $item.removeClass('menu-hover');

   //e.stopPropagation();
   return true;

} // end handleMouseOut()

/**
* @method handleMouseLeave
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process mouseout events for the top menus.
*
* @param {object} $menu - the jquery object of the item firing the event
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns false;
*/

OAA_EXAMPLES.menubar.prototype.handleMouseLeave = function($menu, e) {

   var $active = $menu.find('.menu-focus');

   // Remove hover style
   $menu.removeClass('menu-hover');

   // if any item in the child menu has focus, move focus to root item
   if ($active.length > 0) {
      this.bChildOpen = false;

      // remove the focus style from the active item
      $active.removeClass('menu-focus'); 

      // store the active item
      this.$activeItem = $menu;
 
      // cannot hide items with focus -- move focus to root item
      $menu.focus();
   }

   // hide the child menu
   $menu.children('ul').attr('aria-hidden', 'true');

   return true;

} // end handleMouseLeave()

/**
* @method handleClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events for the top menus.
*
* @param {object} $item - the jquery object of the item firing the event
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns false;
*/

OAA_EXAMPLES.menubar.prototype.handleClick = function($item, e) {

   var $parentUL = $item.parent();

   if ($parentUL.is('.root-level')) {
         // open the child menu if it is closed
         $item.children('ul').first().attr('aria-hidden', 'false');
   }
   else {
      // process the menu choice
      this.processMenuChoice($item);

      // remove hover and focus styling
      this.$allItems.removeClass('menu-hover menu-focus');

      // close the menu
      this.$id.find('ul').not('.root-level').attr('aria-hidden','true');

      // move focus to the text area
      this.textarea.$id.focus();
   }

   e.stopPropagation();
   return false;

} // end handleClick()

/**
* @method handleFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process focus events for the menu.
*
* @param {object} $item - the jquery object of the item firing the event
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true;
*/

OAA_EXAMPLES.menubar.prototype.handleFocus = function($item, e) {

   // if activeItem is null, we are getting focus from outside the menu. Store
   // the item that triggered the event
   if (this.$activeItem == null) {
      this.$activeItem = $item;
   }
   else if ($item[0] != this.$activeItem[0]) {
      return true;
   }
   
   // get the set of jquery objects for all the parent items of the active item
   var $parentItems = this.$activeItem.parentsUntil('div').filter('li');

   // remove focus styling from all other menu items
   this.$allItems.removeClass('menu-focus');

   // add focus styling to the active item
   this.$activeItem.addClass('menu-focus');

   // add focus styling to all parent items.
   $parentItems.addClass('menu-focus');

   if (this.vmenu == true) {
      // if the bChildOpen flag has been set, open the active item's child menu (if applicable)
      if (this.bChildOpen == true) {

         var $itemUL = $item.parent();

         // if the itemUL is a root-level menu and item is a parent item,
         // show the child menu.
         if ($itemUL.is('.root-level') && ($item.attr('aria-haspopup') == 'true')) {
            $item.children('ul').attr('aria-hidden', 'false');
         }
      }
      else {
         this.vmenu = false;
      }
   }

   return true;

} // end handleFocus()

/**
* @method handleBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process blur events for the menu.
*
* @param {object} $item - the jquery object of the item firing the event
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true;
*/

OAA_EXAMPLES.menubar.prototype.handleBlur = function($item, e) {

   $item.removeClass('menu-focus');

   return true;

} // end handleBlur()

/**
* @method OAA_EXAMPLES handleKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for the menus.
*
* @param {object} $item - the jquery object of the item firing the event
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns false if consuming; true if propagating
*/

OAA_EXAMPLES.menubar.prototype.handleKeyDown = function($item, e) {

   if (e.altKey || e.ctrlKey) {
       // Modifier key pressed: Do not process
       return true;
   }

   switch(e.keyCode) {
      case this.keys.tab: {

         // hide all menu items and update their aria attributes
         this.$id.find('ul').attr('aria-hidden', 'true');

         // remove focus styling from all menu items
         this.$allItems.removeClass('menu-focus');

         this.$activeItem = null;

         this.bChildOpen = false;

         break;
      }
      case this.keys.esc: {
         var $itemUL = $item.parent();

         if ($itemUL.is('.root-level')) {
            // hide the child menu and update the aria attributes
            $item.children('ul').first().attr('aria-hidden', 'true');
         }
         else {

            // move up one level
            this.$activeItem = $itemUL.parent();

            // reset the bChildOpen flag
            this.bChildOpen = false;

            // set focus on the new item
            this.$activeItem.focus();

            // hide the active menu and update the aria attributes
            $itemUL.attr('aria-hidden', 'true');
         }

         e.stopPropagation();
         return false;
      }
      case this.keys.enter:
      case this.keys.space: {

         var $parentUL = $item.parent();

         if ($parentUL.is('.root-level')) {
            // open the child menu if it is closed
            $item.children('ul').first().attr('aria-hidden', 'false');
         }
         else {
            // process the menu choice
            this.processMenuChoice($item);

            // remove hover and focus styling
            this.$allItems.removeClass('menu-hover');
            this.$allItems.removeClass('menu-focus');

            // close the menu
            this.$id.find('ul').not('.root-level').attr('aria-hidden','true');


            // clear the active item
            this.$activeItem = null;

            // move focus to the text area
            this.textarea.$id.focus();
         }

         e.stopPropagation();
         return false;
      }

      case this.keys.left: {

         if (this.vmenu == true && $itemUL.is('.root-level')) {
            // If this is a vertical menu and the root-level is active, move
            // to the previous item in the menu
            this.$activeItem = this.moveUp($item); 
         }
         else {
            this.$activeItem = this.moveToPrevious($item); 
         }

         this.$activeItem.focus();

         e.stopPropagation();
         return false;
      }
      case this.keys.right: {

         if (this.vmenu == true && $itemUL.is('.root-level')) {
            // If this is a vertical menu and the root-level is active, move
            // to the next item in the menu
            this.$activeItem = this.moveDown($item); 
         }
         else {
            this.$activeItem = this.moveToNext($item);
         }

         this.$activeItem.focus();

         e.stopPropagation();
         return false;
      }
      case this.keys.up: {

         if (this.vmenu == true && $itemUL.is('.root-level')) {
            // If this is a vertical menu and the root-level is active, move
            // to the previous root-level menu
            this.$activeItem = this.moveToPrevious($item); 
         }
         else {
            this.$activeItem = this.moveUp($item); 
         }

         this.$activeItem.focus();

         e.stopPropagation();
         return false;
      }
      case this.keys.down: {

         if (this.vmenu == true && $itemUL.is('.root-level')) {
            // If this is a vertical menu and the root-level is active, move
            // to the next root-level menu
            this.$activeItem = this.moveToNext($item); 
         }
         else {
            this.$activeItem = this.moveDown($item); 
         }

         this.$activeItem.focus();

         e.stopPropagation();
         return false;
      }
   } // end switch

   return true;

} // end handleMenuKeyDown()

/**
* @method moveToNext
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to move to the next menu level.
* This will be either the next root-level menu or the child of a menu parent. If
* at the root level and the active item is the last in the menu, this function will 
* loop to the first menu item.
*
* If the menu is a horizontal menu, the first child element of the newly selected menu will
* be selected
*
* @param {object} $item - the active menu item
*
* @return {object} Returns the item to move to. Returns $item is no move is possible
*/

OAA_EXAMPLES.menubar.prototype.moveToNext = function($item) {

   var $itemUL = $item.parent(); // $item's containing menu 
   var $menuItems = $itemUL.children('li'); // the items in the currently active menu
   var menuNum = $menuItems.length; // the number of items in the active menu
   var menuIndex = $menuItems.index($item); // the items index in its menu
   var $newItem = null;
   var $newItemUL = null;

   if ($itemUL.is('.root-level')) {
      // this is the root level move to next sibling. This will require closing
      // the current child menu and opening the new one.
 
      if (menuIndex < menuNum-1) { // not the last root menu
         $newItem = $item.next();
      }
      else { // wrap to first item
         $newItem = $menuItems.first();
      }

      // close the current child menu (if applicable)
      if ($item.attr('aria-haspopup') == 'true') {

         var $childMenu = $item.children('ul').first();

         if ($childMenu.attr('aria-hidden') == 'false') {
            // update the child menu's aria-hidden attribute
            $childMenu.attr('aria-hidden', 'true');
            this.bChildOpen = true;
         }
      }

      // remove the focus styling from the current menu
      $item.removeClass('menu-focus');

      // open the new child menu (if applicable)
      if (($newItem.attr('aria-haspopup') == 'true') && (this.bChildOpen == true)) {

         var $childMenu = $newItem.children('ul').first();

         // Update the child's aria-hidden attribute
         $childMenu.attr('aria-hidden', 'false');

         /*
          * Uncomment this section if the first item in the child menu should be
          * automatically selected
          *
         if (!this.vmenu) {
            // select the first item in the child menu
            $newItem = $childMenu.children('li').first();
         }
         */

      }
   }
   else {
      // this is not the root level. If there is a child menu to be moved into, do that;
      // otherwise, move to the next root-level menu if there is one
      if ($item.attr('aria-haspopup') == 'true') {
         
         var $childMenu = $item.children('ul').first();

         $newItem = $childMenu.children('li').first();

         // show the child menu and update its aria attributes
         $childMenu.attr('aria-hidden', 'false');
      }
      else {
         // at deepest level, move to the next root-level menu
 
         if (this.vmenu == true) {
            // do nothing
            return $item;
         }

         var $parentMenus = null;
         var $rootItem = null;

         // get list of all parent menus for item, up to the root level
         $parentMenus = $item.parentsUntil('div').filter('ul').not('.root-level');

         // hide the current menu and update its aria attributes accordingly
         $parentMenus.attr('aria-hidden', 'true');

         // remove the focus styling from the active menu
         $parentMenus.find('li').removeClass('menu-focus');
         $parentMenus.last().parent().removeClass('menu-focus');

         $rootItem = $parentMenus.last().parent(); // the containing root for the menu

         menuIndex = this.$rootItems.index($rootItem);

         // if this is not the last root menu item, move to the next one
         if (menuIndex < this.$rootItems.length-1) {
            $newItem = $rootItem.next();
         }
         else { // loop
            $newItem = this.$rootItems.first();
         }

         // add the focus styling to the new menu
         $newItem.addClass('menu-focus');

         if ($newItem.attr('aria-haspopup') == 'true') {
            var $childMenu = $newItem.children('ul').first();

            $newItem = $childMenu.children('li').first();

            // show the child menu and update it's aria attributes
            $childMenu.attr('aria-hidden', 'false');
            this.bChildOpen == true;
         }
      }
   }

   return $newItem;
}

/**
* @method moveToPrevious
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to move to the previous menu level.
* This will be either the previous root-level menu or the child of a menu parent. If
* at the root level and the active item is the first in the menu, this function will loop
* to the last menu item.
*
* If the menu is a horizontal menu, the first child element of the newly selected menu will
* be selected
*
* @param {object} $item - the active menu item
*
* @return {object} Returns the item to move to. Returns $item is no move is possible
*/

OAA_EXAMPLES.menubar.prototype.moveToPrevious = function($item) {

   var $itemUL = $item.parent(); // $item's containing menu 
   var $menuItems = $itemUL.children('li'); // the items in the currently active menu
   var menuNum = $menuItems.length; // the number of items in the active menu
   var menuIndex = $menuItems.index($item); // the items index in its menu
   var $newItem = null;
   var $newItemUL = null;

   if ($itemUL.is('.root-level')) {
      // this is the root level move to previous sibling. This will require closing
      // the current child menu and opening the new one.
 
      if (menuIndex > 0) { // not the first root menu
         $newItem = $item.prev();
      }
      else { // wrap to last item
         $newItem = $menuItems.last();
      }

      // close the current child menu (if applicable)
      if ($item.attr('aria-haspopup') == 'true') {

         var $childMenu = $item.children('ul').first();

         if ($childMenu.attr('aria-hidden') == 'false') {
            // update the child menu's aria-hidden attribute
            $childMenu.attr('aria-hidden', 'true');
            this.bChildOpen = true;
         }
      }

      // remove the focus styling from the current menu
      $item.removeClass('menu-focus');

      // open the new child menu (if applicable)
      if (($newItem.attr('aria-haspopup') == 'true') && (this.bChildOpen == true)) {

         var $childMenu = $newItem.children('ul').first();

         // Update the child's aria-hidden attribute
         $childMenu.attr('aria-hidden', 'false');

         /*
          * Uncomment this section if the first item in the child menu should be
          * automatically selected
          *
         if (!this.vmenu) {
            // select the first item in the child menu
            $newItem = $childMenu.children('li').first();
         }
         */

      }
   }
   else {
      // this is not the root level. If there is a parent menu that is not the
      // root menu, move up one level; otherwise, move to first item of the previous
      // root menu.
 
      var $parentLI = $itemUL.parent();
      var $parentUL = $parentLI.parent();

      var $parentMenus = null;
      var $rootItem = null;

      // if this is a vertical menu or is not the first child menu
      // of the root-level menu, move up one level.
      if (this.vmenu == true || !$parentUL.is('.root-level')) {

         $newItem = $itemUL.parent();

         // hide the active menu and update aria-hidden
         $itemUL.attr('aria-hidden', 'true');

         // remove the focus highlight from the $item
         $item.removeClass('menu-focus');

         if (this.vmenu == true) {
            // set a flag so the focus handler does't reopen the menu
            this.bChildOpen = false;
         }

      }
      else { // move to previous root-level menu

         // hide the current menu and update the aria attributes accordingly
         $itemUL.attr('aria-hidden', 'true');

         // remove the focus styling from the active menu
         $item.removeClass('menu-focus');
         $parentLI.removeClass('menu-focus');

         menuIndex = this.$rootItems.index($parentLI);

         if (menuIndex > 0) {
            // move to the previous root-level menu
            $newItem = $parentLI.prev();
         }
         else { // loop to last root-level menu
            $newItem = this.$rootItems.last();
         }

         // add the focus styling to the new menu
         $newItem.addClass('menu-focus');

         if ($newItem.attr('aria-haspopup') == 'true') {
            var $childMenu = $newItem.children('ul').first();

            // show the child menu and update it's aria attributes
            $childMenu.attr('aria-hidden', 'false');
            this.bChildOpen == true;

            $newItem = $childMenu.children('li').first();
         }
      }
   }

   return $newItem;
}

/**
* @method moveDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to select the next item in a menu.
* If the active item is the last in the menu, this function will loop to the
* first menu item.
*
* @param {object} $item - the active menu item
*
* @param {char} startChr - [optional] the character to attempt to match against the beginning of the
* menu item titles. If found, focus moves to the next menu item beginning with that character.
*
* @return {object} Returns the item to move to. Returns $item is no move is possible
*/

OAA_EXAMPLES.menubar.prototype.moveDown = function($item, startChr) {

   var $itemUL = $item.parent(); // $item's containing menu 
   var $menuItems = $itemUL.children('li').not('.separator'); // the items in the currently active menu
   var menuNum = $menuItems.length; // the number of items in the active menu
   var menuIndex = $menuItems.index($item); // the items index in its menu
   var $newItem = null;
   var $newItemUL = null;

   if ($itemUL.is('.root-level')) { // this is the root level menu

      if ($item.attr('aria-haspopup') != 'true') {
         // No child menu to move to
         return $item;
      }

      // Move to the first item in the child menu
      $newItemUL = $item.children('ul').first();
      $newItem = $newItemUL.children('li').first();

      // make sure the child menu is visible
      $newItemUL.attr('aria-hidden', 'false');

      return $newItem;
   }

   // if $item is not the last item in its menu, move to the next item. If startChr is specified, move
   // to the next item with a title that begins with that character.
   //
   if (startChr) {
      var bMatch = false;
      var curNdx = menuIndex+1;

      // check if the active item was the last one on the list
      if (curNdx == menuNum) {
         curNdx = 0;
      }

      // Iterate through the menu items (starting from the current item and wrapping) until a match is found
      // or the loop returns to the current menu item 
      while (curNdx != menuIndex)  {

         var titleChr = $menuItems.eq(curNdx).html().charAt(0);

         if (titleChr.toLowerCase() == startChr) {
            bMatch = true;
            break;
         }

         curNdx = curNdx+1;

         if (curNdx == menuNum) {
            // reached the end of the list, start again at the beginning
            curNdx = 0;
         }
      }

      if (bMatch == true) {
         $newItem = $menuItems.eq(curNdx);

         // remove the focus styling from the current item
         $item.removeClass('menu-focus');

         return $newItem
      }
      else {
         return $item;
      }
   }
   else {
      if (menuIndex < menuNum-1) {
         $newItem = $menuItems.eq(menuIndex+1);
      }
      else {
         $newItem = $menuItems.first();
      }
   }

   // remove the focus styling from the current item
   $item.removeClass('menu-focus');

   return $newItem;
}

/**
* @method moveUp
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to select the previous item in a menu.
* If the active item is the first in the menu, this function will loop to the
* last menu item.
*
* @param {object} $item - the active menu item
*
* @return {object} Returns the item to move to. Returns $item is no move is possible
*/

OAA_EXAMPLES.menubar.prototype.moveUp = function($item) {

   var $itemUL = $item.parent(); // $item's containing menu 
   var $menuItems = $itemUL.children('li').not('.separator'); // the items in the currently active menu
   var menuNum = $menuItems.length; // the number of items in the active menu
   var menuIndex = $menuItems.index($item); // the items index in its menu
   var $newItem = null;
   var $newItemUL = null;

   if ($itemUL.is('.root-level')) { // this is the root level menu

      // nothing to do
      return $item;
   }

   // if $item is not the first item in its menu, move to the previous item
   if (menuIndex > 0) {

      $newItem = $menuItems.eq(menuIndex-1);
   }
   else {
      // loop to top of menu
      $newItem = $menuItems.last();
   }

   // remove the focus styling from the current item
   $item.removeClass('menu-focus');

   return $newItem;
}

/**
* @method handleKeyPress() is a member function to process keydown events
* for the menus.
*
* The Opera browser performs some window commands from the keypress event,
* not keydown like Firefox, Safari, and IE. This event handler consumes
* keypresses for relevant keys so that Opera behaves when the user is
* manipulating the menu with the keyboard.
*
* @param {object} $menu - the jquery object of the item firing the event
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns false if consuming; true if propagating
*/

OAA_EXAMPLES.menubar.prototype.handleKeyPress = function($item, e) {

   if (e.altKey || e.ctrlKey || e.shiftKey) {
       // Modifier key pressed: Do not process
       return true;
   }

   switch(e.keyCode) {
      case this.keys.tab: {
         return true;
      }
      case this.keys.esc:
      case this.keys.enter:
      case this.keys.space:
      case this.keys.up:
      case this.keys.down:
      case this.keys.left:
      case this.keys.right: {

         e.stopPropagation();
         return false;
      }
      default : {
         var chr = String.fromCharCode(e.which);

         this.$activeItem = this.moveDown($item, chr);
         this.$activeItem.focus();

         e.stopPropagation();
         return false;
      }

   } // end switch

   return true;

} // end handleKeyPress()

/**
* @method handleDocumentClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events on the document. Needed
* to close an open menu if a user clicks outside the menu
*
* @param {object} e - the associated event object
*
* @return {boolean} Returns true;
*/

OAA_EXAMPLES.menubar.prototype.handleDocumentClick = function(e) {

   // get a list of all child menus
   var $childMenus = this.$id.find('ul').not('.root-level');

   // hide the child menus
   $childMenus.attr('aria-hidden', 'true');

   this.$allItems.removeClass('menu-focus');

   this.$activeItem = null;

   // allow the event to propagate
   return true;

} // end handleDocumentClick()

/**
* @method processMenuChoice
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process the user's menu item choice.
* Since the menu will close after this, highlight styling is simply removed.
*
* @param {object} $item - the jquery object of the menu item firing the event
*
* @return {N/A}
*/

OAA_EXAMPLES.menubar.prototype.processMenuChoice = function($item) {

	// find the parent menu for this item
	var menuName = $item.parent().attr('id');
	var choice = $item.attr('id');

	// call the appropriate textarea function
	switch(menuName) {
		case 'fontMenu': {
			this.textarea.setFont(choice);

			// update the aria-checked state of the menu items
			$item.attr('aria-checked', 'true');
			$item.siblings().attr('aria-checked', 'false');

			break;
		}
		case 'styleMenu': {
			this.textarea.setStyle(choice);

			// reverse the aria-checked state
			if ($item.attr('aria-checked') == 'true') {
				$item.attr('aria-checked', 'false');
			}
			else {
				$item.attr('aria-checked', 'true');
			}

			break;
		}
		case 'justificationMenu': {
			this.textarea.setAlignment(choice);

			// update the aria-checked state of the menu items
			$item.attr('aria-checked', 'true');
			$item.siblings().attr('aria-checked', 'false');

			break;
		}
		case 'sizeMenu': {
			var $menuItems = $item.siblings().andSelf();
			var $curItem;

			this.textarea.setSize(choice);

			////////////////////////
			// update the aria-checked state by first setting all items to false
			// and then setting the item that matches the currently selected font
			// size.
			
			// set aria-checked to false and removed checked styling
			$menuItems.attr('aria-checked', 'false');

			// determine which menu item matches the current font size
			$curItem = $menuItems.filter('[id=' + this.textarea.getSize() + ']');

			// Set aria-checked for the matching item and apply the checked styling
			$curItem.attr('aria-checked', 'true');

			break;
		}
	} // end switch

} // end processMenuChoice()

"""

example_obj.style       = """
#st1 {
	padding: .5em;
	border: 1px solid black;
	height: 400px;
	width: 70%;
	font-size: medium;
	font-family: sans-serif;
}
ul.menubar {
	margin: 0 !important;
	padding: 0 .25em !important;
	list-style: none !important;
   font-size: 100% !important;
	height: 1.85em;
	width: 20em;
	border: 1px solid black;
	background: #ccc;
}
ul.menubar li {
	float: left;
	display: inline; position: relative;
	margin: 0;
	padding: .25em .35em;
	height: 1.25em;
}
ul.menu {
	position: absolute;
	left: 0;
	top: 1.75em;
	list-style: none;
	margin: 0 !important;
	padding: 0 !important;
	font-weight: normal !important;
   font-size: 100% !important;
	border: 1px solid black;
	background-color: #ccc;
	width: 8.5em;
}
ul.menu li {
	float: none;
	display: block;
	white-space: nowrap;
	padding: 2px 1em;
	color: black;
}

li.separator {
	margin: 0;
	margin-bottom: 4px !important;
	height: 2px !important;
	border-bottom: 1px solid black;
}

li[aria-checked="true"] {
	font-weight: bold;
	background-image: url('{{EXAMPLE_MEDIA}}images/dot.png');
	background-repeat: no-repeat;
	background-position: 5px 10px;
}

ul[aria-hidden="true"] {
   display: none;
}

.menu-hover {
	background-color: #700 !important;
	color: white !important;
}

.menu-hover[aria-checked="true"] {
	background-color: #700 !important;
	color: white !important;
	background-image: url('{{EXAMPLE_MEDIA}}images/dot-selected.png') !important;
}

.menu-focus {
	background-color: black;
	font-weight: bold;
	color: white !important;
}

li.menu-focus[aria-checked="true"] {
	background-color: black;
	font-weight: bold;
	color: white !important;
	background-image: url('{{EXAMPLE_MEDIA}}images/dot-selected.png') !important;
}
.hidden {
   position: absolute;
   left: -200em;
   top: -20em;
}


/*
 * Text area styles
 */
.italic {
	font-style: italic;
}
.bold {
	font-weight: bold;
}
.underline {
	text-decoration: underline;
}
"""

example2 = create_example(example_obj)