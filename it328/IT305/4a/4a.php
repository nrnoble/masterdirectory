<!--
Neal Noble
January 25th, 2016
IT305
Assignment 4a
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
  
  
  <title>IT305 Assignment 4a</title>
</head>
<body>

<div class="container">
  <div class="row">
    <section class="col-xs-12" >
		<div id = page style="margin-top: 10px">
		  Neal Noble<br>
		  January 25th, 2016<br>
		  IT305<br>
		  Assignment 4a<br>
		</div>
		
		<div  id = "page" style="margin-top: 10px">
		  <h2>Try It</h2>
		  <?php
			echo "<ol type=\"a\">";
  
			$msg = " I love PHP ";
			$trimmed_msg = trim($msg);
			echo "<li> <b>trim()</b>: The string <b>\"$msg\"</b>
				  becomes <b>\"$trimmed_msg\"</b></li>";
			echo "<br>";
			
			$length = strlen($trimmed_msg);
			echo "<li> <b>strlen()</b>: The string <b>\"$trimmed_msg\"</b>
			      has $length characters</li>";
			echo "<br>";
			
			$position = strpos($trimmed_msg,"PHP");
			echo "<li> <b>strpos()</b>: The character position of <b>\"PHP\"
			      </b> is $position using zero based index</li>";
			echo "<br>";
			
			$replaced = str_replace("love", "like", $trimmed_msg);
			echo "<li> <b>str_replace()</b>: The string <b>\"$trimmed_msg\"</b>
			      becomes <b>\"$replaced\"</b> when replacing <b>\"love\"</b>
				  with <b>\"like\"</b></li>";
			echo "<br>";
			
			$function_reverse= reverse ($trimmed_msg);
			
			echo "<li>$function_reverse</li>";
			echo "</ol>";
		  
			function reverse ($str)
			{
			  $revStr = strrev($str);
			  return  "<b>function reverse()</b>: <b>\"$str\"</b>
			           spelled backwards is <b>\"$revStr\"</b>";
			}
		  ?>

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