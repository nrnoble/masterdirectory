<!--
Neal Noble
IT426
Assignment: MVC F.A.T Free in class example
Instructor Josh Archer
Dec 2016
-->
<?php
class Blog
{
    private $blogId;
    private $blogTitle;
    private $blogText;
    private $references;

    public function __construct($blogId, $blogTitle, $blogText, $references)
    {
        $this->blogId = $blogId; //uuid
        $this->blogTitle = $blogTitle;
        $this->blogText = $blogText;
        $this->references = $references;
    }

    public function __get($name)
    {
        return $this->$name;
    }

    public function __toString()
    {
        return $this->blogTitle.'('.$this->blogId.'): '.$this->blogText;
    }
}
?>