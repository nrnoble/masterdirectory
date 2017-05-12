<?php
    class Dog extends Pet
    {
        function fetch()
        {
            echo $this->name . " is fetching.<br>";
        }
        
        function talk()
        {
            echo $this->name . " is barking.<br>";
        }
    }