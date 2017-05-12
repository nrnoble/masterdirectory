<?php
$errors = [];
$missing = [];
//if (isset($_POST['send']))
//{
//    $expected = ['name', 'email', 'comments'];
//    $required = ['name', 'comments'];
//    $to = 'Neal Noble<nrnoble@hotmail.com>';
//    $subject = 'Feedback from online form';
//    $headers = [];
//    $headers[] = 'From: nnoble@greenrivertech.net';
//    $headers[] = 'Cc: neal@nrnoble.com, nnoble@greenrivertech.net';
//    $headers[] = 'Content-type: text/plain; charset=utf-8';
//    #$authorized = '-fdavid@example.com';
//     $authorized = '';
//    require './includes/process_mail.php';
//    if ($mailSent)
//    {
//        header('Location: thanks.php');
//        exit;
//    }
//}
?>

<!DOCTYPE html>
<!--
Neal Noble
Feb 15th, 2016
IT305
Assignment 7b
-->

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
	  
	  li
	  {
		font-family: Arial;
		font-size:24px
	  }
	  
	   a:hover
	   {
		background-color: yellow;
		 
		color:blue;
		font-size: 14pt;
		font-weight: bold;
		 
	   }
	  
	  a
	  {
		text-decoration: none; 
		
	  }
	  
	  
	  
	  b
	  {
		color:blue;
	  }
	  
	  th
	  {
		text-decoration: underline;
		
	  }
	  
	  tr:nth-child(even)
	  {
		background-color: #E0E0E0;
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
	  



	  .page
	  {
  		  border-radius: 7px;
		  max-width: 800px;
		  margin-top: 10px;
		  font-size: 12pt;
		  background-color: #ffffff;
		  border: solid;
		  border-width: 1px;
		  text-align: left;
		  margin-top: 100px;
		  padding: 10px;
		  box-shadow: 5px 5px 5px #0026FF
	  }

	  #page
	  {
		  max-width: 800px;
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

  
  <title>IT305 Assignment 7b</title>


</head>
<body>


<div class="container">

  <div class="row">
   <section class="col-xs-12" >
	 <div id = assignment class = page style="margin-top: 10px">
		 Neal Noble<br>
		 Feb 15th, 2016<br>
		 IT305<br>
		 Assignment 7b<br>
	 </div>

      <? include "functions.php" ?>

	 <div id = sqlconnection class ="page" style="margin-top: 10px;">
	   
	   <h2>SQL CONNECTION</h2>
		 <?php

		 $servername = gethostname();
		 $username = get_current_user();
		 $password = getpwd();
		 
		 // Create connection
		  $conn = new mysqli("127.0.0.1", $username, $password,"nnoble_grcc");

		 // Check connection
		 if ($conn->connect_error)
		 {
			 die("Connection failed: " . $conn->connect_error);
		 }
		 
		 echo "Connected successfully SQL server: <b>" .gethostname() ."</b><br>";;
		 echo 'Current script owner: <b>' . get_current_user() ."</b><br>";
		 echo "Connection info: <b>" .$conn->host_info ."</b><br>";
		 
		  
		  
		  // combine everything into a trans transaction
		  // rollback before closing connection so that the db
		  // gets reset.
		  $sql = "START TRANSACTION";
	      $conn->query($sql);
		 
		 ?>
   
	 </div> <!-- id sqlconnection -->


	  <div class = 'page' style="margin-top: 10px">
		<a href = "https://html5.validator.nu/?doc=http%3A%2F%2Fnnoble.greenrivertech.net%2F7%2F7b.php">
		  Validate this HTML5 page</a>
	  </div>
	  
	  
	  <div id = "tryit" class = 'page' style="margin-top: 10px">
		<span style ="color:red; font-family: Arial; font-size:50px">Try It Again You Smuck!</span>
		
		<ul>
		  <li>Add an input to your form that allows the user to input GPA</li>
		  <li>Validate the GPA in your new-student.php script. It is not required,
		      but if it is entered, it must be between 0.0 and 4.0.
	      </li>
            
		  <li>Write the GPA to the database</li>
		  <!--<li><img src="tryit7a-2.png" alt="TryIt" style="width:95%;height:95%;"></li>-->
		  <li>Add a link from students.php to new-student.php, and vice versa.</li>
		</ul>
		 
	  </div>
	  
	  
	  <div id = "entryform" class = 'page' style="margin-top: 10px">
		
                <div id =kfb_contactform class = "contactform">

                    <h1>Student Entry Form</h1>
                    <?php if ($_POST && ($suspect || isset($errors['mailfail']))) : ?>
                    <p class="warning">Sorry, your mail couldn't be sent.</p>
                    <?php elseif ($errors || $missing) : ?>
                    <p class="warning">Please fix the item(s) indicated</p>
                    <?php endif; ?>
                    <form method="post" action="<?= $_SERVER['PHP_SELF']; ?>">
                      <p>
                        <label for="name" \>Name:
                        <?php if ($missing && in_array('name', $missing)) : ?>
                            <span class="warning">Please enter your name</span>
                        <?php endif; ?>
                        </label>
                        <input type="text" name="name" id="name" value="Neal Noble"
                            <?php
                            if ($errors || $missing) {
                                echo 'value="' . htmlentities($name) . '"';
                            }
                            ?>
                            >
                      </p>
                      <p>
                        <label for="email">Email:
                            <?php if ($missing && in_array('email', $missing)) : ?>
                                <span class="warning">Please enter your email address</span>
                            <?php elseif (isset($errors['email'])) : ?>
                                <span class="warning">Invalid email address</span>
                            <?php endif; ?>
                        </label>
                        <input type="email" name="email" id="email" value="nrnoble@hotmail.com"
                            <?php
                            if ($errors || $missing) {
                                echo 'value="' . htmlentities($email) . '"';
                            }
                            ?>
                            >
                      </p>
                      <p>
                        <label for="comments" >Comments:
                            <?php if ($missing && in_array('comments', $missing)) : ?>
                                <span class="warning">You forgot to add any comments</span>
                            <?php endif; ?>
                        </label>
                          <textarea name="comments" id="comments"><?php
                              if ($errors || $missing) {
                                  echo htmlentities($comments);
                              }
                              
                              ?>comments go here</textarea>
                      </p>
                      <p>
                        <input type="submit" name="send" id="send" value="Send Comments">
                      </p>
                    </form>
                </div>

            
      </div>


	   
	 
	<div id = closesql class="page" style="margin-top: 10px;">
	   <H3>Closing SQL connection</H3>
	   <?php>
	   	  $sql = "ROLLBACK";
	      $conn->query($sql);
		  mysqli_close($conn);
	   ?>
	</div> <!--id = closesql -->
	 
	
	<div id= source class="page" style="margin-top: 10px;">
	  <H2>Assignment Source Code</H2>
		
	  <?php>
		highlight_file(__FILE__);
	  ?>

	</div> <!--id = source -->
	
   </section>
  </div>
 

  </div>  

<script src="js/jquery-2.1.4.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<script src="js/script.js"></script>
</body>
</html>

