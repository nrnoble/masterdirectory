<!DOCTYPE html>
<html>
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
    <!--        State list adopted from open source: https://gist.github.com/RichLogan/9903043                                                          -->
    <!--        how to set Select default from  http://stackoverflow.com/questions/3518002/how-can-i-set-the-default-value-for-an-html-select-element   -->


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
        <div class="mynavbar"><?=  $_SESSION ['adminPageHeaderLink'] ?></div>

            <form action="/328/signup/interests" method="post">

                <div class="row myDiv2">
                        <h2>Profile</h2><hr>
                        <div class="col-md-7" >
                                <div class="form-group row">
                                    <label for="emailID" class="col-1 col-form-label">Email</label>
                                    <div class="col-10">
                                        <input class="form-control" type="email" name="email" value="<?php echo $_SESSION['demail']; ?>" id="emailID">
                                    </div>
                                </div>

                                <div class="form-group row">

                                    <label for="state" class="col-md-1 col-form-label gender">State</label>
                                    <div class="col-10">
                                        <select class="form-control" id="state" name="state" >
                                            <option value="">N/A</option>
                                            <option value="AK">Alaska</option>
                                            <option value="AL">Alabama</option>
                                            <option value="AR">Arkansas</option>
                                            <option value="AZ">Arizona</option>
                                            <option value="CA">California</option>
                                            <option value="CO">Colorado</option>
                                            <option value="CT">Connecticut</option>
                                            <option value="DC">District of Columbia</option>
                                            <option value="DE">Delaware</option>
                                            <option value="FL">Florida</option>
                                            <option value="GA">Georgia</option>
                                            <option value="HI">Hawaii</option>
                                            <option value="IA">Iowa</option>
                                            <option value="ID">Idaho</option>
                                            <option value="IL">Illinois</option>
                                            <option value="IN">Indiana</option>
                                            <option value="KS">Kansas</option>
                                            <option value="KY">Kentucky</option>
                                            <option value="LA">Louisiana</option>
                                            <option value="MA">Massachusetts</option>
                                            <option value="MD">Maryland</option>
                                            <option value="ME">Maine</option>
                                            <option value="MI">Michigan</option>
                                            <option value="MN">Minnesota</option>
                                            <option value="MO">Missouri</option>
                                            <option value="MS">Mississippi</option>
                                            <option value="MT">Montana</option>
                                            <option value="NC">North Carolina</option>
                                            <option value="ND">North Dakota</option>
                                            <option value="NE">Nebraska</option>
                                            <option value="NH">New Hampshire</option>
                                            <option value="NJ">New Jersey</option>
                                            <option value="NM">New Mexico</option>
                                            <option value="NV">Nevada</option>
                                            <option value="NY">New York</option>
                                            <option value="OH">Ohio</option>
                                            <option value="OK">Oklahoma</option>
                                            <option value="OR">Oregon</option>
                                            <option value="PA">Pennsylvania</option>
                                            <option value="PR">Puerto Rico</option>
                                            <option value="RI">Rhode Island</option>
                                            <option value="SC">South Carolina</option>
                                            <option value="SD">South Dakota</option>
                                            <option value="TN">Tennessee</option>
                                            <option value="TX">Texas</option>
                                            <option value="UT">Utah</option>
                                            <option value="VA">Virginia</option>
                                            <option value="VT">Vermont</option>
                                            <option <?php echo $_SESSION['dstate']; ?> value="WA">Washington</option>
                                            <option value="WI">Wisconsin</option>
                                            <option value="WV">West Virginia</option>
                                            <option value="WY">Wyoming</option>
                                        </select>
                                    </div>
                                </div>


                                <div class="gender">
                                    <span class = boldText>Seeking</span>
                                    <div class="form-check-inline">
                                        <label class="form-check-label">
                                            <input class="form-check-input" type="radio" name="seeking" id="SeekingMale" value="male" <?php echo $_SESSION['dseeking']; ?>> Male
                                        </label>

                                        <label class="form-check-label">
                                            <input class="form-check-input" type="radio" name="seeking" id="SeekingFemale" value="female"> Female
                                        </label>
                                    </div>
                                </div>

                        </div>
                        <div class="col-md-4">
                            <div class="form-group">
                  <label for="bio">Biography</label>
                  <textarea class="form-control" name="bio" id="bio" rows="7"><?php echo $_SESSION['dbio']; ?></textarea>
              </div>
                            <div class="wrapper profilepagenextbutton">
                                <input type="submit" class="bet_time btn btn-primary" value="Next >">
                            </div>

                        </div>
                    </div>

            </form>

    </div>

</header>



<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

</body>
</html>