<?php session_start();?>
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
<head>
    <meta charset="UTF-8">
    <!---->
    <!--        Neal Noble                                                                                                                              -->
    <!--        Course: IT 328 - Full-Stack Web Development                                                                                             -->
    <!--        Assignment: The sign-up form                                                                                                            -->
    <!--        April 2017                                                                                                                              -->
    <!--        Instructor: Tina Ostrander                                                                                                              -->
    <!--                                                                                                                                                -->
    <!--        Bootstraps forms on this page were referenced from https://v4-alpha.getbootstrap.com/components/forms/                                  -->

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" type="text/css" href="//cdn.datatables.net/1.10.15/css/jquery.dataTables.css">
    <script src="https://cdn.datatables.net/1.10.15/js/jquery.dataTables.js"></script>
    <script src="https://code.jquery.com/jquery-1.12.4.js"></script>

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
    <link rel="stylesheet" type="text/css" href="http://nnoble.greenrivertech.net/328/signup/styles/signupstyles.css">
    <link rel="stylesheet" type="text/css" href="http://nnoble.greenrivertech.net/328/signup/styles/styles.css">
    <link rel="stylesheet" type="text/css" href="http://nnoble.greenrivertech.net/328/signup/styles/summery.css">
    <link rel="stylesheet" href="http://nnoble.greenrivertech.net/328/signup/styles/navbar.css">

    <style>

    </style>


    <title>Admin Page</title>


</head>

<body>

<header class="bgimage">
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="mynavbar"><?=  \DatingSite\Utilities::getAdminLinkHeader() ?></div>
                <div class="row myDiv2">
                    <table id="table_id" class="display tabledata" data-order='[[ 1, "asc" ]]' data-page-length='5'>
                        <thead>
                        <tr>
                            <th class = "tableIdColumn">ID</th>
                            <th class = "tableNameColumn">Name</th>
                            <th class = "tableAgeColumn">age</th>
                            <th class = "tablePhoneColumn">Phone</th>
                            <th>Email</th>
                            <th>State</th>
                            <th>Gender</th>
                            <th>Seeking</th>
                            <th>Premium</th>
                            <th>Interests</th>
                        </tr>
                        </thead>
                        <tbody>

                        <?= $MembersDB->getTableRows() ?>
                        <?= $test ?>
                        </tbody>
                    </table>

                    <div class="row">
                        <div class="col-md-12">
                            <div class="mycenter">
                               <a href="/328/signup"><button type="button" class=" btn btn-primary">Home Page</button></a>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>

</header>

<script>
    $(document).ready( function () {
        $('#table_id').DataTable({scrollY: 200});
    } );
</script>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
<script src="https://cdn.datatables.net/1.10.15/js/jquery.dataTables.js"></script>

</body>
</html>