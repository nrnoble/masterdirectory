<?php
error_reporting(E_ALL);

//composer autoloader
require('vendor/autoload.php');

$f3 = require('vendor/bcosca/fatfree-core/base.php');

$f3->route('GET /viewAllBlogs/@username', function($f3, $params) {
    $controller = new BlogController($f3);
    $controller->viewAllBlogs($params['username']);
});

$f3->route('GET /viewBlog/@blogId', function($f3, $params) {
    $controller = new BlogController($f3);
    $controller->viewBlog($params['blogId']);
});

//raise the debug level and create a custom error handler
//0 (stack trace suppressed) to 3 (most verbose with class and function call logs).
$f3->set('DEBUG',3);
$f3->set('ONERROR', function($f3) {
    echo 'Error text: '.$f3->get('ERROR.text').'<br>';
    echo 'Stack trace: '.$f3->get('ERROR.trace').'<br>';
});

$f3->run();

exit();
?>
