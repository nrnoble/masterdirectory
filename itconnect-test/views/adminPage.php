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
 * The page where the admin can add/delete/edit posts in the internship table
 *      and change password
 *          and edit resources page
 */
?>

<!DOCTYPE html>
<html>
<head>
    <!-- Responsive design -->
    <meta name="viewport" content="width=device-width, initial-scale=1 , maximum-scale=1">
    <meta charset="utf-8">
    <title>Admin Dashboard</title>
    <link rel="stylesheet" type="text/css" media="all" href="../css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" media="all" href="../css/index.css">
    <link rel="stylesheet" type="text/css" media="all" href="../css/admin-page.css">
    <link rel="stylesheet" type="text/css" media="all" href="../css/navbar.css">
    <link rel="stylesheet" type="text/css" media="all" href="../css/footer.css">

    <!-- Fontawesome -->
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-T8Gy5hrqNKT+hzMclPo118YTQO6cYprQmhrYwIiQ/3axmI1hQomh7Ud2hPOy8SP1" crossorigin="anonymous">

</head>
<body>
<div id="site-container">
    <?php include("../navigation.php"); ?>
    <div id="body-content">
        <div id="change-alert-success" role="alert" class="alert hide">
            <a href="#" class="close" id="close-change-alert" aria-label="close">&times;</a>
            <strong>Success!</strong> Your password has been changed.
        </div>

        <div class="row">
            <div class="col-xs-6" style="padding: 0px">
                <button type="button" id="post-submit" class="btn btn-success add-btn btn-lg" data-toggle="modal" data-target="#addModal">Add
                    Internship
                </button>
            </div>
            <div class="col-xs-6" style="padding: 0px">
                <button type="button" id="resources-edit" class="btn btn-warning add-btn btn-lg" data-toggle="modal" data-target="#resourcesModal">Edit
                    Student Resources
                </button>
            </div>
        </div>

        <div class="row">
            <div class="col-xs-12">
                <div class="internships-table">
                    <div id="toolbar">
                        <button id="delete-btn" class="btn btn-danger">Delete Selected Posts</button>
                    </div>
                    <table id="adminTable""></table>
                </div>

            </div>
        </div>
    </div>

    <?php include("modals/addModal.php"); ?>
    <?php include("modals/updateModal.php"); ?>
    <?php include("modals/deleteModal.php"); ?>
    <?php include("modals/resourcesModal.php"); ?>
    <?php include("modals/changePasswordModal.php"); ?>
    <?php include("../footer.php"); ?>
</div>

<script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
<script src="../js/bootstrap.min.js"></script>

<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.10.1/bootstrap-table.min.css">

<!-- Latest compiled and minified JavaScript -->
<script src="//cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.10.1/bootstrap-table.min.js"></script>

<!-- WYSIWYG Editor -->
<script src='//cdn.tinymce.com/4/tinymce.min.js'></script>

<script src="../js/adminPage.js"></script>

</body>
</html>
