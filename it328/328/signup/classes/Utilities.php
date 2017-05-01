<?php
/**
 * Created by PhpStorm.
 * User: Neal
 * Date: 4/30/2017
 * Time: 6:47 AM
 */

namespace DatingSite;


class Utilities
{
    public static function getAdminLinkHeader(){
        return "<span>My Dating site</span><span class='alignright'><a href='\\admin'>Adminstrative</a></span>";
    }

    /**
     * Turn on debug commenting
     */
    public static function debugOn(){
        $_SESSION['debug'] = true;
    }


    /**
     *  Turn off debug commenting
     */
    public static function debugOff()
    {
        unset($_SESSION['debug']);
    }


    /**
     * Print debug comment to active webpage during debugging
     * @param $comment debug comment
     */
    public static function debug($comment){
        if (isset($_SESSION['debug'])) {
            echo $comment . "<BR>";
        }
    }
}