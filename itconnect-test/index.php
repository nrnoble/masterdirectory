<?php
/**
MIT License

Copyright (c) 2016 Michael Lant, Bogdan Pshonyak, Yegor Shemereko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
 */

/**
 * The website's landing page, allowing the user to decide if they want to view internships
 *      or check out student resources
 */
?>

<!DOCTYPE html>
<html>
    <head>
        <!-- Responsive design -->
        <meta name="viewport" content="width=device-width, initial-scale=1 , maximum-scale=1">
        <meta charset="utf-8">
        <meta name="description" content="IT Connect helps students discover technical internships in the Seattle-Tacoma region,
                                            and provides curated career preparation resources for improving resumes and LinkedIn profiles.">
        <meta name="keyword" content="ITconnect, IT Connect, Green River College, GRC, GRC IT Connect, GRC ITconnect,
                                        Internships, Internship, Student, College, Software, Software Development, IT,
                                        Information Technology">
        <title>IT Connect: A resource for technology students.</title>
        <link rel="stylesheet" type="text/css" media="all" href="/css/bootstrap.min.css">
        <link rel="stylesheet" type="text/css" media="all" href="/css/index.css">
        <link rel="stylesheet" type="text/css" media="all" href="/css/navbar.css">
        <link rel="stylesheet" type="text/css" media="all" href="/css/footer.css">

        <!-- Fontawesome -->
        <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-T8Gy5hrqNKT+hzMclPo118YTQO6cYprQmhrYwIiQ/3axmI1hQomh7Ud2hPOy8SP1" crossorigin="anonymous">

    </head>

    <body>
        <div id="site-container">
            <?php include("./navigation.php"); ?>
            <div id="body-content">
                <div id="landing-banner">
                        <div id="left-landing" class="">
                            <a href="/views/internships.php" class="">
                                <h1>
                                    View Internships
                                </h1>
                            </a>
                        </div>
                        <div id="right-landing" class="">
                            <a href="/views/studentResources.php" class="">
                                <h1>
                                    Student Resources
                                </h1>
                            </a>
                        </div>
                </div>
            </div>
            <?php include("./footer.php"); ?>
        </div>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
        <!-- Include all compiled plugins (below), or include individual files as needed -->
        <script src="/js/bootstrap.min.js"></script>
    </body>
</html>
