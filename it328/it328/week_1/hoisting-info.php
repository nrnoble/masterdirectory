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
    <base href="./bootstrap-switch-master">
    <meta charset="UTF-8">

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/styles.css">
    <link href="styles.css" rel="stylesheet" type="text/css">


   <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Turn checkboxes and radio buttons into toggle switches.">
    <meta name="author" content="Mattia Larentis, Emanuele Marchi and Peter Stein">
    <title>Bootstrap Switch · Turn checkboxes and radio buttons into toggle switches</title>
    <link href="docs/css/bootstrap.min.css" rel="stylesheet">
    <link href="docs/css/highlight.css" rel="stylesheet">
    <link href="dist/css/bootstrap3/bootstrap-switch.css" rel="stylesheet">
    <link href="http://getbootstrap.com/assets/css/docs.min.css" rel="stylesheet">
    <link href="docs/css/main.css" rel="stylesheet">
    <script>
      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-43092768-1']);
      _gaq.push(['_trackPageview']);
      (function () {
        var ga = document.createElement('script');
        ga.type = 'text/javascript';
        ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(ga, s);
      })();
    </script>






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

     
  

</head>


    

<body>
    
    
    <section class="container">
        <section class="row">
            <section class="col-xs-12" >
                <div id = assignment class = page style="margin-top: 10px">
                    Neal Noble<br>
                    March 2016<br>
                    IT301<br>
                    Exercises - Client/Server Programming  <br>
                </div>

                <div id = assignment class = page style="margin-top: 10px">




                    <body lang=en-US style='font-family:Calibri;font-size:11.0pt'>

                    <div style='direction:ltr;border-width:100%'>

                        <div style='direction:ltr;margin-top:0in;margin-left:0in;width:6.109in'>

                            <div style='direction:ltr;margin-top:0in;margin-left:0in;width:.5631in'>

                                <p style='margin:0in;font-family:"Calibri Light";font-size:20.0pt'>&nbsp;</p>

                            </div>

                            <?php
                            include "hoisting_info_include.php";
                            ?>

                        </div>

                    </div>






                </div>


                <div id = assignment class = page style="margin-top: 10px">

                 <h3>block of text goes here</h3>
                </div>

                <div id = assignment class = page style="margin-top: 10px">

                 <h3>block of text goes here</h3>
                </div>

            
            
            </section>
        </section>
    </section>




    <script src="docs/js/jquery.min.js"></script>
    <script src="docs/js/bootstrap.min.js"></script>
    <script src="docs/js/highlight.js"></script>
    <script src="dist/js/bootstrap-switch.js"></script>
    <script src="docs/js/main.js"></script>



</body>
</html>