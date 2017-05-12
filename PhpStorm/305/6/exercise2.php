<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/styles.css">
    <script src="https://code.jquery.com/jquery-1.10.2.js"></script>

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
            max-width: 900px;
            font-size: 12pt;
            background-color: #ffffff;
            border: solid;
            border-width: 1px;
            text-align: left;
            margin-top: 10px;
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

</head>
<body>
<? include "functions.php" ?>

<div id="pagetitle" name="pagetitle" class="page">
Advanced Queries: Excercise 2<br>
Neal Noble<br>
IT301<br>
Feb 2016<br>
</div>



<div id = "sqlconnection" name ="sqlconnection" class ="page" style="margin-top: 10px;">

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




<div class = "page">
    <h3>Assignment: Retrieve the following results by writing joins against the sakila database.</h3>
    Menu Selection:
    <ol>
        <li><a id="1a" href="#">List of all movies with their language</a></li>
        <li><a id="2a" href="#">List of all actors who starred in the movie 'WORLD LEATHERNECKS</a></li>
        <li><a id="3a" href="#">List of all categories for the movie 'UNITED PILOT'</a></li>
        <li><a id="4a" href="#">The first and last name of all customers who placed a rental on 05/25/2005</a></li>
        <li><a id="5a" href="#">The languages of all PG rated movies from the year 2000 as a single string value</a></li>
        <li><a id="6a" href="#">The number of movies released each year. This should include the total movie and the year listed</a></li>
        <li><a id="7a" href="#">The largest Virginia postal code found in the address table</a></li>
    </ol>

</div>


<script>
    $( "<div>" ).hide();
    $( "#1" ).hide();
    $( "#1a" ).click(function( event )
    {
        $( "#div1").show();
        $( "#div2" ).hide();
        $( "#div3" ).hide();
        $( "#div4" ).hide();
        $( "#div5" ).hide();
        $( "#div6" ).hide();
        $( "#div7" ).hide();

        event.preventDefault();

    });

    $( "#2a" ).click(function( event )
    {
        $( "#div2").show();
        $( "#div1" ).hide();
        $( "#div3" ).hide();
        $( "#div4" ).hide();
        $( "#div5" ).hide();

        event.preventDefault();

    });

    $( "#3a" ).click(function( event )
    {
        $( "#div3").show();
        $( "#div1" ).hide();
        $( "#div2" ).hide();
        $( "#div4" ).hide();
        $( "#div5" ).hide();
        $( "#div6" ).hide();
        $( "#div7" ).hide();

        event.preventDefault();

    });

    $( "#4a" ).click(function( event )
    {
        $( "#div4").show();
        $( "#div1" ).hide();
        $( "#div2" ).hide();
        $( "#div3" ).hide();
        $( "#div5" ).hide();
        $( "#div6" ).hide();
        $( "#div7" ).hide();

        event.preventDefault();

    });

    $( "#5a" ).click(function( event )
    {
        $( "#div5").show();
        $( "#div1" ).hide();
        $( "#div2" ).hide();
        $( "#div3" ).hide();
        $( "#div4" ).hide();
        $( "#div6" ).hide();
        $( "#div7" ).hide();

        event.preventDefault();

    });


    $( "#6a" ).click(function( event )
    {
        $( "#div6").show();
        $( "#div1" ).hide();
        $( "#div2" ).hide();
        $( "#div3" ).hide();
        $( "#div4" ).hide();
        $( "#div5" ).hide();
        $( "#div7" ).hide();

        event.preventDefault();

    });


    $( "#7a" ).click(function( event )
    {
        $( "#div7").show();
        $( "#div1" ).hide();
        $( "#div2" ).hide();
        $( "#div3" ).hide();
        $( "#div4" ).hide();
        $( "#div5" ).hide();
        $( "#div6" ).hide();

        event.preventDefault();

    });





</script>

<div id = "1" name="1" class="page" style="display: none; ">

    div 1


</div>


<div id = "2" name="2" class="page" style="display: none;">

    div 2


</div>

<div id = "3" name="3" class="page" style="display: none;">

    div 3

</div>

<div id = "4" name="4" class="page" style="display: none;">

    div 4

</div>

<div id = "5" name="5" class="page" style="display: none;">

    div 5

</div>



<!-- The languages of all PG rated movies from the year 2000 as a single string value.  -->
<div id = "div5" name ="div5" class="page" style="display: none; margin-top: 10px;">
    <H3>The languages of all PG rated movies from the year 2000 as a single string value.</H3>
    <?php
    $sqlfile = file_get_contents("languages2000.sql");
    ?>
    <pre>
<?php
echo $sqlfile;
?>
</pre>

    <?php
    $query = $sqlfile;

    //$result = $conn->query($query)->fetch_assoc();;
    $result = $conn->query($query);
    //TODO: write a function that create debug block
    ?>
    <div style = "display: none" class ="page">
        <?php # echo "var_dump($result->num_rows)"; ?>
    </div>


    <table style = "">

        <?php

        # echo "var dump::  var_dump($result->fetch_field()[0]->name);";
        $fieldnames = [];
        if ($result->field_count > 0)
        {
            echo "<tr>";

            while($field = $result->fetch_field() )
            {
                $fieldnames[] = $field->name;
                echo "<th  style = \"text-align: left ; width: 250px   \">". $field->name . "</th>";
            }
            echo "</tr>";
        }


        //echo (var_dump($result));
        //$row = $result->fetch_assoc();
        //echo var_dump($row);
        // echo $row["AVG (film.length)"];
        if ($result->num_rows > 0)
        {
            // output data of each row
            while($row = $result->fetch_assoc())
            {
                echo "<tr><td  style = \"text-align: left ;\">". $row["$fieldnames[0]"] . "</td>
			             <td>". $row["$fieldnames[1]"]. "</td></tr>\n\r";
            }
        }
        else
        {
            //print_r($result);
            echo "0 results";
        }

        ?>
    </table>
</div> <!-- div5 -->


<!--The first and last name of all customers who placed a rental on 05/25/2005;-->
<div id = "div4" name ="div4" class="page" style="display: none; margin-top: 10px;">
    <H3>The first and last name of all customers who placed a rental on 05/25/2005</H3>
    <?php
    $sqlfile = file_get_contents("rentals.sql");
    ?>
    <pre>
<?php
echo $sqlfile;
?>
</pre>

    <?php
    $query = $sqlfile;

    //$result = $conn->query($query)->fetch_assoc();;
    $result = $conn->query($query);
    //TODO: write a function that create debug block
    ?>
    <div style = "display: none" class ="page">
        <?php # echo "var_dump($result->num_rows)"; ?>
    </div>


    <table style = "">

        <?php

        # echo "var dump::  var_dump($result->fetch_field()[0]->name);";
        $fieldnames = [];
        if ($result->field_count > 0)
        {
            echo "<tr>";

            while($field = $result->fetch_field() )
            {
                $fieldnames[] = $field->name;
                echo "<th  style = \"text-align: left ; width: 250px   \">". $field->name . "</th>";
            }
            echo "</tr>";
        }


        //echo (var_dump($result));
        //$row = $result->fetch_assoc();
        //echo var_dump($row);
        // echo $row["AVG (film.length)"];
        if ($result->num_rows > 0)
        {
            // output data of each row
            while($row = $result->fetch_assoc())
            {
                echo "<tr><td  style = \"text-align: left ;\">". $row["$fieldnames[0]"] . "</td>
			             <td>". $row["$fieldnames[1]"]. "</td></tr>\n\r";
            }
        }
        else
        {
            //print_r($result);
            echo "0 results";
        }

        ?>
    </table>
</div> <!-- div4 -->


<!--List of all categories for the movie 'UNITED PILOT'-->
<div id = "div3" name ="div3" class="page" style="display: none; margin-top: 10px;">
    <H3>List of all categories for the movie 'UNITED PILOT'</H3>
    <?php
    $sqlfile = file_get_contents("catagoriesofunitedpolit.sql");
    ?>
    <pre>
<?php
echo $sqlfile;
?>
</pre>

    <?php
    $query = $sqlfile;

    //$result = $conn->query($query)->fetch_assoc();;
    $result = $conn->query($query);
    //TODO: write a function that create debug block
    ?>
    <div style = "display: none" class ="page">
        <?php # echo "var_dump($result->num_rows)"; ?>
    </div>


    <table style = "">

        <?php

        # echo "var dump::  var_dump($result->fetch_field()[0]->name);";
        $fieldnames = [];
        if ($result->field_count > 0)
        {
            echo "<tr>";

            while($field = $result->fetch_field() )
            {
                $fieldnames[] = $field->name;
                echo "<th  style = \"text-align: left ; width: 250px   \">". $field->name . "</th>";
            }
            echo "</tr>";
        }


        //echo (var_dump($result));
        //$row = $result->fetch_assoc();
        //echo var_dump($row);
        // echo $row["AVG (film.length)"];
        if ($result->num_rows > 0)
        {
            // output data of each row
            while($row = $result->fetch_assoc())
            {
                echo "<tr><td  style = \"text-align: left ;\">". $row["$fieldnames[0]"] . "</td>
			             <td>". $row["$fieldnames[1]"]. "</td></tr>\n\r";
            }
        }
        else
        {
            //print_r($result);
            echo "0 results";
        }

        ?>
    </table>
</div> <!-- div3-->


<!--List of all actors who starred in the movie 'WORLD LEATHERNECKS'-->
<div id = "div2" name ="div2" class="page" style="display: none; margin-top: 10px;">
    <H3>List of all actors who starred in the movie 'WORLD LEATHERNECKS'</H3>
    <?php
    $sqlfile = file_get_contents("wlactor.sql");
    ?>
    <pre>
<?php
echo $sqlfile;
?>
</pre>

    <?php
    $query = $sqlfile;

    //$result = $conn->query($query)->fetch_assoc();;
    $result = $conn->query($query);
    //TODO: write a function that create debug block
    ?>
    <div style = "display: none" class ="page">
        <?php # echo "var_dump($result->num_rows)"; ?>
    </div>


    <table style = "">

        <?php

        # echo "var dump::  var_dump($result->fetch_field()[0]->name);";
        $fieldnames = [];
        if ($result->field_count > 0)
        {
            echo "<tr>";

            while($field = $result->fetch_field() )
            {
                $fieldnames[] = $field->name;
                echo "<th  style = \"text-align: left ; width: 250px   \">". $field->name . "</th>";
            }
            echo "</tr>";
        }


        //echo (var_dump($result));
        //$row = $result->fetch_assoc();
        //echo var_dump($row);
        // echo $row["AVG (film.length)"];
        if ($result->num_rows > 0)
        {
            // output data of each row
            while($row = $result->fetch_assoc())
            {
                echo "<tr><td  style = \"text-align: left ;\">". $row["$fieldnames[0]"] . "</td>
			             <td>". $row["$fieldnames[1]"]. "</td></tr>\n\r";
            }
        }
        else
        {
            //print_r($result);
            echo "0 results";
        }

        ?>
    </table>
</div> <!-- div2 -->


<!--List all movie with their language-->
<div id = "div1" name ="div1" class="page" style="display: none; margin-top: 10px;">
    <H3>List all movie with their language</H3>
    <?php
    $sqlfile = file_get_contents("innerjoinbylangid.sql");
    ?>
    <pre>
<?php
echo $sqlfile;
?>
</pre>

    <?php
    $query = $sqlfile;

    //$result = $conn->query($query)->fetch_assoc();;
    $result = $conn->query($query);
    //echo var_dump($result);

    ?>



    <table style = "">

        <?php


        if ($result->field_count > 0)
        {
            echo "<tr>";
            while($field = $result->fetch_field() )
            {
                echo "<th  style = \"text-align: left ; width: 250px   \">". $field->name . "</th>";

            }
            echo "</tr>";
        }


        //echo (var_dump($result));
        //$row = $result->fetch_assoc();
        //echo var_dump($row);
        // echo $row["AVG (film.length)"];
        if ($result->num_rows > 0)
        {
            // output data of each row
            while($row = $result->fetch_assoc())
            {
                echo "<tr><td  style = \"text-align: left ;\">". $row["title"]. "</td>
			             <td>". $row["name"]. "</td></tr>\n\r";
            }
        }
        else
        {
            //print_r($result);
            echo "0 results";
        }

        ?>
    </table>
</div> <!-- div1 -->



<!--The largest Virginia postal code found in the address table-->
<div id = "div7" name="div7" class="page" style = "display: none;">
    <h3>The largest Virginia postal code found in the address table</h3>

    <b><i>
<pre>
 SELECT MAX(postal_code) AS PC
 FROM address
</pre>
        </i></b>


    <?php
    $PC = "SELECT MAX(postal_code) AS PC FROM address";
    $resultPC = $conn->query($PC)->fetch_assoc();
    echo "The largest Virginia postal code: <b>" . $resultPC['PC'] ."</b><BR>";
    ?>
</div><!--div7 -->

<!--The number of movies released each year. This should include the total movie and the year listed. -->
<div id = "div6" name="div6" class="page" style = "display: none;">
    <h3>The number of movies released each year. This should include the total movie and the year listed.</h3>
    <i><b>
<pre>
SELECT film.release_year,COUNT(*)
FROM film
GROUP BY film.release_year
FROM address
        </b></i>

    <?php
    $sqlmoviecount = "SELECT film.release_year, COUNT(*) FROM film GROUP BY film.release_year";
    $moviecount = $conn->query($sqlmoviecount);
    //$resultPC = $conn->query($sqlmoviecount)->fetch_assoc();
    //echo "The largest Virginia postal code: <b>" . $resultPC['COUNT(*)'] ."</b><BR>";
    ?>

    <table>

        <tr><th style = "width: 100px; text-align: left">Year</th><th>Movie Count</th></tr>

        <?php

        //echo (var_dump($result));
        //$row = $result->fetch_assoc();
        //echo var_dump($row);
        // echo $row["AVG (film.length)"];


        if ($moviecount->num_rows > 0)
        {
            // output data of each row
            while($row = $moviecount->fetch_assoc())
            {
                echo "<tr><td  style = \"text-align: left ;\">". $row["release_year"]. "</td>
			             <td>". $row["COUNT(*)"]. "</td></tr>\n\r";
            }
        }
        else
        {
            //print_r($result);
            echo "0 results";
        }

        ?>
    </table>


</div><!-- div6 -->


<div id = closesql class="page" style="margin-top: 10px;">
    <H3>Closing SQL connection</H3>
    <?php
    $sql = "ROLLBACK";
    $conn->query($sql);
    mysqli_close($conn);
    ?>
</div> <!--id = closesql -->




</body>
</html>