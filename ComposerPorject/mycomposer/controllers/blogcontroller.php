<!--
Neal Noble
IT426
Assignment: MVC F.A.T Free in class example
Instructor Josh Archer
Dec 2016
-->

<?php
class BlogController
{
    private $router;

    public function __construct($router)
    {
        $this->router = $router;
    }

    public function viewAllBlogs($username)
    {
        $repo = new TestBlogRepository();

        if ($repo->isAUser($username)) {
            $blogPosts = $repo->getBlogPosts($username);

            //save blogs, user
            $this->router->set('blogPosts', $blogPosts);
            $this->router->set('username', $username);

            //set our page content and let the layout display it
            $this->router->set('content', 'views/viewblogs.php');
            echo Template::instance()->render('views/viewblogs.php');
        } else {
            $this->router->error(404);
        }
    }

    public function viewBlog($blogId)
    {
        $repo = new TestBlogRepository();

        if ($repo->isABlog($blogId)) {
            $username = $repo->getBlogAuthor($blogId);
            $blogPost = $repo->getBlog($blogId);

            //save blogs, user
            $this->router->set('blogPost', $blogPost);
            $this->router->set('username', $username);

            echo Template::instance()->render('views/viewsingleblog.php');
        } else {
            $this->router->error(404);
        }
    }
}
?>