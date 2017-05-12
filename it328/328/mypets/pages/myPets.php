<pre>
<?php
    //Include the class definition
    //require('classes/pets.php');
    
    //Instantiate the class
    $pet1 = new Pet("Kermit", "green");
    $pet2 = new Pet("Fido");
    $pet3 = new Pet();
    $pet4 = new Pet("", "fuschia");
    $pet4->setName("freddy");
    print("The pet's name is " . $pet4->getName() . "<br>");
    
    //Tell the pet to eat
    $pet1->eat();
    $pet1->talk();
    $pet1->sleep();
    /*
    print_r($pet1);
    print_r($pet2);
    print_r($pet3);
    print_r($pet4);
    */
    $dog1 = new Dog("Kohl", "black");
    $dog1->eat();
    $dog1->fetch();
    
    $dog1 = new Dog("Fifi");
    $dog1->eat();
    $dog1->talk();
    
?>
</pre>