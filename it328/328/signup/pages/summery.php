<?php session_start();?>
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
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
                                <div class="myborder nobottomborder">
                                    Interests
                                    <div class="indent">
                                        <span class="underline">Indoor</span>: <?= $indoorInterests ?><br>
                                        <span class="underline">Outdoor</span>: <?= $outdoorInterests ?>
                                    </div>
                                </div>
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
                        <div class="HomePageIndent col-md-5" >
                            <?php if( $membership == "true") : ?>
                                <img src=" <?= $imagePath ?>" alt="placeholder">
                                <form action="/328/signup/upload" method="post" enctype="multipart/form-data">
                                    <label class="control-label">Change your profile picture</label>
                                    <input type="file" name="fileToUpload" id="fileToUpload" class="btn btn-primary inline">
                                    <input type="submit" id="idimageSummit" class="inline btn btn-primary" value="Upload Image" name="submit">
                                </form>
                            <?php else : ?>
                                <img src="http://nnoble.greenrivertech.net/328/signup/images/placeholder.png" alt="placeholder">
                            <?php endif; ?>
                            <span class="boldText">Biography</span>
                            <div >
                                <?= $bio ?>
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