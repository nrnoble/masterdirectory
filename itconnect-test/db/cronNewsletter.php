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
 * A script to send out the IT Connect internship newsletter
 */
    $config = include("config.php");
    include "../models/PostingsModel.php";
    include "../models/NewsletterModel.php";

    $db = new PDO($config["db"], $config["username"], $config["password"]);

    $postings = new PostingsModel($db);
    $newsletter = new NewsletterModel($db);

    $posts = $postings->getFilteredPostings(90);
    $emails = $newsletter->getEmails();

    function createPostHTML($row)
    {

        $title = $row["title"];
        $url = $row["url"];
        $email = $row["email"];
        $company = $row["company"];
        $category = $row["category"];
        $location = $row["location"];
        $result->qualifications = $row["qualifications"];

        $result = "<li>
                    <h3>{$title}</h3>
                    <p>{$company} - {$location}</p>
                    <a href='{$url}'>{$url}</a>
                    </li>";

        return $result;
    }

    function generateEmailHTML($lists)
    {

        $result = "<html>
                        <head>
                            <title>IT Connect Internship Update</title>
                        </head>
                        <body>
                            <h1>IT Connect - Internships Posted This Week!</h1>
                            <ul style='list-style: none'>";
        foreach ($lists as $list) {
            $result = $result . $list;
        }
        $result = $result . "</ul></body></html>";
        return $result;
    }

    function sendEmails($content, $emails)
    {
        $to = implode(", ", $emails);
        $subject = "IT Connect - Interships update";

        $headers = "MIME-Version: 1.0" . "\r\n";
        $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";

        // More headers
        $headers .= 'From: <no-reply@itconnect.greenrivertech.net>' . "\r\n";

        echo (mail($to,$subject,$content,$headers));
    }

    $postListItems = array();

    foreach ($posts as $row) {
        array_push($postListItems, createPostHTML($row));
    }

    $emailHTML = generateEmailHTML($postListItems);

    sendEmails($emailHTML, $emails);

    $db = null;
    //
    // header("Content-Type: application/json");
    // echo json_encode($posts);
