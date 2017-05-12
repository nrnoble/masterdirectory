
<!--
Neal Noble
Feb 20th, 2016
IT301
Assignment SQL
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
		 Feb 20th, 2016<br>
		 IT301<br>
		 Assignment Inserts and Simple Queries<br>
	 </div>

      <? include "functions.php" ?>

	 <div id = sqlconnection class ="page" style="margin-top: 10px;">
	   
	   <h2>SQL CONNECTION</h2>
		 <?php

		 $servername = gethostname();
		 $username = get_current_user();
		 $password = getpwd();
		 
		 // Create connection
		  $conn = new mysqli("127.0.0.1", $username, $password,"nnoble_sakila");

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
		  // $sql = "START TRANSACTION";
	      // $conn->query($sql);
		 
		 ?>
   
	 </div> <!-- id sqlconnection -->



	 <div id = tryit class="page" style="margin-top: 10px">
		<h2>Assignment</h2>

  Complete the following exercises. Submit the queries you wrote and screenshots
  of the results in a word doc to the Canvas dropbox.
<ol>
   <li>Add five records to each of your tables from Exercises - Table Creation.</li><br>
  
	  <ul>
		<li>Submit your queries used.</li>
		<li>Perform a "SELECT * FROM table_name" query to display your table</li>
		<li>records for each table.</li>
		<li>Add appropriate and realistic record data.</li>
	  </ul><br>
	<li>  Make sure the sakila database is imported to your mysql database
     on greenrivertech.</li><br>
	 
  <li> Retrieve the following results by writing SELECT statements against
     the sakila database. Submit your query and a screenshot of your results:</li><br>
	 <uL>
		<li>All movies from the film table.</li>
		<li>The first and last name of the first 10 actors in the actor table.</li>
		<li>A list of all ratings in the film table with no duplicates.</li>
		<li>A list of all PG rated movies from the film table.</li>
		<li>A list of all movies over 2 hours long from the film table.</li>
		<li>All language names from the language table.</li>
		<li>The category id and genre from each record in the category table.</li>
		<li>All fields for each actor with a last name of "GUINESS" in the actor table.</li>
		<li>Run the following query: SELECT COUNT(*) FROM actor;</li>
		<li>What do you get as results? What does COUNT(*) calculate?</li>
	  </uL>
</ol>
		
		
		
		
<!--		<ol>
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
		  
		</ol>-->
	 </div> <!-- id tryit -->
 
	   
	   
	 <div id = "college_classroom" class="page" style="margin-top: 10px;">
	  <H3>Add five records to each of your tables from Exercises - Table Creation.</H3>
<pre>
USE nnoble_sakila;
TRUNCATE TABLE college_classroom;
INSERT INTO college_classroom (room_num , location, room_size, phone, occupancy)
VALUES ('101','Building-A','200','253-833-1102',40),
       ('102','Building-A','200','253-833-1102',40),
       ('103','Building-A','300','253-833-1103',50),
       ('201','Building-A','200','253-833-1201',40),
       ('202','Building-A','200','253-833-1102',40);
	   
SELECT * FROM college_classroom;
</pre>

	  <?php
		$sql = "
		USE nnoble_sakila;
		TRUNCATE TABLE college_classroom;
		INSERT INTO college_classroom (room_num , location, room_size, phone, occupancy)
		VALUES ('101','Building-A','200','253-833-1102',40),
		('102','Building-A','200','253-833-1102',40),
		('103','Building-A','300','253-833-1103',50),
		('201','Building-A','200','253-833-1201',40),
		('202','Building-A','200','253-833-1102',40);";
		
		
		
		#echo "<b>SELECT</b> <i>sid, first, last, birthdate</i>
		#	  <br><b>FROM</b> <i>student</i><br><br>\n\n\r";
		
		# $result = $conn->query($sql);
		# echo mysql_errno($sql) . ": " . mysql_error($sql) . "\n";
		$sql ="SELECT * FROM college_classroom";
		$result = $conn->query($sql);
		print_r($result);
		# echo mysql_errno($sql) . ": " . mysql_error($sql) . "\n";
	  ?>
		
	  <table style>
		<tr>
		<th>Room Number</th><th>Location</th><th>Room Size in SQF</th><th>Phone</th><th>Occupancy</th>
		</tr>
		  <?php
		  if ($result->num_rows > 0)
		  {
			// output data of each row
			while($row = $result->fetch_assoc())
			{
				echo "<tr><td width=120>". $row["room_num"]. "</td><td width=120>"
				    . $row["location"]. "</td><td width=100>" . $row["room_size"] . "
					  </td><td width=100>" . $row["phone"] . "</td><td width=100>"
					  . $row["occupancy"]."</td></tr>\n\r";
			}
		  }
		  else
		  {
			echo "0 results";
		  }		 
	   ?>
	  </table>
	</div> <!-- id q1 -->
 
 
 
 	 
	 
	 
	 <div id = "Grocery_store_products" class="page" style="margin-top: 10px;">
<pre>
USE nnoble_sakila;.
TRUNCATE TABLE Grocery_store_products;
INSERT INTO `Grocery_store_products`(`type`, `name`, `brand`, `price`, `units`) 
VALUES ('dairy','milk','dairy gold','3.00','100'),
       ('dairy','butter','dairy gold','4.00','300'),
       ('fruit','oranges','Sunkissed','1.00','430'),
       ('Candy','Mounds Bar','Hershey','1.50','500'),
       ('cerceal','Oatmeal','Store Band','2.50','430')
       
SELECT * FROM Grocery_store_products;

</pre>

	  <?php
		$sql = "USE nnoble_sakila;# MySQL returned an empty result set (i.e. zero rows).\n"
			. "TRUNCATE TABLE Grocery_store_products;# MySQL returned an empty result set (i.e. zero rows).\n"
			. "INSERT INTO `Grocery_store_products`(`type`, `name`, `brand`, `price`, `units`) \n"
			. "VALUES (\'dairy\',\'milk\',\'dairy gold\',\'3.00\',\'100\'),\n"
			. " (\'dairy\',\'butter\',\'dairy gold\',\'4.00\',\'300\'),\n"
			. "	(\'fruit\',\'oranges\',\'Sunkissed\',\'1.00\',\'430\'),\n"
			. "	(\'Candy\',\'Mounds Bar\',\'Hershey\',\'1.50\',\'500\'),\n"
			. "	(\'cerceal\',\'Oatmeal\',\'Store Band\',\'2.50\',\'430\')# 5 rows affected.\n"
			. "";
		
		
		#echo "<b>SELECT</b> <i>sid, first, last, birthdate</i>
		#	  <br><b>FROM</b> <i>student</i><br><br>\n\n\r";
		
		///$result = $conn->query($sql);
		$sql ="SELECT * FROM Grocery_store_products";
		$result = $conn->query($sql);
	  ?>
		
	  <table style>
		<tr>
		<th>type</th><th>name</th><th>brand</th><th>price</th><th>units</th>
		</tr>
		  <?php
		  if ($result->num_rows > 0)
		  {
			// output data of each row
			while($row = $result->fetch_assoc())
			{
				echo "<tr><td width=120>". $row["type"]. "</td><td width=120>"
				    . $row["name"]. "</td><td width=100>" . $row["brand"] . "
					  </td><td width=100>" . $row["price"] . "</td><td width=100>"
					  . $row["units"]."</td></tr>\n\r";
			}
		  }
		  else
		  {
			echo "0 results";
		  }		 
	   ?>
	  </table>
	</div> <!-- id q1 -->
 
 
  	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 	 
	 <div id = "Grocery_store_products2" class="page" style="margin-top: 10px;">
<pre>

       
SELECT * FROM Grocery_store_products;

</pre>

	  <?php
		$sql = "USE nnoble_sakila;# MySQL returned an empty result set (i.e. zero rows).\n"
			. "TRUNCATE TABLE Grocery_store_products;# MySQL returned an empty result set (i.e. zero rows).\n"
			. "INSERT INTO `Grocery_store_products`(`type`, `name`, `brand`, `price`, `units`) \n"
			. "VALUES (\'dairy\',\'milk\',\'dairy gold\',\'3.00\',\'100\'),\n"
			. " (\'dairy\',\'butter\',\'dairy gold\',\'4.00\',\'300\'),\n"
			. "	(\'fruit\',\'oranges\',\'Sunkissed\',\'1.00\',\'430\'),\n"
			. "	(\'Candy\',\'Mounds Bar\',\'Hershey\',\'1.50\',\'500\'),\n"
			. "	(\'cerceal\',\'Oatmeal\',\'Store Band\',\'2.50\',\'430\')# 5 rows affected.\n";

		
		#echo "<b>SELECT</b> <i>sid, first, last, birthdate</i>
		#	  <br><b>FROM</b> <i>student</i><br><br>\n\n\r";
		
		///$result = $conn->query($sql);
		$sql ="SELECT * FROM Grocery_store_products";
		$result = $conn->query($sql);
	  ?>
		
	  <table style>
		<tr>
		<th>type</th><th>name</th><th>brand</th><th>price</th><th>units</th>
		</tr>
		  <?php
		  print_r($result);
		  if ($result->num_rows > 0)
		  {
			// output data of each row
			while($row = $result->fetch_assoc())
			{
				echo "<tr><td width=120>". $row["type"]. "</td><td width=120>"
				    . $row["name"]. "</td><td width=100>" . $row["brand"] . "
					  </td><td width=100>" . $row["price"] . "</td><td width=100>"
					  . $row["units"]."</td></tr>\n\r";
			}
		  }
		  else
		  {
			echo "0 results";
		  }		 
	   ?>
	  </table>
	</div> <!-- id q1 -->
 
 
  	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 <div id = "movie_star" class="page" style="margin-top: 10px;">
<pre>

INSERT INTO `movie_star`(`first_name`, `last_name`, `networth`, `total_movies`,
            `degrees_to_kevin_bacon`) 
VALUES ('George' ,'Clooney','10000000' ,'15' ,'2'),
       ('Robert' ,'Deniro' ,'10000000' ,'15' ,'1'),
       ('Kevin'  ,'Spacey' ,'100000000','23' ,'2'),
       ('John'   ,'Wayne'  ,'15000000' ,'150','2'),
       ('William','Shatner','100000000','15' ,'2')

</pre>
<?php
$sql = "USE nnoble_sakila; \n"
    . "TRUNCATE TABLE movie_star;/n"
    . "INSERT INTO `movie_star`(`first_name`, `last_name`, `networth`, `total_movies`, `degrees_to_kevin_bacon`) \n"
    . "VALUES (\'George\',\'Clooney\',\'10000000\',\'15\',\'2\'),\n"
    . "(\'Robert\',\'Deniro\',\'10000000\',\'15\',\'1\'),\n"
    . "\n"
    . "(\'Kevin\',\'Spacey\',\'100000000\',\'23\',\'2\'),\n"
    . "(\'John\',\'Wayne\',\'15000000\',\'150\',\'2\'),\n"
    . "(\'William\',\'Shatner\',\'100000000\',\'15\',\'2\')";
		
		
		#echo "<b>SELECT</b> <i>sid, first, last, birthdate</i>
		#	  <br><b>FROM</b> <i>student</i><br><br>\n\n\r";
		
		$result = $conn->query($sql);
		$sql ="SELECT * FROM movie_star";
		$result = $conn->query($sql);
	  ?>
		
	  <table style>
		<tr>
		<th>first_name</th><th>last_name</th><th>networth</th><th>total_movies</th><th>degrees_to_kevin_bacon</th>
		</tr>
		  <?php
		  if ($result->num_rows > 0)
		  {
			// output data of each row
			while($row = $result->fetch_assoc())
			{
				echo "<tr><td width=120>". $row["first_name"]. "</td><td width=120>"
				    . $row["last_name"]. "</td><td width=100>" . $row["networth"] . "
					  </td><td width=100>" . $row["total_movies"] . "</td><td width=100>"
					  . $row["degrees_to_kevin_bacon"]."</td></tr>\n\r";
			}
		  }
		  else
		  {
			echo "0 results";
		  }		 
	   ?>
	  </table>
	</div> <!-- id q1 -->
 
 
	 
 


 
	 
	 
	 
	 
	 
	 
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
				// output data of each row
				while($row = $result->fetch_assoc())
				{
				  
					echo "<tr><td width=120>". $row["first"]. "</td><td width=200>"
					     . $row["last"]. "</td><td>" . $row["gpa"] ."</td></tr>\n\r";
		
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

