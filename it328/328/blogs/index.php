<?php
/**
 * Neal Noble
 * Course: IT 328 - Full-Stack Web Development
 * Assignment: Blogs
 * May 2017
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


$f3->route ('GET /',
    function() {




        $view = new View;
        echo $view->render('/pages/home.php');
    });


?>

