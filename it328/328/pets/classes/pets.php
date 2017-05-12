<?php
    class Pet
    {
        protected $name;
        protected $color;
        
        function __construct($name="unknown", $color="?")
        {
            $this->name = $name;
            $this->color = $color;
        }
        
        function eat()
        {
            echo $this->name . " is Eating...<br>";
        }
        
        function talk()
        {
            echo $this->name . " is Talking...<br>";
        }
        
        function sleep()
        {
            echo $this->name . " is Sleeping...<br>";
        }
        
        function setName($name)
        {
            $this->name = $name;
        }
        
        function getName()
        {
            return $this->name;
        }
    }