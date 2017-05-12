<?php
	// Turn on error reporting
   ini_set('display_errors', 1);
   error_reporting(E_ALL);

	// Include the pizza validation functions
	include ("includes/pizzaFunctions.php");
?>

<!DOCTYPE html>

<html>
<head> 
    <title>Poppa's Pizza</title>
	<link rel="stylesheet" type="text/css" href="styles/pizzaStyles.css">
	
<style>

    #page
    {
        max-width: 900px;
        font-size: 12pt;
        background-color: #ffffff;
        border: solid;
        border-width: 1px;
        text-align: left;
        margin-top: 100px;
        padding: 25px;
        box-shadow: 5px 5px 5px #9C2700
    }
	
	
	.response
    {
       text-align: center;
       border-width: 1px;
       
       background-color: gray;
       color: black;
    }
	
	


.centered
{
    margin: 0 auto;
    text-align: left;
    width: 800px;
}

</style>
	
</head>

<body>
	
	<?php
	//See if the form has been submitted

   if (isset($_GET['submit']))
   {

		$fname = "";
		$lname = "";
		//Create a boolean flag to track validation errors
		$isValid = true;

		//Check first name
		if (validName($_GET['fname']))
		{
		    $fname = $_GET['fname'];
		}
		else
		{
		    print "<p>Invalid first name.</p>";
		    $isValid = false;
		}
		
		//Check last name
		if (validName($_GET['lname']))
		{
		    $lname = $_GET['lname'];
		} else
		{
		    print "<p>Invalid last name.</p>";
		    $isValid = false;
		}
		
		
		//Get the method (pick up or delivery)
		$method = "";
		if (isset($_GET['method']) AND validMethod($_GET['method']))
		{
		    $method = $_GET['method'];
		}
		else
		{
		    print "<p>Please select Pick-up or Delivery.</p>";
		    $isValid = false;                
		}

	   //Get toppings
		if (isset($_GET['toppings']))
		{
		    $toppings = $_GET['toppings'];
		    if (!validToppings($toppings))
			{
				print "Aack! I've been spoofed.";
				return;
		    }
		    $toppingCount = sizeof($toppings);
		}
		

		// Check for address if method is delivery
		if ($method == 'delivery')
		{
		    if (!empty($_GET['address']))
			{
				$address = $_GET['address'];
		    } else
			{
				print '<p>Please enter a delivery address.</p>';
				$isValid = false;                     
		    }
		}

		
		// Display summary
		if ($isValid)
		{
			echo "<span class = \"response\" style = \"text-align:center; \">";
				echo "<div id = page >";
				echo "Thank you for your order, $fname $lname";
				echo "<p>Method: $method</p>";
	
				//Display address if method is delivery
				if ($method == "delivery")
				{
					print "<p>Address: $address</p>";
				}
	
				//Display toppings if selected
				if ($toppingCount > 0)
				{
					print "<p>Toppings: " . implode(", ", $toppings) . "</p>";
					print "<p>Topping count: $toppingCount</p>";
				}
				echo "</div>";
			echo "</span>";
		    //We're done! Terminate the script.
		    
			
			
			
			return;

	}


   }
?>
	
    <div id="main">
	<h1>Welcome to Poppa's Pizza</h1>
	<form method="get" action="">
            
                <fieldset>
                    <legend>Contact Info</legend>
                    First Name:&nbsp;<input type="text" size="20" maxlength="20" name="fname" id="fname">&nbsp
		    Last Name:&nbsp;<input type="text" size="20" maxlength="20" name="lname" id="lname"><br>
		    <label>Address:<br>
                        <textarea rows="5" cols="20" name="address" id="address"></textarea>
                    </label>
                </fieldset>

		<fieldset>
                    <legend>Choose One</legend>
		    <label><input type="radio" value="pickup" name="method" id="method">&nbsp;Pick-up</label><br>
		    <label><input type="radio" value="delivery" name="method" id="method">&nbsp;Delivery</label>		
                </fieldset>

                <fieldset>
                    <legend>Toppings</legend>
                    <label><input type="checkbox" value="pepperoni" name="toppings[]" >
                            Pepperoni</label><br>
                    <label><input type="checkbox" value="sausage" name="toppings[]" >
                            Sausage</label><br>
                    <label><input type="checkbox" value="olives" name="toppings[]" >
                            Olives</label><br>
                    <label><input type="checkbox" value="artichokes" name="toppings[]" >
                            Artichokes</label><br>
                    <label><input type="checkbox" value="anchovies" name="toppings[]" >
                            Anchovies</label><br>
                </fieldset>

		<fieldset>
                    <legend>Crust</legend>
                    <label><input type="radio" value="thin" name="crust" checked="checked">
                            Thin</label><br>
                    <label><input type="radio" value="thick" name="crust" >
                            Thick</label><br>
                    <label><input type="radio" value="wheat" name="crust" >
                            Wheat</label><br>
                    <label><input type="radio" value="glutenfree" name="crust" >
                            Gluten-free</label><br>
                </fieldset>
				
		<fieldset>
                    <legend>Select Size</legend>
		    <select name="size" id="size">
			<option value="none">Select a Size</option>
			<option value="small">Small</option>
			<option value="medium">Medium</option>
			<option value="large">Large</option>
		    </select>
		</fieldset>
		
		<p><input type="submit" id="submit" name="submit" value="Submit your order" /></p>
	</form>
    </div>
</body>
</html>
