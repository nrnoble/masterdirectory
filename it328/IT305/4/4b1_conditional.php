<!--
Neal Noble
January 26th, 2016
IT305
Assignment 4b
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
  
  
  <title>IT305 Assignment 4b</title>
</head>
<body>

<div class="container">
  <div class="row">
    <section class="col-xs-12" >
		<div id = page style="margin-top: 10px">
		  Neal Noble<br>
		  January 26th, 2016<br>
		  IT305<br>
		  Assignment 4b<br><br>
		</div>
		
		<div  id = "page" style="margin-top: 10px">
		  <h2>Try It</h2>
		  <b>Instructions</b>: Refresh browser to generate another scoring grade.
		  <br><br>
		  <?php
			$score = rand(50, 100);
		
			
			switch (true)
			{
			  
			  case ($score == 100):
			  {
				echo  "Score: $score is an A.
				       You aced the quiz with a PERFECT SCORE!!";
				break; 
			  }
			  
			  case ($score  >= 96):
			  {
				echo  "Score: $score is an A. You almost aced the quiz!!";
				break; 
			  }
			    
			  case ($score >= 90):
			  {
				echo  "Score: $score is an A. VERY IMPRESSIVE!";
				break;
			  }
			  
			  case ($score >= 80):
			  {
				echo  "Score: $score is a B. Very good score";
				break;
			  }
			  
			  case ($score >= 70):
			  {
				echo  "Score: $score is a C. Consider taking
				       quiz again to get a better score";
				break;
			  }
			  
			  case ($score >= 60):
			  {
				echo  "Score: $score is a D. This is passing,
				       but recommend taking quiz again";
				break;
			  }
			  
			  case ($score < 60):
			  {
				echo  "Score: $score is not passing, review
				       and take quiz again";
				break;
			  }
			  
			  # default never should be executed, but is added to catch
			  # any known results that may occure.
			  default:
			  {
				 echo  "score: $score can not be graded at this time";
			  }
			  	
			}

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