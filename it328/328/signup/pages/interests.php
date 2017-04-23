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
    <link rel="stylesheet" type="text/css" href="../styles/styles.css">
    <link rel="stylesheet" type="text/css" href="../styles/signupstyles.css">
    <link rel="stylesheet" type="text/css" href="./styles/styles.css">
    <link rel="stylesheet" type="text/css" href="./styles/signupstyles.css">

    <link rel="stylesheet" href="http://nnoble.greenrivertech.net/328/signup/styles/navbar.css">
    <link rel="stylesheet" href="http://nnoble.greenrivertech.net/328/signup/styles/signupstyle.css">

    <title>Dating Profile</title>



    
</head>

<body>

<header class="bgimage">
    <div class="container">
        <div class="mynavbar">My Dating site</div>
        <form action="/328/signup/summery" method="post">
            <div class="row myDiv2">
            <div class="indent row ">
                <h2>Interests</h2><hr>
                <span class="boldText">In-door interests</span><BR>
                <div class="col-md-3" >
                    <label class="custom-control custom-checkbox">
                        <input type="checkbox" name="tv" class="custom-control-input" checked value="tv">
                        <span class="custom-control-indicator"></span>
                        <span class="custom-control-description">tv</span>
                    </label>
               </div>
                <div class="col-md-3" >
                    <label class="custom-control custom-checkbox">
                        <input type="checkbox" name="movies" class="custom-control-input" value="movies">
                        <span class="custom-control-indicator"></span>
                        <span class="custom-control-description">movies</span>
                    </label>
                </div>
                <div class="col-md-3" >
                    <label class="custom-control custom-checkbox">
                        <input type="checkbox" name="cooking" class="custom-control-input" checked value="cooking">
                        <span class="custom-control-indicator"></span>
                        <span class="custom-control-description">cooking</span>
                    </label>
                </div>
                <div class="col-md-3" >
                    <label class="custom-control custom-checkbox">
                        <input type="checkbox" name="boardgames" class="custom-control-input" value="board games">
                        <span class="custom-control-indicator"></span>
                        <span class="custom-control-description">board games</span>
                    </label>
                </div>

                    <div class="col-md-3" >

                        <label class="custom-control custom-checkbox">
                            <input type="checkbox" name="puzzles" class="custom-control-input"  value="puzzles">
                            <span class="custom-control-indicator"></span>
                            <span class="custom-control-description">puzzles</span>
                        </label>
                    </div>
                    <div class="col-md-3" >
                        <label class="custom-control custom-checkbox">
                            <input type="checkbox" name="reading" class="custom-control-input" value="reading">
                            <span class="custom-control-indicator"></span>
                            <span class="custom-control-description">reading</span>
                        </label>
                    </div>

                <div class="col-md-3" >

                    <label class="custom-control custom-checkbox">
                        <input type="checkbox" name="playing card" class="custom-control-input" checked value="playing cards">
                        <span class="custom-control-indicator"></span>
                        <span class="custom-control-description">playing cards</span>
                    </label>
                </div>
                <div class="col-md-3" >
                    <label class="custom-control custom-checkbox">
                        <input type="checkbox" name="video games" class="custom-control-input" checked value="video games">
                        <span class="custom-control-indicator"></span>
                        <span class="custom-control-description">video games</span>
                    </label>
                </div>

                </div>
                
            <div class="indent row">

                <span class="boldText">Out-door interests</span><BR>
                <div class="col-md-3" >
                    <label class="custom-control custom-checkbox">
                        <input type="checkbox" name="hiking" class="custom-control-input" checked value="hiking">
                        <span class="custom-control-indicator"></span>
                        <span class="custom-control-description">hiking</span>
                    </label>
                </div>
                <div class="col-md-3" >
                    <label class="custom-control custom-checkbox">
                        <input type="checkbox" name="biking"  class="custom-control-input" value="biking">
                        <span class="custom-control-indicator"></span>
                        <span class="custom-control-description">biking</span>
                    </label>
                </div>
                <div class="col-md-3" >
                    <label class="custom-control custom-checkbox">
                        <input type="checkbox" name="swimming" class="custom-control-input" checked value="swimming">
                        <span class="custom-control-indicator"></span>
                        <span class="custom-control-description">swimming</span>
                    </label>
                </div>
                <div class="col-md-3" >
                    <label class="custom-control custom-checkbox">
                        <input type="checkbox" name="collecting" class="custom-control-input" value="collecting">
                        <span class="custom-control-indicator"></span>
                        <span class="custom-control-description">collecting</span>
                    </label>
                </div>

                <div class="col-md-3" >

                    <label class="custom-control custom-checkbox">
                        <input type="checkbox" name="walking" class="custom-control-input" checked value="walking">
                        <span class="custom-control-indicator"></span>
                        <span class="custom-control-description">walking</span>
                    </label>
                </div>
                <div class="col-md-3" >
                    <label class="custom-control custom-checkbox">
                        <input type="checkbox" name="climbing" class="custom-control-input" checked value="climbing">
                        <span class="custom-control-indicator"></span>
                        <span class="custom-control-description">climbing</span>
                    </label>
                </div>
            </div>
            <div class="wrapper interestNextButton">
                <input type="submit" class="bet_time btn btn-primary" value = "Next >">
            </div>
            </div>
        </form>

    </div>





<!--                <div class="wrapper nextButton">-->
<!--            <button type="button" class="bet_time btn btn-primary">Next ></button>-->
<!--        </div>-->

</header>



<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

</body>
</html>