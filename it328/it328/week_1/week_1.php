<!--
Neal Noble
March 30th, 2016
IT328
Assignment introduction to Javascript
-->
<!doctype html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
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
    <script src="tv_show.js"></script>
    <script src="buttons.js"></script>

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

        ol
        {
            padding: 5px;
            padding-left: 20px;
            margin-top: 0px;
            margin: 10 px;
        }

        th
        {
            text-decoration: underline;

        }

        tr:nth-child(even)
        {
            background-color: #E0E0E0;
        }

        .instructions
        {
            text-align: left;
            font-size: 10pt;
            margin: 0px;
            margin-top: 0px;
            font-family: Verdana;
            color:blue;
            background-color:#f5f5f5;
            box-shadow: 3px 3px 3px #e8e8e8
        }
        div
        {

        }

        .page
        {
            max-width: 800px;
            background-color: #ffffff;
            border: solid;
            border-width: 1px;
            text-align: left;
            padding: 10px;

            font-size: 10pt;
            margin: auto;

            box-shadow: 5px 5px 5px #0026FF
        }

        .star_trek
        {
            text-align: left;
            font-size: 10pt;
            margin: 0px;
            margin-top: 0px;
            font-family: Verdana;
        }

    </style>

    <script src="tv_show.js"></script>
</head>

<body>
<script src="tv_show.js"></script>

<section class="container">
    <section class="row">
        <section class="col-xs-12" >
            <div id = assignment class = page style="margin-top: 10px">
                Neal Noble<br>
                March 2016<br>
                IT328<br>
                Week 1: Intro to Javascript <br>
            </div>



            <!-- Question #1: Name the data types supported by Javascript start-->
            <div id = question#1_id class = page style="margin-top: 10px">

                    <div class = "instructions"><ol start="1"><li>Name the data types supported by
                        Javascript (there are at least eight!).</li></ol>
                    </div>
                <ul>
                    <li>Number</li>
                    <li>String</li>
                    <li>Array</li>
                    <li>Ojbect</li>
                    <li>undefined</li>
                    <li>Boolean</li>
                    <li>Null</li>
                    <li>RegExp</li>
                    <li>Symbol</li>
                </ul>


            </div>
            <!-- Question #1: Name the data types supported by Javascript end -->


            <!-- Question #2: Three Buttons start-->
            <div id = question#2_id class = page style="margin-top: 10px">

                <div ip = "buttons_id" class = "buttons">
                    <div class = "instructions"><ol start="2"><li>Give the code for an HTML page that contains three buttons with the text "red", "white"
                        and "blue." Add Javascript function(s) that respond to clicking on each button.
                        The function(s) should change the background color of each button to match the text on the
                        button (ie. the button with "blue" as text should have a blue background).</li></ol>
                    </div>
                    <button id="redbtn" class= "button" onclick="red()">Red</button>
                    <button id="whitebtn" class= "button" onclick="white()">White</button>
                    <button id="bluebtn" class= "button" onclick="blue()">Blue</button>
                </div>

            </div>
            <!-- Question #2: Three Buttons end -->

            <p style="page-break-after:always;"></p>
            <p><!-- pagebreak --></p>

            <!-- Question #3: Browser Screen shots start -->
            <div id = assignment3 class = page style="margin-top: 10px">
                <div class = "instructions"> <ol start ="3"><li>Open the following browsers: Chrome, Firefox, IE and Opera.
                    Research how to open the Javascript console in each browser and give a screenshot of the
                    global object "window". The screenshot should show each of the properties on the window object.</li></ol>
                </div>
                <img src="images/chrome.png" style="width:49%;height:auto"/>
                <img src="images/firefox.png" style="width:41%;height: auto; float: right "/>

                <img src="images/opera.png" style="width:49%;height:auto"/>
                <img src="images/ie_edge.png" style="width:45%;height:30%; float: right"/>
            </div>
            <!-- Question #3: Browser Screen shots end -->

            <p style="page-break-after:always;"></p>
            <p><!-- pagebreak --></p>

            <!-- Question #4: Define TV show object  start-->
            <div id = question#4_id class = page style="margin-top: 10px">

                <div class = "instructions"><ol start="4"><li>Write a code segment that declares a
                    Javascript object that represents a TV show. Your object should include:<br>
                    &#60;show name	&#62; (&#60;year	&#62;)<br>
                        &#60;synopsis><br>
                        &#60;channel1>, &#60;channel2	&#62;, &#60;channel3	&#62;, ...<br>
                    Total channels: &#60;channel count	&#62;</li></ol>
                </div>

                <div id="answer#4_id">
                    <?php
                    highlight_file("tv_show.js");
                    ?>
                </div>

            </div>
            <!-- Question #4: Define TV show object end -->

            <p style="page-break-after:always;"></p>
            <p><!-- pagebreak --></p>

            <!-- Question #5: Display Star Trek info  start -->
            <div id = "question#5_id" class = page style="margin-top: 10px">
                <div class = "instructions">
                    <ol start = "5">
                        <li>Add your Javascript from (4) to a webpage and use your Javascript object to print out
                            the following information to the body of the page.
                        </li>
                    </ol>
                </div>
                <div id="Star_Trek_id" class="star_trek"></div>
                <script>
                    var  show = Star_Trek.title + " (" + Star_Trek.year + ")";

                    document.getElementById("Star_Trek_id").innerHTML ="<strong>" + show + "</strong><br>"
                            + "<i> " + Star_Trek.synopsis + "</i><br><br>"
                            + "Total Channels:" + Star_Trek.totalChannels() +"<br>"
                            + Star_Trek.channels + "<br><br>"
                            + "<strong>Cast:</strong><br>"
                            + Star_Trek.cast_crew[0] + "<br><br>"
                            + "<strong>Directors:</strong><br>"
                            + Star_Trek.cast_crew[1] + "<br><br>"
                            + "<strong>Writers:</strong><br>"
                            + Star_Trek.cast_crew[2] + "<br><br>"
                            + "<strong>Producers:</strong><br>"
                            + Star_Trek.cast_crew[3] + "<br><br>"
                            + "<strong>Music:</strong><br>"
                            + Star_Trek.cast_crew[4] + "<br><br>";
                </script>
            </div>
            <!-- Question #5: Display Star Trek info  end -->



            <!-- Question #6:  start-->
            <div id = question#6_id _id class = page style="margin-top: 10px">

                <div class = "instructions"><ol start="6"><li>Explain the concept of hoisting.</li></ol>
                </div>

                <div class = "instructions"><ol start="7"><li>Give a code example that highlights the concept
                            of hoisting. Your code should be commented so that a new-comer to the concept can follow
                            along without any further instructions</li></ol>
                </div>

                <div id="answer#6_id">

                    <?php
                    include "hoisting_info_include.php";
                    ?>
                    
                   
                </div>


            </div>
            <!-- Question #6:  end -->


            <!-- Question #7:  start-->
            <div id = question#7_id class = page style="margin-top: 10px; display: none">

                    <div class = "instructions"><ol start="7"><li>Give a code example that highlights the concept
                        of hoisting. Your code should be commented so that a new-comer to the concept can follow
                        along without any further instructions</li></ol>
                    </div>
                <div id="answer#7_id">
                    answer goes here
                </div>

            </div>
            <!-- Question #7:  end -->


            <!-- Question #8:  start-->
            <div id = question#8_id class = page style="margin-top: 10px">

                    <div class = "instructions"><ol start="8"><li>What are the Javascript style conventions?
                        (ie. naming conventions, spacing and indentation, bracket placement, ...)</li></ol>
                    </div>
                <div id="answer#8_id">
                    <?php
                    include "javascript_style.html";
                    ?>
                </div>

            </div>
            <!-- Question #8:  end -->



        </section>
    </section>
</section>




</body>
</html>