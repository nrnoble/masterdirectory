<?php
if (isset($_COOKIE["fruit"]))
    $cookie1 = "Your favorite fruit is <b>" . $_COOKIE["fruit"] ."</b>";
  else
      $cookie1 = "I dunno your favorite fruit.";



if (isset($_COOKIE["name"]))
    $cookie2 = "Your name is <b>" . $_COOKIE["name"] ."</b>";
else
    $cookie2 = "It appears you have no name, so I will call you Bob.";




?>
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/styles.css">
    <script src="https://code.jquery.com/jquery-1.10.2.js"></script>

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
            max-width: 900px;
            font-size: 12pt;
            background-color: #ffffff;
            border: solid;
            border-width: 1px;
            text-align: left;
            margin-top: 10px;
            padding: 10px;
            box-shadow: 5px 5px 5px #0026FF
        }

        #page
        {
            max-width: 800px;
            font-size: 12pt;
            background-color: #ffffff;
            border: solid;
            border-width: 1px;
            text-align: left;
            margin-top: 100px;
            padding: 10px;
            box-shadow: 5px 5px 5px #0026FF
        }
    </style>

    <title>305 Assignment</title>

</head>
<body>

<div id="assignmentinfo"  class="page">
    Assn 9a - Cookies 2<br>
    Neal Noble<br>
    IT305<br>
    Feb 2016<br>
</div>


<div id = "validate" class="page">

    <script>
        var url = $(location).attr('href');
        var url1 = "<a href='https://html5.validator.nu/?doc=" + url + "&showsource=yes'  target=\"#mytarget\">Validate this page</a>";
        $('#validate').html(url1);
    </script>


    <script>
        $("https://html5.validator.nu/?doc=http%3A%2F%2Fnnoble.greenrivertech.net%2F9%2Ficecream.php&showsource=yes").load();
    </script>
</div>



<div id= "assignment" class="page">
<?php

echo "$cookie1" ;
echo "<br>";
echo "$cookie2";
?>
</div>


<div id= source class="page" onclick="$(sourcode).toggle();" style="margin-top: 10px;">

    <H2>Click to display source code</H2>

    <div id="sourcode" style="display: none">
        <?php
        highlight_file(__FILE__);
        ?>
    </div>
</div> <!--id = source -->



</body></html>