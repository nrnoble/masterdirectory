
<!--
Define a function in pizzaFunctions.php called validName($name).
The validName function should return true if:
The name is not blank.
The name contains only characters.
-->

<?php

	function validName($name)
    {
		if (!empty($name) and ctype_alpha($name))
        {
			return true;
		} else {
			return false;
		}
	}
    
    
    function validMethod($method)
    {
		if ($method == "pickup" OR $method == "delivery") {
			return true;
		} else {
			return false;
		}
	}

    
		
    function validToppings($toppings)
    {

		// define an array of valid toppings
       $validToppings = array("pepperoni", "sausage",
                              "olives", "artichokes", "anchovies");

		// heck each selected topping, and return false
		// f it's not valid
 		foreach ($toppings as $topping)
        {
			if (!in_array($topping, $validToppings))
            {
      			return false;
			}
		}
 
   
		// If we made it this far, all our toppings are valid
		return true;
    }
    

?>	
