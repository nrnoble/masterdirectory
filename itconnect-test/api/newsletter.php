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
 * Newsletter api
 */

//Session holds admin login data
session_start();

include "../models/NewsletterModel.php";

//Files to connect to the DB
$config = include("../db/config.php");
$db = new PDO($config["db"], $config["username"], $config["password"]);
$newsletter = new NewsletterModel($db);

//The switch chooses what server Request_Method is being submitted
SWITCH ($_SERVER["REQUEST_METHOD"]) {

    // Attempt user login
    case "POST":

        $email = $_POST["email"];

        //TODO: Validate email

        $status = $newsletter->addEmail($email);

        if($status) {
            $result = array('status' => 200, 'msg' => "{$email} an authentication email has been sent. The email contains an authentication link!");

            //TODO (Neal Noble): Send authentication email here.
        }
        else {
            $result = array('status' => 403, 'msg' =>  " email is subscribed.");

            / // TODO (Neal Noble) if db.newsletter.subscribe == false, change to true.
        }

        break;

}

header("Content-Type: application/json");
echo json_encode($result);
