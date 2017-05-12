<!--
    Name: Marlene Leano
    Date: April 16, 2017
    URL: mleano.greenrivertech.net/IT328/dating/pages/profile_summary.html
    Profile summary for my dating website
-->
<?php
    //Retrieve member object
    $member = $_SESSION['member'];
    
    //Store properties to variables
    $fname = $member->getFirstName();
    $lname = $member->getLastName();
    $name = $fname . ' ' . $lname;
    $age = $member->getAge();
    $gender = $member->getGender();
    $phone = $member->getPhone();
    $email = $member->getEmail();
    $state = $member->getState();
    $seeking = $member->getSeeking();
    $bio = $member->getBio();
    
    //Initialize variables to hold interests
    $indoorInterest = "";
    $outdoorInterest = "";
    
    //If user is a premium member, retrieve interests
    if (get_class($member) == PremiumMember) {
        $indoorInterestArray = $member->getInDoorInterests();
        $outdoorInterestArray = $member->getOutDoorInterests();

        //If user selected indoor interests
        if (!empty($indoorInterestArray)) {
            //Concatenate all indoor interests into as single String variable
            foreach ($indoorInterestArray as $indoor)
            {
                $indoorInterest .= $indoor . " ";
            }
        }
        
        //If user selected outdoor interests
        if (!empty($outdoorInterestArray)) {
            //Concatenate all outdoor interests into as single String variable
            foreach ($outdoorInterestArray as $outdoor)
            {
                $outdoorInterest .= $outdoor . " ";
            }
        }
    }

?>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>My Dating Website</title>
        
        <!--Bootstrap-->
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        
        <!--Link my styles-->
        <link href="./styles/profile_summary_styles.css" rel="stylesheet">       
    </head>
    
    <body>
        <!--The navigation bar-->
        <nav>
            <ul>
                <li><a href="http://mleano.greenrivertech.net/IT328/dating/">My Dating Website</a></li>
            </ul>
        </nav>
        
        <!--Profile Summary Panel-->
        <form action="../dating" method="post">  <!--No action yet as of Assign #3; goes back to home for now-->
            <div class="panel panel-default">
                <div class="panel-body">
                    
                    <!--Profile Summary-->
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-md-6">
                                <ul id="summary" class="list-group">
                                    <li class="list-group-item">Name: <?php echo $name; ?></li>
                                    <li class="list-group-item">Gender: <?php echo $gender; ?></li>
                                    <li class="list-group-item">Age: <?php echo $age; ?></li>
                                    <li class="list-group-item">Phone: <?php echo $phone; ?></li>
                                    <li class="list-group-item">Email: <?php echo $email; ?></li>
                                    <li class="list-group-item">State: <?php echo $state; ?></li>
                                    <li class="list-group-item">Seeking: <?php echo $seeking; ?></li>
                                    <?php
                                        if (get_class($member) == PremiumMember) {
                                            echo "<li class='list-group-item'>Interests: {$indoorInterest} {$outdoorInterest}</li>";
                                        }
                                    ?>
                                </ul>
                            </div> <!--End profile summary-->
                    
                            <!--Picture and Biography-->
                            <div class="col-md-6" id="picandbio">
                                <img src="./images/default_profile_pic.jpg"  class="img-rounded" alt="default profiile icon">
                                <br>
                                <h4>Biography</h4>
                                <p>
                                    <?php echo $bio; ?>
                                </p>
                            </div> <!--End picture & biography-->      
                        </div>
                    </div> <!--End first container-->
                    
                    <!--Contact me button-->
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-md-12" id="button">
                                    <button type="submit" class="btn btn-primary">Contact me!</button>
                            </div>
                        </div>
                    </div> <!--End contact me button-->
                </div> 
            </div> 
        </form> <!--End summary panel-->    
    </body>
</html>