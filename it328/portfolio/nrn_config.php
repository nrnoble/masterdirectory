<?php
// Check if session has been started, if not then start
if(!isset($_SESSION))
{
    session_start();
}

// Set global session variables.
$isIncluded = $_SESSION["isIncluded"] = true;
$sql_user = $_SESSION["sql_user"] = "nnoble_nrnoble";
$sql_database = $_SESSION["sql_database"] = "nnoble_portfolio";
$sql_password = $_SESSION["sql_password"] = "J\$p1ter2";

//user admin account
$user_admin = $_SESSION["user_admin"] = "admin";
$user_admin_password = $_SESSION["user_admin_password"] = "@dm1n";

// email
$email_subject = $_SESSION["email_subject"] = "Thank you!";
$email_from = $_SESSION["email_from"] =  "nnoble@greenrivertech.net";
#$_session["email_from"] = "kaneses@greenrivertech.net";
$email_cc = $_SESSION["email_cc"] = "neal@nnoble.greenrivertech.net";
$site_HTTP_REFERER = $_SESSION["site_HTTP_REFERER"] = "nnoble.greenrivertech.net";





?>