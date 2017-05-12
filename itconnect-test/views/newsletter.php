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
 * The page allows users to sign-up to for internship updates via email
 */
?>

<!DOCTYPE html>
<html>
<head>
    <!-- Responsive design -->
    <meta name="viewport" content="width=device-width, initial-scale=1 , maximum-scale=1">
    <meta charset="utf-8">
    <title>IT Connect - Newsletter sign-up</title>
    <link rel="stylesheet" type="text/css" media="all" href="../css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" media="all" href="../css/index.css">
    <link rel="stylesheet" type="text/css" media="all" href="../css/form.css">
    <link rel="stylesheet" type="text/css" media="all" href="../css/navbar.css">
    <link rel="stylesheet" type="text/css" media="all" href="../css/footer.css">

    <!-- Fontawesome -->
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-T8Gy5hrqNKT+hzMclPo118YTQO6cYprQmhrYwIiQ/3axmI1hQomh7Ud2hPOy8SP1" crossorigin="anonymous">

</head>
<body>
<div id="site-container">
    <?php include("../navigation.php"); ?>
    <div id="body-content">
        <div id="alert-success" role="alert" class="alert hide">
            <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
            <strong>Success!</strong> You have subscribed to weekly internship updates!
        </div>
        <div class="row">
            <div class="col-xs-12">

                <div class="wrapper">
                    <form id="newsletter-form" class="form">
                        <h2 class="form-heading text-center">Enter your email to receive <b>weekly internship updates!</b></h2>
                        <p id="email-error" class="hide margin-top"></p>
                        <input type="email" id="email" class="form-control margin-top-bottom " name="email" placeholder="student@greenriver.mail.edu" required="" autofocus="" />
                        <button class="btn btn-lg btn-success btn-block btn-theme" type="submit">Get Updates!</button>
                    </form>
                </div>

            </div>
        </div>
    </div>
    <?php include("../footer.php"); ?>
</div>
<script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
<script src="../js/bootstrap.min.js"></script>
<script src="../js/newsletter.js"></script>
</body>
</html>
