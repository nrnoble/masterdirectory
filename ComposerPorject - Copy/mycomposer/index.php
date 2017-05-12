<?php
//always include the composer autoloader when accessing
//class files
require('vendor/autoload.php');

//get router
$f3 = require('vendor/bcosca/fatfree-core/base.php');

//define routes
/*$f3->route('GET /home', function() {
    echo 'Hello world!';
});*/

$f3->route('GET /', 'PracticeController->showHome');
$f3->route('GET /about', 'PracticeController->showAboutUs');
$f3->route('GET /sitemap', 'PracticeController->showSiteMap');

//include a "token" into my route
$f3->route('GET /isPrime/@number', function($f3, $params) {
    $number = intval($params['number']);

    if ($number < 2) {
        //cause a 404
        //$f3->error(404);

        //redirect the userass
        $f3->reroute('/');
    }

    //is this prime?
    $found = false;
    for ($i = $number - 1; $i >= 2; $i--) {
        if ($number % $i == 0) {
            $found = true;
            echo "$number is not prime";
            break;
        }
    }

    if (!$found) {
        //print that the number is prime
        echo "$number is prime";
    }
});

$f3->route('GET /variables', function($f3) {
    //save data to my router for use in my views
    $f3->set('username', 'jarcher');
    $f3->set('password', sha1('password'));

    $f3->set('bookmarks', array('https://www.livecoding.tv/',
        'http://imgur.com/',
        'https://www.udacity.com/'));

    echo Template::instance()->render('views/myview.php');
});

//0 (suppress errors) ... 3 (verbose errors)
$f3->set('DEBUG', 3);

$f3->run();
?>