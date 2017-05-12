<!--
Neal Noble
IT426
Assignment: MVC F.A.T Free in class example
Instructor Josh Archer
Dec 2016
-->

<?php
interface IBlogRepository
{
    //blog data
    public function getBlogPosts($username);
    public function getBlog($blogId);
    public function getBlogReferences($blogId);

    //user data
    public function getRegisteredUsers();
    public function isAUser($username);
}
?>
