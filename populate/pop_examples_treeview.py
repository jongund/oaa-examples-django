"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples import *

spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

order = 1

m1 = ElementDefinition.objects.get(spec = spec_aria10, attribute='role', value='tree')
m2 = ElementDefinition.objects.get(spec = spec_aria10, attribute='role', value='treeitem')
m3 = ElementDefinition.objects.get(spec = spec_aria10, attribute='role', value='group')
m4 = ElementDefinition.objects.get(spec = spec_aria10, attribute='aria-expanded')
m5 = ElementDefinition.objects.get(spec = spec_aria10, attribute='aria-hidden')
m6 = ElementDefinition.objects.get(spec = spec_aria10, attribute='aria-labelledby')
m7 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-owns')

# =============================
# Example 1
# =============================

example_obj             = example_object()
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order          = order
example_obj.title       = 'Treeview'
example_obj.permanent_slug = 'tree1'

example_obj.a11y_features = """
Simple example of a treeview widget.
"""

example_obj.keyboard    = """
The following keyboard shortcuts are implemented for this example (based on recommended shortcuts specified by the "DHTML Style Guide Working Group":http://dev.aol.com/dhtml_style_guide/

    * Up: Select the previous visible tree item
    * Down: Select next visible tree item.
    * Left: Collapse the currently selected parent node if it is expanded. Move to the previous parent node (if possible) when the current parent node is collapsed.
    * Right: Expand the currently selected parent node and move to the first child list item.
    * Enter: Toggle the expanded or collapsed state of the selected parent node.
    * Home: Select the root parent node of the tree.
    * End: Select the last visible node of the tree.
    * Tab: Navigate away from tree.
    * * (asterisk on the numpad): Expand all group nodes.
    * Double-clicking on a parent node will toggle its expanded or collapsed state.

"""

example_obj.markup = [m1,m2,m3,m4,m5,m6]

example_obj.html        = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<h2 id="label_1">Foods</h2>
<ul id="tree1" class="tree root-level" role="tree" aria-labelledby="label_1">
   <li id="fruits" class="tree-parent" role="treeitem" tabindex="0" aria-expanded="true"><span>Fruits</span>
      <ul id="fruit-grp" role="group">
         <li id="oranges" role="treeitem" tabindex="-1">Oranges</li>
         <li id="pinapples" role="treeitem" tabindex="-1">Pineapples</li>
         <li id="apples" class="tree-parent" role="treeitem" tabindex="-1" aria-expanded="false"><span>Apples</span>
            <ul id="apple-grp" role="group">
               <li id="macintosh" role="treeitem" tabindex="-1">Macintosh</li>
               <li id="granny_smith" class="tree-parent" role="treeitem" tabindex="-1" aria-expanded="false"><span>Granny Smith</span>
                  <ul id="granny-grp" role="group">
                     <li id="Washington" role="treeitem" tabindex="-1">Washington State</li>
                     <li id="Michigan" role="treeitem" tabindex="-1">Michigan</li>
                     <li id="New_York" role="treeitem" tabindex="-1">New York</li>
                  </ul>
               </li>
               <li id="fuji" role="treeitem" tabindex="-1">Fuji</li>
            </ul>
         </li>
         <li id="bananas" role="treeitem" tabindex="-1">Bananas</li>		
         <li id="pears" role="treeitem" tabindex="-1">Pears</li>		
      </ul>
   </li>
   <li id="vegetables" class="tree-parent" role="treeitem" tabindex="-1" aria-expanded="true"><span>Vegetables</span>
      <ul id="veg-grp" role="group">
         <li id="broccoli" role="treeitem" tabindex="-1">Broccoli</li>
         <li id="carrots" role="treeitem" tabindex="-1">Carrots</li>
         <li id="lettuce" class="tree-parent" role="treeitem" tabindex="-1" aria-expanded="false"><span>Lettuce</span>
         <ul id="lettuce-grp" role="group">
               <li id="romaine" role="treeitem" tabindex="-1">Romaine</li>
               <li id="iceberg" role="treeitem" tabindex="-1">Iceberg</li>
               <li id="butterhead" role="treeitem" tabindex="-1">Butterhead</li>
         </ul>
         </li>
         <li id="spinach" role="treeitem" tabindex="-1">Spinach</li>		
         <li id="squash" class="tree-parent" role="treeitem" tabindex="-1" aria-expanded="true"><span>Squash</span>
            <ul id="squash-grp" role="group">
               <li id="acorn" role="treeitem" tabindex="-1">Acorn</li>
               <li id="ambercup" role="treeitem" tabindex="-1">Ambercup</li>
               <li id="autumn_cup" role="treeitem" tabindex="-1">Autumn Cup</li>
               <li id="hubbard" role="treeitem" tabindex="-1">Hubbard</li>
               <li id="kobacha" role="treeitem" tabindex="-1">Kabocha</li>
               <li id="butternut" role="treeitem" tabindex="-1">Butternut</li>
               <li id="spaghetti" role="treeitem" tabindex="-1">Spaghetti</li>
               <li id="sweet_dumpling" role="treeitem" tabindex="-1">Sweet Dumpling</li>
               <li id="turban" role="treeitem" tabindex="-1">Turban</li>
            </ul>
         </li>
      </ul>
   </li>
</ul>

"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};

$(document).ready(function() {

  var treeviewApp = new OAA_EXAMPLES.treeview('tree1');

}); // end ready

/**
* @constructor treeview
*
* @memberOf OAA_EXAMPLES
*
* @desc a class constructor for a treeview widget. The widget binds to an
* unordered list. The top-level <ul> must have role='tree'. All list items must have role='treeitem'.
*
* Tree groups must be embedded lists within the listitem that heads the group. the top <ul> of a group
* must have role='group'. aria-expanded is used to indicate whether a group is expanded or collapsed. This
* property must be set on the listitem the encapsulates the group.
*
* parent nodes must be given the class tree-parent.
*
* @param {string} treeID - the html id of the top-level <ul> of the list to bind the widget to
*
* @return {N/A}
*/

/**
* @constructor Internal Properties
*
* @property {array} $items - jQuery array of list items
*
* @property {array} $parents - jQuery array of parent nodes
*
* @property {array} $visibleItems - holds a jQuery array of the currently visible items in the tree
*
* @property {object} $activeItem - holds the jQuery object for the active item
*/

OAA_EXAMPLES.treeview = function(treeID) {

  // define the object properties
  this.$id = $('#' + treeID);
  this.$items = this.$id.find('li');
  this.$parents = this.$id.find('.tree-parent');
   this.$visibleItems = null;
   this.$activeItem = null; 

  this.keys = {
            tab:      9,
            enter:    13,
            space:    32,
            pageup:   33,
            pagedown: 34,
            end:      35,
            home:     36,
            left:     37,
            up:       38,
            right:    39,
            down:     40,
            asterisk: 106
   };


  // initialize the treeview
  this.init();

  // bind event handlers
  this.bindHandlers();

} // end treeview() constructor

/**
* @method init
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to initialize the treeview widget. It traverses the tree, identifying
* which listitems are headers for groups and applying initial collapsed are expanded styling
*
* @return {N/A}
*/

OAA_EXAMPLES.treeview.prototype.init = function() {

   // insert the header image. Note: this method allows the widget to degrade gracefully
   // if javascript is disabled or there is some other error.
   this.$parents.prepend('<img class="headerImg" src="{{EXAMPLE_MEDIA}}images/expanded.gif" alt="Group expanded"/>');

   // If the aria-expanded is false, hide the group and display the collapsed state image
   this.$parents.each(function() {
      if ($(this).attr('aria-expanded') == 'false') {
         $(this).children('ul').hide().attr('aria-hidden', 'true');
         $(this).children('img').attr('src', '{{EXAMPLE_MEDIA}}images/contracted.gif').attr('alt', 'Group collapsed');
      }
   });

   this.$visibleItems = this.$id.find('li:visible');

} // end init()

/**
* @method expandGroup
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to expand a collapsed group
*
* @param {object} $item - the jquery id of the parent item of the group
*
* @param {boolean} hasFocus - true if the parent has focus, false otherwise
*
* @return {N/A}
*/

OAA_EXAMPLES.treeview.prototype.expandGroup = function($item, hasFocus) {

  var $group = $item.children('ul'); // find the first child ul node

  // expand the group
  $group.show().attr('aria-hidden', 'false');

   // set the aria-expanded property
  $item.attr('aria-expanded', 'true');

  if (hasFocus == true) {
    $item.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/expanded-focus.gif').attr('alt', 'Group expanded');
  }
  else {
    $item.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/expanded.gif').attr('alt', 'Group expanded');
  }

   // update the list of visible items
   this.$visibleItems = this.$id.find('li:visible');

} // end expandGroup()

/**
* @method collapseGroup
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to collapse an expanded group
*
* @param {object} $item - the jquery id of the parent item of the group to collapse
*
* @param {boolean} hasFocus - true if the parent item has focus, false otherwise
*
* @return {N/A}
*/

OAA_EXAMPLES.treeview.prototype.collapseGroup = function($item, hasFocus) {

  var $group = $item.children('ul');

  // collapse the group
  $group.hide().attr('aria-hidden', 'true');

   // update the aria-expanded property
  $item.attr('aria-expanded', 'false');

  if (hasFocus == true) {
    $item.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/contracted-focus.gif').attr('alt', 'Group collapsed');
  }
  else {
    $item.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/contracted.gif').attr('alt', 'Group collapsed');
  }

   // update the list of visible items
   this.$visibleItems = this.$id.find('li:visible');

} // end collapseGroup()

/**
* @method toggleGroup
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to toggle the display state of a group
*
* @param {object} $item - the jquery id of the parent item of the group to toggle
*
* @param {boolean} hasFocus - true if the parent item has focus, false otherwise
*
* @return {N/A}
*/

OAA_EXAMPLES.treeview.prototype.toggleGroup = function($item, hasFocus) {

  var $group = $item.children('ul');

  if ($item.attr('aria-expanded') == 'true') {
    // collapse the group
    this.collapseGroup($item, hasFocus);
  }
  else {
    // expand the group
    this.expandGroup($item, hasFocus);
  }

} // end toggleGroup()

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers to the listitems
*
* return {N/A}
*/

OAA_EXAMPLES.treeview.prototype.bindHandlers = function() {

  var thisObj = this;

  // bind a dblclick handler to the parent items
  this.$parents.dblclick(function(e) {
    return thisObj.handleDblClick($(this), e);
  });

  // bind a click handler
  this.$items.click(function(e) {
    return thisObj.handleClick($(this), e);
  });

  // bind a keydown handler
  this.$items.keydown(function(e) {
    return thisObj.handleKeyDown($(this), e);
  });

  // bind a keypress handler
  this.$items.keypress(function(e) {
    return thisObj.handleKeyPress($(this), e);
  });

  // bind a focus handler
  this.$items.focus(function(e) {
    return thisObj.handleFocus($(this), e);
  });

  // bind a blur handler
  this.$items.blur(function(e) {
    return thisObj.handleBlur($(this), e);
  });

   // bind a document click handler
   $(document).click(function(e) {

         if (thisObj.$activeItem != null) {
            // remove the focus styling
            thisObj.$activeItem.removeClass('tree-focus');

            if (thisObj.$activeItem.hasClass('tree-parent') == true) {

               // this is a parent item, remove the focus image
               if (thisObj.$activeItem.attr('aria-expanded') == 'true') {
                  thisObj.$activeItem.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/expanded.gif');
               }
               else {
                  thisObj.$activeItem.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/contracted.gif');
               }
            }

            // set activeItem to null
            thisObj.$activeItem = null;
         }

         return true;
   });

} // end bindHandlers()

/**
* @method updateStyling
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to update the styling for the tree items
*
* @param {object} $item - the jQuery object of the item to highlight
*
* @return {N/A}
*/

OAA_EXAMPLES.treeview.prototype.updateStyling = function($item) {

  // remove the focus and highlighting from the treeview items
  // and remove them from the tab order.
  this.$items.removeClass('tree-focus').attr('tabindex', '-1');

  // remove the focus image from other parents
  this.$parents.each(function() {

    // remove the focus image
    if ($(this).attr('aria-expanded') == 'true') {
      $(this).children('img').attr('src', '{{EXAMPLE_MEDIA}}images/expanded.gif');
    }
    else {
      $(this).children('img').attr('src', '{{EXAMPLE_MEDIA}}images/contracted.gif');
    }
  });

   // add the focus image to the current parent
  if ($item.is('.tree-parent')) {
    if ($item.attr('aria-expanded') == 'true') {
      $item.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/expanded-focus.gif');
    }
    else {
      $item.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/contracted-focus.gif');
    }
  }


  // apply the focus and styling and place the element in the tab order
  $item.addClass('tree-focus').attr('tabindex', '0');

} // end updateStyling()

/**
* @method handleKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for the treeview items
*
* @param {object} $id - the jQuery id of the item firing the event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false if consuming event; true if not
*/

OAA_EXAMPLES.treeview.prototype.handleKeyDown = function($item, e) {

  var curNdx = this.$visibleItems.index($item);

  if ((e.altKey || e.ctrlKey)
       || (e.shiftKey && e.keyCode != this.keys.tab)) {
    // do nothing
    return true;
  }

  switch (e.keyCode) {
      case this.keys.tab: {
         // set activeItem to null
         this.$activeItem = null;

         // remove the focus styling
         $item.removeClass('tree-focus');

         if ($item.hasClass('tree-parent') == true) {

            // this is a parent item, remove the focus image
            if ($item.attr('aria-expanded') == 'true') {
               $item.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/expanded.gif');
            }
            else {
               $item.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/contracted.gif');
            }
         }

         return true;
      }
    case this.keys.home: { // jump to first item in tree

         // store the active item
         this.$activeItem = this.$parents.first();

         // set focus on the active item
      this.$activeItem.focus();

      e.stopPropagation();
      return false;
    }
    case this.keys.end: { // jump to last visible item

         // store the active item
         this.$activeItem = this.$visibleItems.last();

         // set focus on the active item
      this.$activeItem.focus();

      e.stopPropagation();
      return false;
    }
    case this.keys.enter:
    case this.keys.space: {

      if (!$item.is('.tree-parent')) {
        // do nothing
      }
         else {
            // toggle the child group open or closed
         this.toggleGroup($item, true);
         }

      e.stopPropagation();
      return false;
    }
    case this.keys.left: {
      
      if ($item.is('.tree-parent') && $item.attr('aria-expanded') == 'true') {
            // collapse the group and return

            this.collapseGroup($item, true);
         }
         else {
            // move up to the parent
            var $itemUL = $item.parent();
            var $itemParent = $itemUL.parent();

            // store the active item
            this.$activeItem = $itemParent;

            // set focus on the parent
            this.$activeItem.focus();
         }

      e.stopPropagation();
      return false;
    }
    case this.keys.right: {
      
      if (!$item.is('.tree-parent')) {
        // do nothing

         }
         else if ($item.attr('aria-expanded') == 'false') {
        this.expandGroup($item, true);
      }
         else {
            // move to the first item in the child group
            this.$activeItem = $item.children('ul').children('li').first();

            this.$activeItem.focus();
         }

      e.stopPropagation();
      return false;
    }
    case this.keys.up: {

      if (curNdx > 0) {
        var $prev = this.$visibleItems.eq(curNdx - 1);

            // store the active item
            this.$activeItem = $prev;

        $prev.focus();
      }

      e.stopPropagation();
      return false;
    }
    case this.keys.down: {

      if (curNdx < this.$visibleItems.length - 1) {
        var $next = this.$visibleItems.eq(curNdx + 1);

            // store the active item
            this.$activeItem = $next;

        $next.focus();
      }
      e.stopPropagation();
      return false;
    }
    case this.keys.asterisk: {
      // expand all groups

      var thisObj = this;

         this.$parents.each(function() {
            if (thisObj.$activeItem[0] == $(this)[0]) {
               thisObj.expandGroup($(this), true);
            }
            else {
               thisObj.expandGroup($(this), false);
            }
      });

      e.stopPropagation();
      return false;
    }
  }

  return true;

} // end handleKeyDown

/**
* @method handleKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for the treeview items
* This function is needed for browsers, such as Opera, that perform window
* manipulation on kepress events rather than keydown. The function simply consumes the event.
*
* @param {object} $id - the jQuery id of the parent item firing event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false if consuming event; true if not
*/

OAA_EXAMPLES.treeview.prototype.handleKeyPress = function($item, e) {

  if (e.altKey || e.ctrlKey || e.shiftKey) {
    // do nothing
    return true;
  }

  switch (e.keyCode) {
    case this.keys.tab: {
      return true;
    }
    case this.keys.enter:
    case this.keys.home:
    case this.keys.end:
    case this.keys.left:
    case this.keys.right:
    case this.keys.up:
    case this.keys.down: {
      e.stopPropagation();
      return false;
    }
      default : {
         var chr = String.fromCharCode(e.which);
         var bMatch = false;
         var itemNdx = this.$visibleItems.index($item);
         var itemCnt = this.$visibleItems.length;
         var curNdx = itemNdx + 1;

         // check if the active item was the last one on the list
         if (curNdx == itemCnt) {
            curNdx = 0;
         }

         // Iterate through the menu items (starting from the current item and wrapping) until a match is found
         // or the loop returns to the current menu item
         while (curNdx != itemNdx)  {

            var $curItem = this.$visibleItems.eq(curNdx);
            var titleChr = $curItem.text().charAt(0);
            
            if ($curItem.is('.tree-parent')) {
               titleChr = $curItem.find('span').text().charAt(0);
            }

            if (titleChr.toLowerCase() == chr) {
               bMatch = true;
               break;
            }

            curNdx = curNdx+1;

            if (curNdx == itemCnt) {
               // reached the end of the list, start again at the beginning
               curNdx = 0;
            }
         }

         if (bMatch == true) {
            this.$activeItem = this.$visibleItems.eq(curNdx);
            this.$activeItem.focus();
         }

         e.stopPropagation();
         return false;
      }
  }

  return true;

} // end handleKeyPress

/**
* @method handleDblClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process double-click events for parent items.
* Double-click expands or collapses a group.
*
* @param {object} $item - the jQuery object of the tree parent item firing event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false if consuming event; true if not
*/

OAA_EXAMPLES.treeview.prototype.handleDblClick = function($id, e) {

  if (e.altKey || e.ctrlKey || e.shiftKey) {
    // do nothing
    return true;
  }

   // update the active item
   this.$activeItem = $id;

  // apply the focus highlighting
  this.updateStyling($id);

  // expand or collapse the group
  this.toggleGroup($id, true);

  e.stopPropagation();
  return false;

} // end handleDblClick

/**
* @method handleClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events.
*
* @param {object} $id - the jQuery id of the parent item firing event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false if consuming event; true if not
*/

OAA_EXAMPLES.treeview.prototype.handleClick = function($id, e) {

  if (e.altKey || e.ctrlKey || e.shiftKey) {
    // do nothing
    return true;
  }

   // update the active item
   this.$activeItem = $id;

  // apply the focus highlighting
  this.updateStyling($id);

  e.stopPropagation();
  return false;

} // end handleClick

/**
* @method handleFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process focus events.
*
* @param {object} $item - the jQuery id of the parent item firing event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.treeview.prototype.handleFocus = function($item, e) {

   if (this.$activeItem == null) {
      this.$activeItem = $item;
   }

   this.updateStyling(this.$activeItem);

  return true;

} // end handleFocus

/**
* @method handleBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process blur events.
*
* @param {object} $id - the jQuery id of the parent item firing event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.treeview.prototype.handleBlur = function($id, e) {

  return true;

} // end handleBlur
"""

example_obj.style       = """
h2#label_1 {
margin: .5em 0 !important;
padding: 0 !important;
font-size: 1.6em !important;
}
ul.tree {
  width: 16em;
  font-size: 100% !important;
}
ul.tree, ul.tree ul {
  list-style: none;
  margin: 0 !important;
  padding-left: 20px !important;
  font-weight: normal;
  font-size: 100% !important;
  background-color: #f9f9f9;
  color: black;
}

ul.tree li {
  margin-left: 17px !important;
}

li.tree-parent {
  font-weight: bold;
  margin-left: 0px;
}

img.headerImg {
	margin-right: 5px;
}

li.tree-focus {
  color: white;
  background: black;
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
example_obj.title       = 'Treeview: Using aria-owns'
example_obj.permanent_slug = 'tree2'

example_obj.a11y_features = """
Simple example of a treeview widget using aria-owns to define markup relationships.
"""

example_obj.keyboard    = """
The following keyboard shortcuts are implemented for this example (based on recommended shortcuts specified by the "DHTML Style Guide Working Group":http://dev.aol.com/dhtml_style_guide/

    * Up: Select the previous visible tree item.
    * Down: Select next visible tree item.
    * Left: Collapse the currently selected parent node if it is expanded. Move to the previous parent node (if possible) when the current parent node is collapsed.
    * Right: Expand the currently selected parent node and move to the first child list item.
    * Enter: Toggle the expanded or collapsed state of the selected parent node.
    * Home: Select the root parent node of the tree.
    * End: Select the last visible node of the tree.
    * Tab: Navigate away from tree.
    * * (asterisk on the numpad): Expand all group nodes.
    * Double-clicking on a parent node will toggle its expanded or collapsed state.

"""

example_obj.markup = [m1,m2,m3,m4,m5,m6,m7]

example_obj.html        = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<div id="application" role="application">

<h2 id="label_1">Animal, Mineral, or Vegetable</h2>
<div id="tree1" class="tree root-level" role="tree" aria-labelledby="label_1" tabindex="-1">
   <div id="animals" class="tree-parent" role="treeitem" aria-owns="animalGroup" aria-expanded="true" tabindex="0">
      <img class="parentImg" role="treeitem" src="{{EXAMPLE_MEDIA}}images/expanded.gif" alt="Group expanded"/>
      <span>Animals</span>
   </div>
   <div id="animalGroup" class="group" role="group">
      <div id="birds" class="tree-item" role="treeitem" tabindex="-1">Birds</div>

      <div id="cats" class="tree-parent" role="treeitem" aria-owns="catGroup" aria-expanded="false" tabindex="-1">
         <img class="parentImg" role="treeitem" tabindex="-1" src="{{EXAMPLE_MEDIA}}images/contracted.gif" alt="Group collapsed"/>
         <span>Cats</span>
      </div>
      <div id="catGroup" class="group" role="group">
         <div id="siamese" class="tree-item" role="treeitem" tabindex="-1">Siamese</div>
         <div id="tabby" class="tree-item" role="treeitem" tabindex="-1">Tabby</div>
      </div>
      <div id="dogs" class="tree-parent" role="treeitem" aria-owns="dogGroup" aria-expanded="true" tabindex="-1">
         <img class="parentImg" role="treeitem" tabindex="-1" src="{{EXAMPLE_MEDIA}}images/expanded.gif" alt="Group expanded"/>
         <span>Dogs</span>
      </div>
      <div id="dogGroup" class="group" role="group">
         <div id="smallBreeds" class="tree-parent" role="treeitem" aria-owns="smallBreedGroup" aria-expanded="true" tabindex="-1">
            <img class="parentImg" role="treeitem" tabindex="-1" src="{{EXAMPLE_MEDIA}}images/expanded.gif" alt="Group expanded"/>
            <span>Small Breeds</span>
         </div>
         <div id="smallBreedGroup" class="group" role="group">
            <div id="chihuahua" class="tree-item" role="treeitem" tabindex="-1">Chihuahua</div>
            <div id="italian_greyhound" class="tree-item" role="treeitem" tabindex="-1">Italian Greyhound</div>
            <div id="Japanese_chin" class="tree-item" role="treeitem" tabindex="-1">Japanese Chin</div>
         </div>
         <div id="mediumBreeds" class="tree-parent" role="treeitem" aria-owns="mediumBreedGroup" aria-expanded="false" tabindex="-1">
            <img class="parentImg" role="treeitem" tabindex="-1" src="{{EXAMPLE_MEDIA}}images/contracted.gif" alt="Group collapsed"/>
            <span>Medium Breeds</span>
         </div>
         <div id="mediumBreedGroup" class="group" role="group">
            <div id="beagle" class="tree-item" role="treeitem" tabindex="-1">Beagle</div>
            <div id="cocker_spaniel" class="tree-item" role="treeitem" tabindex="-1">Cocker Spaniel</div>
            <div id="pit_bull" class="tree-item" role="treeitem" tabindex="-1">Pit Bull</div>
         </div>
         <div id="largeBreeds" class="tree-parent" role="treeitem" aria-owns="largeBreedGroup" aria-expanded="false" tabindex="-1">
            <img class="parentImg" role="treeitem" tabindex="-1" src="{{EXAMPLE_MEDIA}}images/contracted.gif" alt="Group collapsed"/>
            <span>Large Breeds</span>
         </div>
         <div id="largeBreedGroup" class="group" role="group">
            <div id="afghan" class="tree-item" role="treeitem", tabindex="-1">Afghan</div>
            <div id="great_dane" class="tree-item" role="treeitem" tabindex="-1">Great Dane</div>
            <div id="mastiff" class="tree-item" role="treeitem" tabindex="-1">Mastiff</div>
         </div>
      </div>
   </div>
   <div id="minerals" class="tree-parent" role="treeitem" aria-owns="mineralGroup" aria-expanded="true" tabindex="-1">
      <img class="parentImg" role="treeitem" tabindex="-1" src="{{EXAMPLE_MEDIA}}images/expanded.gif" alt="Group expanded"/>
      <span>Minerals</span>
   </div>
   <div id="mineralGroup" class="group" role="group">
      <div id="zinc" class="tree-item" role="treeitem" tabindex="-1">Zinc</div>
      <div id="gold" class="tree-parent" role="treeitem" aria-owns="goldGroup" aria-expanded="false" tabindex="-1">
         <img class="parentImg" role="treeitem" tabindex="-1" src="{{EXAMPLE_MEDIA}}images/contracted.gif" alt="Group collapsed"/>
         <span>Gold</span>
      </div>
      <div id="goldGroup" class="group" role="group">
         <div id="yellow_gold" class="tree-item" role="treeitem" tabindex="-1">Yellow Gold</div>
         <div id="white_gold" class="tree-item" role="treeitem" tabindex="-1">White Gold</div>
      </div>
      <div id="silver" class="tree-item" role="treeitem" tabindex="-1">Silver</div>
   </div>
   <div id="vegetables" class="tree-parent" role="treeitem" aria-owns="vegetableGroup" aria-expanded="true" tabindex="-1">
      <img class="parentImg" role="treeitem" tabindex="-1" src="{{EXAMPLE_MEDIA}}images/expanded.gif" alt="Group expanded"/>
      <span>Vegetables</span>
   </div>
   <div id="vegetableGroup" class="group" role="group">
      <div id="carrot" class="tree-item" role="treeitem" tabindex="-1">Carrot</div>
      <div id="tomato" class="tree-item" role="treeitem" tabindex="-1">Tomato</div>
      <div id="lettuce" class="tree-item" role="treeitem" tabindex="-1">Lettuce</div>
   </div>
</div>

</div>
"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};
$(document).ready(function() {

	var treeviewApp = new OAA_EXAMPLES.treeview('tree1');

}); // end ready

/**
* @constructor treeview
*
* @memberOf OAA_EXAMPLES
*
* @desc a class constructor for a treeview widget. The widget binds to an
* unordered list. The top-level <ul> must have role='tree'. All list items must have role='treeitem'.
*
* Tree groups must be embedded lists within the listitem that heads the group. the top <ul> of a group
* must have role='group'. aria-expanded is used to indicate whether a group is expanded or collapsed. This
* property must be set on the listitem the encapsulates the group.
*
* parent nodes must be given the class tree-parent.
*
* @param {string} treeID - the html id of the top-level <ul> of the list to bind the widget to
*
* @return {N/A}
*/

/**
* @constructor Internal Properties
*
* @property {array} $ListItems - jQuery array of tree items
*
* @property {array} $parents - jQuery array of parent nodes
*
* @property {array} $visibleItems - holds a jQuery array of the currently visible items in the tree
*
* @property {object} $activeItem - holds the jQuery object for the active item
*/

OAA_EXAMPLES.treeview = function (treeID) {

	// define the object properties
	this.$id = $('#' + treeID);
	this.$listItems = this.$id.find('div').not('.group'); // an array of tree items
	this.$parents = this.$id.find('.tree-parent'); // an array of the parent items
	this.$visibleItems = undefined; // an array of currently visible tree Items (including parents)
   this.$activeItem = null; // holds the jQuery object of the active tree item

   this.keys = {
            tab:      9,
            enter:    13,
            space:    32,
            pageup:   33,
            pagedown: 34,
            end:      35,
            home:     36,
            left:     37,
            up:       38,
            right:    39,
            down:     40,
            asterisk: 106
   };

	// initialize the treeview
	this.init();

	// bind event handlers
	this.bindHandlers();

} // end treeview() constructor

/**
* @method init
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to initialize the treeview widget. It traverses the tree, identifying
* which listitems are headers for groups and applying initial collapsed are expanded styling
*
* @return {N/A}
*/

OAA_EXAMPLES.treeview.prototype.init = function() {

	var thisObj = this;

	// iterate through the tree and apply the styling to the tree parents
	this.$parents.each (function(index) {

		var $group = $('#' + $(this).attr('aria-owns'));

		// If the aria-expanded is false, hide the group and display the collapsed state image
		if ($(this).attr('aria-expanded') == 'false') {
			$group.hide().attr('aria-hidden', 'true');
			$(this).find('img').attr('src', '{{EXAMPLE_MEDIA}}images/contracted.gif').attr('alt', 'Group collapsed');
		}
	});

	// create the initial visible item array
	this.$visibleItems = this.$listItems.filter(':visible');

} // end init()

/**
* @method expandGroup
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to expand a collapsed group
*
* @param {object} $item - the jquery id of the parent item of the group
*
* @param {boolean} hasFocus - true if the parent has focus, false otherwise
*
* @return {N/A}
*/

OAA_EXAMPLES.treeview.prototype.expandGroup = function($item, hasFocus) {

	var $group = $('#' + $item.attr('aria-owns'));

	// expand the group
	$group.show().attr('aria-hidden', 'false');

	$item.attr('aria-expanded', 'true');

	if (hasFocus == true) {
		$item.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/expanded-focus.gif').attr('alt', 'Group expanded');
	}
	else {
		$item.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/expanded.gif').attr('alt', 'Group expanded');
	}

	// refresh the list of visible items
	this.$visibleItems = this.$listItems.filter(':visible');

} // end expandGroup()


/**
* @method collapseGroup
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to collapse an expanded group
*
* @param {object} $item - the jquery id of the parent item of the group to collapse
*
* @param {boolean} hasFocus - true if the parent item has focus, false otherwise
*
* @return {N/A}
*/

OAA_EXAMPLES.treeview.prototype.collapseGroup = function($item, hasFocus) {

	var $group = $('#' + $item.attr('aria-owns'));

	// collapse the group
	$group.hide().attr('aria-hidden', 'true');

	$item.attr('aria-expanded', 'false');

	if (hasFocus == true) {
		$item.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/contracted-focus.gif').attr('alt', 'Group collapsed');
	}
	else {
		$item.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/contracted.gif').attr('alt', 'Group collapsed');
	}

	// refresh the list of visible items
	this.$visibleItems = this.$listItems.filter(':visible');

} // end collapseGroup()

/**
* @method collapseGroup
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to collapse an expanded group
*
* @param {object} $item - the jquery id of the parent item of the group to collapse
*
* @param {boolean} hasFocus - true if the parent item has focus, false otherwise
*
* @return {N/A}
*/

OAA_EXAMPLES.treeview.prototype.toggleGroup = function($item, hasFocus) {

	if ($item.attr('aria-expanded') == 'true') {
		// collapse the group
		this.collapseGroup($item, hasFocus);
	}
	else {
		// expand the group
		this.expandGroup($item, hasFocus);
	}

} // end toggleGroup()

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers to the listItems
*
* return {N/A}
*/

OAA_EXAMPLES.treeview.prototype.bindHandlers = function() {

	var thisObj = this;

	// bind a dblclick handler to the parent items
	this.$parents.dblclick(function(e) {
		return thisObj.handleDblClick($(this), e);
	});

	// bind a click handler
	this.$listItems.click(function(e) {
		return thisObj.handleClick($(this), e);
	});

	// bind a keydown handler
	this.$listItems.keydown(function(e) {
		return thisObj.handleKeyDown($(this), e);
	});

	// bind a keypress handler
	this.$listItems.keypress(function(e) {
		return thisObj.handleKeyPress($(this), e);
	});

	// bind a focus handler
	this.$listItems.focus(function(e) {
		return thisObj.handleFocus($(this), e);
	});

	// bind a blur handler
	this.$listItems.blur(function(e) {
		return thisObj.handleBlur($(this), e);
	});

   // bind a document click handler
   $(document).click(function(e) {

         if (thisObj.$activeItem != null) {
            // remove the focus styling
            thisObj.$activeItem.removeClass('tree-focus');

            if (thisObj.$activeItem.hasClass('tree-parent') == true) {

               // this is a parent item, remove the focus image
               if (thisObj.$activeItem.attr('aria-expanded') == 'true') {
                  thisObj.$activeItem.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/expanded.gif');
               }
               else {
                  thisObj.$activeItem.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/contracted.gif');
               }
            }

            // set activeItem to null
            thisObj.$activeItem = null;
         }

         return true;
   });

} // end bindHandlers()

/**
* @method updateStyling
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to update the styling for the tree items
*
* @param {object} $item - the jQuery object of the item to highlight
*
* @return {N/A}
*/

OAA_EXAMPLES.treeview.prototype.updateStyling = function($item) {

	// remove the focus highlighting from the treeview items
	// and remove them from the tab order.
	this.$listItems.removeClass('tree-focus').attr('tabindex', '-1');

	// remove the focus image from parent items
	this.$parents.each(function() {
		// add the focus image
		if ($(this).attr('aria-expanded') == 'true') {
			$(this).children('img').attr('src', '{{EXAMPLE_MEDIA}}images/expanded.gif');
		}
		else {
			$(this).children('img').attr('src', '{{EXAMPLE_MEDIA}}images/contracted.gif');
		}
	});

	if ($item.hasClass('tree-parent') == true) {

		// add the focus image
		if ($item.attr('aria-expanded') == 'true') {
			$item.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/expanded-focus.gif');
		}
		else {
			$item.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/contracted-focus.gif');
		}
	}

	// apply the focus highlighting and place the element in the tab order
	$item.addClass('tree-focus').attr('tabindex', '0');

} // end updateStyling()

/**
* @method handleKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for the treeview items
*
* @param {object} $id - the jQuery id of the item firing the event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false if consuming event; true if not
*/

OAA_EXAMPLES.treeview.prototype.handleKeyDown = function($item, e) {

	var $itemGroup = $item.parent();
	var curNdx = this.$visibleItems.index($item);

	if ((e.altKey || e.ctrlKey)
       || (e.shiftKey && e.keyCode != this.keys.tab)) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
      case this.keys.tab: {
         // set activeItem to null
         this.$activeItem = null;

         // remove the focus styling
         $item.removeClass('tree-focus');

         if ($item.hasClass('tree-parent') == true) {

            // this is a parent item, remove the focus image
            if ($item.attr('aria-expanded') == 'true') {
               $item.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/expanded.gif');
            }
            else {
               $item.children('img').attr('src', '{{EXAMPLE_MEDIA}}images/contracted.gif');
            }
         }

         return true;
      }
		case this.keys.home: {

         // store the active item
         this.$activeItem = this.$parents.first();

         // set focus on the active item
			this.$activeItem.focus();

			e.stopPropagation();
			return false;
		}
		case this.keys.end: {

         // store the active item
         this.$activeItem = this.$visibleItems.last();

         // set focus on the active item
			this.$activeItem.focus();

			e.stopPropagation();
			return false;
		}
		case this.keys.enter:
		case this.keys.space: {

			if ($item.hasClass('tree-parent') == false) {
				// do nothing
			}
         else {
            // toggle the display of the child group
            this.toggleGroup($item, true);
         }

			e.stopPropagation();
			return false;
		}
		case this.keys.left: {
			
			if ($item.hasClass('tree-parent') == true
            && $item.attr('aria-expanded') == 'true') {

            this.collapseGroup($item, true);
			}
			else {
				// move up to the parent

            var groupID = $itemGroup.attr('id');

            // set the parent tree item as the active item
            this.$activeItem = this.$parents.filter('[aria-owns=' + groupID + ']'); 

            // set focus on the active item
            this.$activeItem.focus();
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.right: {
			
			if ($item.hasClass('tree-parent') == false) {
				// do nothing
			}
         else if ($item.attr('aria-expanded') == 'false') {
               this.expandGroup($item, true);
         }
         else {
            var $childGroup = $('#' + $item.attr('aria-owns'));

            // move to the first item in the child group
            this.$activeItem = $childGroup.children('div').not('group').first();

            // set focus on the active item
            this.$activeItem.focus();
         }

			e.stopPropagation();
			return false;
		}
		case this.keys.up: {

			if (curNdx > 0) {
				var $prev = this.$visibleItems.eq(curNdx - 1);

            // stroe the new active item
            this.$activeItem = $prev;

            // set focus
				$prev.focus();
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.down: {

			if (curNdx < this.$visibleItems.length - 1) {
				var $next = this.$visibleItems.eq(curNdx + 1);

            // stroe the new active item
            this.$activeItem = $next;

				$next.focus();
			}
			e.stopPropagation();
			return false;
		}
		case this.keys.asterisk: {
			// expand all groups

			var thisObj = this;

			this.$parents.each(function() {
            if (thisObj.$activeItem[0] == $(this)[0]) {
               thisObj.expandGroup($(this), true);
            }
            else {
               thisObj.expandGroup($(this), false);
            }
			});

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleKeyDown

/**
* @method handleKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for the treeview items
* This function is needed for browsers, such as Opera, that perform window
* manipulation on kepress events rather than keydown. The function simply consumes the event.
*
* @param {object} $id - the jQuery id of the parent item firing event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false if consuming event; true if not
*/

OAA_EXAMPLES.treeview.prototype.handleKeyPress = function($item, e) {

	if (e.altKey || e.ctrlKey || e.shiftKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
      case this.keys.tab: {
         return true;
      }
		case this.keys.enter:
		case this.keys.space:
		case this.keys.home:
		case this.keys.end:
		case this.keys.left:
		case this.keys.right:
		case this.keys.up:
		case this.keys.down: {
			e.stopPropagation();
			return false;
		}
      default : {
         var chr = String.fromCharCode(e.which);
         var bMatch = false;
         var itemNdx = this.$visibleItems.index($item);
         var itemCnt = this.$visibleItems.length;
         var curNdx = itemNdx + 1;

         // check if the active item was the last one on the list
         if (curNdx == itemCnt) {
            curNdx = 0;
         }

         // Iterate through the menu items (starting from the current item and wrapping) until a match is found
         // or the loop returns to the current menu item 
         while (curNdx != itemNdx)  {

            var $curItem = this.$visibleItems.eq(curNdx);
            var titleChr = $curItem.text().charAt(0);
            
            if ($curItem.is('.tree-parent')) {
               titleChr = $curItem.find('span').text().charAt(0);
            }

            if (titleChr.toLowerCase() == chr) {
               bMatch = true;
               break;
            }

            curNdx = curNdx+1;

            if (curNdx == itemCnt) {
               // reached the end of the list, start again at the beginning
               curNdx = 0;
            }
         }

         if (bMatch == true) {
            this.$activeItem = this.$visibleItems.eq(curNdx);
            this.$activeItem.focus();
         }

         e.stopPropagation();
         return false;
      }
	}

	return true;

} // end handleKeyPress

/**
* @method handleDblClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process double-click events for parent items.
* Double-click expands or collapses a group.
*
* @param {object} $item - the jQuery object of the tree parent item firing event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false if consuming event; true if not
*/

OAA_EXAMPLES.treeview.prototype.handleDblClick = function($id, e) {

	if (e.altKey || e.ctrlKey || e.shiftKey) {
		// do nothing
		return true;
	}

   // update the active item
   this.$activeItem = $id;

	// apply the focus highlighting
	this.updateStyling($id);

	// expand or collapse the group
	this.toggleGroup($id, true);

	e.stopPropagation();
	return false;

} // end handleDblClick

/**
* @method handleClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events.
*
* @param {object} $id - the jQuery id of the parent item firing event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false if consuming event; true if not
*/

OAA_EXAMPLES.treeview.prototype.handleClick = function($item, e) {

	if (e.altKey || e.ctrlKey || e.shiftKey) {
		// do nothing
		return true;
	}

   // update the active item
   this.$activeItem = $item;

	// apply the focus highlighting
	this.updateStyling($item);

	e.stopPropagation();
	return false;

} // end handleClick

/**
* @method handleFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process focus events.
*
* @param {object} $item - the jQuery id of the parent item firing event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.treeview.prototype.handleFocus = function($item, e) {


   if (this.$activeItem == null) {
      this.$activeItem = $item;
   }

   this.updateStyling(this.$activeItem);


	return true;

} // end handleFocus

/**
* @method handleBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process blur events.
*
* @param {object} $id - the jQuery id of the parent item firing event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns true
*/
OAA_EXAMPLES.treeview.prototype.handleBlur = function($id, e) {

	return true;

} // end handleBlur
"""

example_obj.style       = """
h2#label_1 {
margin: .5em 0 !important;
padding: 0 !important;
font-size: 1.6em !important;
}
div.tree {
  margin-left: 20px;
  padding: 0;
  width: 15em;
}
div.group {
  padding-left: 22px;
}
div.tree-item {
  padding-left: 22px;
}
div.tree-parent {
	font-weight: bold;
}

img.parentImg {
	margin-right: 5px;
}

div.tree-focus {
  color: white;
  background: black;
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
example_obj.title       = 'Treeview: ARIA CSS Selectors'
example_obj.permanent_slug = 'tree3'

example_obj.a11y_features = """
Simple example of a tree widget using ARIA CSS selectors to show visual state. Not all browsers support CSS selectors. Further, some browsers will not display background images in high contrast mode.
"""
example_obj.keyboard    = """
The following keyboard shortcuts are implemented for this example (based on recommended shortcuts specified by the "DHTML Style Guide Working Group":http://dev.aol.com/dhtml_style_guide/

    * Up: Select the previous visible tree item.
    * Down: Select next visible tree item.
    * Left: Collapse the currently selected parent node if it is expanded. Move to the previous parent node (if possible) when the current parent node is collapsed.
    * Right: Expand the currently selected parent node and move to the first child list item.
    * Enter: Toggle the expanded or collapsed state of the selected parent node.
    * Home: Select the root parent node of the tree.
    * End: Select the last visible node of the tree.
    * Tab: Navigate away from tree.
    * (asterisk on the numpad): Expand all group nodes.
    * Double-clicking on a parent node will toggle its expanded or collapsed state.

"""

example_obj.markup = [m1,m2,m3,m4,m5,m6]

example_obj.html        = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<h2 id="label_1">Foods</h2>
<ul id="tree1" class="tree root-level" role="tree" aria-labelledby="label_1">
   <li id="fruits" class="tree-parent" role="treeitem" tabindex="0" aria-expanded="true"><span>Fruits</span>
      <ul role="group">
         <li id="oranges" role="treeitem" tabindex="-1"><span>Oranges</span></li>
         <li id="pinapples" role="treeitem" tabindex="-1"><span>Pineapples</span></li>
         <li id="apples" class="tree-parent" role="treeitem" tabindex="-1" aria-expanded="false"><span>Apples</span>
            <ul role="group">
               <li id="macintosh" role="treeitem" tabindex="-1"><span>Macintosh</span></li>
               <li id="granny_smith" class="tree-parent" role="treeitem" tabindex="-1" aria-expanded="false"><span>Granny Smith</span>
                  <ul role="group">
                     <li id="Washington" role="treeitem" tabindex="-1"><span>Washington State</span></li>
                     <li id="Michigan" role="treeitem" tabindex="-1"><span>Michigan</span></li>
                     <li id="New_York" role="treeitem" tabindex="-1"><span>New York</span></li>
                  </ul>
               </li>
               <li id="fuji" role="treeitem" tabindex="-1"><span>Fuji</span></li>
            </ul>
         </li>
         <li id="bananas" role="treeitem" tabindex="-1"><span>Bananas</span></li>		
         <li id="pears" role="treeitem" tabindex="-1"><span>Pears</span></li>		
      </ul>
   </li>
   <li id="vegetables" class="tree-parent" role="treeitem" tabindex="-1" aria-expanded="true"><span>Vegetables</span>
      <ul role="group">
         <li id="broccoli" role="treeitem" tabindex="-1"><span>Broccoli</span></li>
         <li id="carrots" role="treeitem" tabindex="-1"><span>Carrots</span></li>
         <li id="lettuce" class="tree-parent" role="treeitem" tabindex="-1" aria-expanded="false"><span>Lettuce</span>
         <ul role="group">
               <li id="romaine" role="treeitem" tabindex="-1"><span>Romaine</span></li>
               <li id="iceberg" role="treeitem" tabindex="-1"><span>Iceberg</span></li>
               <li id="butterhead" role="treeitem" tabindex="-1"><span>Butterhead</span></li>
         </ul>
         </li>
         <li id="spinach" role="treeitem" tabindex="-1"><span>Spinach</span></li>		
         <li id="squash" class="tree-parent" role="treeitem" tabindex="-1" aria-expanded="true"><span>Squash</span>
            <ul role="group">
               <li id="acorn" role="treeitem" tabindex="-1"><span>Acorn</span></li>
               <li id="ambercup" role="treeitem" tabindex="-1"><span>Ambercup</span></li>
               <li id="autumn_cup" role="treeitem" tabindex="-1"><span>Autumn Cup</span></li>
               <li id="hubbard" role="treeitem" tabindex="-1"><span>Hubbard</span></li>
               <li id="kobacha" role="treeitem" tabindex="-1"><span>Kabocha</span></li>
               <li id="butternut" role="treeitem" tabindex="-1"><span>Butternut</span></li>
               <li id="spaghetti" role="treeitem" tabindex="-1"><span>Spaghetti</span></li>
               <li id="sweet_dumpling" role="treeitem" tabindex="-1"><span>Sweet Dumpling</span></li>
               <li id="turban" role="treeitem" tabindex="-1"><span>Turban</span></li>
            </ul>
         </li>
      </ul>
   </li>
</ul>

"""
example_obj.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {} ;
$(document).ready(function() {

	var treeviewApp = new OAA_EXAMPLES.treeview('tree1');

}); // end ready

/**
* @constructor treeview
*
* @memberOf OAA_EXAMPLES
*
* @desc a class constructor for a treeview widget. The widget binds to an
* unordered list. The top-level <ul> must have role='tree'. All list items must have role='treeitem'.
*
* Tree groups must be embedded lists within the listitem that heads the group. the top <ul> of a group
* must have role='group'. aria-expanded is used to indicate whether a group is expanded or collapsed. This
* property must be set on the listitem the encapsulates the group.
*
* parent nodes must be given the class tree-parent.
*
* @param {string} treeID - the html id of the top-level <ul> of the list to bind the widget to
*
* @return {N/A}
*/

/**
* @constructor Internal Properties
*
* @property {array} $ListItems - jQuery array of tree items
*
* @property {array} $parents - jQuery array of parent nodes
*
* @property {array} $visibleItems - holds a jQuery array of the currently visible items in the tree
*
* @property {object} $activeItem - holds the jQuery object for the active item
*/

OAA_EXAMPLES.treeview = function(treeID) {

	// define the object properties
	this.$id = $('#' + treeID);
	this.$items = this.$id.find('li'); 
	this.$parents = this.$id.find('.tree-parent');
   this.$visibleItems = null;  
   this.$activeItem = null; 
	this.keys = {
            tab:      9,
            enter:    13,
            space:    32,
            pageup:   33,
            pagedown: 34,
            end:      35,
            home:     36,
            left:     37,
            up:       38,
            right:    39,
            down:     40,
            asterisk: 106
   };


	// initialize the treeview
	this.init();

	// bind event handlers
	this.bindHandlers();

} // end treeview() constructor

/**
* @method init
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to initialize the treeview widget. It traverses the tree, identifying
* which listitems are headers for groups and applying initial collapsed are expanded styling
*
* @return {N/A}
*/

OAA_EXAMPLES.treeview.prototype.init = function() {

   // insert the header image. Note: this method allows the widget to degrade gracefully
   // if javascript is disabled or there is some other error.

   // If the aria-expanded is false, hide the group and display the collapsed state image
   this.$parents.each(function() {
      if ($(this).attr('aria-expanded') == 'false') {
         $(this).children('ul').attr('aria-hidden', 'true');
      }
      else {
         $(this).children('ul').attr('aria-hidden', 'false');
      }
   });

   this.$visibleItems = this.$id.find('li:visible');

} // end init()

/**
* @method expandGroup
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to expand a collapsed group
*
* @param {object} $item - the jquery id of the parent item of the group
*
* @param {boolean} hasFocus - true if the parent has focus, false otherwise
*
* @return {N/A}
*/

OAA_EXAMPLES.treeview.prototype.expandGroup = function($item, hasFocus) {

	var $group = $item.children('ul'); // find the first child ul node

	// display the group
	$group.attr('aria-hidden', 'false');

   // set the aria-expanded property
	$item.attr('aria-expanded', 'true');

   // update the list of visible items
   this.$visibleItems = this.$id.find('li:visible');

} // end expandGroup()

/**
* @method collapseGroup
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to collapse an expanded group
*
* @param {object} $item - the jquery id of the parent item of the group to collapse
*
* @param {boolean} hasFocus - true if the parent item has focus, false otherwise
*
* @return {N/A}
*/

OAA_EXAMPLES.treeview.prototype.collapseGroup = function($item, hasFocus) {

	var $group = $item.children('ul');

	// hide the group
	$group.attr('aria-hidden', 'true');

   // update the aria-expanded property
	$item.attr('aria-expanded', 'false');

   // update the list of visible items
   this.$visibleItems = this.$id.find('li:visible');

} // end collapseGroup()

/**
* @method toggleGroup
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to toggle the display state of a group
*
* @param {object} $item - the jquery id of the parent item of the group to toggle
*
* @param {boolean} hasFocus - true if the parent item has focus, false otherwise
*
* @return {N/A}
*/

OAA_EXAMPLES.treeview.prototype.toggleGroup = function($item, hasFocus) {

	var $group = $item.children('ul');

	if ($item.attr('aria-expanded') == 'true') {
		// collapse the group
		this.collapseGroup($item, hasFocus);
	}
	else {
		// expand the group
		this.expandGroup($item, hasFocus);
	}

} // end toggleGroup()

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers to the listitems
*
* return {N/A}
*/

OAA_EXAMPLES.treeview.prototype.bindHandlers = function() {

	var thisObj = this;

	// bind a dblclick handler to the parent items
	this.$parents.dblclick(function(e) {
		return thisObj.handleDblClick($(this), e);
	});

	// bind a click handler
	this.$items.click(function(e) {
		return thisObj.handleClick($(this), e);
	});

	// bind a keydown handler
	this.$items.keydown(function(e) {
		return thisObj.handleKeyDown($(this), e);
	});

	// bind a keypress handler
	this.$items.keypress(function(e) {
		return thisObj.handleKeyPress($(this), e);
	});

	// bind a focus handler
	this.$items.focus(function(e) {
		return thisObj.handleFocus($(this), e);
	});

	// bind a blur handler
	this.$items.blur(function(e) {
		return thisObj.handleBlur($(this), e);
	});

   // bind a document click handler
   $(document).click(function(e) {

         if (thisObj.$activeItem != null) {
            // remove the focus styling
            thisObj.$activeItem.removeClass('tree-focus');

            // set activeItem to null
            thisObj.$activeItem = null;
         }

         return true;
   });

} // end bindHandlers()

/**
* @method updateStyling
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to update the styling for the tree items
*
* @param {object} $item - the jQuery object of the item to highlight
*
* @return {N/A}
*/

OAA_EXAMPLES.treeview.prototype.updateStyling = function($item) {

	// remove the focus and highlighting from the treeview items
	// and remove them from the tab order.
	this.$items.removeClass('tree-focus').attr('tabindex', '-1');


	// apply the focus and styling and place the element in the tab order
	$item.addClass('tree-focus').attr('tabindex', '0');

} // end updateStyling()

/**
* @method handleKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for the treeview items
*
* @param {object} $id - the jQuery id of the item firing the event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false if consuming event; true if not
*/

OAA_EXAMPLES.treeview.prototype.handleKeyDown = function($item, e) {

	var curNdx = this.$visibleItems.index($item);

	if ((e.altKey || e.ctrlKey)
       || (e.shiftKey && e.keyCode != this.keys.tab)) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
      case this.keys.tab: {
         // set activeItem to null
         this.$activeItem = null;

         // remove the focus styling
         $item.removeClass('tree-focus');

         return true;
      }
		case this.keys.home: { // jump to first item in tree

         // store the active item
         this.$activeItem = this.$parents.first();

         // set focus on the active item
			this.$activeItem.focus();

			e.stopPropagation();
			return false;
		}
		case this.keys.end: { // jump to last visible item

         // store the active item
         this.$activeItem = this.$visibleItems.last();

         // set focus on the active item
			this.$activeItem.focus();

			e.stopPropagation();
			return false;
		}
		case this.keys.enter:
		case this.keys.space: {

			if (!$item.is('.tree-parent')) {
				// do nothing
			}
         else {
            // toggle the child group open or closed
			   this.toggleGroup($item, true);
         }

			e.stopPropagation();
			return false;
		}
		case this.keys.left: {
			
			if ($item.is('.tree-parent') && $item.attr('aria-expanded') == 'true') {
            // collapse the group and return
 
            this.collapseGroup($item, true);
         }
         else {
            // move up to the parent
            var $itemUL = $item.parent();
            var $itemParent = $itemUL.parent();

            // store the active item
            this.$activeItem = $itemParent;

            // set focus on the parent
            this.$activeItem.focus();
         }

			e.stopPropagation();
			return false;
		}
		case this.keys.right: {
			
			if (!$item.is('.tree-parent')) {
				// do nothing 

         }
         else if ($item.attr('aria-expanded') == 'false') {
				this.expandGroup($item, true);
			}
         else {
            // move to the first item in the child group
            this.$activeItem = $item.children('ul').children('li').first();

            this.$activeItem.focus();
         }

			e.stopPropagation();
			return false;
		}
		case this.keys.up: {

			if (curNdx > 0) {
				var $prev = this.$visibleItems.eq(curNdx - 1);

            // store the active item
            this.$activeItem = $prev;

				$prev.focus();
			}

			e.stopPropagation();
			return false;
		}
		case this.keys.down: {

			if (curNdx < this.$visibleItems.length - 1) {
				var $next = this.$visibleItems.eq(curNdx + 1);

            // store the active item
            this.$activeItem = $next;

				$next.focus();
			}
			e.stopPropagation();
			return false;
		}
		case this.keys.asterisk: {
			// expand all groups

			var thisObj = this;

         this.$parents.each(function() {
            if (thisObj.$activeItem[0] == $(this)[0]) {
               thisObj.expandGroup($(this), true);
            }
            else {
               thisObj.expandGroup($(this), false);
            }
			});

			e.stopPropagation();
			return false;
		}
	}

	return true;

} // end handleKeyDown

/**
* @method handleKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for the treeview items
* This function is needed for browsers, such as Opera, that perform window
* manipulation on kepress events rather than keydown. The function simply consumes the event.
*
* @param {object} $id - the jQuery id of the parent item firing event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false if consuming event; true if not
*/

OAA_EXAMPLES.treeview.prototype.handleKeyPress = function($item, e) {

	if (e.altKey || e.ctrlKey || e.shiftKey) {
		// do nothing
		return true;
	}

	switch (e.keyCode) {
      case this.keys.tab: {
         return true;
      }
		case this.keys.enter:
		case this.keys.home:
		case this.keys.end:
		case this.keys.left:
		case this.keys.right:
		case this.keys.up:
		case this.keys.down: {
			e.stopPropagation();
			return false;
		}
      default : {
         var chr = String.fromCharCode(e.which);
         var bMatch = false;
         var itemNdx = this.$visibleItems.index($item);
         var itemCnt = this.$visibleItems.length;
         var curNdx = itemNdx + 1;

         // check if the active item was the last one on the list
         if (curNdx == itemCnt) {
            curNdx = 0;
         }

         // Iterate through the menu items (starting from the current item and wrapping) until a match is found
         // or the loop returns to the current menu item 
         while (curNdx != itemNdx)  {

            var titleChr = this.$visibleItems.eq(curNdx).find('span').text().charAt(0);

            if (titleChr.toLowerCase() == chr) {
               bMatch = true;
               break;
            }

            curNdx = curNdx+1;

            if (curNdx == itemCnt) {
               // reached the end of the list, start again at the beginning
               curNdx = 0;
            }
         }

         if (bMatch == true) {
            this.$activeItem = this.$visibleItems.eq(curNdx);
            this.$activeItem.focus();
         }

         e.stopPropagation();
         return false;
      }
	}

	return true;

} // end handleKeyPress

/**
* @method handleDblClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process double-click events for parent items.
* Double-click expands or collapses a group.
*
* @param {object} $item - the jQuery object of the tree parent item firing event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false if consuming event; true if not
*/

OAA_EXAMPLES.treeview.prototype.handleDblClick = function($id, e) {

	if (e.altKey || e.ctrlKey || e.shiftKey) {
		// do nothing
		return true;
	}

   // update the active item
   this.$activeItem = $id;

	// apply the focus highlighting
	this.updateStyling($id);

	// expand or collapse the group
	this.toggleGroup($id, true);

	e.stopPropagation();
	return false;

} // end handleDblClick

/**
* @method handleClick
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process click events.
*
* @param {object} $id - the jQuery id of the parent item firing event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns false if consuming event; true if not
*/

OAA_EXAMPLES.treeview.prototype.handleClick = function($id, e) {

	if (e.altKey || e.ctrlKey || e.shiftKey) {
		// do nothing
		return true;
	}

   // update the active item
   this.$activeItem = $id;

	// apply the focus highlighting
	this.updateStyling($id);

	e.stopPropagation();
	return false;

} // end handleClick

/**
* @method handleFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process focus events.
*
* @param {object} $item - the jQuery id of the parent item firing event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.treeview.prototype.handleFocus = function($item, e) {

   if (this.$activeItem == null) {
      this.$activeItem = $item;
   }

   this.updateStyling(this.$activeItem);

	return true;

} // end handleFocus

/**
* @method handleBlur
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process blur events.
*
* @param {object} $id - the jQuery id of the parent item firing event
*
* @param {object} e - the associated event object
*
* @return {boolean} returns true
*/

OAA_EXAMPLES.treeview.prototype.handleBlur = function($id, e) {

	return true;

} // end handleBlur
"""

example_obj.style       = """
h2#label_1 {
margin: .5em 0 !important;
padding: 0 !important;
font-size: 1.6em !important;
}
ul.tree {
  width: 17em;
  font-size: 100% !important;
}
ul.tree, ul.tree ul {
  list-style: none;
  margin: 0 !important;
  padding-left: 20px !important;
  font-weight: normal;
  font-size: 100% !important;
  background-color: #f9f9f9;
  color: black;
}

ul.tree li {
  margin-left: 17px !important;
}

li.tree-focus {
  color: white;
  background-color: black !important;
}

li.tree-parent {
  font-weight: bold;
  margin-left: 0;
  background: url('{{EXAMPLE_MEDIA}}images/contracted.gif') no-repeat 2px 3px;
}
li.tree-parent[aria-expanded="true"] {
  background: url('{{EXAMPLE_MEDIA}}images/expanded.gif') no-repeat 2px 3px;
}

li.tree-focus[aria-expanded="false"] {
  background: url('{{EXAMPLE_MEDIA}}images/contracted-focus.gif') no-repeat 2px 3px;
}
li.tree-focus[aria-expanded="true"] {
  background: url('{{EXAMPLE_MEDIA}}images/expanded-focus.gif') no-repeat 2px 3px;
}

li.tree-parent span {
   margin-left: 17px;
}

ul[aria-hidden="true"] {
   display: none;
}
"""

example3 = create_example(example_obj)