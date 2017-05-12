<!DOCTYPE html>
<html>
<head>
    <!---->
    <!--        Neal Noble-->
    <!--        Course: IT 328 - Full-Stack Web Development-->
    <!--        Assignment: The sign-up form-->
    <!--        April 2017-->
    <!--        Instructor: Tina Ostrander-->

    <!--bootstraps forms on this page were referenced from https://v4-alpha.getbootstrap.com/components/forms/-->

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">

    <link rel="stylesheet" type="text/css" href="//cdn.datatables.net/1.10.15/css/jquery.dataTables.css">
    <script src="https://cdn.datatables.net/1.10.15/js/jquery.dataTables.js"></script>
    <script src="https://code.jquery.com/jquery-1.12.4.js"></script>


    <link rel="stylesheet" type="text/css" href="../styles/styles.css">
    <link rel="stylesheet" type="text/css" href="../styles/signupstyles.css">
    <link rel="stylesheet" type="text/css" href="./styles/styles.css">
    <link rel="stylesheet" type="text/css" href="./styles/signupstyles.css">
    <link rel="stylesheet" type="text/css" href="http://nnoble.greenrivertech.net/328/signup/styles/styles.css">
    <link rel="stylesheet" type="text/css" href="http://nnoble.greenrivertech.net/328/signup/styles/signupstyles.css">
    <link rel="stylesheet" type="text/css" href="http://nnoble.greenrivertech.net/328/signup/styles/navbar.css">

    <title>Dating profile</title>

    <style>
        .mydefaultfont
        {
            font-family: Arial, serif;
            font-size:10pt;
        }
    </style>
    
    
</head>



<body>

<header class="bgimage">
    <div class="container">

        <form action="/328/signup/profile" method="POST">
        <div class="row">
            <div class="mynavbar"><?=  \DatingSite\Utilities::getAdminLinkHeader() ?></div>
            <div class ="row myDiv2">
            <h2>Personal Information</h2><hr>
            <div class="col-md-7" >


                <div class="form-group row">
                    <label for="FirstName" class="col-1 col-form-label">First Name</label>
                    <div class="col-10">
                        <input class="form-control" type="text" name="firstName" value="<?php echo $_SESSION['dfirstname']; ?>" id="FirstName">
                    </div>
                </div>
                <div class="form-group row">
                    <label for="lastName" class="col-1 col-form-label">Last Name</label>
                    <div class="col-10">
                        <input class="form-control" type="text" name="lastName" value="<?php echo $_SESSION['dlastname']; ?>"  id="lastName">
                    </div>
                </div>
                <div class="form-group row">
                    <label for="age" class="col-1 col-form-label">Age</label>
                    <div class="col-10">
                        <input class="form-control numbersOnly" type="text" name="age" value="<?php echo $_SESSION['dage']; ?>" id="age">
                    </div>
                </div>
                <div class="gender">
                Gender
                    <div class="form-check form-check-inline">
                        <label class="form-check-label">
                            <input class="form-check-input" type="radio" name="gender" id="genderMale" value="male"> Male
                        </label>

                        <label class="form-check form-check-label">
                            <input class="form-check-input" type="radio" name="gender" id="genderFemale" value="female" <?php echo $_SESSION['dgender']; ?>> Female
                        </label>
                    </div>
                </div>

                <div class="form-group row">
                    <label for="phone" class="col-2 col-form-label">Phone Number</label>
                    <div class="col-10">
                        <input class="form-control numbersOnly" type="tel" value="<?php echo $_SESSION['dphone']; ?>" name="phone" id="phone">
                    </div>
                </div>
                <div class="form-group row">
                    <label class="custom-control custom-checkbox">Premium Membership<br>
                        <input type="checkbox" name="membership" class="custom-control-input" <?php echo $_SESSION['dmembership']; ?> value="true">

                        <span class="mydefaultfont">Sign me up for a Premium Account!</span>
                    </label>
                </div>


            </div>
            <div class="col-md-4">
<pre>
<span class="boldText">Note:</span> all information entered is protected
by our <a href="/328/signup/privacy">privacy policy</a>. Profile information
can only be viewed by others with your
permission.
</pre>
                <div class="wrapper infopagenextbutton">
                    <input type="submit" class="bet_time btn btn-primary" value="Next >">
                </div>
            </div>

                </div>

        </div>

        </form>
    </div>
</header>


<script>
//    [0-9\-\(\)\s]+

    $('.numbersOnly').keyup(function () {
        if (this.value != this.value.replace(/[^0-9\.]/g, '')) {
            this.value = this.value.replace (/[^0-9\.]/g, '');
        }
    });

</script>

<SCRIPT>
    $('.phoneNumberFilter').keyup(function () {
        if (this.value != this.value.replace(/[0-9\-\(\)\s]/g, '')) {
            this.value = this.value.replace (/[0-9\-\(\)\s]/g, '');
        }
    });
</SCRIPT>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

</body>
</html>