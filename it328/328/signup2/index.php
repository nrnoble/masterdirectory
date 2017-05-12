<?php
/**
 * Neal Noble
 * Course: IT 328 - Full-Stack Web Development
 * Assignment: The sign-up form
 * April 2017
 * Instructor: Tina Ostrander
 */

    //Require autoload
    require_once('vendor/autoload.php');

    //Start the session
    session_start();


    //Create an instance of the Base class
    $f3 = Base::instance();

    //Set debug level
    $f3->set('DEBUG', 2);
    $f3 = Base::instance();

    use \DatingSite\Utilities;


    Utilities::debugOff();
//    $adminPageHeaderLink= "<span><a href='/328/signup/'>My Dating site</a></span><span class='alignright'><a href=/'328/signup/admin'>Adminstrative</a></span>";
 //   $_SESSION ['adminPageHeaderLink'] = $adminPageHeaderLink;
    $MembersDB = new \DatingSite\MembersDB();


/**
     * route to default page to Dating site
     */
    $setDefaults = null;
    $setDefaults = $_GET['defaults'];
    $f3->route ('GET /',
        function($setDefaults) {




           // $MembersDB = new \DatingSite\MembersDB();
           // $insert = 'INSERT I(fname,  lname, age,  gender,  phone,         premium,  email,                 state,  seeking,   bio,   indoor,                                  outdoor,         image)
        //    $MembersDB->addMember("Neal","Noble",33,   "Male",  "555-555-5555",1,        "nrnoble@hotmail.com", "WA",   "Female", "test", "TV Movies reading playing video games", "hiking, biking","images");
         //   $MembersDB->addMember("Neal", "Noble",33,"male", "555-555-5555", 1, "nrnoble@hotmail.com", "WA", "Female", "test", "TV Movies reading playing video games", "hiking, biking","images");


            $setDefaults = null;
            $setDefaults = $_GET['defaults'];
            if ($setDefaults == 1) {
                session_unset();
                $_SESSION['dfirstname'] = "Sarah";
                $_SESSION['dlastname'] = "Smith";
                $_SESSION['dage'] = "30";
                $_SESSION['dgender'] = "checked";
                $_SESSION['dphone'] = "222-333-4445";
                $_SESSION['dmembership'] = "checked";
                $_SESSION['demail'] = "myemail@gmail.com";
                $_SESSION['dstate'] = "Selected='selected'";
                $_SESSION['dseeking'] = "checked";
                $_SESSION['imagePath'] = "http://nnoble.greenrivertech.net/328/signup/images/placeholder.png";
                $_SESSION['indoor interests'] = "checked";
                $_SESSION['outdoor interests'] = "checked";
                $_SESSION['dbio'] = " orum eloquentiam ut sed, usu ut iudico regione. 
                                      Te cum porro sententiae, aeque clita facilisis 
                                      sit et. Cum partem melius detraxit ex, sea et 
                                      graeci scripta adversarium. No pri unum dicit 
                                      vituperatoribus, alterum principes repudiare ad pro.";
                $_SESSION['dchecked'] = "checked";


            }
            else{
                session_unset();
                $_SESSION['dfirstname'] = "";
                $_SESSION['dlastname'] = "";
                $_SESSION['dage'] = "";
                $_SESSION['dgender'] = "";
                $_SESSION['dphone'] = "";
                $_SESSION['dmembership'] = "";
                $_SESSION['demail'] = "";
                $_SESSION['dstate'] = "";
                $_SESSION['dseeking'] = "";
                $_SESSION['indoor interests'] = "";
                $_SESSION['outdoor interests'] = "";
                $_SESSION['dbio'] = "";
                $_SESSION['d'] = "";
                $_SESSION['dchecked'] = "";
                $_SESSION['imagePath'] = "http://nnoble.greenrivertech.net/328/signup/images/placeholder.png";




            }

        $view = new View;
        echo $view->render('/pages/home.php');
    });


    /**
     * route to the second page of site.
     * User enters personal information into online profile from
     */
    $f3->route ('GET /info',function() {
        $view = new View;
        echo $view->render('/pages/info.php');
    });


    /**
     *  Route to the process 'profile' page
     *  Process the POST from from on 'info;
     *  - First Name
     *  - Last Name
     *  - Gender
     *  - Age
     *  - Phone
     *  - Membership
     */
    $f3->route ('GET|POST /profile',
        function() {
            $profile = null;
            $validateAge = false;
            


            if (($_POST['membership']) == "true"){
                $profile = new \DatingSite\PremiumMember($_POST['firstName'],
                    $_POST['lastName'],
                    $_POST['age'],
                    $_POST['gender'],
                    $_POST['phone'],
                    1);
        }
        else {
           $profile = new \DatingSite\Member($_POST['firstName'],
               $_POST['lastName'],
               $_POST['age'],
               $_POST['gender'],
               $_POST['phone'],
               0);
        }

        $_SESSION['profile-data'] = $profile;
        $view = new View;
        echo $view->render('/pages/profile.php');
    });


    /**
     * Route to interest page.
     * Process POST from form on the 'profile' page
     *  - email
     *  - state
     *  - seeking
     *  - bio
     *
     * If the user has checked PremiumMembership, then the next page will
     * be the interest page, otherwise the next page will be the summery
     * page for all non Premium users.
     */
    $f3->route ('GET|POST /interests',
        function($f3) {
            $profile = $_SESSION['profile-data'];
            $profile->setEmail($_POST['email']);
            $profile->setState($_POST['state']);
            $profile->setSeekingGender($_POST['seeking']);
            $profile->setBio($_POST['bio']);
           // $profile->setPremiumMember(1);

            $view = new View;
            if ($profile->getPremiumMember() == 1) {
                echo $view->render('/pages/interests.php');
            }
            else {
                header('Location: /328/signup/summery');
            }
    });


    /**
     * Route to the summery page
     * Display user profile information
     * Create fat free variables
     */
    $f3->route ('POST|GET /summery',
        function($f3) use ($MembersDB) {
            $profile = $_SESSION['profile-data'];
            echo "test" . "<BR>";
            echo "test" . "<BR>";
            echo "test" . "<BR>";
            echo "test" . "<BR>";
            echo "test" . "<BR>";
                print_r($_SERVER);


            if (isset($_SESSION['imagePath']))
            {
                Utilities::debug( "image path is sets: " . $_SESSION['imagePath']);
                Utilities::debug( "profile->getPremiumMember: " . $profile->getPremiumMember());
                if ($profile->getPremiumMember == 1) {
                    Utilities::debug( "is a premium member");
                    if ($profile->getImageLocation() != $_SESSION['imagePath']) {
                        Utilities::debug("Images paths are not equal");
                        $profile->setImageLocation($_SESSION['imagePath']);

                        Utilities::debug('Changing image path to: $_SESSION[\'imagePath\'] =' . $_SESSION['imagePath']);
                    }
                    else
                    {
                        Utilities::debug("Images paths are equal");
                        Utilities::debug("_SESSION['imagePath']: " . $_SESSION['imagePath']);
                    }
                }
            }

            // Set fatfree variables
            $f3->set('firstName', $profile->getFirstName());
            $f3->set('lastName', $profile->getLastName());
            $f3->set('fullName', $profile->getFullName());
            $f3->set('gender', $profile->getGender());
            $f3->set('age', $profile->getAge());
            $f3->set('phone', $profile->getPhone());
            $f3->set('membership', $profile->getPremiumMember());
            $f3->set('email', $profile->getEmail());
            $f3->set('state', $profile->getState());
            $f3->set('seeking', $profile->getSeekingGender());
            $f3->set('bio', $profile->getBio());
            $f3->set('imagePath', $profile->getImageLocation());
            if ($profile->getPremiumMember() == 1) {
                $f3->set('indoorInterests', $profile->inDoorInterestsToString());
                $f3->set('outdoorInterests', $profile->outDoorInterestsToString());
            }
            $indoorInterest = "";
            $outdoorInterest = "";


            if ($profile->getPremiumMember() == 1 && $profile->getinDoorInterests() == null){
                $profile->setinDoorInterests($_POST['indoor']);
            }

            if ($profile->getPremiumMember() == 1 && $profile->getoutDoorInterests() == null){
                $profile->setoutDoorInterests($_POST['outdoor']);
            }



            if ($profile->getPremiumMember() == 1) {
                $f3->set('indoorInterests', $profile->indoorInterestsToString());
                $f3->set('outdoorInterests', $profile->outdoorInterestsToString());
            }


            // check to see if member has been added to DB already. Block refreshing the page from
            // adding the member more than once.

            Utilities::debug( "isset(_SESSION['memberId']:" . isset($_SESSION['memberId']));
            if (!isset ($_SESSION['memberId'])) {
                    if ($profile->getPremiumMember() == 1) {
                    $memberId = $MembersDB->addMember($profile->getFirstName(), $profile->getLastName(), $profile->getAge(), $profile->getGender(), $profile->getPhone(), $profile->getPremiumMember(), $profile->getEmail(), $profile->getState(), $profile->getSeekingGender(), $profile->getBio(), $profile->indoorInterestsToString(), $profile->outdoorInterestsToString(), $profile->getImageLocation());
                    $_SESSION['memberId'] = $memberId;
                        Utilities::debug( "Adding Premium Member:" . $memberId);

                    }
                else
                {
                    $memberId = $MembersDB->addMember($profile->getFirstName(), $profile->getLastName(), $profile->getAge(), $profile->getGender(), $profile->getPhone(), $profile->getPremiumMember(), $profile->getEmail(), $profile->getState(), $profile->getSeekingGender(), $profile->getBio(), null, null, $profile->getImageLocation());
                    $_SESSION['memberId'] = $memberId;
                    Utilities::debug( "Adding standard member:" . $memberId);

                }
            }


            $profile->getImageLocation();
            Utilities::debug(  "isset(SESSION['updateProfile']=" . isset($_SESSION['updateProfile']));
            Utilities::debug(  '$_SESSION["updateProfile"]=' . $_SESSION['updateProfile']);
            Utilities::debug(  '$profile->getImageLocation();=' . $profile->getImageLocation());

            if (isset($_SESSION['updateProfile'])){
                Utilities::debug(  'Updating file location to:' . ($_SESSION['imagePath']));
                $MembersDB->updateImageLocations($_SESSION['imagePath'], $_SESSION['memberId']);
                unset($_SESSION['updateProfile']);
            }

            $view = new View;
            echo $view->render('/pages/summery.php');
        });


    /**
     *  Route to admin page.
     */
    $member = "";
    $f3->route ('GET /admin',
        function() use ($MembersDB,$f3){

            //$memberData = $MembersDB->memberById(71);
            //$f3->set(tableData,$tableData);

//
//            $tableData = $MembersDB->getTableRows();
//
//            $tableRows = "";
//            foreach ($tableData as $row)
//            {
//                $tableRows = $tableRows . $row;
//                //echo $row;
//            }
//
           $f3->set(MembersDB,$MembersDB);


            $view = new View;
            echo $view->render('/pages/admin.php');
            //         print_r($tableRows);
//
//            foreach ($tableData as $row){
//                echo($row['member_id']) . " ";
//                echo($row['fname']) . " ";
//                echo($row['lname']) . " ";
//                echo($row['age']) . " ";
//                echo($row['phone']) . " ";
//                echo($row['email']) . " ";
//                echo($row['state']) . " ";
//                echo($row['gender']) . " ";
//                echo($row['seeking']) . " ";
//                echo($row['premium']) . " ";
//                echo($row['indoor']) . " ";
//                echo($row['outdoor']) . " ";
//                echo "<BR>";
//            }



    });



    /**
     *  Route to privacy page.
     */
    $f3->route ('GET /privacy',
        function() {
            $view = new View;
            echo $view->render('/pages/privacypolicy.php');
        });


    /**
     * route to the 'signupstyles' css file
     */
    $f3->route ('GET /signupstyles',
        function() {
            $view = new View;
            echo $view->render('/styles/signupstyles.css');
    });


    /**
     * route to the 'styles' css file
     */
    $f3->route ('GET /styles/styles',
        function() {
            $view = new View;
            echo $view->render('/styles/styles.css');
        });


    /**
     * route to the 'summery' css file
     */
    $f3->route ('GET /styles/summerycss',
        function() {
            $view = new View;
            echo $view->render('/styles/summery.css');
    });


/**
 * upload profile image.
 * verify size
 * verify type
 * verify duplicate
 */
    $f3->route ('POST|GET /upload',
    function($f3) {

        // Reference. upload script from https://www.w3schools.com/php/php_file_upload.asp
        $profile = $_SESSION['Profile-data'];
        //print_r($_SESSION);
       // $target_dir = $_SERVER['DOCUMENT_ROOT'] ."/328/signup/images/";
        $target_dir = "nnoble.greenrivertech.net" ."/328/signup/images/";
        echo $target_dir . "<BR>";
        //$target_dir = "./images/";

        $imageFileName = $target_dir . basename($_FILES["fileToUpload"]["name"]);
   //     $f3->set(imagePath,$imageFileName);

        $uploadOk = 1;
        $imageFileType = pathinfo($imageFileName,PATHINFO_EXTENSION);
        // Check if image file is a actual image or fake image
        if(isset($_POST["submit"])) {

            if ($_FILES["fileToUpload"]["tmp_name"] == "")
            {
                $uploadOk = 0;
            }
            else {
                $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
            }
            if($check !== false) {
                echo "File is an image - " . $check["mime"] . ".";
                $uploadOk = 1;

            } else {
               echo "File is not an image.";
                $uploadOk = 0;
            }
        }

        // Check if file already exists
        if (file_exists($imageFileName)) {
            echo "Sorry, file already exists.";
            $uploadOk = 0;
            $_SESSION['imagePath'] = $imageFileName;
            $_SESSION['updateProfile']=$imageFileName;
        }
        // Check file size
        if ($_FILES["fileToUpload"]["size"] > 500000) {
            echo "Sorry, your file is too large.";
            $uploadOk = 0;
        }
        // Allow certain file formats
        if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"
            && $imageFileType != "gif" ) {
            echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
            $uploadOk = 0;
        }
        // Check if $uploadOk is set to 0 by an error
        if ($uploadOk == 0) {
            echo "Sorry, your file was not uploaded.";
            // if everything is ok, try to upload file
        } else {
            // target_file
            if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $imageFileName)) {
                echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
                $_SESSION['imagePath'] = $_FILES["fileToUpload"]["tmp_name"]. $imageFileName;
                $_SESSION['updateProfile']=$_FILES["fileToUpload"]["tmp_name"]. $imageFileName;
            }
            else {
        //        echo "Sorry, there was an error uploading your file.";
            }
        }$view = new View;
      echo $view->render('/pages/summery.php');
        header('Location: /328/signup/summery');
        //print_r($imageFileName);
    });

    $f3->run();

?>