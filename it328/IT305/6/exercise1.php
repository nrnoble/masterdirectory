
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


    <title></title>


</head>



<html>
    <div id="" name="" class="page">Excercise 1</div>
<body>
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


<Div class ="page">
<pre>
Retrieve the following results by writing SELECT statements using aggregate
functions and the GROUP BY clause against the sakila database. 

1. The average movie length of each type of movie rating.
2. The largest Virginia postal code (numerically) found in the address table.
3. The number of movies released each year. This should include the total movie
   and the year listed.
4. A list of all movie titles in the year 1995 as a single string value.
    (Use the GROUP_CONCAT() function).
</pre>
</div>


<div id = "average_minutes" class="page" style="margin-top: 10px;">
    <H3>The average movie length of each type of movie rating</H3>

    <?php
    $G = "SELECT AVG (film.length) FROM film WHERE rating = 'G';";
    $PG = "SELECT AVG (film.length) FROM film WHERE rating = 'PG';";
    $PG13 = "SELECT AVG (film.length) FROM film WHERE rating = 'PG-13';";
    $R = "SELECT AVG (film.length) FROM film WHERE rating = 'R';";
    $NC17 = "SELECT AVG (film.length) FROM film WHERE rating = 'NCG-17';";
    //$sql = "SELECT * FROM film WHERE rating = 'G' LIMIT 10";
     //$sql = "SELECT * FROM film";

    $resultG = $conn->query($G)->fetch_assoc();
    $resultPG = $conn->query($PG)->fetch_assoc();;
    $resultPG13 = $conn->query($PG13)->fetch_assoc();;
    $resultR = $conn->query($R)->fetch_assoc();;
    $resultNC17 = $conn->query($NC17)->fetch_assoc();;

    echo "Average length for <b>G</b> rated films: " .ceil ($resultG['AVG (film.length)'])  ." minutes<BR>";
    echo "Average length for <b>PG</b> rated films: " .ceil ($resultPG['AVG (film.length)'])  ." minutes<BR>";
    echo "Average length for <b>PG13</b> rated films: " . ceil($resultPG13['AVG (film.length)'])  ." minutes<BR>";
    echo "Average length for <b>R</b> rated films: " . ceil($resultR['AVG (film.length)'])  ." minutes<BR>";
    echo "Average length for <b>NC17</b> rated films: " . ceil($resultNC17['AVG (film.length)'])  ." minutes<BR>";
    ?>



    <table style = "display: none">

        <?php

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
			             <td>". $row["rating"]. "</td></tr>\n\r";
            }
        }
        else
        {
            //print_r($result);
            //echo "0 results";
        }

        ?>
    </table>
</div> <!-- id q2 -->

<div id = "max_postal_code" class="page">
    <h3>The largest Virginia postal code found in the address table</h3>
<b><i>
<pre>
 SELECT MAX(postal_code) AS PC
 FROM address
</i></b>
</pre>
    <?php
        $PC = "SELECT MAX(postal_code) AS PC FROM address";
        $resultPC = $conn->query($PC)->fetch_assoc();
        echo "The largest Virginia postal code: <b>" . $resultPC['PC'] ."</b><BR>";
    ?>
</div>


<div id = "moviecount" class="page">
    <h3>The number of movies released each year. This should include the total
        movie and the year listed.</h3>
<i><b>
<pre>
SELECT film.release_year,COUNT(*)
FROM film
GROUP BY film.release_year
FROM address
</b></i>

    <?php
    $sqlmoviecount = "SELECT film.release_year, COUNT(*) FROM film GROUP BY film.release_year";
    $moviecount = $conn->query($sqlmoviecount)
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


</div>



<div id = "concat" class="page">
    <h3>The number of movies released each year. This should include the total
        movie and the year listed.</h3>
<i><b>
<pre>
SELECT film.title,GROUP_CONCAT(film.title)
FROM film
WHERE film.release_year = '1995'
GROUP BY film.release_year;
</b></i>
</pre>
    <?php
    $sqlconcat= "SELECT film.title,GROUP_CONCAT(film.title)FROM film
                      WHERE film.release_year = '1995' GROUP BY film.release_year;";
    //$movieconcat = $conn->query($sqlmoviecount)
    $resultPC = $conn->query($sqlconcat)->fetch_assoc();
    //echo "dump: " .var_dump($resultPC) ."<br>";
    echo "Concat string of movies from 1995: <br><b><i>" . $resultPC["GROUP_CONCAT(film.title)"] ."</i></b><BR>";

    ?>
    <table style = "display: none">

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


</div>




<div id = closesql class="page" style="margin-top: 10px;">
    <H3>Closing SQL connection</H3>
    <?php>
    $sql = "ROLLBACK";
    $conn->query($sql);
    mysqli_close($conn);
    ?>
</div> <!--id = closesql -->

</body>
</html>