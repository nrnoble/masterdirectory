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
            max-width: 600px;
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
            max-width: 500px;
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

    <title>An excercise in Ice Cream</title>
</head>

<body>

<div id="Assignment" class="page" >
    Exercise 9b - Ice Cream<br>
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


<div id = "assignment" class ="page">
<img src="9bbtryit.png" alt="image" style="max-width: 100%; max-height: 50%" >
</div>



<div id = "mytarget">

</div>


<div class ="page">


        <form action="process_post.php" method="post">
            <table>
                <tbody>
                <tr>
                    <td style="text-align: right;">
                        What is your real name (no lying):</td>
                    <td><input type="text" name="name"     value="Neal">
                    </td>
                </tr>
                <tr>
                    <td style="text-align: right;">
                        Enter your favorite ice cream:
                    </td>
                    <td>
                        <input type="text" name="icecream" value ="Chocolate">
                    </td>
                </tr>
                <tr>
                    <td style="background: white; !important;">
                        <input type="submit" value="Submit">
                    </td>
                    <td>

                    </td>
                </tr>
                </tbody>
            </table>
        </form>
</div>



<div id= source class="page" onclick="$(sourcode).toggle();" style="margin-top: 10px;">

    <H2>Click to display source code</H2>

    <div id="sourcode" style="display: none">
    <?php
    highlight_file(__FILE__);
    ?>
    </div>
</div> <!--id = source -->



</body>
</html>
