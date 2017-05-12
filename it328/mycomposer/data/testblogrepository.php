<?php
class TestBlogRepository implements IBlogRepository
{
    private $testBlogs;
    private $testAuthors;

    public function __construct()
    {
        $this->testBlogs = array(new Blog('58291242766ed3.99076523',
            'Testing at Google', 'We have seen...’,  
                                     array('https://developers.google.com/...',
                                           'https://www.google.com/webmasters/...',
                                            'https://en.wikipedia.org/...)),
                                     new Blog('58291242767273.55585439',
                                         'Windows 10 Blog', 'On Wednesday, ...’,
                                     array('http://www.extremetech.com/tag/windows-10',
                                         'https://www.cnet.com/news/...',
                                         'http://www.windows10update.com/')),
                                     new Blog('582912427672d9.53850465',
                                         'Owning a Pet Blog', 'Have you ever...’,
                                     array('http://www.huffingtonpost.com/news/pets/',
                                           'http://www.lifewithdogs.tv/...',
                                           'http://www.today.com/pets')));

            $this->authors = array('tech4me' => array(
                $this->testBlogs[0],
                $this->testBlogs[1]),
                'petsforever' => array($this->testBlogs[2]));
        }


    //blog data

    //returns all posts for a user
    public function getBlogPosts($username)
    {
        if (!$this->isAUser($username)) {
            throw new Exception('Username does not exist');
        }

        return $this->authors[$username];
    }

    //returns a blog by id
    public function getBlog($blogId)
    {
        foreach ($this->testBlogs as $blog) {
            if ($blog->blogId == $blogId)
            {
                return $blog;
            }
        }

        throw new Exception('Blog does not exist');
    }

    //returns all references for a blog
    public function getBlogReferences($blogId)
    {
        $blog = $this->getBlog($blogId);

        return $blog->getReferences;
    }


    //returns the author of a blog
    public function getBlogAuthor($blogId)
    {
        //for every author
        foreach ($this->authors as $author => $blogs) {
            //search for the blog
            foreach ($blogs as $blog) {
                if ($blog->blogId == $blogId) {
                    return $author;
                }
            }
        }

        //not found
        throw new Exception("Author not found...");
    }

    //user data

    //returns all registered users
    public function getRegisteredUsers()
    {
        return array_keys($this->authors);
    }

    //returns whether the username is registered or not
    public function isAUser($username)
    {
        return array_key_exists($username, $this->authors);
    }

    //returns whether the blog id is valid or not
    public function isABlog($blogId)
    {
        foreach ($this->testBlogs as $blog) {
            if ($blog->blogId == $blogId) {
                return true;
            }
        }

        return false;
    }
}
?>
