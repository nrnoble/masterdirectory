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
 * Controller for admin dashboard page
 */

//Session holds admin login data
session_start();

// Check if the user if logged in
if (!(isset($_SESSION['loggedIn']) && !empty($_SESSION['loggedIn']))) {
    header("Location: ../views/adminLogin.php");
}else {
    // If user is logged in then put two buttons into the navbar
    $logOutButton = '
                <ul class="nav navbar-nav pull-right">
                    <li><a id="change-password-link">Change Password</a></li>
                    <li><a href = "./logoutScript.php" >Log Out</a></li>
                </ul>';
}

// Postings Model that includes functions to handle posts
include "../models/PostingsModel.php";

// Files to connect to DB
$config = include("../db/config.php");
$db = new PDO($config["db"], $config["username"], $config["password"]);
$postings = new PostingsModel($db);

// Getting all postings
$rows = $postings->getAllPostings();

// Display the page and put $rows into a table
include "../views/adminPage.php";
