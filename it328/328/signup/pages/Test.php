<!DOCTYPE html>
<html lang="en">

<!---->
<!--        Neal Noble-->
<!--        Course: IT 328 - Full-Stack Web Development-->
<!--        Assignment: The sign-up form-->
<!--        April 2017-->
<!--        Instructor: Tina Ostrander-->



<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
    <link rel="stylesheet" type="text/css" href="../styles/styles.css">
    <link rel="stylesheet" type="text/css" href="../styles/signupstyles.css">

    <title>Template</title>

</head>

<body>

<header class="bgimage">
    <div class="container">
        <div class="row">
            <h2>Header Goes here</h2>
            <hr>
            <div class="col-md-6" >
                <div>
                    <h2>Column One</h2>
                    <form action="./testresult"  method="post" class="form-horizontal">
                        <input type="text" name="name" id="name" value="NealrNoble">
                        <input class="form-control btn btn-default"
                               type="submit" value="Next">
                    </form>
                    <form action="./testresult" method="post" class="form-horizontal">

                        <!-- animal -->
                        <div class="form-group">
                            <label for="title" class="col-sm-2 control-label">Name</label>

                            <div class="col-sm-10">
                                <input class="form-control" type="text" name="pet-name" id="pet-name">
                            </div>
                        </div>


                        <div class="col-xs-4 col-xs-offset-4">
                            <input class="form-control btn btn-default"
                                   type="submit" value="Next">
                        </div>
                    </form>
                </div>
            </div>
            <div class="col-md-6">
                <div>
                    <h2>Column two</h2>
                    text

                </div>

            </div>
            <hr>
            <h2>page Footer Goes here</h2>
            test
        </div>
    </div>
</header>



<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

</body>
</html>