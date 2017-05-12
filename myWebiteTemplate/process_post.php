<?php

    session_start();
    $_SESSION['name'] = $_POST["name"];
    $_SESSION['flavor'] = $_POST["icecream"];
    header("Location: icecream2.php");


?>
