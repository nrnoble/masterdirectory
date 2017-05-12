<?php
//  Neal Noble
//  Course: IT 328 - Full-Stack Web Development
//  Assignment: Functions and Arrays
//  April 2017
//  Instructor: Tina Ostrander

    require_once ('vendor/autoload.php');

    $f3 = Base::instance();

    $f3->route ('GET /',function() {
        $view = new View;
        echo $view->render('/pages/array-review.php');
        });
        
        
    $f3->route ('GET /stuff/a',function() {
        $view = new View;
        echo $view->render('pages/array-review.php');
    });


    $f3->run();

?>