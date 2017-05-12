<?php
    /*
    Name: Marlene Leano
    Date: April 9, 2017
    Updated: April 23, 2017
    URL: mleano.greenrivertech.net/IT328/dating
    This file routes to the proper web page of my dating website.
    */
    
    //Require autoload
    require_once('vendor/autoload.php');
    
    //Start session
    session_start();    
      
    //Create an instance of the Base class
    $f3 = Base::instance();
    
    //Define a default route
    $f3->route('GET /', function() {
                $view = new View;
                echo $view->render('pages/home.html');
            }
    );
    
    //Route to personal info form
    $f3->route('GET /personal_info',
                function() {
                    $view = new View;
                    echo $view->render('pages/personal_info.html');
           });

    //Route to profile form
    $f3->route('POST /profile',
                function() {
                    /*
                     * Create membership object depending on whether "Premium
                     * Membership" option has been selected or not.
                     */
                    if (isset($_POST['premium-member'])) {
                        $member = new PremiumMember();
                    } else {
                        $member = new Member();
                    }
                    
                    //Set member object's properties
                    $member->setFirstName($_POST['firstname']);
                    $member->setLastName($_POST['lastname']);
                    $member->setAge($_POST['age']);
                    $member->setGender($_POST['gender']);
                    $member->setPhone($_POST['phone']);
                    
                    //Store updated member object into session
                    $_SESSION['member'] = $member;
                     
                     //Create new view and render profile page
                     $view = new View;
                     echo $view->render('./pages/profile.html');
            });
    
    /*
     *  Route to interests form if premium member. Route to profile
     *  summary otherwise.
     */
    $f3->route('POST /member',
                function($f3) {
                    
                    //Retrieve member object from session variable
                    $member = $_SESSION['member'];
                    
                    //Set member object properties
                    $member->setEmail($_POST['email']);
                    $member->setState($_POST['state']);
                    $member->setSeeking($_POST['seeking']);
                    $member->setBio($_POST['biography']);
                    
                    /*
                     * Create new view. If premium member, render the Interests form.
                     * If not, render the profile page.
                     */
                    $view = new View;
                    if (get_class($member) == PremiumMember) {
                        //Store updated member object back into session
                        $_SESSION['member'] = $member;   
                        echo $view->render('pages/interests.html');  
                    } else {
                        echo $view->render('pages/profile_summary.php');
                    }
                });
    
    //Route to profile summary
    $f3->route('POST /profile_summary',
                function($f3) {
                    
                    //Retrieve member object
                    $member = $_SESSION['member'];
                    
                    //Set premium member object's interest properties 
                    $member->setInDoorInterests($_POST['indoor_interests']);
                    $member->setOutDoorInterests($_POST['outdoor_interests']);
                      
                    //Create new view and render profile summary page
                    $view = new View;
                    echo $view->render('pages/profile_summary.php');
                });

    //Run fat free
    $f3->run();