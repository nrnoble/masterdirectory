<!--
Neal Noble
feburary 1st, 2016
IT305
test
Assignment 5a process.php
-->
<!DOCTYPE html>
<html lang="en">
    <head>
        <link rel = "stylesheet" type="text/css"
            href="http://nnoble.greenrivertech.net/css/nrnoble.css">
    </head>
    <body>

    <div id = page>
            <pre>
            <form method="get" action="process.php">
			  <label>
Please enter your first name:  <input type="text" name="first" size="20" >
			  </label>   <label>
               Year of birth:  <input type="text" name="year" size="4" maxlength="4" >
			  </label><label>
          Credit card number:  <input type="text" name="ccnum" size="20" maxlength="20" >
			  </label>
   			       <input type="submit" value="Validate">
				   
            </form>	
            </pre>
        </div>
        <div id=page>
        <h1>Validation Results</h1>
            
        <?php
    
           
               
               include "myfunctions.php"; 
                 
                echo "<pre>";
                print_r($_GET);
                echo "</pre>";
                                     
                
                if (validName($_GET['first']))
                {
                    $firstName = $_GET['first'];
                    echo "<p>Hello, $firstName!</p>";
                }
                else
                {
                    echo "<p>First name is required.</p>";
                }
        
                
                $tmp = $_GET['year'];
                if (validYear($tmp) == 1)
                {
                    $year = $_POST['year'];
                    echo "<p>Year entered: $tmp</p>";
                }
                else
                {
                    echo "<p>Invalid year.</p>";
                }
                
 
    ?>
    
     </div>
       <div id = "page" style="margin-top: 10px;">
			<H2>Source Code for form.php</H2>
		  	
			<?php>
			  highlight_file("form.php");
			?>

		</div>
     
     
       <div id = "page" style="margin-top: 10px;">
			<H2>Source Code for process.php</H2>
		  	
			<?php>
			  highlight_file("process.php");
			?>

		</div>
		
		
		<div id = "page" style="margin-top: 10px;">
			<H2>Source Code for myfunctions.php</H2>
		  	
			<?php>
			  highlight_file("myfunctions.php");
			?>

		</div>
    
      
    </body>     
</html>