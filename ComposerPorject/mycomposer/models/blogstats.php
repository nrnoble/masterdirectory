
<?php
class blogstats
{


    public function blogLength($blogText)
    {
        return strlen($blogText);
    }

    public function keywordFrequency($blogText, $word)
    {
        //get the size of the array of text on each side of the word found
        //return sizeof(explode(strtolower($word), strtolower($blogText))) - 1;

        //or use substr_count()
        return substr_count(strtolower($blogText), strtolower($word));
    }
}
?>
