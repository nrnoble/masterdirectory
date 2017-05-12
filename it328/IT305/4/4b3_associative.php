<!--
Neal Noble
January 26th, 2016
IT305
Assignment 4b associative arrays 
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
  
  
  <title>IT305 Assignment 4b associative arrays </title>
</head>
<body>

<div class="container">
  <div class="row">
    <section class="col-xs-12" >
		<div id = page style="margin-top: 10px">
		  Neal Noble<br>
		  January 26th, 2016<br>
		  IT305<br>
		  Assignment 4b associative arrays<br><br>
		</div>
		
		<div  id = "page" style="margin-top: 10px">
		  <h2>Try It</h2>
		  
		  
		  <?php
			$courses = array("Networking 201" => "4.0",
							  "Network Security 200" => "3.8",
							  "SQL 101" => "4.0",
							  "Programming 101" => "4.0",
							  "Film 101" => "4.0");
			
			echo "<ul>";
			  foreach ($courses as $course => $grade)	
			  {	    
				echo "<li>$course, Grade: $grade</li>";
			  }
			echo "</ul>";
	    
 
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