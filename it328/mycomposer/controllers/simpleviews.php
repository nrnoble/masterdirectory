<!--
Neal Noble
IT426
Assignment: MVC F.A.T Free in class example
Instructor Josh Archer
Dec 2016
-->

<?php
class SimpleViews
{
    public function showHome()
    {
        echo 'Welcome to my Home!, <a href="/about">
                  About us!</a> <a href="/sitemap">
                  Site Map</a>';
    }

    public function showAboutUs()
    {
        echo 'About us!';
    }

    public function showSiteMap()
    {
        echo 'Sitemap!';
    }
}
?>
