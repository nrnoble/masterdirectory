
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
		  $sql = "START TRANSACTION";
	      $conn->query($sql);
		 
		 ?>
   
	 </div> <!-- id sqlconnection -->



	 <div id = assignment class="page" style="margin-top: 10px">
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
		</div>

	   
	   
	 <div id = "insert_college_classroom.sql" class="page" style="margin-top: 10px;">
	  <H3>Add five records to each of your tables from Exercises - Table Creation.</H3>


	 <?php
			$sqlfile = file_get_contents("insert.college_classroom.sql");
	 ?>



<pre>
<?php
echo "$sqlfile";
?>
</pre>

	  <?php
$sql = $sqlfile;

		//$resultx = $conn->query($sql);
	    //$resultx = $conn->multi_query($sql);
		$sql ="SELECT * FROM college_classroom";
		$result = $conn->query($sql);
	    //print_r($result);
	  ?>
		
	  <table style>
		<tr>
		<th>Room Number</th><th>Location</th><th>Room Size SQF</th><th>Phone</th><th>Occupancy</th>
		</tr>
		  <?php
		  if ($result->num_rows > 0)
		  {
			// output data of each row
			while($row = $result->fetch_assoc())
			{
				echo "<tr>
					 <td width=120>" . $row["room_num"]
					. "</td><td width=120>" . $row["location"]
					. "</td><td width=150>" . $row["room_size"]
					. "</td><td width=175>" . $row["phone"]
					. "</td><td width=100>" . $row["occupancy"]."</td></tr>\n\r";
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


	 <?php
	 $sqlfile = file_get_contents("insert_grocery_store_products.sql");
	 ?>
<pre>

<?php
echo $sqlfile;
?>

</pre>

	  <?php
		$sql = $sqlfile;
		
		#echo "<b>SELECT</b> <i>sid, first, last, birthdate</i>
		#	  <br><b>FROM</b> <i>student</i><br><br>\n\n\r";
	    $resultx = $conn->query("TRUNCATE TABLE Grocery_store_products;");
	    $resultx = $conn->query($sqlfile);
	    //$sql ="SELECT * FROM Grocery_store_products";
		$result = $conn->query("SELECT * FROM Grocery_store_products");
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
				$price = number_format((float)$row["price"], 2, '.', '');
				echo "<tr><td width=120>". $row["type"]. "</td><td width=120>"
				    . $row["name"]. "</td><td width=100>" . $row["brand"] . "
					  </td><td width=100>" . $price . "</td><td width=100>"
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


		   <?php
		   $sqlfile = file_get_contents("insert_movie_star.sql");
		   ?>
		   <pre>

<?php
echo $sqlfile;
?>

</pre>

		   <?php
		   $sql = $sqlfile;

		   #echo "<b>SELECT</b> <i>sid, first, last, birthdate</i>
		   #	  <br><b>FROM</b> <i>student</i><br><br>\n\n\r";
		   $resultx = $conn->query("TRUNCATE TABLE movie_star;");
		   $resultx = $conn->query($sqlfile);
		   //$sql ="SELECT * FROM Grocery_store_products";
		   $result = $conn->query("SELECT * FROM movie_star");
		   ?>

		   <table style>
			   <tr>
				   <th>First Name</th><th>Last Name</th><th>Net Worth</th><th>Total Movie</th><th>Degrees To Kevin Bacon</th>
			   </tr>
			   <?php
			   if ($result->num_rows > 0)
			   {
				   // output data of each row
				   while($row = $result->fetch_assoc())
				   {
					   //$price = number_format((float)$row["price"], 2, '.', '');
					   echo "<tr> <td width=120>" . $row["first_name"]
					      . "</td><td width=120>" . $row["last_name"]
					      . "</td><td width=100>" . $row["networth"]
					      . "</td><td width=100>" . $row["total_movies"]
					      . "</td><td width=100>" . $row["degrees_to_kevin_bacon"]."</td></tr>\n\r";
				   }
			   }
			   else
			   {
				   echo "0 results";
			   }
			   ?>
		   </table>
	   </div> <!-- id q1 -->


   	 <div id = "employee" class="page" style="margin-top: 10px;">


		   <?php
		   $sqlfile = file_get_contents("insert_employee.sql");
		   ?>
		   <pre>

<?php
echo $sqlfile;
?>

</pre>

		   <?php
		   $sql = $sqlfile;

		   #echo "<b>SELECT</b> <i>sid, first, last, birthdate</i>
		   #	  <br><b>FROM</b> <i>student</i><br><br>\n\n\r";
		   $resultx = $conn->query("TRUNCATE TABLE employee;");
		   $resultx = $conn->query($sqlfile);
		   //$sql ="SELECT * FROM Grocery_store_products";
		   $result = $conn->query("SELECT * FROM employee");
		   ?>

		   <table style>
			   <tr>
				   <th>First Name</th><th>Last Name</th><th>Title</th><th>Hire Date</th><th>Department</th>
			   </tr>
			   <?php
			   if ($result->num_rows > 0)
			   {
				   // output data of each row
				   while($row = $result->fetch_assoc())
				   {
					   //$price = number_format((float)$row["price"], 2, '.', '');
					   echo "<tr> <td width=120>" . $row["first_name"]
						   . "</td><td width=120>" . $row["last_name"]
						   . "</td><td width=150>" . $row["title"]
						   . "</td><td width=100>" . $row["hiredate"]
						   . "</td><td width=100>" . $row["department"]."</td></tr>\n\r";
				   }
			   }
			   else
			   {
				   echo "0 results";
			   }
			   ?>
		   </table>
	   </div> <!-- id q1 -->


     <div id = "allmovies" class="page" style="margin-top: 10px;">


		   <?php
		   $sqlfile = file_get_contents("selectallfilms.sql");
		   ?>
		   <pre>

<?php
echo $sqlfile;
?>

</pre>

		   <?php
		   $sql = $sqlfile;

		   #echo "<b>SELECT</b> <i>sid, first, last, birthdate</i>
		   #	  <br><b>FROM</b> <i>student</i><br><br>\n\n\r";
		   // $resultx = $conn->query("TRUNCATE TABLE employee;");
		   // $resultx = $conn->query($sqlfile);
		   //$sql ="SELECT * FROM Grocery_store_products";
		   $result = $conn->query($sqlfile);
		   ?>

		   <table style>
			   <tr>
				   <th>Title</th>
			   </tr>
			   <?php
			   if ($result->num_rows > 0)
			   {
				   // output data of each row
				   while($row = $result->fetch_assoc())
				   {
					   //$price = number_format((float)$row["price"], 2, '.', '');
					   echo "<tr> <td width=250>" . $row["title"];
//						   . "</td><td width=120>" . $row["last_name"]
//						   . "</td><td width=150>" . $row["title"]
//						   . "</td><td width=100>" . $row["hiredate"]
//						   . "</td><td width=100>" . $row["department"]."</td></tr>\n\r";
				   }
			   }
			   else
			   {
				   echo "0 results";
			   }
			   ?>
		   </table>
	   </div> <!-- id q1 -->


     <div id = "selectactors" class="page" style="margin-top: 10px;">


		   <?php
		   $sqlfile = file_get_contents("selectactors.sql");
		   ?>
		   <pre>

<?php
echo $sqlfile;
?>

</pre>

		   <?php
		   $sql = $sqlfile;

		   #echo "<b>SELECT</b> <i>sid, first, last, birthdate</i>
		   #	  <br><b>FROM</b> <i>student</i><br><br>\n\n\r";

		   //$sql ="SELECT * FROM Grocery_store_products";
		   $result = $conn->query("$sqlfile");
		   ?>

		   <table style>
			   <tr>
				   <th>First Name</th><th>Last Name</th>
			   </tr>
			   <?php
			   if ($result->num_rows > 0)
			   {
				   // output data of each row
				   while($row = $result->fetch_assoc())
				   {
					   //$price = number_format((float)$row["price"], 2, '.', '');
					   echo "<tr> <td width=120>" .  $row["first_name"]
						   . "</td><td width=120>" . $row["last_name"]
						   ."</td></tr>\n\r";
				   }
			   }
			   else
			   {
				   echo "0 results";
			   }
			   ?>
		   </table>
	   </div> <!-- id q1 -->


     <div id = "listratings" class="page" style="margin-top: 10px;">


		   <?php
		   $sqlfile = file_get_contents("listratings.sql");
		   ?>
		   <pre>

<?php
echo $sqlfile;
?>

</pre>

		   <?php
		   $sql = $sqlfile;

		   #echo "<b>SELECT</b> <i>sid, first, last, birthdate</i>
		   #	  <br><b>FROM</b> <i>student</i><br><br>\n\n\r";
		   // $resultx = $conn->query("TRUNCATE TABLE employee;");
		   // $resultx = $conn->query($sqlfile);
		   //$sql ="SELECT * FROM Grocery_store_products";
		   $result = $conn->query($sqlfile);
		   ?>

		   <table style>
			   <tr>
				   <th>Title</th>
			   </tr>
			   <?php
			   if ($result->num_rows > 0)
			   {
				   // output data of each row
				   while($row = $result->fetch_assoc())
				   {
					   //$price = number_format((float)$row["price"], 2, '.', '');
					   echo "<tr> <td width=250>" . $row["rating"];
//						   . "</td><td width=120>" . $row["last_name"]
//						   . "</td><td width=150>" . $row["title"]
//						   . "</td><td width=100>" . $row["hiredate"]
//						   . "</td><td width=100>" . $row["department"]."</td></tr>\n\r";
				   }
			   }
			   else
			   {
				   echo "0 results";
			   }
			   ?>
		   </table>
	   </div> <!-- id q1 -->



	   <div id = "pgmovies" class="page" style="margin-top: 10px;">


		   <?php
		   $sqlfile = file_get_contents("pgmovies.sql");
		   ?>
		   <pre>

<?php
echo $sqlfile;
?>

</pre>

		   <?php
		   $sql = $sqlfile;

		   #echo "<b>SELECT</b> <i>sid, first, last, birthdate</i>
		   #	  <br><b>FROM</b> <i>student</i><br><br>\n\n\r";
		   // $resultx = $conn->query("TRUNCATE TABLE employee;");
		   // $resultx = $conn->query($sqlfile);
		   //$sql ="SELECT * FROM Grocery_store_products";
		   $result = $conn->query($sqlfile);
		   ?>

		   <table style>
			   <tr>
				   <th>Title</th>
			   </tr>
			   <?php
			   if ($result->num_rows > 0)
			   {
				   // output data of each row
				   while($row = $result->fetch_assoc())
				   {
					   //$price = number_format((float)$row["price"], 2, '.', '');
					   echo "<tr> <td width=250>" . $row["title"];
//						   . "</td><td width=120>" . $row["last_name"]
//						   . "</td><td width=150>" . $row["title"]
//						   . "</td><td width=100>" . $row["hiredate"]
//						   . "</td><td width=100>" . $row["department"]."</td></tr>\n\r";
				   }
			   }
			   else
			   {
				   echo "0 results";
			   }
			   ?>
		   </table>
	   </div> <!-- id q1 -->



	   <div id = "longmovies" class="page" style="margin-top: 10px;">


		   <?php
		   $sqlfile = file_get_contents("longmovies.sql");
		   ?>
		   <pre>

<?php
echo $sqlfile;
?>

</pre>

		   <?php
		   $sql = $sqlfile;

		   #echo "<b>SELECT</b> <i>sid, first, last, birthdate</i>
		   #	  <br><b>FROM</b> <i>student</i><br><br>\n\n\r";
		   // $resultx = $conn->query("TRUNCATE TABLE employee;");
		   // $resultx = $conn->query($sqlfile);
		   //$sql ="SELECT * FROM Grocery_store_products";
		   $result = $conn->query($sqlfile);
		   ?>

		   <table style>
			   <tr>
				   <th>Title</th>
			   </tr>
			   <?php
			   if ($result->num_rows > 0)
			   {
				   // output data of each row
				   while($row = $result->fetch_assoc())
				   {
					   //$price = number_format((float)$row["price"], 2, '.', '');
					   echo "<tr> <td width=250>" . $row["title"]
						   . "</td><td width=120>" . $row["length"];
//						   . "</td><td width=150>" . $row["title"]
//						   . "</td><td width=100>" . $row["hiredate"]
//						   . "</td><td width=100>" . $row["department"]."</td></tr>\n\r";
				   }
			   }
			   else
			   {
				   echo "0 results";
			   }
			   ?>
		   </table>
	   </div> <!-- id q1 -->



	   <div id = "languages" class="page" style="margin-top: 10px;">


		   <?php
		   $sqlfile = file_get_contents("languages.sql");
		   ?>
		   <pre>

<?php
echo $sqlfile;
?>

</pre>

		   <?php
		   $sql = $sqlfile;

		   #echo "<b>SELECT</b> <i>sid, first, last, birthdate</i>
		   #	  <br><b>FROM</b> <i>student</i><br><br>\n\n\r";
		   // $resultx = $conn->query("TRUNCATE TABLE employee;");
		   // $resultx = $conn->query($sqlfile);
		   //$sql ="SELECT * FROM Grocery_store_products";
		   $result = $conn->query($sqlfile);
		   ?>

		   <table style>
			   <tr>
				   <th>Language</th>
			   </tr>
			   <?php
			   if ($result->num_rows > 0)
			   {
				   // output data of each row
				   while($row = $result->fetch_assoc())
				   {
					   //$price = number_format((float)$row["price"], 2, '.', '');
					   echo "<tr> <td width=250>" . $row["name"];
//						   . "</td><td width=120>" . $row["last_name"]
//						   . "</td><td width=150>" . $row["title"]
//						   . "</td><td width=100>" . $row["hiredate"]
//						   . "</td><td width=100>" . $row["department"]."</td></tr>\n\r";
				   }
			   }
			   else
			   {
				   echo "0 results";
			   }
			   ?>
		   </table>
	   </div> <!-- id q1 -->



	   <div id = "filmcatatories" class="page" style="margin-top: 10px;">


		   <?php
		   $sqlfile = file_get_contents("filmcatatories.sql");
		   ?>
		   <pre>

<?php
echo $sqlfile;
?>

</pre>

		   <?php
		   $sql = $sqlfile;

		   #echo "<b>SELECT</b> <i>sid, first, last, birthdate</i>
		   #	  <br><b>FROM</b> <i>student</i><br><br>\n\n\r";
		   // $resultx = $conn->query("TRUNCATE TABLE employee;");
		   // $resultx = $conn->query($sqlfile);
		   //$sql ="SELECT * FROM Grocery_store_products";
		   $result = $conn->query($sqlfile);
		   ?>

		   <table style>
			   <tr>
				   <th>id</th><th>name</th>
			   </tr>
			   <?php
			   if ($result->num_rows > 0)
			   {
				   // output data of each row
				   while($row = $result->fetch_assoc())
				   {
					   //$price = number_format((float)$row["price"], 2, '.', '');
					   echo "<tr> <td width=50>" . $row["category_id"]
						   . "</td><td width=100>" . $row["name"];
//						   . "</td><td width=150>" . $row["title"]
//						   . "</td><td width=100>" . $row["hiredate"]
//						   . "</td><td width=100>" . $row["department"]."</td></tr>\n\r";
				   }
			   }
			   else
			   {
				   echo "0 results";
			   }
			   ?>
		   </table>
	   </div> <!-- id q1 -->



	   <div id = "actorsnamedguiness" class="page" style="margin-top: 10px;">


		   <?php
		   $sqlfile = file_get_contents("actorsnamedguiness.sql");
		   ?>
		   <pre>

<?php
echo $sqlfile;
?>

</pre>

		   <?php
		   $sql = $sqlfile;

		   #echo "<b>SELECT</b> <i>sid, first, last, birthdate</i>
		   #	  <br><b>FROM</b> <i>student</i><br><br>\n\n\r";

		   //$sql ="SELECT * FROM Grocery_store_products";
		   $result = $conn->query("$sqlfile");
		   ?>

		   <table style>
			   <tr>
				   <th>First Name</th><th>Last Name</th>
			   </tr>
			   <?php
			   if ($result->num_rows > 0)
			   {
				   // output data of each row
				   while($row = $result->fetch_assoc())
				   {
					   //$price = number_format((float)$row["price"], 2, '.', '');
					   echo "<tr> <td width=120>" .  $row["first_name"]
						   . "</td><td width=120>" . $row["last_name"]
						   ."</td></tr>\n\r";
				   }
			   }
			   else
			   {
				   echo "0 results";
			   }
			   ?>
		   </table>
	   </div> <!-- id q1 -->




	   <div id = "closesql" class="page" style="margin-top: 10px;">
	   <H3>Closing SQL connection</H3>
	   <?php>
	   	  $sql = "ROLLBACK";
	      $conn->query($sql);
		  mysqli_close($conn);
	   ?>
	</div> <!--id = closesql -->
	 

	 <div id= source class="page" style="margin-top: 10px;">
	  <H2>Assignment Source Code</H2>
		
	  <?php
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

