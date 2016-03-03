"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples import *

order = 1

spec_html4 = LanguageSpec.objects.get(url_slug='html4')
spec_html5 = LanguageSpec.objects.get(url_slug='html5')
spec_aria = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec=spec_html4, element='a', attribute='href')
m2 = ElementDefinition.objects.get(spec=spec_aria, attribute='aria-describedby')

# =============================
# Example 1
# =============================

example_obj             = example_object()
example_obj.example_id = 44
example_obj.rule_category = RuleCategory.objects.get(category_id='ID_CATEGORY_WIDGETS')
example_obj.order = order
example_obj.title       = 'Using aria-describedby to satisfy WCAG 2.4.4 Link Purpose in Context'
example_obj.permanent_slug = 'link1'

example_obj.a11y_features = """
The current WCAG 2.0 Techniques for links in context requirement 2.4.4 do not provide a progammatic means to determine the authors intended context.
The following examples use the <code>aria-describedby</code> attribute to provide a means for authors to define the context to users and to support assistive technologies to identify the correct context.
This technique it supported by the JAWS screen reader for both Internet Explorer 9.0 and Firefox 4.0.
"""

example_obj.keyboard    = """
"""

example_obj.markup = [m1,m2]

example_obj.html        = """
<div role="document">


<h3>Link context with a <code>LI</code> element</h3> 
<p>The following example is modified from WCAG <a href="http://www.w3.org/TR/2010/NOTE-WCAG20-TECHS-20101014/H77">H77: Identifying the purpose of a link using link text combined with its enclosing list item technique</a></p>

<ul>
  <li id="li1">
    Check out the video report for last year's 
    <a href="festival.htm" aria-describedby="li1">National Folk Festival</a>.
  </li>
  <li id="li2">
    <a href="listen.htm" aria-describedby="li2">Listen to the instruments</a>
  </li>
  <li id="li3">
    Guitar Man: George Golden talks about 
    <a href="mkguitars.htm" aria-describedby="li3">making guitars</a>.
  </li>
</ul>

<h3>Link context from a preceeding sibling <code>LI</code> element</h3> 

<p>The following example is modified from WCAG <a href="http://www.w3.org/TR/2010/NOTE-WCAG20-TECHS-20101014/H77">H77: Identifying the purpose of a link using link text combined with its enclosing list item technique</a></p>

<ul>
  <li>
    <a href="tomb_raider.htm" id="a1">Tomb Raider: Legend</a>
    <a href="tomb_raider_images.htm" aria-describedby="a1">See Images</a>
    <a href="tomb_raider.mpeg" aria-describedby="a1">(Download Demo)</a>
  </li>
  <li>
    <a href="fear_extraction.htm" id="a2">F.E.A.R. Extraction Point</a>
    <a href="fear_extraction_images.htm" aria-describedby="a2">See Images</a>
    <a href="fear_extraction.mpeg" aria-describedby="a2">(Download Demo)</a>
  </li>
  <li>
    <a href="call_of_duty.htm" id="a3">Call of Duty 2</a>
    <a href="call_of_duty_images.htm" aria-describedby="a3">See Images</a>
    <a href="call_of_duty.mpeg" aria-describedby="a3">(Download Demo)</a>
  </li>
  <li>
    <a href="Warhammer_40K.htm" id="a4">Warhammer 40K</a>
    <a href="warhammer_40k_images.htm"  aria-describedby="a4">See Images</a>
    <a href="Warhammer_40k.mpeg"  aria-describedby="a4">(Download Demo)</a>
  </li>
</ul>  

<h3>Link context from <code>P</code> element</h3>

<p>The following example is modified from WCAG <a href="http://www.w3.org/TR/2010/NOTE-WCAG20-TECHS-20101014/H78">H78: Identifying the purpose of a link using link text combined with its enclosing paragraph</a></p>

<h4>The final 15</h4>
<p id="p1">Coming soon to a town near you...the final 15 in the 
National Folk Festival lineup.
<a href="final15.html" aria-describedby="p1">[Read more...]</a>
</p>

<h4>Folk artists get awards</h4>
<p id="p2">Performers from the upcoming National Folk Festival receive 
 National Heritage Fellowships. 
 <a href="nheritage.html" aria-describedby="p2">[Read more...]</a>
</p>

<h3>Link context from <code>th</code> elements of a table</h3>

<p>The following example is modified from WCAG <a href="http://www.w3.org/TR/2010/NOTE-WCAG20-TECHS-20101014/H79">
H79: Identifying the purpose of a link using link text combined with its enclosing table cell and associated table headings</a></p>

<table class="links" border="1" style="border-collapse:collapse;">
<caption>Comparison of Rental Car Rates</caption>
<tr>
  <th></th>
  <th id="c1">Alamo</th>
  <th id="c2">Budget</th>
  <th id="c3">National</th>
  <th id="c4">Avis</th>
  <th id="c5">Hertz</th>
</tr>
<tr>
  <th id="r1">Economy cars</th>
  <td><a href="econ_ala.htm" aria-describedby="c1 r1">$67/day</a></td>
  <td><a href="econ_bud.htm" aria-describedby="c2 r1">$68/day</a></td>
  <td><a href="econ_nat.htm" aria-describedby="c3 r1">$72/day</a></td>
  <td><a href="econ_av.htm" aria-describedby="c4 r1">$74/day</a></td>
  <td><a href="econ_hz.htm" aria-describedby="c5 r1">$74/day</a></td>
</tr>
<tr>
  <th id="r2">Compact cars</th>
  <td><a href="comp_ala.htm" aria-describedby="c1 r2">$68/day</a></td>
  <td><a href="comp_bud.htm" aria-describedby="c2 r2">$69/day</a></td>
  <td><a href="comp_nat.htm" aria-describedby="c3 r2">$74/day</a></td>
  <td><a href="comp_av.htm" aria-describedby="c4 r2">$76/day</a></td>
  <td><a href="comp_hz.htm" aria-describedby="c5 r2">$76/day</a></td>
</tr>
<tr>
  <th id="r3">Mid-sized cars</th>
  <td><a href="mid_ala.htm" aria-describedby="c1 r3">$79/day</a></td>
  <td><a href="mid_bud.htm" aria-describedby="c2 r3">$80/day</a></td>
  <td><a href="mid_nat.htm" aria-describedby="c3 r3">$83/day</a></td>
  <td><a href="mid_av.htm" aria-describedby="c4 r3">$85/day</a></td>
  <td><a href="mid_hz.htm" aria-describedby="c5 r3">$85/day</a></td>
</tr>
<tr>
  <th id="r4">Full-sized cars</th>
  <td><a href="full_ala.htm" aria-describedby="c1 r4">$82/day</a></td>
  <td><a href="full_bud.htm" aria-describedby="c2 r4">$83/day</a></td>
  <td><a href="full_nat.htm" aria-describedby="c3 r4">$89/day</a></td>
  <td><a href="full_av.htm" aria-describedby="c4 r4">$91/day</a></td>
  <td><a href="full_hz.htm" aria-describedby="c5 r4">$91/day</a></td>
</tr>
</table> 

<h3>Link context from preceeding <code>h1-h6</code> heading elements</h3>

<p>The following example is modified from WCAG <a href="http://www.w3.org/TR/2010/NOTE-WCAG20-TECHS-20101014/H80">H80: Identifying the purpose of a link using link text combined with the preceding heading element</a></p>

<h2 id="head1"><a href="royal_palm_hotel.html">Royal Palm Hotel</a></h2>
  <ul class="horizontal">
    <li><a href="royal_palm_hotel_map.html" aria-describedby="head1">Map</a></li>
    <li><a href="royal_palm_hotel_photos.html" aria-describedby="head1">Photos</a></li>
    <li><a href="hroyal_palm_hotel_directions.html" aria-describedby="head1">Directions</a></li>
    <li><a href="royal_palm_hotel_reviews.html" aria-describedby="head1">Guest reviews</a></li>
    <li><a href="royal_palm_hotel_book.html" aria-describedby="head1">Book now</a></li>
  </ul>

<h2 id="head2"><a href="hotel_three_rivers.html">Hotel Three Rivers</a></h2>
  <ul class="horizontal">
    <li><a href="hotel_three_rivers_map.html" aria-describedby="head2">Map</a></li>
    <li><a href="hotel_three_rivers_photos.html" aria-describedby="head2">Photos</a></li>
    <li><a href="hotel_three_rivers_directions.html"  aria-describedby="head2">Directions</a></li>
    <li><a href="hotel_three_rivers_reviews.html"  aria-describedby="head2">Guest reviews</a></li>
    <li><a href="hotel_three_rivers_book.html"  aria-describedby="head2">Book now</a></li>
  </ul>     
  
  
<h3>Link context from nested list content</h3>

<p>The following example is modified from WCAG <a href="http://www.w3.org/TR/2010/NOTE-WCAG20-TECHS-20101014/H81">H81: Identifying the purpose of a link in a nested list using link text combined with the parent list item under which the list is nested</a></p>

<ul>
<li id="li4">Annual Report 2005-2006
  <ul> 
  <li><a href="annrep0506.html" aria-describedby="li4">(HTML)</a></li>
  <li><a href="annrep0506.pdf"  aria-describedby="li4">(PDF)</a></li>
  <li><a href="annrep0506.rtf"   aria-describedby="li4">(RTF)</a></li>
  </ul>
</li>
<li id="li5">Annual Report 2006-2007
  <ul> 
  <li><a href="annrep0607.html" aria-describedby="li5">(HTML)</a></li>
  <li><a href="annrep0607.pdf" aria-describedby="li5">(PDF)</a></li>
  <li><a href="annrep0607.rtf" aria-describedby="li5">(RTF)</a></li>
  </ul>
</li>
</ul> 

<ul>
<li id="li6"><a href="royal_palm_hotel.html">Royal Palm Hotel</a>
  <ul class="horizontal">
    <li><a href="royal_palm_hotel_map.html" aria-describedby="li6">Map</a></li>
    <li><a href="royal_palm_hotel_photos.html" aria-describedby="li6">Photos</a></li>
    <li><a href="hroyal_palm_hotel_directions.html" aria-describedby="li6">Directions</a></li>
    <li><a href="royal_palm_hotel_reviews.html" aria-describedby="li6">Guest reviews</a></li>
    <li><a href="royal_palm_hotel_book.html" aria-describedby="li6">Book now</a></li>
  </ul>
</li>
<li id="li7"><a href="hotel_three_rivers.html">Hotel Three Rivers</a>
  <ul class="horizontal">
    <li><a href="hotel_three_rivers_map.html" aria-describedby="li7">Map</a></li>
    <li><a href="hotel_three_rivers_photos.html" aria-describedby="li7">Photos</a></li>
    <li><a href="hotel_three_rivers_directions.html" aria-describedby="li7">Directions</a></li>
    <li><a href="hotel_three_rivers_reviews.html" aria-describedby="li7">Guest reviews</a></li>
    <li><a href="hotel_three_rivers_book.html" aria-describedby="li7">Book now</a></li>
  </ul>
</li>
</ul> 

</div>
"""

example_obj.script      = """
"""

example_obj.style       = """
"""

example1 = create_example(example_obj)