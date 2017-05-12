<!--
Neal Noble
IT426
Assignment: MVC F.A.T Free in class example
Instructor Josh Archer
Dec 2016
-->
<?php
    class blogvalidator
    {
            public function isValidTitle($title)
            {
                //title must be longer than 8 characters and contain no
                //special characters
                return strlen($title > 8) && !preg_match('[^a-zA-Z 0-9]+', $title);
            }

            public function isValidText($text)
            {
                //all blog posts must exceed a certain minimum number of characters
                return strlen($text > 500);
            }

            public function makeSafe($text)
            {
                return htmlentities($text);
            }
    }
?>
