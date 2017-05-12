<?php

# This is called from Admin dialog.
# If login is successful the user will be taken to the Contact list page
# Contact List menu item will appear in menu bar when $_SESSION["access"] == true;
#

if(!isset($_SESSION))
{
   session_start();
}

$id = $_POST['uid'];
$pass1 = $_POST['password'];

$host = 'localhost';
$user = 'root';
$pass = ' ';

$_SESSION["access"] = false;


if ($id == $_SESSION["user_admin"] && $pass1 == $_SESSION["user_admin_password"])
{
   $_SESSION["access"] = true;
   //echo $_SESSION["access"] ;
   $test = $_SESSION['access'];



   //echo "<script>alert('$test')</script>";
   header("Location: nrn_administrative.php");
}
else
{
   $_SESSION["access_err"] =  "Wrong Id Or Password";
   $_SESSION["access"] = false;
  //echo $_SERVER['HTTP_REFERER'];
   header('Location: ' . $_SERVER['HTTP_REFERER']);
   //echo "<script>showpopup();</script>";
   //echo "fail<";
   //echo "user: $id<br>";
   //echo "password: $pass1<br>";
}
?>

