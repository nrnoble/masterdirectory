<!DOCTYPE html>
<!--
Neal Noble
Feb 15th, 2016
IT305
Assignment 7a
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

  
  <title>IT305 Assignment 7a</title>


</head>
<body>


<div class="container">

  <div class="row">
   <section class="col-xs-12" >
	 <div id = assignment class = page style="margin-top: 10px">
		 Neal Noble<br>
		 Feb 15th, 2016<br>
		 IT305<br>
		 Assignment 7a<br>
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
		<a href = "https://html5.validator.nu/?doc=http%3A%2F%2Fnnoble.greenrivertech.net%2F7%2F7a.php">
			Validate this HTML5 page</a>
	  </div>
	  
	  
	  <div class = 'page' style="margin-top: 10px">
		<span style ="color:red; font-family: Arial; font-size:50px">Mission: Impossible!</span>
		<ul>
		  <li>Display the students as an unordered list.</li>
		  <li>Display the students alphabetically by last name.
		   <ul><li>Hint: Add an ORDER BY clause to your SELECT statement.</li></ul>
		  </li>
            
		  <li>Add the students' GPAs to the listing.</li>
		  <li><img src="tryit7a-2.png" alt="TryIt" style="width:95%;height:95%;"></li>
		</ul>
		 
	  </div>


	  <div class = 'page' style="margin-top: 10px">
		<a href = "http://nnoble.greenrivertech.net/7/7b.php">Link to New Student Entry form</a>
	  </div>
<!--<div id = tryit class="page" style="margin-top: 10px">

  
  <img src="try7a.PNG" alt="TryIt" style="width:95%;height:95%;">
</div>>-->



<!--	 <div id = tryit class="page" style="margin-top: 10px">
		<h2>Try It</h2>
		Using your GRCC database :
		<ol>
		  <li><a href="#q1">Display the sid, first and last names, and birthdates of
			  all students.</a></li>
		  <li><a href="#q2"> Display the names and advisor numbers of students with
			  advisor 1 or 2.</a></li>
		  <li><a href="#q3"> Display the names and birthdates of students born after
			  January 1, 1960.
		  (Remember to use MySQL's date format:  YYYY-MM-DD.)</a></li>
		  <li><a href="#q4">Display names and GPA's of students with GPAs between
			  3.0 and 4.0.</a></li>
		  <li><a href="#q5"> Add a new class and three grades.</a></li>
		  <li><a href="#q6"> Change the grade for Herbert Powell in IT 190 to 3.4.</a></li>
		  <li><a href="#q7"> Delete one of your students.</a></li>
		  <li><a href="#source"> Source Code</a></li>
		  
		</ol>
	 </div>-->
	 
	 <!-- id tryit -->
 
	   
	 <div id = "q1" class="page" style="margin-top: 10px;">
	  <H3>Display the students as an unordered list</H3>

	  <?php
		$sql = "SELECT sid, first, last FROM student";
		echo "<b>SELECT</b> <i>sid, last, first </i>
			  <br><b>FROM</b> <i>student</i><br><br>\n\n\r";
		$result = $conn->query($sql);
	  ?>
		

		  <?php
		  if ($result->num_rows > 0)
		  {
			// output data of each row
			
			echo "<ul>";
			while($row = $result->fetch_assoc())
			{
				echo "<li style =\"font-family: courier; font-size:12pt; \">". $row["sid"]. "&nbsp;&nbsp;&nbsp;"
				    . $row["last"]. ", " . $row["first"] . "</li>\n\r";
			}
			echo "</ul>";
  
		  }
		  else
		  {
			echo "0 results";
		  }		 
	   ?>
 
	</div> <!-- id q1 -->
 
 
	 <div id = q2 class="page" style="margin-top: 10px;">
	  <H3>Display the students alphabetically by last name.</H3>

		<?php
		  $sql = "SELECT first, last FROM student ORDER BY Last";
		  
		  echo "<b>SELECT</b> <i> first, last </i> <br><b>FROM</b>
		        <i>student</i><b><br>ORDER BY</b> <i>last
				</i><br><br>\n\n\r";
		  
		  $result = $conn->query($sql);
		?>
		  
	  <table style>
		<tr>
		<th style="width: 200px;">Last Name</th><th style="width: 200px;">First Name</th>
		</tr>
		  
		<?php
		 if ($result->num_rows > 0)
		 {
		   // output data of each row
		   while($row = $result->fetch_assoc())
		   {
			   echo "<tr><td  style = \"text-align: left ;\">". $row["last"]. "</td>
			             <td>". $row["first"]. "</td></tr>\n\r";
		   }
		 }
		 else
		 {
		   echo "0 results";
		 }
  
		?>
	 </table>
	</div> <!-- id q2 -->
 
	
	 <div id = "gpa" name = "gpa" class="page" style="margin-top: 10px;">
	  <H3>Add the students' GPAs to the listing.</H3>

		<?php
		  $sql = "SELECT first, last, gpa FROM student ORDER BY Last";
		  
		  echo "<b>SELECT</b> <i>first, last, gpa </i> <br><b>FROM</b>
		        <i>student</i><b><br>ORDER BY</b> <i>last
				</i><br><br>\n\n\r";
		  
		  $result = $conn->query($sql);
		?>
		  
	  <table style>
		<tr>
		<th style="width: 200px;">Last Name</th>
		<th style="width: 200px;">First Name</th>
		<th style="width: 100px;">GPA</th>
		</tr>
		  
		<?php
		 if ($result->num_rows > 0)
		 {
		   // output data of each row

		  $gpa = number_format($number, 2, ',', ' ');

		   while($row = $result->fetch_assoc())
		   {
			   if ($row["gpa"] == 0)
			   {
				   $gpa = "";
			   }
			   else
			   {
				   $gpa = number_format($row["gpa"], 2);
			   }
				   echo "<tr><td style = \"text-align: left ;\">". $row["last"] . "</td>"
			          . "<td style = \"text-align: left ;\">". $row["first"]. "</td>"
				      . "<td style = \"text-align: left ;\">". $gpa . "</td>"
				      . "</tr>\n\r";
		   }
		 }
		 else
		 {
		   echo "0 results";
		 }
  
		?>
	 </table>
	</div> <!-- id q2 -->
 	 
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

