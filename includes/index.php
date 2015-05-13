<!DOCTYPE html>

<html>
	
<head>
	
	<meta charset="utf-8">
		
<title>Command and Conquer - Tiberian Dawn - HTML5</title>
	
	<?php
	  require_once $_SERVER["DOCUMENT_ROOT"]."/includes/ViewManager.php";
  require_once $_SERVER["DOCUMENT_ROOT"]."/includes/DataManager.php";
  require_once $_SERVER["DOCUMENT_ROOT"]."/includes/ConfigManager.php";
  use ArcherSys\Viewer\ViewManager;
  use ArcherSys\Data\DataManager;
  use ArcherSys\Config\ConfigManager;
   use ArcherSys\Viewer\LogicManager;
   use ArcherSys\Viewer\FontManager;
	   ConfigManager::addFavicon();
	?>

		
						
		<link rel="stylesheet" type="text/css" href="css/stylesheet.css"/>
		
		
		
				
<script src="jquery-ui/external/jquery/jquery.js"	 type="text/javascript" charset="utf-8"></script>

<?php
  LogicManager::addPolymerWebComponentsScript();
  ?>

<script src="js/cnc.js"	 type="text/javascript" charset="utf-8">
		</script>
	
</head>
	

		 

<?php
ViewManager::DefineView();
LogicManager::addAnalytics();
ViewManager::addPolymer();
ViewManager::addHeaderPanels();
ViewManager::addToolbars();
ViewManager::addCoreButtons();
ViewManager::addPaperTabs();

?>
<!-- End Piwik Code -->
	
				
<core-header-panel id="game-ui">
  <core-toolbar>
      <div>Comanquer</div>
    </core-toolbar>
      <section id="game-ui"><paper-tabs selected="{{selected}}"><paper-tab><a href="#info">FYI Comanquer</a></paper-tab><paper-tab><a href="#game">Play</a></paper-tab></paper-tabs>
<core-pages selected="{{selected}}">
  <div id="info">
<img style="float:left;"src="images/logo.jpg" width="400" height="146" alt="Command and Conquer">

				<h1 >C&amp;C - HTML5 v0.3d created by
<span style="font-size:small;color:white;">
<a href="http://www.adityaravishankar.com">Aditya Ravi Shankar</a> Refurbished by Weldon Henson
</span>
				
</h1>
				
<!--img src="images/cursors/blank.gif"-->
	
<p>This is a recreation of the original Command and Conquer, Real Time Strategy game entirely in HTML5 and Javascript. </p>
				<p>This page works best on <a href="http://www.google.com/chrome" title="Google Chrome - Get a fast new browser. For PC, Mac, and Linux">Google Chrome</a> or <a href="http://www.mozilla.org/en-US/firefox/new/" title="Mozilla Firefox Web Browser — Free Download">Mozilla Firefox</a>. The images can take a little while to load so please be patient.</p>
				
				
<p style="color:green">This is still a work in progress. Any comments or feedback (including bugs), is appreciated. I intend to develop this game further - improving the AI,  pathfinding (<a href="http://www.adityaravishankar.com/projects/games/pathfinding-javascript-rts-demo/" title="Command and Conquer - RTS Game Pathfinding - HTML5">See improved pathfinding demo here</a>), adding more units and levels. If you are interested in helping out with this effort (even by just testing the game and giving feedback), please let me know.
</p>
		
<p><u>BUGS and ISSUES:</u>
Please report bugs on the github issues page or in the comments section below.
<a href="https://github.com/adityaravishankar/command-and-conquer/issues">https://github.com/adityaravishankar/command-and-conquer/issues</a>
</p>
				
				
<p style='color:blue'>If you liked this demo, please let me know by clicking on the Like button below and leaving me a comment. Please share this page with your friends so that they can see it too. </p>
				
<p>You can read more about <a href="http://www.adityaravishankar.com/2011/11/command-and-conquer-programming-an-rts-game-in-html5-and-javascript/" title="Command and Conquer - Programming an RTS game in HTML5 and Javascript |">the development of this game</a> on my blog. You can also check out some of the <a href="http://www.adityaravishankar.com/software-projects/games/" title="Games  have written">other games I have written</a>
or read some of my
<a href="http://www.adityaravishankar.com/category/programming/game-programming/" title="Game Programming Articles">game programming articles</a>.
</p>
		</div>
  <div id = "featuresdiv">
				
<p style="clear:all;float:right;margin-left:10px;margin-top:10px;">
<div id="debugger">
						Debugging off.
					
</div>
						
	<p style="font-size:smaller;">Updates:
					
<ul style="font-size:smaller;">
						<li>v0.3d Released
							<ul>
							<li>Harvester saved when refinery is sold</li>
							<li>Ctrl + 0-9 can be used to set unit control groups</li>
							<li>No building on fog of war or half outside screen</li>
							
<li>Canceling returns money</li>
							
<li>Can start building with insufficient funds. Waits when out of money</li>
							
							</ul>
						</li>
						<br>
						<li>v0.3c Released - Performance patch
							<ul>
							<li>Harvesters collect 700 per trip</li>
							<li>Using sprite sheets for faster loading and processing.</li>
							</ul>
						</li>
						<br>
						<li>Special thanks to <a href="http://www.nahklick.de/">http://www.nahklick.de/</a> for hosting during periods of high traffic. <br><br>Please continue to bookmark &amp; share <a href="http://www.adityaravishankar.com/projects/games/command-and-conquer/">http://www.adityaravishankar.com/projects/games/command-and-conquer/</a> instead of the temporary redirect page.
						</li><br>
						<li>v0.3b Released - Bugfixes - Thank you for all your feedback!!
							<ul>
							<li>Tanks can turn in place</li>
							<li>Tooltip shows unit/building cost</li>
							<li>Harvester life does not regenerate inside refinery</li>
							
<li>Can pan to the right edge of the map even with sidebar visible</li>
							</ul>
						</li>
						<br>
						<li>v0.3 Released
							<ul>
							<li>Can repair or sell buildings</li>
							<li>Refinery and Harvesters to process tiberium (cash)</li>
							<li>Lots of bug fixes and Speed/Performance optimization</li>
							</ul>
						</li>
						<br>
						<li>v0.2 Released
							<ul>
							<li>Improved pathfinding</li>
							</ul>
						</li>
						<br>
						<li>v0.1 Released</li>
					</ul>
				</p>
				<p style="font-size:smaller;margin-top:10px;">Controls:
					<ul style="font-size:smaller;">
						<li>Unit Selection
							<ul>
							<li>Single Unit - Click on a unit to select it</li>
							<li>Drag Selection - Drag mouse to select multiple units</li>
							<li>Multiple Selection - Shift + Click to add unit  multiple units</li>
							</ul>
						</li>
						<li>Movement/Attacking
							<ul>
							<li>Move - Select unit(s) and click on destination to move</li>
							
<li>Attack - Select unit(s) and click on target building or unit to attack</li>
							<li>Map panning - Move cursor near edge of map to pan and scroll around</li>
							</ul>
						</li>
						<li>Building
							<ul>
							<li>Build Construction Yard - Move MCV to where you want, and click on it to deploy</li>
							<li>Expand Sidebar and click on construction options to build them. Once you finish contruction, more options become available</li>
							</ul>
						</li>
						
					</ul>

				
							<p style="font-size:smaller;">DISCLAIMER: This project is only intended as a technical proof of concept to demonstrate the basic working elements of an RTS game in HTML5. No commercial use is intended. All images and sounds used are from C&amp;C - Tiberian Dawn and are property of the original game creators. </p>

			</div>
	

		
			<div style="float:left;margin-left:20px;padding:20px;">
				<div style="">
								
				
	
				</div>
				
<div style="padding:20px;">
		
</div>

</div>
  <div id="game">
								<input type="hidden" name="cmd" value="_s-xclick">

				<input type="hidden" name="encrypted" value="-----BEGIN PKCS7-----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-----END PKCS7-----
">
									
	<label for="debug_mode">Debug Mode: </label>
<input type="checkbox" name="debug_mode" id="debug_mode">

<canvas id="canvas" width="640" height="535">
				Your browser does not support the HTML5 Canvas feature. This game uses new HTML5 features and will only work on the latest versions of Firefox, Safari or Chrome (and maybe Internet Explorer 9).
			</canvas>

		My goal is to take this game as far as possible - Add more units, optimize the code, add better AI and multiplayer games. You would be able to come to this page, find a random partner and start playing!!<br> <br>
Several developers have volunteered to help with this effort. I am grateful to everyone who came forward to help.
<br><br>	If you enjoyed playing this game and would like to support the continued development of the game with donations/contributions, please use the donate button below. Every little bit would help.
		</div>
</core-pages>

	
			
	

</section>
</core-header-panel>


</body>
</html>