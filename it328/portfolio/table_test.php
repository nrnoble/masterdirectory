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
    <script type="text/javascript" charset="utf-8" src="//cdn.datatables.net/1.10.11/js/jquery.dataTables.js"></script>

    <title>datatable test</title>
</head>
<body>

    <script>
        $(document).ready(function()
        {
            $('#contact_table_id').DataTable();
        } );
    </script>


    <script>
        $(document).ready(function()
        {
            $('#example').DataTable();
        } );
    </script>

    <!-- id sqlconnection -->
    <div id=sqlconnection class="pageblock" style="margin-top: 10px; display: none ;">

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


    <table id="example" class="display" cellspacing="0" width="100%">

            <thead>
            <tr><th>Name</th><th>Email</th><th>comments</th></tr>
            </thead>

        <tfoot>
        <tr><th>Name</th><th>Email</th><th>comments</th></tr>
        </tfoot>

        <tbody>

        <tr id ="row1"><td>Will</td>
                <td>neal@nrnoble.com</td>
                <td> Mail test</td>
            </tr>

            <tr id ="row3"><td>Neal</td>
                <td>nrnoble@hotmail.com</td>
                <td> asdfasdf</td>
            </tr>

            <tr id ="row5"><td>tina</td>
                <td></td>
                <td> hi</td>
            </tr>

            <tr id ="row7"><td>Tina</td>
                <td>tostrander@greenriver.edu</td>
                <td> Hello, Neal. Please reply when you get this.</td>
            </tr>

            <tr id ="row9"><td>Jimmy</td>
                <td>Calhowen@mail.com</td>
                <td> test</td>
            </tr>

            <tr id ="row11"><td>Jack</td>
                <td>Safari@email.com</td>
                <td> Good day mate!</td>
            </tr>

            <tr id ="row13"><td>Truman</td>
                <td>truman@email.com</td>
                <td>Good morning, and in case I don't see ya, good afternoon, good evening, and good night!</td>
            </tr>

            <tr id ="row15"><td>Mr. Spock</td>
                <td>neal@nrnoble.com</td>
                <td> Mr. Spock at neal@nrnoble.com</td>
            </tr>

            <tr id ="row17"><td>neal</td>
                <td>neal@nnoble.greenrivertech.net</td>
                <td> neal, neal@nnoble.greenrivertech.net</td>
            </tr>

            <tr id ="row19"><td>Neal2</td>
                <td>neal@nrnoble.com</td>
                <td> Neal2, neal@nrnoble.com</td>
            </tr>

            <tr id ="row21"><td>foo8</td>
                <td>nrnoble@hotmail.com</td>
                <td> foo8 at nrnoble@hotmail.com</td>
            </tr>

            <tr id ="row23"><td>neal1</td>
                <td>nrnoble@hotmail.com</td>
                <td> should be working now.</td>
            </tr>

            <tr id ="row25"><td>Tester</td>
                <td>nrnoble@hotmail.com</td>
                <td> Checking to see if data is entered into DB</td>
            </tr>

            <tr id ="row27"><td>Neal</td>
                <td>neal@nrnoble.com</td>
                <td> This is another test</td>
            </tr>
        </tbody>
        </table>


    <div id = closesql class="pageblock" style="margin-top: 10px; display:none;">
        <H3>Closing SQL connection</H3>
        <?php
        //$sql = "ROLLBACK";
        //$conn->query($sql);
        mysqli_close($conn);
        ?>
    </div> <!--id = closesql -->

</body>
</html>