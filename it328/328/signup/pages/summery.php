<?php
$_SESSION['interests-data'] = $_POST;

$myName = $_SESSION['name'];
$flavor = $_SESSION['flavor'];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

    <!---->
    <!--        Neal Noble                                                                                                                              -->
    <!--        Course: IT 328 - Full-Stack Web Development                                                                                             -->
    <!--        Assignment: The sign-up form                                                                                                            -->
    <!--        April 2017                                                                                                                              -->
    <!--        Instructor: Tina Ostrander                                                                                                              -->
    <!--                                                                                                                                                -->
    <!--        Bootstraps forms on this page were referenced from https://v4-alpha.getbootstrap.com/components/forms/                                  -->

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
    <link rel="stylesheet" type="text/css" href="http://nnoble.greenrivertech.net/328/signup/styles/signupstyles.css">
    <link rel="stylesheet" type="text/css" href="http://nnoble.greenrivertech.net/328/signup/styles/styles.css">
    <link rel="stylesheet" type="text/css" href="http://nnoble.greenrivertech.net/328/signup/styles/summery.css">
    <link rel="stylesheet" href="http://nnoble.greenrivertech.net/328/signup/styles/navbar.css">

    <title>Dating Summery</title>

</head>

<body>

<header class="bgimage">
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="mynavbar">My Dating site</div>
                    <div class="row myDiv2">
                        <div class="col-md-5" >
                        <br>
                            <?php if( $membership == "true") : ?>
                            <div class="box1">
                                <div class="myborder notopborder">Name: <?= $fullName ?></div>
                                <div class="myborder">Gender: <?= $gender ?></div>
                                <div class="myborder">Age: <?= $age ?></div>
                                <div class="myborder">Phone: <?= $phone ?></div>
                                <div class="myborder">Email: <?= $email ?></div>
                                <div class="myborder">State: <?= $state ?></div>
                                <div class="myborder">Seeking: <?= $seeking ?></div>
                                <div class="myborder nobottomborder">Interests:  </div>
                            </div>
                            <?php else : ?>
                            <div class="box1">
                                <div class="myborder notopborder">Name: <?= $fullName ?></div>
                                <div class="myborder">Gender: <?= $gender ?></div>
                                <div class="myborder">Age: <?= $age ?></div>
                                <div class="myborder">Phone: <?= $phone ?></div>
                                <div class="myborder">Email: <?= $email ?></div>
                                <div class="myborder">State: <?= $state ?></div>
                                <div class="myborder nobottomborder">Seeking: <?= $seeking ?></div>
                            </div>
                            <?php endif; ?>

                        </div>
                        <div class="indent col-md-5" >
                            <img src="http://nnoble.greenrivertech.net/328/signup/images/placeholder.png" alt="placeholder">
                            <span class="boldText">Biography</span>
                            <div >
                                <?= $_SESSION['bio'] ?>
                            </div>
                        </div>
                        <br>
                        <div class="row">
                            <div class="col-md-12">
                                <div class="mycenter">
                                    <button type="button" class=" btn btn-primary">Contact Me!</button>
                                </div>
                            </div>
                        </div>
                    </div>

            </div>
        </div>
    </div>

</header>



<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

</body>
</html>