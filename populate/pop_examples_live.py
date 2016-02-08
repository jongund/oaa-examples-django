"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples import *

order = 1

spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='log')
m2 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='option')
m3 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='timer')
m4 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-activedescendant')
m5 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-atomic')
m6 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-live')
m7 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-relevant')
m8 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-selected')

# =============================
# Example 1
# =============================


example_obj             = example_object()
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order       = order
example_obj.title       = 'Live Region'
example_obj.permanent_slug = 'live1'

example_obj.a11y_features = """
Simple example of a live region widget with two timers.
"""
example_obj.keyboard    = """
"""

example_obj.markup = [m1,m2,m3,m4,m5,m6,m7,m8]

example_obj.html        = """
<div class="controls">

<h2>RSS Feed Controls</h2>

<div><label for="id_rss_feed_select">Select an RSS Feed</label>:
       <select id="id_rss_feed_select">
         <option id="id_feed1"
          value="http://en-us.fxfeeds.mozilla.com/en-US/firefox/headlines.xml" selected>Mozilla Latest Headlines
         </option>
         <option id="id_feed2"
          value="http://news.google.com/?output=rss">Google News
         </option>
         <option id="id_feed3"
           value="http://feeds.bbci.co.uk/news/rss.xml">BBC News
         </option>
         <option id="id_feed4"
          value="http://hosted.ap.org/lineups/TOPHEADS.rss?SITE=AP&SECTION=HOME">Associated Press News
         </option>
         <option id="id_feed5"
          value="http://rss.slashdot.org/Slashdot/slashdot">Slashdot
         </option>
       </select></div>

<div><label for="id_interval_select">Select an Update Interval</label>:
       <select id="id_interval_select">
         <option value="1">1 minute</option>
         <option value="5" selected >5 minutes</option>
         <option value="10">10 minutes</option>
       </select></div>
<hr />

<div><label for="id_rss_politeness_select">Politeness Level (aria-live value)</label>:
       <select id="id_rss_politeness_select">
         <option id="id_rss_polite1" value="off">off
         </option>
         <option id="id_rss_polite2" value="polite">polite
         </option>
         <option id="id_rss_polite3" value="assertive" selected>assertive
         </option>
       </select>
</div>

<div><label for="id_rss_atomic_select">Atomic Updates</label>:
       <select id="id_rss_atomic_select">
         <option id="id_atomic_select1" value="false" selected>false
         </option>
         <option id="id_atomic_select2" value="true">true
         </option>
       </select></div>

<div><label for="id_rss_relevant_select">Change Relevance</label>:
       <select id="id_rss_relevant_select">
         <option selected value="additions" selected>additions
         </option>
         <option value="removals">removals
         </option>
         <option value="text">text
         </option>
         <option value="all">all
         </option>
       </select></div>
</div>

<div class="controls">
<h2>Timer Controls</h2>
<div><label for="id_timer_politeness_select">Politeness Level (aria-live value)</label>:
       <select id="id_timer_politeness_select">
         <option id="id_timer_polite1" value="off">off
         </option>
         <option id="id_timer_polite2" value="polite" selected>polite
         </option>
         <option id="id_timer_polite3" value="assertive">assertive
         </option>
       </select>
</div>

<div><label for="id_timer_atomic_select">Atomic Updates</label>:
       <select id="id_timer_atomic_select" role="listbox">
         <option id="id_timer_atomic1" value="false">false
         </option>
         <option id="id_timer_atomic2" value="true" selected>true
         </option>
       </select></div>

<div><label for="id_timer_relevant_select">Change Relevance</label>:
       <select id="id_timer_relevant_select">
         <option id="id_timer_relevant1" value="additions" selected>additions
         </option>
         <option id="id_timer_relevant2" value="removals">removals
         </option>
         <option id="id_timer_relevant3" value="text">text
         </option>
         <option id="id_timer_relevant4" value="all" selected>all
         </option>
       </select></div>

<hr/>
  <div id="id_countdown">
    <label for="timer">Time until next update</label>:
    <div id="id_timer"></div>
  </div>
</div>

<div id="id_rss_feed_content">
  &nbsp;
</div> 
"""
example_obj.script = """

// jQuery reference for jGFeed
(function($){$.extend({jGFeed:function(url,fnk,num,key){if(url==null){return false;}var gurl="http://ajax.googleapis.com/ajax/services/feed/load?v=1.0&callback=?&q="+url;if(num!=null){gurl+="&num="+num;}if(key!=null){gurl+="&key="+key;}$.getJSON(gurl,function(data){if(typeof fnk=="function"){fnk.call(this,data.responseData.feed);}else{return false;}});}});})(jQuery);

var g_seconds =  0;
var OAA_EXAMPLES = OAA_EXAMPLES ||{};  // Class of Open Ajax Alliance methods used in the examples

/**
* @method ready
*
* @desc executed when page is opened. Initializes text arrays
* and other variables required to perform later functions.
* 
* @return {N/A}
*/

$(document).ready(function() {

  // set the globabal second countdown variable before we create the associated
  // live region
  g_seconds =  $('#id_interval_select').val() * 60 - 1;

  var timerRegion = new OAA_EXAMPLES.liveRegion('timer', 'OAA_EXAMPLES.countdown()', 1000);
  var rssRegion = new OAA_EXAMPLES.liveRegion('id_rss_feed_content', 'getRssFeed()', $('#id_interval_select').val() * 60000);

  // do initial rss grab
  getRssFeed();

  //////////////////// bind event handlers for rssRegion controls /////////////////////////////

  // bind a change event handler for the RSS feed select
  $('#id_rss_feed_select').change(function(e) {

    if ($(this).val() != null) {
      // get the new feed
      getRssFeed();
    }

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the interval select
  $('#id_interval_select').change(function(e) {

    if ($(this).val() != null) {
      // set the new timer interval
      rssRegion.setInterval($(this).val() * 60000);

      // update the countdown interval
      g_seconds = $(this).val() * 60 - 1;
    }

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the politeness select
  $('#id_rss_politeness_select').change(function(e) {

    if ($(this).val() != null) {
      // set the politeness level
      rssRegion.setPoliteness($(this).val());
    }

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the atomic updates select
  $('#id_rss_atomic_select').change(function(e) {

    if ($(this).val() != null) {
      // set the atomic update setting
      rssRegion.setAtomic($(this).val());
    }

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the update relevance select
  $('#id_rss_relevant_select').change(function(e) {

    if ($(this).val() != null) {
      // set the update relevance setting
      rssRegion.setRelevant($(this).val());
    }

    e.stopPropagation();
    return false;
  });

  //////////////////// bind event handlers for timer controls /////////////////////////////

  // bind a change event handler for the politeness select
  $('#id_timer_politeness_select').change(function(e) {

    if ($(this).val() != null) {
      // set the politeness level
      timerRegion.setPoliteness($(this).val());
    }

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the atomic updates select
  $('#id_timer_atomic_select').change(function(e) {

    if ($(this).val() != null) {
      // set the atomic update setting
      timerRegion.setAtomic($(this).val());
    }

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the update relevance select
  $('#id_timer_relevant_select').change(function(e) {

    if ($(this).val() != null) {
      // set the update relevance setting
      timerRegion.setRelevant($(this).val());
    }

    e.stopPropagation();
    return false;
  });
}); // end ready


/**
* @method countdown
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback to update the countdown live region. This callback is passed to rssRegion.
*
* @return {N/A}
*/

OAA_EXAMPLES.countdown = function() {
  var minutes = Math.floor(g_seconds / 60);
  var seconds = g_seconds % 60;

  if (seconds < 10) {
    seconds = '0' + seconds;
  }

  if (g_seconds == 0) {
    // do nothing - countdown will be reset by the
    // rssRegion interval timer
    $('#id_timer').text('updating');
  }
  else {
  $('#id_timer').text(minutes + ':' + seconds);
    g_seconds--;
  }
}

/**
* @method getRssFeed
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback to obtain the top 5 items from an RSS feed. the function checks
* the entries obtained against those that may have been obtained previously (present in the live region).
* It will remove old entries and prepend newer ones it has received. This callback is passed to rssRegion.
*
* @return {N/A}
*/

function getRssFeed(){

  var $id = $('#id_rss_feed_content');
  var $topEntry = $id.find('.entry').first();

  $.jGFeed($('#id_rss_feed_select').val(), function(feed) {
    if(!feed) {
      alert('there was an error');
    }

    // Check to see if this is a new article
    if ($topEntry) {
      var topTitle = $topEntry.find('.storyLink').text();
      var topNdx;

      // iterate through the feed entries and find the index
      // of the matching story.
      for(topNdx = 0; topNdx < feed.entries.length; topNdx++) {
        if (topTitle == feed.entries[topNdx].title) {
          break;
        }
      }

      if (topNdx == feed.entries.length) {
        // there was no match. Clear the region and
        // append all articles
        $id.empty();
      }
      else {
        // there was a match. Remove as many articles
        // as there are new ones from the feed.
        for (var ndx = 0; ndx < topNdx; ndx++) {
          // remove the last entry
          $id.find('.entry').last().remove();
        }
      }
    }

    for (var i = topNdx - 1; i >= 0; i--) {

      var entry = feed.entries[i];
      var title = entry.title;
      var link = entry.link;
      var description = entry.contentSnippet;
      var pubDate = entry.publishedDate;

      var html = '<div class="entry"><h4 class="postTitle">'
               + '<a class="storyLink" href="' + link + '" target="_blank" tabindex="0">'
        + title + '</a>';
      html += '<br><em class="date">' + pubDate + '</em></h4><div class="summary">';
      html += '<p class="description">' + description + '</p></div></div>';
        
      $id.prepend(html);
    }
  }, 5);

  // reset cowntdown
  g_seconds = $('#id_interval_select').val() * 60 - 1;

} // end getRssFeed() 

///////////////////////////////// liveRegion  Widget Definition /////////////////////////////////////

/**
* @method liveRegion
*
* @memberOf OAA_EXAMPLES
*
* @desc a constructor to define an ARIA live region widget. The widget binds to a div
* on the page and accepts a callback function that is triggered at a specified interval.
*
* By default, the live region's alert level is polite, it's updates are non-atomic, additions are relevant,
* and it uses the general channel. These default values may be overridden by either specifying different
* values in the html markup or by calling the widget's corresponding update functions.
*
* @param {string} id - the html id of the div to bind to.
*
* @param {callback} func - the callback function to execute at the specified interval
*
* @param {integer} interval - the initial update interval
*
* @return N/A
*/

/**
* @constructor liveRegion
*
* @memberOf OAA_EXAMPLES
*
* @desc Define the object properties
*
* @property {string}  - the id of the text region to update
*
* @property {Array} content - an array of text strings
* @property {object} func - the callback to execute after each interval
*
* @property {integer} interval - the interval to use for the timer
*
* @property {object} timer - the interval timer object
*/

OAA_EXAMPLES.liveRegion = function(id, func, interval) {

  // define widget properties

  this.$id = $('#' + id);

  this.func = func;
  this.interval = interval;
  this.timer = null;

  // set the initial live region aria attributes. Check if the user
  // has specified values in the html markup. If so, use those
  // values.

  var tmp = this.$id.attr('aria-live');

  if (tmp) {
    this.politeness = tmp;
  }
  else {
    this.politeness = 'polite';
  }

  tmp = this.$id.attr('aria-atomic');
  if (tmp) {
    this.atomic = tmp;
  }
  else {
    this.atomic = 'false';
  }

  tmp = this.$id.attr('aria-relevant');
  if (tmp) {
    this.relevant = tmp;
  }
  else {
    this.relevant = 'additions';
  }

  this.busy = false; // set to true while the region is updating

  // create the update timer
  this.createTimer();

} // end liveRegion constructor

/**
* @method createTimer
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to create an interval timer for
* the live region widget.
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.createTimer = function() {

  if (this.timer != null) {
    // destroy the existing timer
    this.destroyTimer();
  }

  this.timer = setInterval(this.func, this.interval);

} // end createTimer()

/**
* @method destroyTimer
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to remove the interval timer for
* the live region widget.
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.destroyTimer = function() {

  if (this.timer != null) {
    clearInterval(this.timer);    
    this.timer = null;
  }

} // end createTimer()

/**
* @method setInterval
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to change the update interval
* of the live region. This function stores the new interval, clears the current
* interval timer and creates new one with the specified interval.
*
* @param {integer} interval - the new interval, in minutes, to set
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setInterval = function(interval) {
  this.interval = interval;

  this.createTimer();

} // end setInterval()

/**
* @method setPoliteness
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the aria-polite attribute of
* the live region.
*
* @param {string} val - one of three possible states: 'off', 'polite', 'assertive';
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setPoliteness = function(val) {

  this.$id.attr('aria-live', val);
} // end setPoliteness()

/**
* @method setAtomic
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the aria-atomic attribute of
* the live region.
*
* @param {boolean} val - true if live region updates should be atomic
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setAtomic = function(val) {

  this.$id.attr('aria-atomic', val);

} // end setAtomic()

/**
* @method setRelevant
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the aria-relevant attribute of
* the live region.
*
* @param {string} val - may be 'additions', 'removals', or 'text'. It may also be a
* space seperated combination of these.
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setRelevant = function(val) {

  this.$id.attr('aria-relevant', val);

} // end setRelevant()


"""
example_obj.style       = """
div#application {
  height: 30em;
}
div.controls {
  margin-left: 10px;
  padding: 5px 10px;
  width: 21em;
  float: left;
  clear: both;
  border-bottom: 1px solid #008;
}
button,
select {
  float: right;
}
h2 {
  clear: both;
}
div.example {
  margin-top: 50px;
  margin-left: 30px;
  width: 22em;
  float: left;
}
div#region1Container {
  margin-left: 4em;
  padding: 10px;
  width: 11em;
  height: 1.6em;
  float: left;
}
div#region1Container label {
  padding-top: 10px;
  font-weight: bold;
}
div#liveregion1 {
  margin: 0;
  padding: 2px 5px;
  float: right;
  width: 2em;
  text-align: right;
  border: 1px solid black;
}
label#region2Label {
  font-weight: bold;
  font-size: 1.2em;
}
div#liveregion2 {
  padding: 2px 5px;
  width: 22em;
  border: 1px solid black;
  height: 9em;
  overflow: auto;
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
example_obj.title       = 'Live Region 2'
example_obj.permanent_slug = 'live2'

example_obj.a11y_features = """
Simple example of a live region widget with two timers.
"""
example_obj.keyboard    = """
"""

example_obj.markup = [m1,m2,m3,m4,m5,m6,m7,m8]

example_obj.html        = """
<div class="controls">
   <h2>Live Region 1: Simple Counter</h2>
   <p><label for="id_time1">Change Interval (seconds)</label>:
      <select id="id_time1">
         <option id="id_time1_opt1" selected>1</option>
         <option id="id_time1_opt2">2</option>
         <option id="id_time1_opt3">3</option>
         <option id="id_time1_opt4">4</option>
         <option id="id_time1_opt5">5</option>
         <option id="id_time1_opt6">6</option>
         <option id="id_time1_opt7">7</option>
         <option id="id_time1_opt8">8</option>
         <option id="id_time1_opt9">9</option>
         <option id="id_time1_opt10">10</option>
      </select>
   </p>

   <p><label for="id_politeness1">Live Property Value</label>:
      <select id="id_politeness1">
         <option id="id_polite1_opt1">off</option>
         <option id="id_polite1_opt2">polite</option>
         <option id="id_polite1_opt3" selected>assertive</option>
         <option id="id_polite1_opt4">rude</option>
      </select>
   </p>

   <p><label for="id_atomic1">Atomic Property Value</label>:
         <select id="id_atomic1">
            <option id="id_atomic1_opt1" selected>true</option>
            <option id="id_atomic1_opt2">false</option>
          </select>
   </p>

   <p><label for="id_relevant1">Relevant Property Value</label>:
         <select id="id_relevant1" >
            <option id="id_relevant1_opt1">additions</option>
            <option id="id_relevant1_opt2">removals</option>
            <option id="id_relevant1_opt3">text</option>
            <option id="id_relevant1_opt4" selected>all</option>
          </select>
   </p>
</div>
<div class="example">
   <div id="id_region1Container">
      <label for="liveregion1">Changing value</label>:
      <div id="id_liveregion1">XXX
      </div>
   </div>
</div>
<div class="controls">
   <h2>Live Region 2: Text Log</h2>
   <p><label for="id_time2">Change Interval (in seconds)</label>:
      <select id="id_time2">
         <option id="id_time2_opt1">1</option>
         <option id="id_time2_opt2">2</option>
         <option id="id_time2_opt3">3</option>
         <option id="id_time2_opt4">4</option>
         <option id="id_time2_opt5" selected>5</option>
         <option id="id_time2_opt6">6</option>
         <option id="id_time2_opt7">7</option>
         <option id="id_time2_opt8">8</option>
         <option id="id_time2_opt9">9</option>
         <option id="id_time2_opt10">10</option>
      </select>
   </p>

   <p><label for="id_politeness2">Live Property Value</label>:
      <select id="id_politeness2">
         <option id="id_polite2_opt1">off</option>
         <option id="id_polite2_opt2"selected>polite</option>
         <option id="id_polite2_opt3">assertive</option>
         <option id="id_polite2_opt4">rude</option>
      </select>
   </p>

   <p><label id="id_atomic2Label" for="atomic2">Atomic Property Value</label>:
         <select id="id_atomic2" aria-labelledby="id_atomic2Label">
            <option id="id_atomic2_opt1" aria-selected="false">true</option>
            <option id="id_atomic2_opt2" aria-selected="true" selected>false</option>
          </select>
   </p>

   <p><label id="id_relevant2Label" for="relevant2">Relevant Property Value</label>:
         <select id="id_relevant2" aria-labelledby="id_relevant2Label" aria-activedescendant="id_relevant2_opt1">
            <option id="id_relevant2_opt1" role="option" aria-selected="true" selected>additions</option>
            <option id="id_relevant2_opt2" role="option" aria-selected="false">removals</option>
            <option id="id_relevant2_opt3" role="option" aria-selected="false">text</option>
            <option id="id_relevant2_opt4" role="option" aria-selected="false">all</option>
          </select>
   </p>
</div>

<div class="example">
   <label for="id_liveregion2">Log Text</label>

   <div id="id_liveregion2">
   </div>
</div> 
"""

example_obj.script = """
var OAA_EXAMPLES = OAA_EXAMPLES ||{};
/**
* @method liveRegion
*
* @memberOf OAA_EXAMPLES
*
* @desc a constructor to define an ARIA live region widget. The widget binds to a div
* on the page and accepts a callback function that is triggered at a specified interval.
*
* By default, the live region's alert level is polite, it's updates are non-atomic, additions are relevant,
* and it uses the general channel. These default values may be overridden by either specifying different
* values in the html markup or by calling the widget's corresponding update functions.
*
* @param {string} id - the html id of the div to bind to.
*
* @param (func callback) func is the callback function to execute at the specified interval
*
* @param (interval integer) interval is the initial update interval
*
* @return N/A
*/

/**
* @constructor liveRegion
*
* @memberOf OAA_EXAMPLES
*
* @desc Define the object properties
*
* @property {object} $id - the jquery object of the live region
*
* @property {object} func - the callback to execute after each interval
*
* @property {integer} interval - the interval to use for the timer
*
* @property {object} timer - the interval timer object
*/

OAA_EXAMPLES.liveRegion = function(id, func, interval) {

  // define widget properties

  this.$id = $('#' + id); 

  this.func = func; 
  this.interval = interval;
  this.timer = null;

  // set the initial live region aria attributes. Check if the user
  // has specified values in the html markup. If so, use those
  // values.

  var tmp = this.$id.attr('aria-live');

  if (tmp) {
    this.politeness = tmp;
  }
  else {
    this.politeness = 'polite';
  }

  tmp = this.$id.attr('aria-atomic');
  if (tmp) {
    this.atomic = tmp;
  }
  else {
    this.atomic = 'false';
  }

  tmp = this.$id.attr('aria-relevant');
  if (tmp) {
    this.relevant = tmp;
  }
  else {
    this.relevant = 'additions';
  }

  this.busy = false; // set to true while the region is updating

  // create the update timer
  this.createTimer();

} // end liveRegion constructor

/**
* @method createTimer
*
* @memberOf OAA_EXAMPLES
* 
* @desc a member function to create an interval timer for
* the live region widget.
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.createTimer = function() {

  if (this.timer != null) {
    // destroy the existing timer
    this.destroyTimer();
  }

  this.timer = setInterval(this.func, this.interval);

} // end createTimer()

/**
* @method destroyTimer
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to remove the interval timer for
* the live region widget.
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.destroyTimer = function() {

  if (this.timer != null) {
    clearInterval(this.timer);    
    this.timer = null;
  }

} // end createTimer()

/**
* @method setInterval
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to change the update interval
* of the live region. This function stores the new interval, clears the current
* interval timer and creates new one with the specified interval.
*
* @param {integer} interval - the new interval, in minutes, to set
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setInterval = function(interval) {
  this.interval = interval;

  this.createTimer();

} // end setInterval()

/**
* @method setPoliteness
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the aria-polite attribute of
* the live region.
*
* @param {string} val - one of three possible states: 'off', 'polite', 'assertive';
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setPoliteness = function(val) {

  this.$id.attr('aria-live', val);
} // end setPoliteness()

/**
* @method setAtomic
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the aria-atomic attribute of
* the live region.
*
* @param {boolean} val - true if live region updates should be atomic
*
* @return N/A
*/

OAA_EXAMPLES.liveRegion.prototype.setAtomic = function(val) {

  this.$id.attr('aria-atomic', val);

} // end setAtomic()

/**
* @method setRelevant
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the aria-relevant attribute of
* the live region.
*
* @param {string} val may be 'additions', 'removals', or 'text'. It may also be a
* space seperated combination of these.
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setRelevant = function(val) {

  this.$id.attr('aria-relevant', val);

} // end setRelevant() 


var g_msg1 = {
  msgArray: new Array("0","1","2","3","4","5","6","7","8","9"),  
  index: 0
};

var g_msg2 = {
  msgArray: new Array(
    "The birch canoe slid on the smooth planks.",
    "Glue the sheet to the dark blue background.",
    "It's easy to tell the depth of a well.",
    "These days a chicken leg is a rare dish.",
    "Rice is often served in round bowls.",
    "The juice of lemons makes fine punch.",
    "The box was thrown beside the parked truck.",
    "The hogs were fed chopped corn and garbage.",
    "Four hours of steady work faced us.",
    "Large size in stockings is hard to sell."
  ),  
  index: 0
};

var g_msg1index = 0;
var g_msg2index = 0;

/**
* @method ready
*
* @desc executed when page is opened. Initializes text arrays
* and other variables required to perform later functions.
*
* @return {N/A}
*/

$(document).ready(function() {
  var live1 = new OAA_EXAMPLES.liveRegion('liveregion1', function() {OAA_EXAMPLES.updateRegion('id_liveregion1', g_msg1, false);}, 1000);
  var live2 = new OAA_EXAMPLES.liveRegion('liveregion2', function() {OAA_EXAMPLES.updateRegion('id_liveregion2', g_msg2, true);}, 5000);

  //Bind event handlers for live1 controls

  // bind a change event handler for the interval select
  $('#id_time1').change(function(e) {

    
    // set the interval
    live1.setInterval($(this).val()*1000);

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the politeness select
  $('#id_politeness1').change(function(e) {

    // set the politeness
    live1.setPoliteness($(this).val());

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the atomic select
  $('#id_atomic1').change(function(e) {

    // set the politeness
    live1.setAtomic($(this).val());

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the update relevance select
  $('#id_relevant1').change(function(e) {

    // set the update revelance setting
    live1.setRelevant($(this).val());

    e.stopPropagation();
    return false;
  });

  //Bind event handlers for live2 controls
  
  $('#id_time2').change(function(e) {

    // set the interval
    live2.setInterval($(this).val()*1000);

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the politeness select
  $('#id_politeness2').change(function(e) {

    // set the politeness
    live2.setPoliteness($(this).val());

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the atomic select
  $('#id_atomic2').change(function(e) {

    // set the politeness
    live2.setAtomic($(this).val());

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the update relevance select
  $('#id_relevant2').change(function(e) {

    // set the update revelance setting
    live2.setRelevant($(this).val());

    e.stopPropagation();
    return false;
  });

}); // end ready()

/**
* @method updateRegion()
*
* @memberOf OAA_EXAMPLES
*
* @desc called by a liveRegion timer to updates the live region
* with new content based on the passed messageArray.
*
* @param {object} LiveRegion - the liveRegion widget object
*
* @param {array} msgArray - an array of messages to use for the update
*
* @param {boolean} append - true if messages should be appended, false if message should
* replace live region content
*
* @return {N/A}
*/

OAA_EXAMPLES.updateRegion = function(region, msgObj, append) {

  var $regionID = $('#' + region);
  var msg = '';
  
  if (msgObj.index == msgObj.msgArray.length) {
    // We've reached the end of the array, reset the index.
    msgObj.index = 0;

    // clear the region
    $regionID.empty();
  }

  if (append == false) {

    msg = msgObj.msgArray[msgObj.index];

    // messages should replace live region contents.
    // Empty the live region
    $regionID.empty();
  }
  else {
    msg = msgObj.msgArray[msgObj.index] + '<br/>';
  }

  // append the new message to the live region
  $regionID.append(msg);

  if (append == true) {
    $regionID.scrollTop($regionID.attr('scrollHeight'));
  }

  // increment the message index
  msgObj.index++;
 
} 

"""
example_obj.style       = """
div#application {
  height: 30em;
}
div.controls {
  margin-left: 10px;
  padding: 5px 10px;
  width: 21em;
  float: left;
  clear: both;
  border-bottom: 1px solid #008;
}
button,
select {
  float: right;
}
h2 {
  clear: both;
}
div.example {
  margin-top: 50px;
  margin-left: 30px;
  width: 22em;
  float: left;
}
div#id_region1Container {
  margin-left: 4em;
  padding: 10px;
  width: 11em;
  height: 1.6em;
  float: left;
}
div#id_region1Container label {
  padding-top: 10px;
  font-weight: bold;
}
div#id_liveregion1 {
  margin: 0;
  padding: 2px 5px;
  float: right;
  width: 2em;
  text-align: right;
  border: 1px solid black;
}
label#region2Label {
  font-weight: bold;
  font-size: 1.2em;
}
div#id_liveregion2 {
  padding: 2px 5px;
  width: 22em;
  border: 1px solid black;
  height: 9em;
  overflow: auto;
}
"""

example2 = create_example(example_obj)


# =============================
# Example 3
# =============================
order +=1

example_obj             = example_object()
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order          = order
example_obj.title       = 'Live Region 3'
example_obj.permanent_slug = 'live3'

example_obj.a11y_features = """
Simple example of a live region widget with two timers.
"""
example_obj.keyboard    = """
"""

spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

example_obj.markup = [m1,m2,m3,m4,m5,m6,m7,m8]

example_obj.html        = """
<script type="text/javascript" src="http://localhost/coding/examples/js/jquery-1.4.2.min.js"></script>
  <div class="controls">  
    <h2>Set Text Live Region ARIA Properties</h2>
    <div>
    <label for="id_text_interval">Seconds before a change</label>:
    <select id="id_text_interval">
      <option>1</option>
      <option>2</option>
      <option>3</option>
      <option>4</option>
      <option>5</option>
      <option>6</option>
      <option>7</option>
      <option>8</option>
      <option>9</option>
      <option selected>10</option>
      <option>11</option>
      <option>12</option>
      <option>13</option>
      <option>14</option>
      <option>15</option>
    </select>
    </div>

    <div>
    <label for="id_text_live">Politeness Level</label>:
    <select id="id_text_live">
       <option>off</option>
       <option>polite</option>
       <option selected>assertive</option>
       <option>rude</option>
    </select>
    </div>
    <div>
    <label for="id_text_atomic">Atomic</label>:
    <select id="id_text_atomic">
      <option id="id_text_atomic1">true</option>
      <option id="id_text_atomic2" selected>false</option>
    </select>
    </div>
    <div>
    <label for="id_text_relevant">Replace or Append Text?</label>:
    <select id="id_text_relevant">
      <option>Additions</option>
      <option>All</option>
    </select>
    </div>
  </div>
  
  <div class="controls">  
    <h2>Set Message Live Region ARIA Properties</h2>
    
    <div>
      <label for="id_msg_interval">Seconds before a change</label>:
      <select id="id_msg_interval">
       <option>1</option>
       <option>2</option>
       <option>3</option>
       <option>4</option>
       <option>5</option>
       <option>6</option>
       <option>7</option>
       <option>8</option>
       <option>9</option>
       <option selected>10</option>
       <option>11</option>
       <option>12</option>
       <option>13</option>
       <option>14</option>
       <option>15</option>
      </select>
    </div>

    <div>
      <label for="id_msg_live">Politeness Level</label>:
      <select id="id_msg_live">
        <option>off</option>
        <option>polite</option>
        <option selected>assertive</option>
        <option>rude</option>
      </select>
    </div>
    <div>
      <label for="id_msg_atomic">Atomic</label>:
      <select id="id_msg_atomic">
        <option>true</option>
        <option selected>false</option>
      </select>
    </div>
    
    <input type="hidden" id="id_msg_relevant" value="Replace">
  
   </div>

  <div class="example">
    <h2>Live region example: Reader</h2>

    <p>Description: Click the button below to start reading your messages.  Each sentence will appear for the time set above.  Every so often another message will replace the previous one.</p>

    <p><button id="id_start_button">Begin reading</button> </p>

    <h3>Message</h3>
    <div id="id_msg_content" aria-live="assertive" aria-atomic="true" aria-relevant="all" class="message"></div>

    <h3>Text</h3>
    <div id="id_text_content" aria-live="polite" aria-atomic="false" aria-relevant="additions" class="text"></div>
</div>
  </div> 
"""
example_obj.script = """
var OAA_EXAMPLES = OAA_EXAMPLES ||{};

/**
* @method liveRegion
*
* @memberOf OAA_EXAMPLES
*
* @desc a constructor to define an ARIA live region widget. The widget binds to a div
* on the page and accepts a callback function that is triggered at a specified interval.
*
* By default, the live region's alert level is polite, it's updates are non-atomic, additions are relevant,
* and it uses the general channel. These default values may be overridden by either specifying different
* values in the html markup or by calling the widget's corresponding update functions.
*
* @param {string} id - the html id of the div to bind to.
*
* @param {callback} func - the callback function to execute at the specified interval
* @param {string} content - String that goes in the text region
* @param {integer} interval - the initial update interval
*
* @return N/A
*/

/**
* @constructor liveRegion
*
* @memberOf OAA_EXAMPLES
*
* @desc Define the object properties
*
* @property {object} live_node - the jquery object of the live region
*
* @property {object} callback_func - the callback to execute after each interval
*
* @property {integer} interval - the interval to use for the timer
*
* @property {object} timer - the interval timer object
*/

OAA_EXAMPLES.liveRegion = function(id, content) {

function updateContent() {
  
  if (content_node.attr("aria-relevant").toLowerCase() == "additions") {
      if (index < content.length) {
        content_node.append(content[index] + "<br>");
        index++;
      }
      else {
        index = 0;
        content_node.empty();
      }
  }
  else {
      var i = index % content.length;
      content_node.empty();
      content_node.append(content[i]);
      index++;
  }

} 

  this.id = id; 

  this.content_node = $('#'+ this.id + '_content');

  this.callback_func = updateContent;
  this.timer = null;
 
  var index = 0; 
  var content_node = this.content_node;

} // end liveRegion constructor

/**
* @method createTimer
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to create an interval timer for
* the live region widget.
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.createTimer = function() {

  if (this.timer != null) {
    // destroy the existing timer
    this.destroyTimer();
  }

  this.timer = setInterval(this.callback_func, $('#' + this.id + '_interval').val() * 1000);

}

/**
* @method updateTimer
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to remove the interval timer for
* the live region widget.
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.updateTimer = function() {

  if (this.timer != null) {
    clearInterval(this.timer);    
    this.timer = null;
  }
  this.createTimer();
} 

/**
* @method setPoliteness
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the aria-polite attribute of the live region.
*
* @param {string} val - one of three possible states: 'off', 'polite', 'assertive';
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setLive = function() {

  this.content_node.attr('aria-live', $('#'+ this.id + '_live').val().toLowerCase());
} // end setPoliteness()

/**
* @method setAtomic
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the aria-atomic attribute of
* the live region.
*
* @param {boolean} val - true if live region updates should be atomic
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setAtomic = function(val) {

   this.content_node.attr('aria-atomic', $('#'+ this.id + '_atomic').val().toLowerCase());

}

/**
* @method setRelevant
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the aria-relevant attribute of the live region.
*
* @param {string} val - may be 'additions', 'removals', or 'text'. It may also be a
* space seperated combination of these.
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setRelevant = function(val) {

   this.content_node.attr('aria-relevant', $('#'+ this.id + '_relevant').val().toLowerCase());

}

/**
* @method ready
*
* @desc executed when page is opened. Initializes text arrays
* and other variables required to perform later functions.
*
* @property {array} $g_text - the jQuery objects of the text loaded from the file
* @property {object} $g_curLine - the jQuery object of the current line in g_text
* @property {string} g_append - set to either 'Append' or 'Replace'
* @property {object} g_msgLive - the message live region
* @property {object} g_textLive - the text live region
* @property {array} g_messages - array of strings to be put in the message liveRegion
* @property {integer} interval - the value (in milliseconds) of time between liveRegion changes
* 
* @return {N/A}
*/

$(document).ready(function() {

var $g_text = new Array();
$g_text[0] = "Moby Dick";
$g_text[1] = "Call me Ishmael.  Some years ago--never mind how long";
$g_text[2] = "precisely--having little or no money in my purse, and nothing";
$g_text[3] = "particular to interest me on shore, I thought I would sail about a";
$g_text[4] = "little and see the watery part of the world.  It is a way I have of";
$g_text[5] = "driving off the spleen and regulating the circulation.  Whenever I";
$g_text[6] = "find myself growing grim about the mouth; whenever it is a damp,";
$g_text[7] = "drizzly November in my soul; whenever I find myself involuntarily";
$g_text[8] = "pausing before coffin warehouses, and bringing up the rear of every";
$g_text[9] = "funeral I meet; and especially whenever my hypos get such an upper";
$g_text[10] = "hand of me, that it requires a strong moral principle to prevent me";
$g_text[11] = "from deliberately stepping into the street, and methodically knocking";

var g_text_live = new OAA_EXAMPLES.liveRegion('id_text', $g_text);

$("#id_text_interval").change(function(e){
g_text_live.updateTimer();
});

$("#id_text_live").change(function(e){
g_text_live.setLive();
});

$("#id_text_atomic").change(function(e){
g_text_live.setAtomic();
});

$("#id_text_relevant").change(function(e){
g_text_live.setRelevant();
});

var $g_messages = new Array();
$g_messages[0] = "...";
$g_messages[1] = "you have new mail."
$g_messages[2] = "there are new news feeds."

var g_msg_live = new OAA_EXAMPLES.liveRegion('id_msg', $g_messages);

$("#id_msg_interval").change(function(e){
g_msg_live.updateTimer();
});

$("#id_msg_live").change(function(e){
g_msg_live.setLive();
});

$("#id_msg_atomic").change(function(e){
g_msg_live.setAtomic();
});

$("#id_start_button").click(function(e){
g_msg_live.updateTimer();
g_text_live.updateTimer();
});

}); // end ready()

"""
example_obj.style       = """
div.controls {
  margin-left: 30px;
  padding: 5px 10px;
  width: 28em;
}
label {
  margin-left: 20px;
}
select {
  float: right;
  display: inline;
  margin-right: 13em;
}

div.example {
  margin: 20px;
  padding: 10px;
  width: 50em;
  border: 1px solid black;
}
div.message {
  padding: 2px 5px;
  height: 1.2em;
  border: thin solid black;
  background-color: #CCCCCC;
}
div.text {
  padding: 2px 5px;
  height: 8em;
  border: thin solid black;
  overflow: auto;
}

div#id_loadedText {
  display: none;
}
span.title {
  font-weight: bold;
  font-size: 1.3em;
  margin-left: 6em;
  margin-bottom: .5em;
  display: block;
}
span.new {
  color: #922;
} 
"""

example3 = create_example(example_obj)