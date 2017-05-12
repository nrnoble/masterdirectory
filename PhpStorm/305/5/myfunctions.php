<!--
Neal Noble
feburary 1st, 2016
IT305
Assignment 5a myfunctions.php
-->

<?php
		#echo "<h1>myfuction start</h1>"; 
        function validName($string)
        {
            return ctype_alpha($string)
                AND !empty($string);
        }
		
		function validYear($string)
		{		
				return !empty($string) AND
						is_numeric($string) 
						AND strlen($string) == 4
						AND $string >= 1800;	         
		}
		#echo "<h1>myfuction end</h1>"; 
?>
