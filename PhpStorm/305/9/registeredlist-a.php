<?php
session_id('243212');
session_start(); ?>

<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
<!--    <link rel="stylesheet" href=".././Bootstrap/css/bootstrap.min.css">-->
<!--    <link rel="stylesheet" href="//css/styles.css">-->
    <link rel="stylesheet" href="../nrnoble.css">
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
            max-width: 950px;
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
            max-width: 500px;
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

    <title>User List</title>
</head>

<body>


<div class="container">

    <div class="row">
        <section class="col-xs-12" >


            <? include "functions.php" ?>

            <div id = "validate" class="page">

                <script>
                    var url = $(location).attr('href');
                    var url1 = "<a href='https://html5.validator.nu/?doc=" + url + "&showsource=yes'  target=\"#mytarget\">Validate this page</a>";
                    $('#validate').html(url1);
                </script>

            </div>


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


            <div class = "page">
                <?php
               //print_r($_SESSION);
                $firstname = $_SESSION["first_name2"];
                $validate_email = $_SESSION["last_email"];
                $_SESSION["first_name"] = "";
                echo "$firstname, you have successfully been registered" ?>
            </div>


            <!--User List-->
            <div id = "userlist" class="page" style=" margin-top: 10px;"> <!--User List-->
                <H3>User List</H3>
                <?php
                $sqlfile = file_get_contents("user_list.sql");
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
                        $count =0;

                        while($field = $result->fetch_field() )
                        {
                            $count = $count + 1;
                            if ($count <=4)
                            {
                                $fieldnames[] = $field->name;
                                echo "<th  style = \"text-align: left ; width: 250px   \">" . $field->name . "</th>";
                            }
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
                            echo "<tr>
                                      <td  style = \"text-align: left ;\">". $row["$fieldnames[0]"] . "</td>"
			                        ."<td>". $row["$fieldnames[1]"]. "</td>"
                                    ."<td>". $row["$fieldnames[2]"]. "</td>"
                                    ."<td>". $row["$fieldnames[3]"]. "</td>"
                                    ."</tr>\n\r";
                        }
                    }
                    else
                    {
                        //print_r($result);
                        echo "0 results";
                    }

                    ?>
                </table>
            </div>  <!--User List-->



            <div id = closesql class="page" style="margin-top: 10px;">
                <H3>Closing SQL connection</H3>
                <?php>
                $sql = "ROLLBACK";
                $conn->query($sql);
                mysqli_close($conn);
                ?>
            </div> <!--id = closesql -->

            <div id= 'test_Login' class="page" onclick="$(login_formx).toggle();" style="margin-top: 10px;">
                Test Login Credentials
                <form id = "login_form" action="login_security_check.php" method="post" style="display: ">
                    <table>
                        <tbody>

                        <tr>
                            <td style="text-align: left;">
                                Email Address:
                            </td>
                            <td>
                                <input type="text" name="email" value ="<?php echo "$validate_email"; ?>"><?php echo "$email_err"; ?>
                            </td>
                        </tr>

                        <tr>
                            <td style="text-align: left;">
                                Password:
                            </td>
                            <td>
                                <input id="pwd1" type="password" name="pwd1" value ="<?php echo ""; ?>" class="form-control"><?php echo " $pwd_err"; ?>
                            </td>
                        <tr>
                            <td>
                                <?php $_POST['verifyme'] = 'istrue'; ?>
                                <input type="hidden" name="verifyme" id="hiddenField" value="istrue" />
                                <input type="submit" value="Test Login">
                            </td>
                            <td>

                            </td>
                        </tr>

                        </tbody>
                    </table>
                </form>
                <?php
                $result = $_SESSION["login_test"];
                session_destroy();
                echo "$result";
                ?>
            </div>

            <div id= 'source' class="page" onclick="$(sourcode).toggle();" style="margin-top: 10px;">

                <H2>Click to display source code</H2>

                <div id="sourcode" style="display: none ">
                    <?php
                    highlight_file(__FILE__);
                    ?>
                </div>
            </div> <!--id = source -->



        </section>
    </div>


</div>

<script src="js/jquery-2.1.4.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<script src="js/script.js"></script>
</body>
</html>

