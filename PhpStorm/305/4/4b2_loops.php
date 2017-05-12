<!--
Neal Noble
January 26th, 2016
IT305
Assignment 4b loops
-->


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="css/bootstrap.min.css">
  <link rel="stylesheet" href="css/styles.css">
  <!-- background-image: url("DSC_0042.jpg"); -->
  <style type="text/css">

                body
                {
                    text-align:justify;
                    font-family: courier;
					font-size: 8pt;
                    background-color:#4A62E8;
                }
                
                #text
                {
                    text-align: left;
                    font-size: 8pt;
                   
                }
                div
                {
				   font-size: 8pt;
                    margin: auto;
                }


                #page
                {
                    max-width: 700px;
                    font-size: 12pt;
                    background-color: #ffffff;
                    border: solid;
                    border-width: 1px;
                    text-align: left;
                    margin-top: 100px;
					padding: 10px;
					box-shadow: 5px 5px 5px #0026FF
                }
            </style>      
  
  
  <title>IT305 Assignment 4b loops</title>
</head>
<body>

<div class="container">
  <div class="row">
    <section class="col-xs-12" >
		<div id = page style="margin-top: 10px">
		  Neal Noble<br>
		  January 26th, 2016<br>
		  IT305<br>
		  Assignment 4b loops<br><br>
		</div>
		
		<div  id = "page" style="margin-top: 10px">
		  <h2>Try It</h2>
		  
		  
		  <?php
			$characters[0] = "Capt Kirk";	
			$characters[1] = "Mr. Spock";
			$characters[2] = "Dr. McCoy";	
			$characters[3] = "Mr. Scott";
			$characters[4] = "Lt. Uhura";
			echo '<ul>
			<li>$characters[0] = "Capt Kirk";</li>	
			<li>$characters[1] = "Mr. Spock";</li>
			<li>$characters[2] = "Dr. McCoy";</li>
			<li>$characters[3] = "Mr. Scott";</li>
			<li>$characters[4] = "Lt. Uhura;"</li></ul>';
	
	
			
			echo "<ul>";
			  echo "<li><pre><b>print_r:</b> "; print_r($characters);
			  echo "</pre></li><br>";
			  echo "<li>First item is <b>Array[0]:</b> $characters[0]</li>";
			  echo "<br>";
			  echo "<li>Last item is <b>Array[4]:</b> $characters[4]</li>";
			  echo "<br>";
			  echo '<li><b>for</b> ($x = 0; $x < 5; $x++)';
			  echo "<ol>";

			  for ($x = 0; $x < 5; $x++)
			  {
				echo "<li><b>Array[$x]:</b> $characters[$x]</li>";
			  }
			  echo "</ol></li>";
			  
			  echo"<br>";
			  
			  echo '<li><b>foreach</b> ($characters as $character)';
			  echo "<ul>";
			  foreach ($characters as $character)
			  {
				echo "<li>$character</li>";
			  }
			  echo "</ul></li>";
			echo "</ul>"
		  ?>
		  <br><br>
		</div>
		
		<div id = "page" style="margin-top: 10px;">
			<H2>Source Code</H2>
		  	
			<?php>
			  highlight_file(__FILE__);
			?>
	
	
		  
		</div>
	
    </section>
  </div>  
</div>


<script src="js/jquery-2.1.4.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<script src="js/script.js"></script>
</body>
</html>