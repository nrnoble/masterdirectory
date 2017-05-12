<!--
Neal Noble
Feb 8th, 2016
IT305
Assignment 6b
--><?php
$errors = [];
$missing = [];
if (isset($_POST['send']))
{
    $expected = ['name', 'email', 'comments'];
    $required = ['name', 'comments'];
    $to = 'Neal Noble<nrnoble@hotmail.com>';
    $subject = 'Feedback from online form';
    $headers = [];
    $headers[] = 'From: nnoble@greenrivertech.net';
    $headers[] = 'Cc: neal@nrnoble.com, nnoble@greenrivertech.net';
    $headers[] = 'Content-type: text/plain; charset=utf-8';
    #$authorized = '-fdavid@example.com';
     $authorized = '';
    require './includes/process_mail.php';
    if ($mailSent)
    {
        header('Location: thanks.php');
        exit;
    }
}
?><!doctype html>
<html lang="en">
<head>
    <base href="./bootstrap-switch-master">
    <meta charset="UTF-8">

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/styles.css">
    <link href="styles.css" rel="stylesheet" type="text/css">


   <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Turn checkboxes and radio buttons into toggle switches.">
    <meta name="author" content="Mattia Larentis, Emanuele Marchi and Peter Stein">
    <title>Bootstrap Switch · Turn checkboxes and radio buttons into toggle switches</title>
    <link href="docs/css/bootstrap.min.css" rel="stylesheet">
    <link href="docs/css/highlight.css" rel="stylesheet">
    <link href="dist/css/bootstrap3/bootstrap-switch.css" rel="stylesheet">
    <link href="http://getbootstrap.com/assets/css/docs.min.css" rel="stylesheet">
    <link href="docs/css/main.css" rel="stylesheet">
    <script>
      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-43092768-1']);
      _gaq.push(['_trackPageview']);
      (function () {
        var ga = document.createElement('script');
        ga.type = 'text/javascript';
        ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(ga, s);
      })();
    </script>






    <style type="text/css">

        body
        {
            text-align:justify;
            font-family: courier;
            font-size: 8pt;
            background-color:#4A62E8;
        }

        a:hover
        {
            background-color: yellow;

            color:blue;
            font-size: 14pt;
            font-weight: bold;
        }

        a
        {
            text-decoration: none;

        }

        b
        {
            color:blue;
        }

        th
        {
            text-decoration: underline;

        }

        tr:nth-child(even)
        {
            background-color: #E0E0E0;
        }

        #text
        {
            text-align: left;
            font-size: 8pt;

        }
        div
        {
            font-size: 8pt;
            margin: auto;
        }

        .page
        {
            max-width: 800px;
            font-size: 12pt;
            background-color: #ffffff;
            border: solid;
            border-width: 1px;
            text-align: left;
            margin-top: 10px;
            padding: 10px;
            box-shadow: 5px 5px 5px #0026FF
        }

        #kfb_contactform
        {
            max-width: 800px;
            font-size: 12pt;
            background-color: #ffffff;
            border: solid;
            border-width: 1px;
            text-align: left;
            margin-top: 10px;
            padding: 10px;
            box-shadow: 5px 5px 5px #0026FF
        }
    </style>

     
  

</head>


    

<body>
    
    
    <section class="container">
        <section class="row">
            <section class="col-xs-12" >
                <div id = assignment class = page style="margin-top: 10px">
                    Neal Noble<br>
                    Feb 8th, 2016<br>
                    IT305<br>
                    Assignment 6b <br>
                </div>

                <div id =kfb_contactform class = "contactform">

            <legend>Select Size</legend>
                <select name="size" id="size">
                    <option value="none">Select a Size</option>
                    <option value="small">Small</option>
                    <option value="medium">Medium</option>
                    <option value="large">Large</option>
                </select>
              

            
            <p class="btn-group">
              </p><div class="btn-group">
                <button type="button" data-toggle="dropdown" class="btn btn-default dropdown-toggle">Set &nbsp;<span class="caret"></span></button>
                <div role="menu" class="dropdown-menu">
                  <li><a data-switch-set="onColor" data-switch-value="primary">Primary</a></li>
                  <li><a data-switch-set="onColor" data-switch-value="info">Info</a></li>
                  <li><a data-switch-set="onColor" data-switch-value="success">Success</a></li>
                  <li><a data-switch-set="onColor" data-switch-value="warning">Warning</a></li>
                  <li><a data-switch-set="onColor" data-switch-value="default">Default</a></li>
                </div>
              </div>
              <button type="button" data-switch-get="onColor" class="btn btn-default">Get</button>
            <p></p>
          </div>
                
                
         <div id = assignment class = page style="margin-top: 10px">
            <!-- Fixed navbar -->
    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Bootstrap theme</a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Themes <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="#" data-theme="default" class="theme-link">Default</a></li>
                <li><a href="#" data-theme="amelia" class="theme-link">Amelia</a></li>
                <li><a href="#" data-theme="cerulean" class="theme-link">Cerulean</a></li>
                <li><a href="#" data-theme="cosmo" class="theme-link">Cosmo</a></li>
                <li><a href="#" data-theme="cyborg" class="theme-link">Cyborg</a></li>
                <li><a href="#" data-theme="flatly" class="theme-link">Flatly</a></li>
                <li><a href="#" data-theme="journal" class="theme-link">Journal</a></li>
                <li><a href="#" data-theme="readable" class="theme-link">Readable</a></li>
                <li><a href="#" data-theme="simplex" class="theme-link">Simplex</a></li>
                 <li><a href="#" data-theme="slate" class="theme-link">Slate</a></li>
                  <li><a href="#" data-theme="spacelab" class="theme-link">Spacelab</a></li>
                  <li><a href="#" data-theme="united" class="theme-link">United</a></li>
              </ul>
            </li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>
<div style="height:80px;"></div>
    <div class="container theme-showcase">

      <!-- Main jumbotron for a primary marketing message or call to action -->
      <div class="jumbotron">
        <h1>Hello, world!</h1>
        <p>This is a template for a simple marketing or informational website. It includes a large callout called the hero unit and three supporting pieces of content. Use it as a starting point to create something more unique.</p>
        <p><a class="btn btn-primary btn-lg">Learn more &raquo;</a></p>
      </div>



      <div class="page-header">
        <h1>Buttons</h1>
      </div>
      <p>
        <button type="button" class="btn btn-lg btn-default">Default</button>
        <button type="button" class="btn btn-lg btn-primary">Primary</button>
        <button type="button" class="btn btn-lg btn-success">Success</button>
        <button type="button" class="btn btn-lg btn-info">Info</button>
        <button type="button" class="btn btn-lg btn-warning">Warning</button>
        <button type="button" class="btn btn-lg btn-danger">Danger</button>
        <button type="button" class="btn btn-lg btn-link">Link</button>
      </p>
      <p>
        <button type="button" class="btn btn-default">Default</button>
        <button type="button" class="btn btn-primary">Primary</button>
        <button type="button" class="btn btn-success">Success</button>
        <button type="button" class="btn btn-info">Info</button>
        <button type="button" class="btn btn-warning">Warning</button>
        <button type="button" class="btn btn-danger">Danger</button>
        <button type="button" class="btn btn-link">Link</button>
      </p>
      <p>
        <button type="button" class="btn btn-sm btn-default">Default</button>
        <button type="button" class="btn btn-sm btn-primary">Primary</button>
        <button type="button" class="btn btn-sm btn-success">Success</button>
        <button type="button" class="btn btn-sm btn-info">Info</button>
        <button type="button" class="btn btn-sm btn-warning">Warning</button>
        <button type="button" class="btn btn-sm btn-danger">Danger</button>
        <button type="button" class="btn btn-sm btn-link">Link</button>
      </p>
      <p>
        <button type="button" class="btn btn-xs btn-default">Default</button>
        <button type="button" class="btn btn-xs btn-primary">Primary</button>
        <button type="button" class="btn btn-xs btn-success">Success</button>
        <button type="button" class="btn btn-xs btn-info">Info</button>
        <button type="button" class="btn btn-xs btn-warning">Warning</button>
        <button type="button" class="btn btn-xs btn-danger">Danger</button>
        <button type="button" class="btn btn-xs btn-link">Link</button>
      </p>



      <div class="page-header">
        <h1>Thumbnails</h1>
      </div>
      <img data-src="holder.js/200x200" src="data:image/png;base64," class="img-thumbnail" alt="A generic square placeholder image with a white border around it, making it resemble a photograph taken with an old instant camera">



      <div class="page-header">
        <h1>Dropdown menus</h1>
      </div>
      <div class="dropdown theme-dropdown clearfix">
        <a id="dropdownMenu1" href="#" role="button" class="sr-only dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
        <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">
          <li role="presentation"><a role="menuitem" tabindex="-1" href="#">Action</a></li>
          <li role="presentation"><a role="menuitem" tabindex="-1" href="#">Another action</a></li>
          <li role="presentation"><a role="menuitem" tabindex="-1" href="#">Something else here</a></li>
          <li role="presentation" class="divider"></li>
          <li role="presentation"><a role="menuitem" tabindex="-1" href="#">Separated link</a></li>
        </ul>
      </div>




      <div class="page-header">
        <h1>Navbars</h1>
      </div>

      <div class="navbar navbar-default">
        <div class="container">
          <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">Project name</a>
          </div>
          <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
              <li class="active"><a href="#">Home</a></li>
              <li><a href="#about">About</a></li>
              <li><a href="#contact">Contact</a></li>
              <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
                <ul class="dropdown-menu">
                  <li><a href="#">Action</a></li>
                  <li><a href="#">Another action</a></li>
                  <li><a href="#">Something else here</a></li>
                  <li class="divider"></li>
                  <li class="dropdown-header">Nav header</li>
                  <li><a href="#">Separated link</a></li>
                  <li><a href="#">One more separated link</a></li>
                </ul>
              </li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
              <li><a href="../navbar/">Default</a></li>
              <li><a href="../navbar-static-top/">Static top</a></li>
              <li class="active"><a href="./">Fixed top</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>

      <div class="navbar navbar-inverse">
        <div class="container">
          <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">Project name</a>
          </div>
          <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
              <li class="active"><a href="#">Home</a></li>
              <li><a href="#about">About</a></li>
              <li><a href="#contact">Contact</a></li>
              <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
                <ul class="dropdown-menu">
                  <li><a href="#">Action</a></li>
                  <li><a href="#">Another action</a></li>
                  <li><a href="#">Something else here</a></li>
                  <li class="divider"></li>
                  <li class="dropdown-header">Nav header</li>
                  <li><a href="#">Separated link</a></li>
                  <li><a href="#">One more separated link</a></li>
                </ul>
              </li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
              <li><a href="../navbar/">Default</a></li>
              <li><a href="../navbar-static-top/">Static top</a></li>
              <li class="active"><a href="./">Fixed top</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>



      <div class="page-header">
        <h1>Alerts</h1>
      </div>
      <div class="alert alert-success">
        <strong>Well done!</strong> You successfully read this important alert message.
      </div>
      <div class="alert alert-info">
        <strong>Heads up!</strong> This alert needs your attention, but it's not super important.
      </div>
      <div class="alert alert-warning">
        <strong>Warning!</strong> Best check yo self, you're not looking too good.
      </div>
      <div class="alert alert-danger">
        <strong>Oh snap!</strong> Change a few things up and try submitting again.
      </div>



      <div class="page-header">
        <h1>Progress bars</h1>
      </div>
      <div class="progress">
        <div class="progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%;"><span class="sr-only">60% Complete</span></div>
      </div>
      <div class="progress">
        <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width: 40%"><span class="sr-only">40% Complete (success)</span></div>
      </div>
      <div class="progress">
        <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100" style="width: 20%"><span class="sr-only">20% Complete</span></div>
      </div>
      <div class="progress">
        <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%"><span class="sr-only">60% Complete (warning)</span></div>
      </div>
      <div class="progress">
        <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width: 80%"><span class="sr-only">80% Complete (danger)</span></div>
      </div>
      <div class="progress">
        <div class="progress-bar progress-bar-success" style="width: 35%"><span class="sr-only">35% Complete (success)</span></div>
        <div class="progress-bar progress-bar-warning" style="width: 20%"><span class="sr-only">20% Complete (warning)</span></div>
        <div class="progress-bar progress-bar-danger" style="width: 10%"><span class='sr-only'>10% Complete (danger)</span></div>
      </div>



      <div class="page-header">
        <h1>List groups</h1>
      </div>
      <div class="row">
        <div class="col-sm-4">
          <ul class="list-group">
            <li class="list-group-item">Cras justo odio</li>
            <li class="list-group-item">Dapibus ac facilisis in</li>
            <li class="list-group-item">Morbi leo risus</li>
            <li class="list-group-item">Porta ac consectetur ac</li>
            <li class="list-group-item">Vestibulum at eros</li>
          </ul>
        </div><!-- /.col-sm-4 -->
        <div class="col-sm-4">
          <div class="list-group">
            <a href="#" class="list-group-item active">
              Cras justo odio
            </a>
            <a href="#" class="list-group-item">Dapibus ac facilisis in</a>
            <a href="#" class="list-group-item">Morbi leo risus</a>
            <a href="#" class="list-group-item">Porta ac consectetur ac</a>
            <a href="#" class="list-group-item">Vestibulum at eros</a>
          </div>
        </div><!-- /.col-sm-4 -->
        <div class="col-sm-4">
          <div class="list-group">
            <a href="#" class="list-group-item active">
              <h4 class="list-group-item-heading">List group item heading</h4>
              <p class="list-group-item-text">Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>
            </a>
            <a href="#" class="list-group-item">
              <h4 class="list-group-item-heading">List group item heading</h4>
              <p class="list-group-item-text">Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>
            </a>
            <a href="#" class="list-group-item">
              <h4 class="list-group-item-heading">List group item heading</h4>
              <p class="list-group-item-text">Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>
            </a>
          </div>
        </div><!-- /.col-sm-4 -->
      </div>



      <div class="page-header">
        <h1>Panels</h1>
      </div>
      <div class="row">
        <div class="col-sm-4">
          <div class="panel panel-default">
            <div class="panel-heading">
              <h3 class="panel-title">Panel title</h3>
            </div>
            <div class="panel-body">
              Panel content
            </div>
          </div>
          <div class="panel panel-primary">
            <div class="panel-heading">
              <h3 class="panel-title">Panel title</h3>
            </div>
            <div class="panel-body">
              Panel content
            </div>
          </div>
        </div><!-- /.col-sm-4 -->
        <div class="col-sm-4">
          <div class="panel panel-success">
            <div class="panel-heading">
              <h3 class="panel-title">Panel title</h3>
            </div>
            <div class="panel-body">
              Panel content
            </div>
          </div>
          <div class="panel panel-info">
            <div class="panel-heading">
              <h3 class="panel-title">Panel title</h3>
            </div>
            <div class="panel-body">
              Panel content
            </div>
          </div>
        </div><!-- /.col-sm-4 -->
        <div class="col-sm-4">
          <div class="panel panel-warning">
            <div class="panel-heading">
              <h3 class="panel-title">Panel title</h3>
            </div>
            <div class="panel-body">
              Panel content
            </div>
          </div>
          <div class="panel panel-danger">
            <div class="panel-heading">
              <h3 class="panel-title">Panel title</h3>
            </div>
            <div class="panel-body">
              Panel content
            </div>
          </div>
        </div><!-- /.col-sm-4 -->
      </div>



      <div class="page-header">
        
        <h1>Wells</h1>
      </div>
      <div class="well">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sed diam eget risus varius blandit sit amet non magna. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Cras mattis consectetur purus sit amet fermentum. Duis mollis, est non commodo luctus, nisi erat porttitor ligula, eget lacinia odio sem nec elit. Aenean lacinia bibendum nulla sed consectetur.</p>
      </div>


     <script>
        
        var themes =
        {
            "default": "//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css",
            "amelia" : "//bootswatch.com/amelia/bootstrap.min.css",
            "cerulean" : "//bootswatch.com/cerulean/bootstrap.min.css",
            "cosmo" : "//bootswatch.com/cosmo/bootstrap.min.css",
            "cyborg" : "//bootswatch.com/cyborg/bootstrap.min.css",
            "flatly" : "//bootswatch.com/flatly/bootstrap.min.css",
            "journal" : "//bootswatch.com/journal/bootstrap.min.css",
            "readable" : "//bootswatch.com/readable/bootstrap.min.css",
            "simplex" : "//bootswatch.com/simplex/bootstrap.min.css",
            "slate" : "//bootswatch.com/slate/bootstrap.min.css",
            "spacelab" : "//bootswatch.com/spacelab/bootstrap.min.css",
            "united" : "//bootswatch.com/united/bootstrap.min.css"
            }
            $(
              function()
              {
                var themesheet = $('<link href="'+themes['default']+'" rel="stylesheet" />');
                themesheet.appendTo('head');
                $('.theme-link').click(function()
                  {
                   var themeurl = themes[$(this).attr('data-theme')]; 
                       themesheet.attr('href',themeurl);
                   }
                  );
              }
            );
        
     </script>


    </div>
         </div>
    
<!--    
    <div class="col-sm-8">
        <div class="input-group">                                            
            <input type="TextBox" ID="datebox" Class="form-control"></input>
            <div class="input-group-btn">
                <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
                    <span class="caret"></span>
                </button>
                <ul id="demolist" class="dropdown-menu">
                    <li><a href="#">A</a></li>
                    <li><a href="#">B</a></li>
                    <li><a href="#">C</a></li>
                </ul>
            </div>
        </div>
    </div>
    
    <script>
        
        $('#demolist li').on('click', function()
         {
           $('#datebox').val($(this).text());
          }
         );
        
    </script>-->
            </section>
        </section>
    </section>



    <footer class="bs-docs-footer">
      <div class="container">
        <p>Code licensed under <a href="http://www.apache.org/licenses/LICENSE-2.0" target="_blank">Apache License, Version 2.0</a><br>Created by <a href="https://github.com/nostalgiaz" target="_blank">Mattia Larentis</a><br>Mantained by <a href="https://github.com/lostcrew" target="_blank">Emanuele Marchi</a>
        </p>
      </div>
    </footer>

    <script src="docs/js/jquery.min.js"></script>
    <script src="docs/js/bootstrap.min.js"></script>
    <script src="docs/js/highlight.js"></script>
    <script src="dist/js/bootstrap-switch.js"></script>
    <script src="docs/js/main.js"></script>



</body>
</html>