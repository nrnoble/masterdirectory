<?php
    session_start();
    require './includes/validate.php';
    require 'functions.php';


    $first_name  = trim(htmlentities($_POST['first_name']));
    $last_name  = trim(htmlentities($_POST['last_name']));
    $email = trim(htmlentities($_POST['email']));
    $pwd1 = trim(htmlentities($_POST['pwd1']));
    $pwd2 = trim(htmlentities($_POST['pwd2']));

    $_SESSION["first_name2"] = $first_name;
    $_SESSION["first_name"] = $first_name;
    $_SESSION["last_name"] = $last_name;
    $_SESSION["email"] = $email;

    $_SESSION["first_name_err"] = "";
    $_SESSION["last_name_err"] = "";
    $_SESSION["email_err"] = "";
    $_SESSION["pwd_err"] = "";

    $security_check = true;

//    if ($first_name == "" || $last_name == "" || $email == "" || $pwd1 == "")
//    {
//        header("Location: register.php");
//        return;
//    }

    if($_POST['verifyme'] != 'istrue')
    {

        die("Sorry no ice cream and cookies for you");
    }

    if(!strstr($_SERVER['HTTP_REFERER'], "nnoble.greenrivertech.net"))
    {
        die("Are you lost?");
    }



   if (ctype_alpha ($first_name) == false || $first_name == "")
   {
       $security_check = false;
       $_SESSION["first_name_err"] = " <-- Must be A-Z";

   }


    if (ctype_alpha ($last_name) == false  || $last_name == "")
    {
        $security_check = false;
        $_SESSION["last_name_err"] = " <-- Must be A-Z";
    }







    $blankpwd_hash = sha1("");

    $pwd1_hash  = sha1($pwd1);
    $pwd2_hash  = sha1($pwd2);



    if ($pwd1 == "" || $pwd2 == "")
    {
        $security_check = false;
        $_SESSION["pwd_err"] = " Passwords can not be blank";
    }
    elseif ($pwd1_hash  != $pwd2_hash)
    {
        $security_check = false;
        $_SESSION["pwd_err"] = " Passwords do not match";

        #die("Sorry your passwords do not match");
    }
    else
    {
        $_SESSION["pwd"] = $pwd1;
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



    if (strpos($email, '@') == false || $email == "")
    {
        $security_check = false;
        $_SESSION["email_err"] = " must unclude '@'";
        //$_SESSION["email"] = "";
    }
    else
    {
        $email1 = mysqli_real_escape_string($conn, $email);

        $sql = "SELECT `email` FROM `nnoble_grcc`.`users` WHERE `email` = '" . $email . "'";

        $result = @mysqli_query($conn, $sql);
        if (!$result) {
            echo "<h2 style = 'color:red'>";
            echo "hash: $pwd1_hash<br>";
            echo "SQL: $sql<br>";
            echo "user: $username<br>";
            echo "user: $password<br>";
            echo "<p>Error: " . mysqli_error($conn) . "</p>";
            print_r($_POST);
            echo "</h2>";

            return;

        }


        if ($result->num_rows > 0)
        {
            $security_check = false;
            //echo "$result->num_rows ";
            $_SESSION["email_err"] = " email address already in use";
        }
        else
        {
//            $_SESSION["email_err"] = " invalid email address";
        }
    }

    if($security_check == false)
    {
        header("Location: register.php");
        return;
    }


    //
    $_SESSION["first_name"] = "";
    $_SESSION["last_name"] = "";
    $_SESSION["email"] = "";
    $_SESSION["pwd"] = "";


    $_SESSION["last_email"] = $email;
    $_SESSION["login_test"] = "";
    $_SESSION["first_name2"] = $first_name;

    $first_name = mysqli_real_escape_string($conn, $first_name);
    $last_name = mysqli_real_escape_string($conn, $last_name);
    $email = mysqli_real_escape_string($conn, $email);
    $pwd1_hash = mysqli_real_escape_string($conn, $pwd1_hash);



    $sql =   "INSERT INTO `nnoble_grcc`.`users` (`first_name`, `last_name`, `email`, `pwdhash`) VALUES ('" . $first_name . "', '" . $last_name . "', '" . $email ."', '" . $pwd1_hash . "')";


    $result = @mysqli_query($conn, $sql);
    if (!$result)
    {
        echo "<h2 style = 'color:red'>";
        echo "hash: $pwd1_hash";

        echo "<p>Error: " . mysqli_error($conn) . "</p>";
        print_r($_POST);
        echo "</h2>";

        return;

        header("Location: registered_list.php");


}
$email ="";
header("Location: registered_list.php");
?>