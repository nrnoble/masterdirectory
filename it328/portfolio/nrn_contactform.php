<?php

// Check if session has been started, if not then start
if(!isset($_SESSION))
{
	session_start();
}

// include global configuration variables
include "nrn_config.php";
$name_err = "";
$email_err = "";
$security_check = true;

if (isset($_POST['send']))
{

    #require './includes/validate.php';
    #require 'functions.php';


    $name  		= trim(htmlentities($_POST['name']));
    $comments   = trim(htmlentities($_POST['comments']));
    $email		= trim(htmlentities($_POST['email']));



    if(!strstr($_SERVER['HTTP_REFERER'],$_SESSION["site_HTTP_REFERER"] ))
	{
		die("Are you lost?");
	}



   if (ctype_alpha ($name) == false || $name == "")
   {
	   $security_check = false;
	   $_SESSION["name_err"] = "    <-- Must be A-Z";
	   $name_err = $_SESSION["name_err"];
   }


	if (strpos($email, '@') == false || $email == "")
	{
		$security_check = false;
		$_SESSION["email_err"] = "    <-- must include '@'";
		$email_err = $_SESSION["email_err"];

	}

	if ($comments == "")
	{
		$security_check = false;
		$_SESSION["comments_err"] = "    <--Please enter a short message";
		$comments_err = $_SESSION["comments_err"];
	}

}




if (isset($_POST['send']) && ($security_check == true))
{
	//echo("<h2>sending email...</h2>"); 
    $expected = ['name', 'email', 'comments'];
    $required = ['name', 'comments'];
    $to = $_POST['email'];
    $subject = $_SESSION["email_subject"];
    $headers = [];
    #$headers[] = 'From: ' . $_SESSION["email_from"];
    $headers[] = 'From: ' . $_SESSION["email_from"];
    $headers[] = 'Cc: ' . $_SESSION["email_cc"];
	#print_r($_session);
    //$headers[] = 'Content-type: text/plain; charset=utf-8';
	$headers[] = "'MIME-Version: 1.0'";
	$headers[] = "Content-type: text/html; charset=iso-8859-1";
     $authorized = '';

	$_SESSION['name'] = $_POST['name'];
	$_SESSION['email'] = $_POST['email'];
	$_SESSION['comments'] = $_POST['comments'];
#print_r($headers);
    require './kfb_includes/process_mail.php';

    if ($mailSent)
    {
        // print_r($_POST);
        // $_SESSION['name'] = $_POST['name'];
        // $_SESSION['email'] = $_POST['email'];
        // $_SESSION['comments'] = $_POST['comments'];
        // echo "<script>showpopup();</script>";
        header('Location: nrn_contact_add.php');



        exit;
    }



    $errors = [];
$missing = [];
}
?>
<?php include "nrn_head.php" ?>








<body class="no-trans kfb_background">


<?php #include "thankyou_dialog.php";

if ($mailSent)
{
    echo "<script>alert(\"Thank you\");</script>";
    exit;
}

?>



<?php include "nrn_menubar.php" ?>

<?php include "nrn_login_dialog.php" ?>

 <div class="page-wrapper" >

		<!-- main-container start -->
			<!-- ================ -->
			<section class="main-container kfb_background">

				<div class="container">
					<div class="row">
						
<!-- Think carefully before modifying code above this line  -->

					<!-- KFB page content starts here  -->
					
						<div class="main col-md-9">
							
		
						
						<div id = pageblock1s class = "pageblock">
						
						
						 
							<div id = "kfb_contactform" class="container" style="width: inherit">
						  
						  
						  
							<form action="<?= $_SERVER['PHP_SELF']; ?>" method="post" >
							  <div class="col-md-9">
					  
								<div class="well well-sm">
                                    <strong style = "color: blue">
										<i class="glyphicon;"></i>
										Contact Neal Noble</strong>
								</div>
							  
								<div class="form-group">
<!--								  <label for="InputName">Your Name</label>-->
									<?php
										if ($name_err != "")
										{
											echo "<label>Your Name $name_err</label>";
											$name_err != "";
										}
										else
										{
											echo "<label>Your Name</label>";
											$name_err != "";
										}
									?>

											  <div class="input-group">

									  <input type="text" class="form-control" name="name" id="name" placeholder="Enter Name" value = '<?php echo "$name" ?>' required>


									  <span class="input-group-addon"><i class="glyphicon glyphicon-ok form-control-feedback"></i></span></div>
								</div>
								<div class="form-group">
<!--								  <label for="InputEmail">Your Email</label>-->
									<?php
									if ($email_err != "")
									{
										echo "<label> Your Email $email_err </label>";
										$email_err = "";
									}
									else
									{
										echo "<label> Your Email </label >";
										$email_err = "";
									}
									?>
									<div class="input-group">
									<input type='email' class='form-control' id='email' name='email' placeholder='Enter Email' value = '<?php echo "$email" ?>' required>

									<span class="input-group-addon"><i class="glyphicon glyphicon-ok form-control-feedback"></i></span></div>
								</div>
								<div class="form-group">
<!--								  <label for="InputMessage">Message</label>-->

									<?php
									if ($comments_err != "")
									{
										echo "<label>Comments $comments_err </label>";
										$comments_err = "";
									}
									else
									{
										echo "<label>Comments</label>";
									}
									?>


								  <div class="input-group">
									<textarea name="comments" id="InputMessage" class="form-control" rows="5" required><?php echo "$comments" ?></textarea>
									<span class="input-group-addon"><i class="glyphicon glyphicon-ok form-control-feedback"></i></span></div>
								</div>
					  
					  <!--		  <div class="form-group">-->
					  <!---->
					  <!--			<label for="InputReal">What is 4+3? (Simple Spam Checker)</label>-->
					  <!--			<div class="input-group">-->
					  <!--			  <input type="text" class="form-control" name="InputReal" id="InputReal" required>-->
					  <!--			  <span class="input-group-addon"><i class="glyphicon glyphicon-ok form-control-feedback"></i></span></div>-->
					  <!--		  </div>-->
					  
								<input type="submit" name="send" id="send" value="send" class="btn btn-info pull-left">
							  </div>
							</form>
					  </div>


  
  
 
						
		
						
						
							
						</div> 
						

						
					
						</div>
					<!-- KFB page content ends here  -->
					
<!-- Think carefully before modifying code below this line  -->

						<!-- sidebar start -->
						<!-- ================ -->
						    
								<?php# include "kfb_sidebar_contactform.php" ?>
							
						<!-- sidebar end -->

					</div>
				
				</div>
			
			</section>
			<!-- main-container end -->
			
			
			
		</div>
		<!-- page-wrapper end -->

 			<!-- sidebar start -->


<?php #include "kfb_footer.html" ?>
</body>
</html>
