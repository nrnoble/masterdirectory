<?php

    require_once ('vendor/autoload.php');

    $f3 = Base::instance();
    $f4 = Base::instance();

    $f3->route('GET /', function(){
        echo '<h1> Hello world! <h1>';
        }
    );

    $f4->route ('GET /',function() {

        $view = new View;
        echo $view->render('pages/myfile.html');
        }
    );


    $f4->run();

?>