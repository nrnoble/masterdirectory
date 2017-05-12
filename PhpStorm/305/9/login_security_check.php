<?php
session_start();
session_regenerate_id();
require './includes/validate.php';
require 'functions.php';


$pwd1  = trim(htmlentities($_POST['pwd1']));
$email = trim(htmlentities($_POST['email']));
$firstname2 = trim(htmlentities($_POST['first_name']));


$_SESSION["first_name"] = $first_name;
$_SESSION["email"] = $email;
$_SESSION["first_name2"] = $firstname2;
$_SESSION["first_name_err"] = "";
$_SESSION["last_name_err"] = "";
$_SESSION["email_err"] = "";
$_SESSION["pwd_err"] = "";

$security_check = true;

$pwd1_hash  = sha1($pwd1);



if($_POST['verifyme'] != 'istrue')
{
    $_SESSION["last_name"] = "";
    die("Sorry no ice cream and cookies for you");
}

if(!strstr($_SERVER['HTTP_REFERER'], "nnoble.greenrivertech.net"))
{
    die("Are you lost?");
}


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

$sql =   "SELECT `email`, `pwdhash` FROM `nnoble_grcc`.`users` WHERE `email` = '" . $email . "'";
//echo "$sql";
//$sql = mysqli_real_escape_string($conn,$sql);

// $sql = $conn->real_escape_string($sql);
$result = @mysqli_query($conn, $sql);
if (!$result)
{
    echo "<h2 style = 'color:red'>";

    echo "<p>Error: " . mysqli_error($conn) . "</p>";

    echo "</h2>";

    return;

    #header("Location: registered_list.php");


}

if ($result->num_rows > 0)
{

    $row = $result->fetch_assoc();
    $pwd2_hash = $row["pwdhash"];
    #echo "$pwd2_hash";
    if ($pwd1_hash == $pwd2_hash)
    {
        $_SESSION["login_test"] = "Login test successful. Hashes match: " . $pwd1_hash;
    }
    else
    {
        $_SESSION["login_test"] = "Login test failed. Hashes do match<BR>PWD=". $pwd1 . "<BR>HASH1: " . $pwd1_hash ."<br>HASH2: " . $pwd2_hash;

    }
}else
{
    $_SESSION["login_test"] = "Unable to find email address in database";
}

header("Location: registered_list.php");