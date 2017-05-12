<?php
if(!isset($_SESSION))
{
	session_start();
}
else
{
//	$sessionID = $
}

if (empty($_POST['logout']))
	$_POST['logout'] = "";

	if ($_POST['logout']== "istrue")
	{
		$_SESSION['access'] = false;
		$_POST['logout'] = null;
		header('Location: index.php');
	}
	else
	{
		//header('Location: index.php');
	}







if ($_SESSION['access'] == true)
{
	//echo "<script>alert('login true')</script>";
}
else
{

	$test = "login false";

	echo "<script>alert('$test')</script>";
	header('Location: index.php');
}

?><?php include "kfb_head.php" ?>

<body class="no-trans   ">

<?php include "kfb_menubar.php" ?>


<div class="page-wrapper">

	<!-- main-container start -->
	<!-- ================ -->
	<section class="main-container kfb_background">

		<div class="container">


				<!-- main start -->

				<div class="main col-md-9">

					<div id = "volunteers" class = "pageblock">
						<h2>Contact List</h2>

						<form id = "logout" method = "post" action = "kfb_administrative.php" >
							<input type="hidden" name="logout" id="hiddenField" value="istrue" />
							<input type = "submit" id = "logout1" value="Logout">
						</form>


					</div>


					<?php include "nrn_contact_list.php"; ?>


					<div id = 'kfb_themes' class = "pageblock" style="display: none">
						Themes
						<select id ="themeId" name ="kfb_themes" onmousedown="this.value='';" onchange="ChangeThemes(this.value);">
							<!--<select name="size" id="size">-->
							<option value="custom-1">Default</option>
							<option value="custom-2">Spring</option>
							<option value="custom-3">Summer</option>
							<option value="custom-4">Christmas</option>
							<option value="custom-5">Solid Colors</option>
						</select>


						<script type="text/javascript">
							function ChangeThemes(value)
							{
								debug=false;
								//var h = document.getElementsByTagName('head').item(0);
								//var s = document.createElement("link");
								//s.type = "text/css";
								//s.appendChild(document.createTextNode("href=\"test.css\ rel=\"stylesheet\""));
								//h.appendChild(s);
								var cssfile = "";
								var cssId = "";
								DebugAlert("ChangeThemes:: value=" + value, debug);

								if (value == "custom-1")
								{
									cssfile = 'kfb_style.css';
									cssId = value;
								}

								if (value == "custom-2")
								{
									DebugAlert("ChangeThemes:: Changing them to 'neal.css'", debug);
									cssfile = 'kfb_style_2.css';
									cssId = value;
								}

								if (value == "custom-3")
								{
									cssfile = 'kfb_style_3.css';
									cssId = value;
								}

								if (value == "custom-4")
								{
									cssfile = 'kfb_style_4.css';
									cssId = value;
								}
								if (value == "custom-5")
								{
									cssfile = 'neal.css';
									cssId = value;
								}

								DebugAlert("ChangeThemes:: cssfile=" + cssfile, debug);

								//var cssId = 'myCss';  // you could encode the css path itself to generate id..
								//if (!document.getElementById(cssId))
								if (value!="")
								{

									// $(document).ready(function(){
									//$("#msgid").html("This is Hello World by JQuery " + value );
									//});
									// $('link[id=myCss2]').remove();
									//$('link[id=myCss1]').remove();
									$("link[href='kfb_style.css']").remove();
									//$("link['kfb_style.css']");
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
									//cssfile = 'kfb_style.css';
									DebugAlert("ChangeThemes:: SetTheme('" + cssfile + "');",debug );
									SetTheme(cssfile);
								}
							}
						</script>
					</div>

				</div>


			</div>

		</div>

	</section>
	<!-- main-container end -->



</div>
<!-- page-wrapper end -->
</div>
<!-- sidebar start -->


<?php #include "kfb_footer.html" ?>
</body>
<html>