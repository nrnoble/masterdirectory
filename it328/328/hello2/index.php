<?php

session_start();

//Require autoload
require_once('vendor/autoload.php');

//Create an instance of the Base class
$f3 = Base::instance();

//Set debug level
$f3->set('DEBUG', 3);

//Define a default route
$f3->route('GET /',
           function() {
            echo 'Hello world';
           });

$f3->route('GET /page1',
           function() {
            echo 'This is page 1';
           });

$f3->route('GET /page1/subpage-a',
           function() {
            echo 'This is page 1, Subpage A';
           });

$f3->route('GET /hi/@first/@last',
           function($f3, $params) {
            /*
            echo '<pre>';
            print_r($params);
            echo '</pre>';
            echo 'Hi, '.$params['first']." ".$params['last'];
            */
            $f3->set('firstName', $params['first']);
            $f3->set('lastName', $params['last']);
            $f3->set('message', 'Howdy!');
            
            $view = new View;
            echo $view->render('pages/howdy.html');
           });

$f3->route('GET /language/@lang',
           function($f3, $params) {
                switch($params['lang']) {
                    case 'swahili':
                        echo 'Jumbo!'; break;
                    case 'spanish':
                        echo 'Hola!'; break;
                    case 'farsi':
                        echo 'Salam!'; break;
                    case 'english':
                        $f3->reroute('/');
                    default:
                        $f3->error(404);
                }
           });

$f3->route('GET /pets/form1',
           function() {
                $view = new View;
                echo $view->render('pages/form1.html');
           });

$f3->route('POST /pets/form2',
           function() {
                $_SESSION['animal'] = $_POST['animal'];
                $view = new View;
                echo $view->render('pages/form2.html');
           });

$f3->route('POST /pets/results',
           function() {
                $_SESSION['color'] = $_POST['color'];
                $view = new View;
                echo $view->render('pages/results.html');
           });
           
//Run fat-free
$f3->run();