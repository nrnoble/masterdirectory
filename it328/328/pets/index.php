<? 
session_start();

    require_once ('vendor/autoload.php');

    $f3 = Base::instance();


    $f3->route('GET /test', function(){
        echo '<h1> Hello world! <h1>';
        }
    );


    $f3->route('GET /create',
        function() {
            $view = new View;
            echo $view->render('pages/form1.html');
    });


//    $f3->route('POST /form2',
//        function() {
//            $view = new View;
//            echo $view->render ('pages/form2.html');
//        });


    $f3->route('POST /form2',
        function() {
            
            $p = new  pet();
            $p->setName($_POST['pet-name']);
            $_session['pet']=$p;
            $view = new View;
            echo $view->render ('pages/form2.html');
            print_r($_SESSION);
        });

    $f3->run();


    $f3->route('POST /results',
        function() {

            $p = new  pet();
            $p->setName($_POST['pet-name']);
            $_session['pet']=$p;
            $view = new View;
            echo $view->render ('pages/results.html');
            print_r($_SESSION);
        });



    $f3->route('POST /result',
        function ($f3){

    $p = $_SESSION['pet'];

    $p->setColor($_POST['color']);
    $f3->set('name', $p->getName());
    $f3->set('color', $p->getColor());

    $view = new View;
    echo $view->render('pages/results/html');
    print_r($_SESSION);

        });

    $f3->run();
?>