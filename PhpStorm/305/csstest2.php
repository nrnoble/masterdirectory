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
    <script type="text/javascript" src="Bootstrap/js/jquery-2.2.0.min.js"></script>


    
    
    
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

 <script type="text/javascript">
        
        function DebugAlert(msg,debug)
        {
            if (debug)
            {
                alert (msg);
            }
        }
        
        function setCookie(CookieName, ThemeName)
        {
            DebugAlert("setCookie:: CookieName=" +  CookieName +   "; Theme name is: " + ThemeName,debug);
            var cookie = CookieName + "=" + ThemeName + "; expires=Sat, 31 Dec 2016 12:00:00 UTC";
            DebugAlert("setCookie:: The cookie being set is: " + cookie, debug);
            document.cookie = cookie;
            DebugAlert("setCookie:: Debug Checking '" + CookieName + "' value: " + "getCookie('" + CookieName + "')) = " + getCookie(CookieName),debug);
            
        }

        function getCookie(cname)
        {
            var name = cname + "=";
            //alert("Debug. The entire cookie is: " + document.cookie);
            DebugAlert ("getCookie:: cname=" + cname,debug);
            var ca = document.cookie.split(';');
            for(var i=0; i<ca.length; i++)
            {
                var c = ca[i];
                while (c.charAt(0)==' ') c = c.substring(1);
                if (c.indexOf(name) == 0)
                {
                    DebugAlert("getCookie:: returning: " + c.substring(name.length,c.length),debug);
                    return c.substring(name.length,c.length);
                }
            }
            
            DebugAlert("getCookie:: returning: Opppps",debug);
            return "Oppps";
        }
        
        function SetTheme(ThemeFileName)
        {
            //alert("Setting theme to: " + ThemeFileName);
            var head  = document.getElementsByTagName('head')[0];
            var link  = document.createElement('link');
            link.id   = ThemeFileName;
            link.rel  = 'stylesheet';
            link.type = 'text/css';
            link.href = ThemeFileName;
            link.media = 'all';
            head.appendChild(link);
            DebugAlert ("ThameFileName="+ThemeFileName,debug);
            setCookie("Theme",ThemeFileName);
            cssId ="";
        }

    </script>
    
    <style type="text/css">

    </style>
   
<script type="text/javascript">
    //SetTheme("test.css");
    var debug = false;
    DebugAlert ("Script::: getCookie(\"Theme\")",debug);
    var Theme = getCookie("Theme");
    
    
    
    // document.getElementById("demo").innerHTML = "checking theme name " + theme;
    if (typeof(Theme) == "undefined")
    {
        DebugAlert("No theme has been set",debug);
        var ThemeFileName = "test.css";
        
        SetTheme(ThemeName);
        setCookie("Theme", ThemeFileName);
        //document.getElementById("demo").innerHTML = "The theme is: " + Theme;
    }
    else
    {
        DebugAlert("Script:: setting theme to::: " + Theme,debug);
        SetTheme(Theme);
        //document.getElementById("demo").innerHTML = "The theme is: " + getCookie("Theme");
    }
</script>
     
  

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

                <div id = assignment class = page style="margin-top: 10px">

                    <script type="text/javascript">


                
                </script>
                
                <div id="msgid">
                </div>
                
                <legend>Select Size</legend>
                <select id ="size" name="size" onmousedown="this.value='';" onchange="ChangeThemes(this.value);">
                <!--<select name="size" id="size">-->
                    <option value="none">Select a Size</option>
                    <option value="small">Small</option>
                    <option value="medium">Medium</option>
                    <option value="large">Large</option>
                </select>                      
                 
                 <script type="text/javascript">
                    function ChangeThemes(value)
                    {
                        //var h = document.getElementsByTagName('head').item(0);
                        //var s = document.createElement("link");
                        //s.type = "text/css"; 
                        //s.appendChild(document.createTextNode("href=\"test.css\ rel=\"stylesheet\""));
                        //h.appendChild(s);
                        var cssfile = "";
                         var cssId = "";
                        if (value == "option-1")
                        {
                            cssfile = 'kfb_style.css';
                            cssId = value;
                        }
                        
                        if (value == "option-2")
                        {
                            cssfile = 'neal.css';
                            cssId = value;
                        }
                        
                        if (value == "option-3")
                        {
                            cssfile = 'kfb_style_2.css';
                            cssId = value;
                        }

                        
                        

                        var cssId = 'myCss';  // you could encode the css path itself to generate id..
                        //if (!document.getElementById(cssId))
                        if (value!="") 
                        {                        
                            
 
                        $(document).ready(function(){
                         $("#msgid").html("This is Hello World by JQuery " + value );
                           });
                            // $('link[id=myCss2]').remove();
                            //$('link[id=myCss1]').remove();
                            //$("link[href='test.css']").remove();
                            //$('link[rel=stylesheet][href="test.css"]').remove();
                            //$('link[rel=stylesheet][href="test2.css"]').remove();
                            //$("link[href='test.css']").prop('disabled', true);
                            //$("link[href='test2.css']").prop('disabled', true);
                            //var head  = document.getElementsByTagName('head')[0];
                            //var link  = document.createElement('link');
                            //link.id   = cssId;
                            //link.rel  = 'stylesheet';
                            //link.type = 'text/css';
                            //link.href = cssfile;
                            //link.media = 'all';
                            //head.appendChild(link);
                            //cssId ="";
                            SetTheme(cssfile);
                            
                        }
                         
                    }
                </script>
                 

                 
                 
                
                        <p id="demo"></p>
                        
                        <script>
                        document.getElementById("demo").innerHTML = "Hello JavaScript!";
                        
                        </script>
                        


                </div>


                <div id = assignment class = page style="margin-top: 10px">

                 <h3>block of text goes here</h3>
                </div>

                <div id = assignment class = page style="margin-top: 10px">

                 <h3>block of text goes here</h3>
                </div>

            
            
            </section>
        </section>
    </section>




    <script src="bootstrap/js/jquery.min.js"></script>
    <script src="bootstrap/js/bootstrap.min.js"></script>
    <script src="bootstrap/js/highlight.js"></script>
    <script src="bootstrap/js/bootstrap-switch.js"></script>
    <script src="bootstrap/js/main.js"></script>



</body>
</html>