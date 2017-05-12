<!--
Neal Noble
Feb 8th, 2016
IT305
Assignment 6b
--><?php
$errors = [];
$missing = [];
if (isset($_POST['send']))
{
    $expected = ['name', 'email', 'comments'];
    $required = ['name', 'comments'];
    $to = 'Neal Noble<nrnoble@hotmail.com>';
    $subject = 'Feedback from online form';
    $headers = [];
    $headers[] = 'From: nnoble@greenrivertech.net';
    $headers[] = 'Cc: neal@nrnoble.com, nnoble@greenrivertech.net';
    $headers[] = 'Content-type: text/plain; charset=utf-8';
    #$authorized = '-fdavid@example.com';
     $authorized = '';
    require './includes/process_mail.php';
    if ($mailSent)
    {
        header('Location: thanks.php');
        exit;
    }
}
?><!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/styles.css">
    <link href="styles.css" rel="stylesheet" type="text/css">

    <style type="text/css">

        body
        {
            text-align:justify;
            font-family: courier;
            font-size: 8pt;
            background-color:#4A62E8;
        }

        a:hover
        {
            background-color: yellow;

            color:blue;
            font-size: 14pt;
            font-weight: bold;
        }

        a
        {
            text-decoration: none;

        }

        b
        {
            color:blue;
        }

        th
        {
            text-decoration: underline;

        }

        tr:nth-child(even)
        {
            background-color: #E0E0E0;
        }

        #text
        {
            text-align: left;
            font-size: 8pt;

        }
        div
        {
            font-size: 8pt;
            margin: auto;
        }

        .page
        {
            max-width: 800px;
            font-size: 12pt;
            background-color: #ffffff;
            border: solid;
            border-width: 1px;
            text-align: left;
            margin-top: 10px;
            padding: 10px;
            box-shadow: 5px 5px 5px #0026FF
        }

        #kfb_contactform
        {
            max-width: 800px;
            font-size: 12pt;
            background-color: #ffffff;
            border: solid;
            border-width: 1px;
            text-align: left;
            margin-top: 10px;
            padding: 10px;
            box-shadow: 5px 5px 5px #0026FF
        }
    </style>

     
     <title>Assignment 6b Contact form</title>

</head>


    

<body>
    <section class="container">
        <section class="row">
            <section class="col-xs-12" >
                <div id = assignment class = page style="margin-top: 10px">
                    Neal Noble<br>
                    Feb 8th, 2016<br>
                    IT305<br>
                    Assignment 6b <br>
                </div>

                <div id =kfb_contactform class = "contactform">

            <legend>Select Size</legend>
                <select name="size" id="size">
                    <option value="none">Select a Size</option>
                    <option value="small">Small</option>
                    <option value="medium">Medium</option>
                    <option value="large">Large</option>
                </select>
              
    <div class="col-sm-8">
        <div class="input-group">                                            
            <input type="TextBox" ID="datebox" Class="form-control"></input>
            <div class="input-group-btn">
                <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
                    <span class="caret"></span>
                </button>
                <ul id="demolist" class="dropdown-menu">
                    <li><a href="#">A</a></li>
                    <li><a href="#">B</a></li>
                    <li><a href="#">C</a></li>
                </ul>
            </div>
        </div>
    </div>
            </section>
        </section>
    </section>

</body>
</html>