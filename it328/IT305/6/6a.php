
<!--
Neal Noble
Feb 8th, 2016
IT305
Assignment 6a
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

  
  <title>IT305 Assignment 6a</title>


</head>


<body>


<div class="container">

  <div class="row">
   <section class="col-xs-12" >
	 <div id = assignment class = page style="margin-top: 10px">
		 Neal Noble<br>
		 Feb 6th, 2016<br>
		 IT305<br>
		 Assignment 6a<br>
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



	 <div id = tryit class="page" style="margin-top: 10px">
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
	 </div> <!-- id tryit -->
 
	   
	   
	 <div id = "q1" class="page" style="margin-top: 10px;">
	  <H3>1. Display the sid, first and last names, and birthdates of
			all students.</H3>

	  <?php
		$sql = "SELECT sid, first, last, birthdate FROM student";
		echo "<b>SELECT</b> <i>sid, first, last, birthdate</i>
			  <br><b>FROM</b> <i>student</i><br><br>\n\n\r";
		$result = $conn->query($sql);
	  ?>
		
	  <table style>
		<tr>
		<th>SID</th><th>First Name</th><th>Last Name</th><th>birthday</th>
		</tr>
		  <?php
		  if ($result->num_rows > 0)
		  {
			// output data of each row
			while($row = $result->fetch_assoc())
			{
				echo "<tr><td width=120>". $row["sid"]. "</td><td width=120>"
				    . $row["first"]. "</td><td width=200>" . $row["last"] . "
					  </td><td>" . $row["birthdate"]."</td></tr>\n\r";
			}
		  }
		  else
		  {
			echo "0 results";
		  }		 
	   ?>
	  </table>
	</div> <!-- id q1 -->
 
 
 
 
	 <div id = q2 class="page" style="margin-top: 10px;">
	  <H3>2. Display the names & advisor numbers of students with advisor 1 or 2.</H3>

		<?php
		  $sql = "SELECT advisor, first, last FROM student WHERE advisor=1
		          OR advisor=2";
		  
		  echo "<b>SELECT</b> <i>advisor, first, last </i> <br><b>FROM</b>
		        <i>student</i><b><br>WHERE</b> <i>advisor=1 OR advisor=2
				</i><br><br>\n\n\r";
		  
		  $result = $conn->query($sql);
		?>
		  
	  <table style>
		<tr>
		<th>advisor</th><th>First Name</th><th>Last Name</th>
		</tr>
		  
		<?php
		 if ($result->num_rows > 0)
		 {
		   // output data of each row
		   while($row = $result->fetch_assoc())
		   {
			   echo "<tr><td width=75 style = \"text-align: center;\">". $row["advisor"]
				  . "</td><td width=120>". $row["first"]. "</td><td width=200>"
				  . $row["last"]. "</td></tr>\n\r";
		   }
		 }
		 else
		 {
		   echo "0 results";
		 }
  
		?>
	 </table>
	</div> <!-- id q2 -->
 


 
	 <div id = q3 class="page"style="margin-top: 10px;">
	  <H3>3. Display the names and birthdates of students born after January 1, 1960.</H3>
		   <!--(Remember to use MySQL's date format: YYYY-MM-DD.) all students. -->

	  <?php
		$sql = "SELECT first, last, birthdate FROM student WHERE birthdate >
		       '1960-01-01'";
			   
		echo "<b>SELECT</b> <i> first, last, birthdate</i> <br><b>FROM</b>
		      <i>student</i><br><b>WHERE</b><i> birthdate > '1960-01-01'</i><br>
			  <br>\n\n\r";
			  
		$result = $conn->query($sql);
	  ?>
	  
	  <table style>
		<tr><th>First Name</th><th>Last Name</th><th>birthday</th></tr>
		<?php
		  if ($result->num_rows > 0)
		  {
			// output data of each row
			while($row = $result->fetch_assoc())
			{				  
				echo "</td><td width=120>". $row["first"]. "</td><td width=200>"
					. $row["last"] ."</td><td>" . $row["birthdate"] ."</td></tr>\n\r";
			}
		  }
		  else
		  {
			echo "0 results";
		  } 
		?>
	  </table>
	</div> <!--id = q3 -->
 
 
 
 
	 <div id = q4 class="page" style="margin-top: 10px;">
	  <H3>4. Display names and GPA's of students with GPAs between 3.0 and 4.0.</H3>

		<?php
		  $sql = "SELECT first,last,gpa FROM student WHERE gpa > 3.0 AND gpa < 4.0";
		  echo "<b>SELECT</b> <i>first, last, gpa</i> <br><b>FROM</b>
		        <i>student</i><br><b>WHERE</b><i> gpa > 3.0 AND gpa < 4.0</i>
				<br><br>\n\n\r";
				
		  $result = $conn->query($sql);
		?>  
		<table style>
		  <tr><th>First Name</th><th>Last Name</th><th>GPA</th></tr>
			<?php
			  if ($result->num_rows > 0)
			  {

				
				while($row = $result->fetch_assoc())
				{
				  // output data of each row
					//echo "<tr><td width=120>". $row["first"]. "</td><td width=200>"
					//     . $row["last"]. "</td><td>" . $row["gpa"] ."</td></tr>\n\r";
						 
						 				
					$gpatemp = number_format((float)$row["gpa"], 2, '.', '');
					echo "<tr><td width=120>". $row["first"]. "</td><td width=200>"
					     . $row["last"]. "</td><td>" . $gpatemp ."</td></tr>\n\r";
		
				}
			  }
			  else
			  {
				echo "0 results";
			  }
		  ?>
		</table>
	 </div> <!--id = q4 -->
 
 
 
 
	 <div id = q5 class="page" style="margin-top: 10px;">
	  <H3>5. Add a new class and three grades.</H3>

		<?php
		  $sql = "INSERT INTO class 
				  (abbrev, title) 
				  VALUES
				  ('IT 344','Virtualization & Storage')";
				  
		  $sql1 = " INSERT INTO grade(sid, classid, grade)
		            VALUES('123-45-6789',6,4.0)";
		  $sql2 = " INSERT INTO grade(sid, classid, grade)
		            VALUES('656-88-0098',6,4.0)";
		  $sql3 = " INSERT INTO grade(sid, classid, grade)
		            VALUES('343-66-9999',6,4.0)";

		  echo "<b>INSERT INTO</b><i> class(abbrev, title)
		        </i><br><b>VALUES</b><i> ('IT 344','Virtualization & Storage')
				</i><br><br>\n\n\r";
	
		  echo " <b>INSERT INTO grade</b><i>(sid, classid, grade)</i><b><br>
		         VALUES</b><i>('123-45-6789',6,4.0)</i><br><br>\n\r";
		  echo " <b>INSERT INTO grade</b><i>(sid, classid, grade)</i><b><br>
		         VALUES</b><i>('656-88-0098',6,4.0)</i><br><br>\n\r";
		  echo " <b>INSERT INTO grade</b><i>(sid, classid, grade)</i><b><br>
		         VALUES</b><i>('343-66-9999',6,4.0)</i><br><br>\n\r";
		  
	
		  $sql4 = "SELECT abbrev, title FROM class";
		  $result = $conn->query($sql);
		  $result = $conn->query($sql4);
		?>  
		
		<table style>
		  
		  <tr><th>abbrev</th><th>Title</th></tr>
	  
		  <?php
			  if ($result->num_rows > 0)
			  {
				// output data of each row
				while($row = $result->fetch_assoc())
				{
					echo "<tr></td><td width=80>". $row["abbrev"]. "</td><td width=300>"
						 . $row["title"] ."</td></tr>\n\r";
		
				}
			  }
			  else
			  {
				echo "0 results";
			  }

			?>
		</table>
		

	 </div> <!--id = q5 -->
	 
	 
	 
	 
	 <div id = q6 class="page" style="margin-top: 10px;">
	   <H3>6. Herbert Powell has offered you $325 to hack into the system
	          and change his grade in IT 190 to 3.4.</H3>
	   <?php
	   
	   

	   
	   	  $sql = "UPDATE grade SET grade = '3.4' WHERE sid='123-43-6554'AND classid = '4'";
		  echo "<b>UPDATE</b><i> grade </i><br><b>SET </b><i>grade = 3.4</i> <b><br>WHERE</b> 
		        <i>sid='123-43-6554'</i> <b>AND</b><i> classid = 4</i>\n\r<br><br>";
		
	   
         if ($conn->query($sql) === TRUE)
		 {
			echo "You have successfully hacked into the system and updated Herbert's grade<br><br>";
		 }
		 else
		 {
			echo "Error updating record: " . $conn->error;		
		 }
		 
		 
		 
		 $sql = "SELECT classid, sid, grade FROM grade WHERE sid='123-43-6554' AND classid = '4'";
		 
		 $result = $conn->query($sql);
	   
	   ?>
	   <table style>
		 <tr><th>classid</th><th>sid</th><th>grade</th></tr>
		 <?php
		  if ($result->num_rows > 0)
		  {
			// output data of each row
			while($row = $result->fetch_assoc())
			{
			  
				echo "<tr><td width=120>". $row["classid"]. "</td><td width=120>". $row["sid"].
				     "</td><td width=200>" . $row["grade"] . "</td></tr>\n\r";
	
			}
		  }
		  else
		  {
			echo "0 results";
		  }
		?>
	   </table>
	 </div> <!--id = q6 -->
 


 
	 <div id = q7 class="page" style="margin-top: 10px;">
	   <H3>7. Eliminate one of your classmates, and then cover
	          your tracks by removing them from the GRCC Student DB</H3>

	   <?php
	   
	     $sql = "DELETE FROM `student` WHERE sid = '880-34-3456'";
		 
		 echo "<b>DELETE FROM</b> <i>`student`</i><b> <br>WHERE</b><i> sid = '880-34-3456'</i>\r\n<br><br>";
		 
		 
		 if ($conn->query($sql) === TRUE)
		 {
			echo "Frodo Baggins has been eliminated!";
		 }
		 else
		 {
			echo "Error updating record: " . $conn->error;		
		 }
		 
		 
		/* 
		 $sql = "SELECT sid, first, last, birthdate FROM student";
		 echo "<b>SELECT</b> <br><i>sid, first, last, birthdate</i>
		       <br><b>FROM</b> <i>student</i><br><br>\n\n\r";
		 $result = $conn->query($sql);
		 */
		?>
		<!--
	   <table style>
		 <tr><th>Sid</th><th>First Name</th><th>Last Name</th><th>birthday</th></tr>
		 -->
		  <?php
		  /*
		   if ($result->num_rows > 0)
		   {
			 // output data of each row
			 while($row = $result->fetch_assoc())
			 {
				 echo "<tr><td width=120>". $row["sid"]. "</td><td width=120>". $row["first"].
				      "</td><td width=200>" . $row["last"] . "</td><td>" . $row["birthdate"]
					 ."</td></tr>\n\r";
			 }
		   }
		   else
		   {
			 echo "0 results";
		   }
		   */
		 ?>
	   </table>
	 
	 </div> <!-- id = q7 -->
	 
	 
	 
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
</div>


<script src="js/jquery-2.1.4.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<script src="js/script.js"></script>
</body>
</html>

