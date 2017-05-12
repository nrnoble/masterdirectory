<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>{{ @blogPost->blogTitle }}</title>
</head>

<body>
<h3>{{ @blogPost->blogTitle }}</h3>
<p>{{ @blogPost->blogText }}</p>

<h4>References</h4>
<ul>
    <repeat group="{{ @blogPost->references }}" value="{{ @reference }}">
        <li><a href="{{ @reference }}">{{ @reference }}</a></li>
    </repeat>
</ul>
</body>
</html>
