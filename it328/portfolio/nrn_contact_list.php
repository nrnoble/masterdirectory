
                    <? include "functions.php" ?>

                    <!-- id sqlconnection -->
                    <div id = sqlconnection class ="pageblock" style="margin-top: 10px; display: none ;">

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

                    </div> <!-- id sqlconnection -->



                    <link rel="stylesheet" type="text/css" href="http://cdn.datatables.net/1.10.11/css/jquery.dataTables.css">
                    <script type="text/javascript" charset="utf-8" src="http://cdn.datatables.net/1.10.11/js/jquery.dataTables.js"></script>

                    <script>
                        $(document).ready(function()
                        {
                            $('#contact_table_id').DataTable();
                        } );
                    </script>


                    <!-- search contacts -->
                    <div id = "div5" class="pageblock" style=" margin-top: 10px; display: none" >

                        <?php
                        $sqlfile = file_get_contents("nrn_contact_list.sql");
                        ?>

                        <div id ="querybox" name="querybox" class="nrn_querybox">

                            <form name="query" method="post" action="">
                                <?php
                                if (isset($_POST))
                                {
                                    if ($_POST['submitquery'] == "Search")
                                    {
                                        $sqlfile = $_POST["textdata"];
                                    }
                                }
                                ?>

                                <!--    File Name: <input type="text" name="filename" value=""><br/>-->
                                <textarea  name="textdata" class = "nrn_queryeditbox"  style ="display:none" ><?php echo "$sqlfile"?></textarea><br/><br>
                                <input type="submit" name="submitquery" value="Search" class="nrn_button" onclick="$('#contact_table').DataTable();">
                                <input type="text" name="sponsor_query" value="*">
                            </form>
                        
                        

                        </div>

                        <p class = 'todo'>TODO: Replace sql query box with a single line query that searches all fields</p>
                        <!--<pre>-->
                        <?php //#echo "$sqlfile"; ?>
                        <!--</pre>-->


                    </div>


                    <!-- Contact List  -->
                    <div id = "div6" class="pageblock" style=" margin-top: 10px;" >
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
                            <?php # echo "var_dump($result->num_rows)"; ?>
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


                        <table id="contact_table_id" class="display">


                            <?php

                            # echo "var dump::  var_dump($result->field_count);";
                            $fieldnames = [];
                            if ($result->field_count > 0)
                            {
                                #echo "<thread>";
                                #echo "<tr>";

                                $th = "<tr>";
                                $count =0;
                                while($field = $result->fetch_field() )
                                {
                                    $count++;
                                    $fieldnames[] = $field->name;

                                    if ($count < 6 )
                                    {
                                        #echo "$field->name \r\n";
                                        $th =  $th . "<th>" . $field->name . "</th>";
                                        #echo "$th";
                                    }
                                }

                                $th = $th . "</tr>";
                                echo "\r\n<thead>" . $th . "</thead>\r\r\n";
                                echo "<tfoot>" . $th . "</tfoot>\r\r\n";
                            }

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

                    </div> <!-- div5 -->


                    <div id = closesql class="pageblock" style="margin-top: 10px; display:none;">
                        <H3>Closing SQL connection</H3>
                        <?php
                        //$sql = "ROLLBACK";
                        //$conn->query($sql);
                        mysqli_close($conn);
                        ?>
                    </div> <!--id = closesql -->

