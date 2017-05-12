<script>
    $(function()
    {
        $( "#loginform").dialog({height: 350, width: 350, autoOpen: false});
//
    });


    function showpopup()
    {





        //alert("showpopup()");


        $("#loginform" ).dialog("open");
        //alert("last popup()");

        $("#loginform").css({"visibility":"visible","display":"none"});
        $("#test1").css({"visibility":"visible","display":"block"});
        $("#loginform").fadeIn();

        var show = $("#loginform").dialog( "option", "show" );

    }

    function hidepopup()
    {
        $("#loginform").fadeOut();
        $("#loginform").css({"visibility":"hidden","display":"none"});
        $("#loginform").dialog("close");
    }


</script>



<div id="loginform" title="Administrative Login" style="display: none;" class = "nrn_login_dialog">



        <form id = "Loginform1" method = "post" action = "nrn_dologin.php" style="text-align: center">
            User and Password
            <input type = "text" id = "login" placeholder = "" name = "uid"><br>
            <input type = "password" id = "password" name = "password" placeholder = "">
            <input type = "submit" id = "dologin" value = "Login">
        </form>



</div>
