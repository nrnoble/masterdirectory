<?php
    $username  = 'kaneses';
    $password = 'Ru4rea2016';
    $database = "nnoble_grcc;
    $hostname ='localhost';
    $conn = @mysqli_connect ($hostname, $username, $password,$Database)
        or die ("Error connecting to the Database: ". mysqli_connect_error());
        
        echo 'connected to database!';
?>