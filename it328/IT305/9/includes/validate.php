<?php


	function validName($name)
    {
        if (!empty($name) and ctype_alpha($name))
        {
            return true;
        } else
        {
            return false;
        }
    }


    function validLastName($lastname)
    {
        if (!empty($lastname) and ctype_alpha($lastname))
        {
            return true;
        }
        else
        {
            return false;
        }
    }



    function validSid($sid)
    {
        if (!empty($sid) and ctype_digit($sid))
        {
            return true;
        }
        else
        {
            return false;
        }

    }


function validGpa($gpa)
{

    if ($gpa == null)
    {
        return true;
    }

    if (is_numeric($gpa))
    {
        if (($gpa >0 and $gpa <= 4.0) || ($gpa == null))
            return true;
    }
    else
    {
        return false;
    }


}



?>
