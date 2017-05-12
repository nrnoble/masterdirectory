<script>
    $(function()
    {
        $( "#thank_you").dialog({height: 350, width: 350, autoOpen: false});
//
    });


    function showpopup_thank_you()
    {


        //alert("showpopup_thank_you()");


        $("#thank_you").dialog("open");
        //alert("last popup()");

        $("#thank_you").css({"visibility":"visible","display":"none"});
        //$("#test1").css({"visibility":"visible","display":"block"});
        $("#thank_you").fadeIn();

        var show = $("#thank_you").dialog( "option", "show" );

    }

    function hidepopup()
    {
        $("#thank_you").fadeOut();
        $("#thank_you").css({"visibility":"hidden","display":"none"});
        $("#thank_you").dialog("close");
    }


</script>


<div id="thank_you" title="Thank You" style="display: none; text-align: center" class = "kfb_login_dialog">



      <h1> Thanks for taking the time to contact Neal</h1>



</div>
