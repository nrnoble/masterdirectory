<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>View {{ @username }} blogs</title>
</head>

<body>
<h1>Blogs by: {{ @username }}</h1>
<repeat group="{{ @blogPosts }}" value="{{ @blogPost }}">
    <hr>
    <h4><a href="/viewBlog/{{ @blogPost->blogId }}">
            {{ @blogPost->blogTitle }}</a></h4>
</repeat>
</body>
</html>
