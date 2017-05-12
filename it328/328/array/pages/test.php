<!---->
<!--        Neal Noble-->
<!--        Course: IT 328 - Full-Stack Web Development-->
<!--        Assignment: Functions and Arrays-->
<!--        April 2017-->
<!--        Instructor: Tina Ostrander-->
<!---->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css" rel="stylesheet">
    <link rel="stylesheet" href="./styles/styles.css">
    <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>

    <title>Assignment: Arrays and functions</title>


</head>


<style>
    .myBox{

        padding: 9px;
        margin: 0 0 20px;
        font-size: 12px;
        margin-left: 10px;
        margin-right: 10px;
        line-height: 15px;
        word-break: break-all;
        word-wrap: break-word;
        white-space: pre;
        white-space: pre-wrap;
        background-color: #f5f5f5;
        border: 1px solid #ccc;

        border-radius: 3px;

    .myBoxed {

        width: 300px;
        border: 25px solid green;
        padding: 25px;
        margin: 25px;
        background-color: #f5f5f5;
    }



</style>

<body>
<div class="container">
    <div class="row">
        <div class="col-md-6" >
            <h1 class="center">Assignment: Arrays and functions</h1>
            <?php

            $animals = array("panda", "alpaca", "boa");

            function bubbleSort($items)
            {

                $sorted = false;

                $looplength = count ($items);

                while (!$sorted)
                {
                    $sorted = true;
                    for($i=1; $i< $looplength; $i++)
                    {
                        $left = $items[$i-1];
                        $right = $items[$i];
                        if ($right < $left)
                        {
                            $items[$i] = $left;
                            $items [$i-1] = $right;
                            $sorted = false;
                        }
                    }

                    $looplength--;

                }
                return $items;
            }
            echo "<div class='myBox'>";
            function AddtoArray ($items, $item)
            {
                echo "adding ".$item . "...<br>";
                $item = strtolower($item);

                foreach ($items as $value)
                {
                    if ($value == $item)
                    {
                        $sortedItems = bubbleSort($items);
                        return $sortedItems;
                    }
                }

                array_push($items,$item);
                $sortedItems = bubbleSort($items);
                return $sortedItems;
            }

            function PrintArray($items)
            {

                foreach ($items as $value)
                    echo $value ." ";
                echo "<br>";
            }


            $sortedItems = bubbleSort($animals);
            PrintArray ($sortedItems);

            $sortedItems = AddtoArray ($animals, "goat");
            PrintArray ($sortedItems);

            $sortedItems = AddtoArray ($sortedItems, "Boa");
            PrintArray ($sortedItems);
            echo "</div><br>";
            ?>

            <?php
            $cupcakeflavors = array("grasshopper"=>"The Grasshopper",
                "maple"=>"Whiskey Maple Bacon",
                "carrot "=>"Carrot Walnut",
                "caramel"=>"Salted Caramel Cupcake",
                "velvet"=>"Red Velvet",
                "lemon"=>"Lemon Drop",
                "tiramisu"=>"Tiramisu!1");

            echo "<div class='myBox'>";

            foreach ($cupcakeflavors as $x=>$x_value)
            {
                echo '<div class="checkbox">';
//                echo '<label>';
                echo '<input type="checkbox" value="">';
//                echo '<span class="cr"><i class="cr-icon glyphicon glyphicon-ok"></i></span>';
                echo "$x_value<br>";
//                echo '</label>';
                echo '</div>';
            }

            echo "</div><br>";
            ?>
        </div>

    </div>
</div>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

</body>
</html>