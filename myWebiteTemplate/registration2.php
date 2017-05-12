<?php session_start(); ?>
<!doctype html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href=".././Bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="../nrnoble.css">
    <!--    <link rel="stylesheet" href="./../css/styles.css">-->
    <script src="http://code.jquery.com/jquery-1.10.2.js"></script>

    <style type="text/css">


    </style>

    <title>Registration/title>
</head>

<body>

<div id="Assignmentinfo" class="page" >
    Exercise 9c - Security<br>
    Neal R. Noble<br>
    IT305<br>
    March 2016<br>
</div>


<div id = "validate" class="page">

    <script>
        var url = $(location).attr('href');
        var url1 = "<a href='https://html5.validator.nu/?doc=" + url + "&showsource=yes'  target=\"#mytarget\">Validate this page</a>";
        $('#validate').html(url1);
    </script>

</div>


<div id = "tryit" class="page" onclick="$(tryitimg).toggle();">
    Click me to show\hide Assignment instructions
    <img id = "tryitimg"  src="tryit_register.png" alt="image" style="max-width: 100%; max-height: 50%; display: none;" >
</div>



<div id = "mytarget">

</div>

<script>

    $("#Assignment").validate
    (
        {
            rules:
            {
                pwd1:
                {
                    required: true,
                    minlength: 6,
                    maxlength: 10

                } ,

                pwd2: {
                    equalTo: "#pwd1",
                    minlength: 6,
                    maxlength: 10
                }


            },
            messages:
            {
                pwd1:
                {
                    required:"the password is required"

                }
            }


        }
    );


</script>

<?php


$email1 = "";
$last_name1 = "";
$first_name1 = "";

session_start();
$first_name = $_SESSION["first_name"] ;
$last_name = $_SESSION["last_name"];
$email = $_SESSION["email"];
$pwd = $_SESSION["pwd"];
#echo "<h2>$email</h2>";
$pwd_err = $_SESSION["pwd_err"];
$first_name_err = $_SESSION["first_name_err"];
$last_name_err = $_SESSION["last_name_err"];
$email_err = $_SESSION["email_err"];


//    if ($first_name =="")
//        {$first_name1 ="*";}
//        if ($last_name =="")
//        {$last_name1 ="*";}
//        if ($email=="")
//        {$email1 ="*" ;}



?>

<div id = "register" class ="page ">

    <form id = "Assignment" action="security_check.php" method="post">
        <table>
            <tbody>
            <tr>
                <td style="text-align: left;">
                    First Name:</td>
                <td><input type="text" name="first_name"   value="<?php echo "$first_name"; ?>"><?php echo "$first_name_err"; ?>
                </td>
            </tr>
            <tr>
                <td style="text-align: left;">
                    Last Name:
                </td>
                <td>
                    <input type="text" name="last_name" value ="<?php echo "$last_name"; ?>"><?php echo "$last_name_err"; ?>
                </td>
            </tr>
            <tr>
                <td style="text-align: left;">
                    Email Address:
                </td>
                <td>
                    <input type="text" name="email" value ="<?php echo "$email"; ?>"><?php echo "$email_err"; ?>
                </td>
            </tr>
            <tr>
                <td style="text-align: left;">
                    Password:
                </td>
                <td>
                    <input id="pwd1" type="password" name="pwd1" value ="<?php echo "$pwd"; ?>" class="form-control"><?php echo " $pwd_err"; ?>
                </td>
            </tr>            <tr>
                <td style="text-align: left;">
                    Confirm Password:
                </td>
                <td>
                    <input id= "pwd2" type="password" name="pwd2" value ="<?php echo "$pwd"; ?>" class="form-control"><?php echo " $pwd_err"; ?>
                </td>
            </tr>

            <tr>
                <td style="background: white; !important;">
                    <?php $_POST['verifyme'] = 'istrue'; ?>
                    <input type="hidden" name="verifyme" id="hiddenField" value="istrue" />
                    <input type="submit" value="Register">
                </td>
                <td>

                </td>
            </tr>
            </tbody>
        </table>
    </form>
</div>



<div id= source class="page" onclick="$(sourcode).toggle();" style="margin-top: 10px;">

    <H2>Click to display source code</H2>

    <div id="sourcode" style="display: none">
        <?php
        highlight_file(__FILE__);
        ?>
    </div>
</div> <!--id = source -->



</body>
</html>
