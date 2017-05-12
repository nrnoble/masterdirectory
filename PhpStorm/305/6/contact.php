<?php
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
?>
<!doctype html>
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
            box-shadow: 5px 5px 5px #0026FF;
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

                    <h1>Contact The Kent Food Bank</h1>
                    <?php if ($_POST && ($suspect || isset($errors['mailfail']))) : ?>
                    <p class="warning">Sorry, your mail couldn't be sent.</p>
                    <?php elseif ($errors || $missing) : ?>
                    <p class="warning">Please fix the item(s) indicated</p>
                    <?php endif; ?>
                    <form method="post" action="<?= $_SERVER['PHP_SELF']; ?>">
                      <p>
                        <label for="name" \>Name:
                        <?php if ($missing && in_array('name', $missing)) : ?>
                            <span class="warning">Please enter your name</span>
                        <?php endif; ?>
                        </label>
                        <input type="text" name="name" id="name" value="Neal Noble"
                            <?php
                            if ($errors || $missing) {
                                echo 'value="' . htmlentities($name) . '"';
                            }
                            ?>
                            >
                      </p>
                      <p>
                        <label for="email">Email:
                            <?php if ($missing && in_array('email', $missing)) : ?>
                                <span class="warning">Please enter your email address</span>
                            <?php elseif (isset($errors['email'])) : ?>
                                <span class="warning">Invalid email address</span>
                            <?php endif; ?>
                        </label>
                        <input type="email" name="email" id="email" value="nrnoble@hotmail.com"
                            <?php
                            if ($errors || $missing) {
                                echo 'value="' . htmlentities($email) . '"';
                            }
                            ?>
                            >
                      </p>
                      <p>
                        <label for="comments" >Comments:
                            <?php if ($missing && in_array('comments', $missing)) : ?>
                                <span class="warning">You forgot to add any comments</span>
                            <?php endif; ?>
                        </label>
                          <textarea name="comments" id="comments"><?php
                              if ($errors || $missing) {
                                  echo htmlentities($comments);
                              }
                              
                              ?>comments go here</textarea>
                      </p>
                      <p>
                        <input type="submit" name="send" id="send" value="Send Comments">
                      </p>
                    </form>
                </div>

            
            </section>
        </section>
    </section>

</body>
</html>