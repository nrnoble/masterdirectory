<?php

    require_once ('vendor/autoload.php');

    $f3 = Base::instance();

    $f3->route('GET /language/@lang',
    function ($f3, $params){
        switch ($params['lang'])
        {
            case 'Swahili':
                echo 'Jumbo';
                break;
            case 'English':
                echo 'Hello';
                break;
            default:
                $f3->error(404);
        }
    });


    $f3->route('POST /pets/form1',
        function()
        {
            $view = new View;
            echo $view->render('pages/form1.html');
        });


     $f3->route('POST /pets/form2',
        function() {
            $view = new View;
            echo $view->render('pages/form2.html');
        });
    
        
    $f3->route('POST /pets/results',
        function () {
            $_SESSION['color'] = $_POST['color'];
            $view = new View;
            echo $view->render ('pages/results.html');
        });


    $f3->route('GET /hi',
        function(){
            echo '<h1> Hello world! <h1>';
        }
    );

    $f3->route ('GET /',
        function() {
            $view = new View;
            echo $view->render('files/myfile.html');
        }
    );

    $f3->run();

?>