
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <!---->
    <!--        Neal Noble-->
    <!--        Course: IT 328 - Full-Stack Web Development-->
    <!--        Assignment: The sign-up form-->
    <!--        April 2017-->
    <!--        Instructor: Tina Ostrander-->
    <!---->

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="../styles/styles.css">
    <link rel="stylesheet" href="./styles/styles.css">
    <link rel="stylesheet" href="http://nnoble.greenrivertech.net/328/signup/styles/navbar.css">
    <link rel="stylesheet" type="text/css" href="http://nnoble.greenrivertech.net/328/signup/styles/signupstyles.css">

    <title>My Dating Website</title>
    
<style>


</style>

</head>


<body>

<header class="bgimage">
    <div class="container">
        <div class="row">

            <div class="mynavbar"><?=  \DatingSite\Utilities::getAdminLinkHeader() ?></div>

            <div class ="row myDiv2">
                <div class="col-md-6" >
                <h1 class="center">My Dating Website</h1>
                <span>Welcome to the web’s most successful dating website. At <span class="boldText">My Dating Website</span>
                    you meet another like minded individuals. We have the highest success rate of couples on the web.
                    User’s are matched by interest and location. Find out why so many others have found love on our site.</span>
                    <br><br>
                <h3 class="center">Hear what our users are saying about us.</h3>
                <hr>
                    <div class = "HomePageIndent">
                        “I met the love of my life after only a month!” – Andrea<br><br>
                        “It was so easy to set up and profile and start meeting people. I didn’t realize how many others
                        were looking for love in my area.” <br>– John Smith<br><br>
                        “Just try it! You never be the same!” – Sarah
                    </div>
                    <hr>
                    <div class="wrapper">
                        <input type = "button" onclick="location.href = '/328/signup/info'"  class="btn btn-primary" value = "Create a Profile!">
                    </div>
                </div>
                <div class="col-md-6">
                    <img class="dropshadowimg center" src="./images/splash.png" alt="couple">
                </div>
            </div>
        </div>
    </div>
</header>



<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

</body>
</html>