<?php
if (!empty($_POST["fruit"]))
{
    //make persistent cookie for one day
    setcookie("fruit",$_POST["fruit"], mktime()+60*60*24);
}

if (!empty($_POST["name"]))
{
    //make persistent cookie for one day
    setcookie("name",$_POST["name"], mktime()+60*60*24);
}

//redirect
header("Location: showFruit.php");
?>





<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>

</body>
</html>