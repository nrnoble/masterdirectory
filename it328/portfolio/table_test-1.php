<?php include "nrn_config.php" ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <!-- Bootstrap core CSS -->
    <link href="bootstrap/css/bootstrap.css" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
    <script src="http://code.jquery.com/ui/1.11.1/jquery-ui.min.js"></script>


    <link rel="stylesheet" type="text/css" href="//cdn.datatables.net/1.10.11/css/jquery.dataTables.css">
    <script type="text/javascript" charset="utf-8" src="http://cdn.datatables.net/1.10.11/js/jquery.dataTables.js"></script>

    <title>datatable test</title>
</head>
<body>
<?php include "nrn_php_functions.php"?>
    <script>
        $(document).ready(function()
        {
            $('#contact_table_id').DataTable();
        } );
    </script>
<!---->

    <script>
        $(document).ready(function()
        {
            $('#example').DataTable();
        } );
    </script>

    <!-- id sqlconnection -->
    <div id=sqlconnection class="pageblock" style="margin-top: 10px; display: ;">

<h2>SQL CONNECTION</h2>
<?php

            // Create connection
            $conn = new mysqli("127.0.0.1", $sql_user, $sql_password,$sql_database );

            // Check connection
            if ($conn->connect_error)
            {
                die("Connection failed: " . $conn->connect_error);
            }

        echo "Connected successfully SQL server: <b>" .gethostname() ."</b><br>";;
        echo 'Current script owner: <b>' . get_current_user() ."</b><br>";
        echo "Connection info: <b>" .$conn->host_info ."</b><br>";

?>

</div>
    <!-- id sqlconnection -->
    

    <!-- Contact List  -->
    <div id = "contact_list_id" class="pageblock1" style=" margin-top: 10px;" >
        <?php

        $filter = "*";
        $filter= $_POST["contact_query"];

        #echo "test: $filter";
        $query = "SELECT `name` as 'Name',`email` as 'Email', `comments` FROM `contacts` "
            . "WHERE `name` LIKE '%$filter%' || `email` LIKE '%$filter%'";
        #echo "test1: $query";

        if ($filter == "*" || $filter == "")
        {
            $query = $query = "SELECT `name` as 'Name',`email` as 'Email', `comments` FROM `contacts`";
        }

        #$query = $sqlfile;

        //$result = $conn->query($query)->fetch_assoc();;
        $result = $conn->query($query);
        //TODO: write a function that create debug block
        ?>
        <div style = "display: none" class ="page11">
            <?php  #echo "var_dump($result->num_rows)"; ?>
        </div>

        <!--put scripts into jsfunctions.php-->
        <script>

            function ShowDetails1(elem)
            {
                var value = $(elem).attr("value");
                var id = $(elem).attr("id");
                //alert(Id);
                value++;
                var rowId = "#row" + value;
                //alert(id + " " +rowId);
                //alert(id + " " +rowId);
                $(rowId).toggle();


            }




            function ShowDetails (e)
            {
                var row = $(e).next("tr");
                $(row).toggle();
//                                e.preventDefault();

            }



        </script>

        
        <table id="example" class="display">


        <?php

            # echo "var dump::  var_dump($result->field_count);";
            $fieldnames = [];

            $fieldnames =  tableHeaderFooter($result);
            //echo (var_dump($result));

            echo "<tbody>";
            if ($result->num_rows > 0)
            {
                // output data of each row

                while($row = $result->fetch_assoc())
                {
                    $rowcount = $rowcount + 1;

                    echo "<tr id =\"row$rowcount\">\r\n"
                        .  "<td>". $row["$fieldnames[0]"]
                        . "</td>\r\n  <td>" . $row["$fieldnames[1]"]
                        . "</td>\r\n  <td>" . $row["$fieldnames[2]"]
//                                        . "</td><td class =\"fkb_datatable\">" . $row["$fieldnames[3]"]
//                                        . "</td><td class =\"fkb_datatable\">" . $row["$fieldnames[4]"]
                        . "</td>\r\n</tr>\n\r";
//                                    class ='kdb_datatable kdb_DataTableDetailedInfo'
//                    $rowcount = $rowcount +1;
//                    echo "<tr id =\"row$rowcount\" style='display:none'>
//<td colspan='$result->field_count'>
//    <div id='contact_id$rowcount' class =''>
//       <ul>
//         <li> <b>$fieldnames[0]:</b> " . $row["$fieldnames[0]"] ."</li>
//         <li> <b>$fieldnames[1]:</b> " . $row["$fieldnames[1]"] ."</li>
//         <li> <b>$fieldnames[2]:</b> " . $row["$fieldnames[2]"] ."</li>
//      </ul>
//    </div>\r\n
//</tr>\n\r\r\n";


                }
                echo "</tbody>\r\n";
            }
            else
            {
                //print_r($result);
                echo "0 results";
            }

            ?>
        </table>
    
    </div>
    <!-- Contact List  -->


    <!--id = closesql -->
    <div id=closesql class="pageblock" style="margin-top: 10px; display:none;">
        <H3>Closing SQL connection</H3>
        <?php
        //$sql = "ROLLBACK";
        //$conn->query($sql);
        mysqli_close($conn);
        echo "<h3> SQL Connection closed </h3>";
        ?>
    </div> <!--id = closesql -->

</body>
</html>