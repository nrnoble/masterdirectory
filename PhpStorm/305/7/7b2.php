<?php

$name = "";
$lastname = "";
$errorMsg = "";
$gpa = "";
$sid = "";
$errorMessages = [];
$errors = [];
$missing = [];
//Create a boolean flag to track validation error
$isValid = false;


    /* Neal Noble
     * IT305
     * Assignment 7b
     * http://nnoble.greenrivertech.net/7/7b.php
     * Add a new student to the GRCC database
     */

    //Turn on error reporting
    ini_set('display_errors', 1);
    error_reporting(E_ALL);

    // Connection to DB occurs after the form data has been validated
    // this reduces SQL connections left open due to validation
    // errors that can lead to SQL error of "Too many open connections"

require './includes/validate.php';

if (isset($_POST['submit']))
{

 
    //Create a boolean flag to track validation error
    $isValid = true;

    //Check first name
    if (validName($_POST['name']))
    {
        $name = $_POST['name'];
    }
    else
    {
        $errorMessages[] = "<p>Invalid first name.</p>";
        $isValid = false;
    }

    //Check last name
    if (validLastName($_POST['lastname']))
    {
        $lastname = $_POST['lastname'];
    } else
    {
        $errorMessages[] = "<p>Invalid last name.</p>";
        $isValid = false;
    }


    //Check last name
    if (validSid($_POST['sid']))
    {
        $sid = $_POST['sid'];
    } else
    {
        $errorMessages[] = "<p>Invalid Student ID</p>";
        $isValid = false;
    }


    //Check last name
    if (validGpa($_POST['gpa']))
    {
        $gpa = $_POST['gpa'];
    } else
    {
        $errorMessages[] = "<p>Invalid GPA</p>";
        $isValid = false;
    }





}
?>




<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/styles.css">
    <link href="styles.css" rel="stylesheet" type="text/css">

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
            margin-top: 10px;
            padding: 10px;
            box-shadow: 5px 5px 5px #0026FF
        }

        #kfb_contactform
        {
            max-width: 800px;
            font-size: 12pt;
            background-color: #ffffff;
            border: solid;
            border-width: 1px;
            text-align: left;
            margin-top: 10px;
            padding: 10px;
            box-shadow: 5px 5px 5px #0026FF;
        }
    </style>

     
     <title>Assignment 7b Contact form</title>

</head>


    

<body>
    <section class="container">
        <section class="row">
            <section class="col-xs-12" >
                <div id = assignment class = page style="margin-top: 10px">
                     Neal Noble<br>
                     Feb 15th, 2016<br>
                     IT305<br>
                     Assignment 7b<br>
                </div>

<? include "functions.php" ?>





    <div id="validateHTML5"  class = 'page' style="margin-top: 10px">
      <a href = "https://html5.validator.nu/?doc=http%3A%2F%2Fnnoble.greenrivertech.net%2F7%2F7b.php">
        Validate this HTML5 page</a>
    </div>


    <div id = "tryit" class = 'page' style="margin-top: 10px">
      <span style ="color:red; font-family: Arial; font-size:50px">Try It Again!!</span>

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




                <div class ="page">

                    <h1>Student Entry Form</h1>


                    <?php if ($_POST && (!$isValid)) : ?>


                        <p class="warning">Please fix the item(s) indicated </p>
                        <div  style = "color:red; padding-left: 50px">
                            <p><ul style = "color:red">
                                <?php

                                foreach ($errorMessages as $value)
                                    echo "<li> $value</li>";

                                ?>
                            </ul></p></div>


                    <?php endif; ?>




                    <form method="post" action="<?= $_SERVER['PHP_SELF']; ?>">

                        <table>
                            <th>SID</th>
                            <th>First Name</th>
                            <th>Last Name</th>
                            <th>GPA</th>
                            <tr>



                            <tr>

                                <td>
                                    <input name="sid" id="sid" style = "width: 100px;"
                                        <?php
                                        // echo 'value="' . htmlentities($sid) . '"';
                                        //                              if ($errors || $missing)
                                        //                              {
                                        //                                  echo htmlentities($sid);
                                        //                              }
                                        //
                                        //                              ?>
                                        >

                                </td>

                                <td>
                                    <input type="text" name="name" id="name" style = "width: 200px;"
                                        <?php
                                        echo 'value="' . htmlentities($name) . '"';
                                        if ($errors || $missing)
                                        {
                                            echo 'value="' . htmlentities($name) . '"';
                                        }
                                        ?>
                                        >
                                </td>

                                <td>
                                    <input type="lastname" name="lastname" id="lastname" style = "width: 200px;"
                                        <?php
                                        echo 'value="' . htmlentities($lastname) . '"';

                                        if ($errors || $missing)
                                        {
                                            echo 'value="' . htmlentities($lastname) . '"';
                                        }
                                        ?>
                                        >
                                </td>

                                <td>
                                    <input name="gpa" id="gpa" style = "width: 100px;"
                                        <?php
                                        echo 'value="' . htmlentities($gpa) . '"';
                                        //                              if ($errors || $missing)
                                        //                              {
                                        //                                  echo htmlentities($gpa);
                                        //                              }
                                        //
                                        //                              ?>
                                        >

                            </tr>

                        </table>
                        <p>
                            <input type="submit" name="submit" id="submit" value="submit">
                        </p>
                    </form>
                </div>




                <div class ="page">

                    <h1>Student Entry Form</h1>


                    <?php if ($_POST && (!$isValid)) : ?>


                        <p class="warning">Please fix the item(s) indicated </p>
                        <div  style = "color:red; padding-left: 50px">
                            <p><ul style = "color:red">
                                <?php

                                foreach ($errorMessages as $value)
                                    echo "<li> $value</li>";

                                ?>
                            </ul></p></div>


                    <?php endif; ?>




                    <form method="post" action="<?= $_SERVER['PHP_SELF']; ?>">

                        <table>
                            <th>SID</th>
                            <th>First Name</th>
                            <th>Last Name</th>
                            <th>GPA</th>
                            <tr>



                            <tr>

                                <td>
                                    <input name="sid" id="sid" style = "width: 100px;"
                                        <?php
                                        echo 'value="' . htmlentities($sid) . '"';
                                        //                              if ($errors || $missing)
                                        //                              {
                                        //                                  echo htmlentities($sid);
                                        //                              }
                                        //
                                        //                              ?>
                                        >

                                </td>

                                <td>
                                    <input type="text" name="name" id="name" style = "width: 200px;"
                                        <?php
                                         echo 'value="' . htmlentities($name) . '"';
                                        if ($errors || $missing)
                                        {
                                            echo 'value="' . htmlentities($name) . '"';
                                        }
                                        ?>
                                    >
                                </td>

                                <td>
                                    <input type="lastname" name="lastname" id="lastname" style = "width: 200px;"
                                        <?php
                                        echo 'value="' . htmlentities($lastname) . '"';

                                        if ($errors || $missing)
                                        {
                                            echo 'value="' . htmlentities($lastname) . '"';
                                        }
                                        ?>
                                        >
                                </td>

                                <td>
                                <input name="gpa" id="gpa" style = "width: 100px;"
                                    <?php
                                    echo 'value="' . htmlentities($gpa) . '"';
    //                              if ($errors || $missing)
    //                              {
    //                                  echo htmlentities($gpa);
    //                              }
    //
    //                              ?>
                                >

                            </tr>

                        </table>
                        <p>
                            <input type="submit" name="submit" id="submit" value="submit">
                        </p>
                    </form>
                </div>


                <?php if ($isValid) : ?>
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
                <?PHP ENDIF ?>


                <?php

                // Display summary
                if ($isValid)
                {
                echo "<span class = \"response\" style = \"text-align:center; \">";
                echo "<div class = 'page' >";
                    echo "<h3>Student has been entered into the database</h3>";
                echo "</div>";

                echo "</span>";
                //We're done! Terminate the script.



                }
                ?>



                <?php if ($isValid) : ?>
                <div id = closesql class="page" style="margin-top: 10px;">
                    <H3>Closing SQL connection</H3>
                    <?php
                    $sql = "ROLLBACK";
                    $conn->query($sql);
                    mysqli_close($conn);
                    ?>
                </div> <!--id = closesql -->
                <?php ENDIF ?>

                <?php if ($isValid) : ?>
                <div id= source class="page" style="margin-top: 10px;">
                    <H2>Assignment Source Code</H2>

                    <?php>
                    highlight_file(__FILE__);
                    ?>

                </div> <!--id = source -->
                <?php ENDIF ?>
            </section>
        </section>
    </section>

</body>
</html>