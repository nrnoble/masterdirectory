<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>{{ @title }}</title>
</head>

<body>
<p>User logged in as {{ @username }} using {{ @password }}</p>

<!-- looping over arrays -->
<p>Bookmarks: </p>
<ul>
    <repeat group="{{ @bookmarks }}" value="{{ @bookmark }}">
        <li><a href="{{ @bookmark }}">
                {{ str_replace('http://', '', @bookmark); }}</a></li>
    </repeat>
</ul>

<hr>
{{ @addresses['primary'] }}
<hr>
{{ @addresses['secondary'] }}
<hr>

<!-- looping over associative arrays -->
<p>Addresses: </p>
<repeat group="{{ @addresses }}" key="{{ @key }}" value="{{ @value }}">
    <p>{{ @key }} - {{ @value }}</p>
</repeat>

<check if="{{ @preferredCustomer }}">
    <strong>Thank you for being a preferred customer...!</strong><br>
</check>

<check if="{{ @lastLogin > strtotime('-1 month') }}">
    <true>
        - Welcome back!
    </true>
    <false>
        - Welcome back, it's been a bit!
    </false>
</check>

<p>Printing objects: </p>
{{ @addressObject->street }}<br>
{{ @addressObject->city }}<br>
{{ @addressObject->state }}<br>
{{ @addressObject->zip }}<br>
</body>
</html>
