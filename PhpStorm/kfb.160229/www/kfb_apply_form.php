<?php include "kfb_head.html" ?>
<?php
//  application Form
// Kandis Brighton

$errors = [];
$missing = [];
if (isset($_POST['send'])) {
    $expected = ['name', 'email', 'comments'];
    $required = ['name', 'comments'];
    $to = 'Kandis <kbrighton@mail.greenriver.edu>';
    $subject = 'Feedback from online form';
    $headers = [];
    $headers[] = 'From: kbrighton@mail.greenriver.edu';
    $headers[] = 'Cc: kandisbrighton@gmail.com';
    $headers[] = 'Content-type: text/plain; charset=utf-8';
    $authorized = null; //'-kbrighton@mail.greenriver.edu';
    require './includes/process_mail.php';
    if ($mailSent) {
        header('Location:thanks.php');
        exit;
    }
}
?>
<body class="no-trans   ">
    <div class="container">
      <div class="row">
        <div class ="kfb_form">
    
	
<?php
     // Kandis Brighton IT 305 Application Form for KaNeSeS Kent Food Bank
     
     // form validation functions
	 
    // validName returns true if $string is not empty and is apphabetic.
    function validName($name)
    {
      return ctype_alpha($name) AND !empty($name);
    }
    function validString($string)
    {
      return !empty($string);
    }
    
    function validActivities($activities)
    {
         $validActivitiesArray = array("clothing","office","food");
         foreach ($activities as $activity)
         {
            if (!in_array($activity, $validActivitiesArray))
            {
              return false;
            }
         }
        // if we made it this far, all of our activities are valid
         return true;
    }
    // check if our App type is valid
    function validAppType($apptype)
    {
         $validAppArray = array("individual","group","organization", "school", "courtordered");
		 
	     if (!in_array($apptype, $validAppArray))
            {
              return false;
            }
         // if we made it this far, the app is valid
         return true;
    }
  
 		// see if the form has been submitted, check for validation and terminate form
		if (isset($_GET['submit']))
        {
			//create a boolean flag to track validation errors
			$isValid = true;
			$fname = "";
			//check first name

			if (validName($_GET['fname'])) {
				$fname = $_GET['fname'];
			} else {
				print "<p>Please enter a valid first name.</p>";
				$isValid = false;
			}
			$lname = "";
			if (validName($_GET['lname'])) {
				$lname = $_GET['lname'];
			} else {
				print "<p>Please enter a valid last name.</p>";
				$isValid = false;
			}
			
			$email = "";
			if (validString($_GET['email'])) {
				$email = $_GET['email'];
			} else {
				print "<p>Please enter a valid email.</p>";
				$isValid = false;
			}
			
			$phonenumber = "";
			if (validString($_GET['phonenumber'])) {
				$phonenumber = $_GET['phonenumber'];
			} else {
				print "<p>Please enter a valid phone number.</p>";
				$isValid = false;
			}

	
			// check if apptype is valid
			$apptype = "";
			if (isset($_GET['apptype']) AND validAppType($_GET['apptype'])) {
				$apptype = $_GET['apptype'];
			} else {
				print "<p>Please select an application type.</p>";
				$isValid = false;
			}
			
			// check if activities are valid
			
			$activitiesChosen = "";
			
			if (isset($_GET['activities'])) {
				$activitiesChosen = $_GET['activities'];
				if (!validActivities($activitiesChosen)) {
					print "<p>Please select at least one activity.</p>";
					$isValid = false;
					//return;
                }
			} else { 
				print "<p>Please select at least one activity.</p>";
					$isValid = false;
			}
			
			$availability = "";
			if (validString($_GET['availability'])) {
				$availability = $_GET['availability'];
			} else {
				print "<p>Please enter the times you are available.</p>";
				$isValid = false;
			}
			
			$whyvolunteer = "";
			if (validString($_GET['whyvolunteer'])) {
				$whyvolunteer = $_GET['whyvolunteer'];
			} else {
				print "<p>Please tell us why you are applying.</p>";
				$isValid = false;
			}
			// if the form is valid then terminate the program and pring out the following.

			if ($isValid)
			{
				// call the termination page.
				   print "<div id=summary>";
				   print "<h1>Volunteer Summary</h1>";
				   
				   print "<p>Thank you for your application, $fname $lname.</p>";

				   print "<p>Email: $email</p>";
				   print "<p>Phone Number: $phonenumber</p>";
				   print "<p>Application Type: $apptype</p>";
				   print "<p>Activities: ";
				
				   for ($i=0; $i<sizeof($activitiesChosen); $i++)
			       {
						   print "$activitiesChosen[$i] ";
			       }
				   
				   print "</p>";
				   print "<p>Availability: </p>";
				   print "<p> $availability </p>";
				   print "<p>Reasons for volunteering: </p>";
				   print "<p>$whyvolunteer</p>";
				   
				
				   return;
            }
        }				   

?>      
    	
        <h1>Kent Food Bank and Emergancy Services</h1>
        <h2>Volunteer Form</h2>
        <form id="volunteer_form" action= "" method="get">
            <fieldset>
               <legend>Contact Info</legend>
                    First Name:&nbsp;<input type="text" size="20" maxlength="20" name="fname" id="fname" value ="<?php echo $fname; ?>" >&nbsp;
				    Last Name:&nbsp;<input type="text" size="20" maxlength="20" name="lname" id="lname" value ="<?php echo $lname; ?>" ><br>
					Email:&nbsp;<input type="text" size="20" maxlength="20" name="email" id="email" value ="<?php echo $email; ?>" >
					Phone Number:&nbsp;<input type="text" size="20" maxlength="20" name="phonenumber" id="phonenumber" value ="<?php echo $phonenumber; ?>" ><br>
			</fieldset>

            <fieldset>
                <legend>Application Type</legend>
				 
                <label><input type="radio" value="individual" name="apptype" id="apptype"
				<?php
				if ($apptype == "individual") {
					echo 'checked="checked"';
				}
				?>
				>Individual</label><br>
                <label><input type="radio" value="group" name="apptype" id="apptype"
				<?php
				if ($apptype == "group") {
					echo 'checked="checked"';
				}
				?>
				>Group</label><br>
                <label><input type="radio" value="organization" name="apptype" id="apptype"
				<?php
				if ($apptype == "organization") {
					echo 'checked="checked"';
				}
				?>
				>Organization</label><br>
                <label><input type="radio" value="school" name="apptype" id="apptype"
				<?php
				if ($apptype == "school") {
					echo 'checked="checked"';
				}
				?>
				>School</label><br>
                <label><input type="radio" value="courtordered" name="apptype" id="apptype"
				<?php
				if ($apptype == "courtordered") {
					echo 'checked="checked"';
				}
				?>
				>Court Ordered Community Service</label><br>
            </fieldset>
          
            <fieldset>
                <legend>Volunteer Activities Offered:</legend>
                <label><input type="checkbox" name="activities[]" value="clothing"
				<?php
				if (sizeof($activitiesChosen)>0 && in_array("clothing", $activitiesChosen)) {
					echo 'checked="checked"';
				}
				?>
				>Clothing</label><br>
                <label><input type="checkbox" name="activities[]" value="office"
				<?php
				if (sizeof($activitiesChosen)>0 && in_array("office", $activitiesChosen)) {
					echo 'checked="checked"';
				}
				?>
				>Office</label><br>
                <label><input type="checkbox" name="activities[]" value="food"
				<?php
				if (sizeof($activitiesChosen)>0 && in_array("food", $activitiesChosen)) {
					echo 'checked="checked"';
				}
				?>
				>Food</label><br>
             </fieldset>

			<fieldset>
				<legend>Questions</legend>	
		            <label>Availability:<br>
						<textarea rows="5" cols="40" name="availability" id="availability"  ><?php echo $availability; ?></textarea>
					</label><br>
					<label>Why are you interested in volunteering at the Kent Food Bank?<br>
						<textarea rows="5" cols="40" name="whyvolunteer" id="whyvolunteer" ><?php echo $whyvolunteer; ?></textarea>
					</label>
            </fieldset>
             <p>
                <input type="submit" id="submit" name="submit" value="Submit your Application">
            </p>
        </form>
        
                                
 
      </div> 
    </div> <!-- row end --> 
  </div> <!-- container end -->
</body>
<html>