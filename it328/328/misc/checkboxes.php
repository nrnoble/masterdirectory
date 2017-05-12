
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <!-- This file has been downloaded from Bootsnipp.com. Enjoy! -->
    <title>Animated radios &amp; checkboxes (noJS) - Bootsnipp.com</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet">
    <style type="text/css">
        .checkbox label:after,
        .radio label:after {
            content: '';
            display: table;
            clear: both;
        }

        .checkbox .cr,
        .radio .cr {
            position: relative;
            display: inline-block;
            border: 1px solid #a9a9a9;
            border-radius: .25em;
            width: 1.3em;
            height: 1.3em;
            float: left;
            margin-right: .5em;
        }

        .radio .cr {
            border-radius: 50%;
        }

        .checkbox .cr .cr-icon,
        .radio .cr .cr-icon {
            position: absolute;
            font-size: .8em;
            line-height: 0;
            top: 50%;
            left: 20%;
        }

        .radio .cr .cr-icon {
            margin-left: 0.04em;
        }

        .checkbox label input[type="checkbox"],
        .radio label input[type="radio"] {
            display: none;
        }

        .checkbox label input[type="checkbox"] + .cr > .cr-icon,
        .radio label input[type="radio"] + .cr > .cr-icon {
            transform: scale(3) rotateZ(-20deg);
            opacity: 0;
            transition: all .3s ease-in;
        }

        .checkbox label input[type="checkbox"]:checked + .cr > .cr-icon,
        .radio label input[type="radio"]:checked + .cr > .cr-icon {
            transform: scale(1) rotateZ(0deg);
            opacity: 1;
        }

        .checkbox label input[type="checkbox"]:disabled + .cr,
        .radio label input[type="radio"]:disabled + .cr {
            opacity: .5;
        }
    </style>
    <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
</head>
<body>
<link href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css" rel="stylesheet">

<div class="container">
    <h1>CheckboxRadio (no JS)</h1>
    <hr/>

    <p>This snippet allows you create nice animated checkboxes and radios without JavaScript. <br/>Just put <code><span class="cr"><i class="cr-icon glyphicon glyphicon-ok"></i></span></code> right after your checkbox or radio.</p>
    <p>Other markup was copied from <a href="http://getbootstrap.com/css/#forms" target="_blank">Bootstrap example</a>.</p>
    <h2>Checkboxes</h2>
    <hr/>

    <h3>Default example</h3>

    <div class="col-sm-12">
        <div class="checkbox">
            <label>
                <input type="checkbox" value="">
                <span class="cr"><i class="cr-icon glyphicon glyphicon-ok"></i></span>
                Option one is this and that — be sure to include why it's great
            </label>
        </div>
        <div class="checkbox">
            <label>
                <input type="checkbox" value="" checked>
                <span class="cr"><i class="cr-icon glyphicon glyphicon-ok"></i></span>
                Option two is checked by default
            </label>
        </div>
        <div class="checkbox disabled">
            <label>
                <input type="checkbox" value="" disabled>
                <span class="cr"><i class="cr-icon glyphicon glyphicon-ok"></i></span>
                Option three is disabled
            </label>
        </div>
    </div>

    <h3>Default example (other icon)</h3>

    <div class="col-sm-12">
        <div class="checkbox">
            <label>
                <input type="checkbox" value="">
                <span class="cr"><i class="cr-icon glyphicon glyphicon-arrow-right"></i></span>
                Option one is this and that — be sure to include why it's great
            </label>
        </div>
        <div class="checkbox">
            <label>
                <input type="checkbox" value="" checked>
                <span class="cr"><i class="cr-icon glyphicon glyphicon-arrow-right"></i></span>
                Option two is checked by default
            </label>
        </div>
        <div class="checkbox disabled">
            <label>
                <input type="checkbox" value="" disabled>
                <span class="cr"><i class="cr-icon glyphicon glyphicon-arrow-right"></i></span>
                Option three is disabled
            </label>
        </div>
    </div>

    <h3>Font awesome example</h3>

    <div class="col-sm-12">
        <div class="checkbox">
            <label>
                <input type="checkbox" value="">
                <span class="cr"><i class="cr-icon fa fa-check"></i></span>
                Option one is this and that — be sure to include why it's great
            </label>
        </div>
        <div class="checkbox">
            <label>
                <input type="checkbox" value="" checked>
                <span class="cr"><i class="cr-icon fa fa-check"></i></span>
                Option two is checked by default
            </label>
        </div>
        <div class="checkbox disabled">
            <label>
                <input type="checkbox" value="" disabled>
                <span class="cr"><i class="cr-icon fa fa-check"></i></span>
                Option three is disabled
            </label>
        </div>
    </div>

    <h3>Font awesome example (other icon)<br/><small>Works best with square icons =)</small></h3>

    <div class="col-sm-12">
        <div class="checkbox">
            <label>
                <input type="checkbox" value="">
                <span class="cr"><i class="cr-icon fa fa-rocket"></i></span>
                Option one is this and that — be sure to include why it's great
            </label>
        </div>
        <div class="checkbox">
            <label>
                <input type="checkbox" value="" checked>
                <span class="cr"><i class="cr-icon fa fa-rocket"></i></span>
                Option two is checked by default
            </label>
        </div>
        <div class="checkbox disabled">
            <label>
                <input type="checkbox" value="" disabled>
                <span class="cr"><i class="cr-icon fa fa-rocket"></i></span>
                Option three is disabled
            </label>
        </div>
    </div>

    <h3>Any size you want depending on label font-size</h3>

    <div class="col-sm-12">
        <div class="checkbox">
            <label style="font-size: 2.5em">
                <input type="checkbox" value="" checked>
                <span class="cr"><i class="cr-icon fa fa-check"></i></span>
                Huge
            </label>
        </div>
        <div class="checkbox">
            <label style="font-size: 2em">
                <input type="checkbox" value="" checked>
                <span class="cr"><i class="cr-icon fa fa-check"></i></span>
                Big
            </label>
        </div>
        <div class="checkbox">
            <label style="font-size: 1.5em">
                <input type="checkbox" value="" checked>
                <span class="cr"><i class="cr-icon fa fa-check"></i></span>
                Bigger
            </label>
        </div>
        <div class="checkbox">
            <label style="font-size: 1em">
                <input type="checkbox" value="" checked>
                <span class="cr"><i class="cr-icon fa fa-check"></i></span>
                Default
            </label>
        </div>
        <div class="checkbox">
            <label style="font-size: .8em">
                <input type="checkbox" value="" checked>
                <span class="cr"><i class="cr-icon fa fa-check"></i></span>
                Smaller
            </label>
        </div>
        <div class="checkbox">
            <label style="font-size: .5em">
                <input type="checkbox" value="" checked>
                <span class="cr"><i class="cr-icon fa fa-check"></i></span>
                Small
            </label>
        </div>
    </div>

    <h2>Radio</h2>
    <hr/>

    <h3>Default example</h3>

    <div class="col-sm-12">
        <div class="radio">
            <label>
                <input type="radio" name="o1" value="">
                <span class="cr"><i class="cr-icon glyphicon glyphicon-ok-sign"></i></span>
                Option one is this and that — be sure to include why it's great
            </label>
        </div>
        <div class="radio">
            <label>
                <input type="radio" name="o1" value="" checked>
                <span class="cr"><i class="cr-icon glyphicon glyphicon-ok-sign"></i></span>
                Option two is checked by default
            </label>
        </div>
        <div class="radio disabled">
            <label>
                <input type="radio" name="o1" value="" disabled>
                <span class="cr"><i class="cr-icon glyphicon glyphicon-ok-sign"></i></span>
                Option three is disabled
            </label>
        </div>
    </div>

    <h3>Default example (other icon)</h3>

    <div class="col-sm-12">
        <div class="radio">
            <label>
                <input type="radio" name="o2" value="">
                <span class="cr"><i class="cr-icon glyphicon glyphicon-arrow-right"></i></span>
                Option one is this and that — be sure to include why it's great
            </label>
        </div>
        <div class="radio">
            <label>
                <input type="radio" name="o2" value="" checked>
                <span class="cr"><i class="cr-icon glyphicon glyphicon-arrow-right"></i></span>
                Option two is checked by default
            </label>
        </div>
        <div class="radio disabled">
            <label>
                <input type="radio" name="o2" value="" disabled>
                <span class="cr"><i class="cr-icon glyphicon glyphicon-arrow-right"></i></span>
                Option three is disabled
            </label>
        </div>
    </div>

    <h3>Font awesome example</h3>

    <div class="col-sm-12">
        <div class="radio">
            <label>
                <input type="radio" name="o3" value="">
                <span class="cr"><i class="cr-icon fa fa-circle"></i></span>
                Option one is this and that — be sure to include why it's great
            </label>
        </div>
        <div class="radio">
            <label>
                <input type="radio" name="o3" value="" checked>
                <span class="cr"><i class="cr-icon fa fa-circle"></i></span>
                Option two is checked by default
            </label>
        </div>
        <div class="radio disabled">
            <label>
                <input type="radio" name="o3" value="" disabled>
                <span class="cr"><i class="cr-icon fa fa-circle"></i></span>
                Option three is disabled
            </label>
        </div>
    </div>

    <h3>Font awesome example (other icon)<br/><small>Works best with square icons =)</small></h3>

    <div class="col-sm-12">
        <div class="radio">
            <label>
                <input type="radio" name="o4" value="">
                <span class="cr"><i class="cr-icon fa fa-star"></i></span>
                Option one is this and that — be sure to include why it's great
            </label>
        </div>
        <div class="radio">
            <label>
                <input type="radio" name="o4" value="" checked>
                <span class="cr"><i class="cr-icon fa fa-star"></i></span>
                Option two is checked by default
            </label>
        </div>
        <div class="radio disabled">
            <label>
                <input type="radio" name="o4" value="" disabled>
                <span class="cr"><i class="cr-icon fa fa-star"></i></span>
                Option three is disabled
            </label>
        </div>
    </div>

    <h3>Any size you want depending on label font-size</h3>

    <div class="col-sm-12">
        <div class="radio">
            <label style="font-size: 2.5em">
                <input type="radio" name="o5" value="" checked>
                <span class="cr"><i class="cr-icon fa fa-circle"></i></span>
                Huge
            </label>
        </div>
        <div class="radio">
            <label style="font-size: 2em">
                <input type="radio" name="o5" value="">
                <span class="cr"><i class="cr-icon fa fa-circle"></i></span>
                Big
            </label>
        </div>
        <div class="radio">
            <label style="font-size: 1.5em">
                <input type="radio" name="o5" value="">
                <span class="cr"><i class="cr-icon fa fa-circle"></i></span>
                Bigger
            </label>
        </div>
        <div class="radio">
            <label style="font-size: 1em">
                <input type="radio" name="o5" value="">
                <span class="cr"><i class="cr-icon fa fa-circle"></i></span>
                Default
            </label>
        </div>
        <div class="radio">
            <label style="font-size: .8em">
                <input type="radio" name="o5" value="">
                <span class="cr"><i class="cr-icon fa fa-circle"></i></span>
                Smaller
            </label>
        </div>
        <div class="radio">
            <label style="font-size: .5em">
                <input type="radio" name="o5" value="">
                <span class="cr"><i class="cr-icon fa fa-circle"></i></span>
                Small
            </label>
        </div>
    </div>
</div>
<script type="text/javascript">

</script>
