<?php

    function tableHeaderFooter($result)
    {
        # echo "var dump::  var_dump($result->field_count);";
        $fieldnames = [];
        if ($result->field_count > 0)
        {
            #echo "<thread>";
            #echo "<tr>";

            $th = "<tr>";
            $count =0;
            while($field = $result->fetch_field() )
            {
                $count++;
                $fieldnames[] = $field->name;

                if ($count < 6 )
                {
                    #echo "$field->name \r\n";
                    $th =  $th . "<th>" . $field->name . "</th>";
                    #echo "$th";
                }
            }

            $th = $th . "</tr>";
            echo "\r\n<thead>" . $th . "</thead>\r\r\n";
            echo "<tfoot>" . $th . "</tfoot>\r\r\n";


        }
        return $fieldnames;
    }
?>