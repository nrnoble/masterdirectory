<?php
    /*
    Name: Marlene Leano
    Date: April 23, 2017
    URL: mleano.greenrivertech.net/IT328/dating
    This file is my Member class.
    */
    
/**
 *  The Member class represents a member of my dating website.
 *
 *  The Member class represents a member with a first name, last
 *  name, age, gender, phone number, email, state, gender sought,
 *  and bio.
 *
 *  @author Marlene Leano <mleano@mail.greenriver.edu>
 *  @copyright 2017
 */
    class Member
    {
    
        //Properties
        protected $fname;
        protected $lname;
        protected $age;
        protected $gender;
        protected $phone;
        protected $email;
        protected $state;
        protected $seeking;
        protected $bio;
        
        //Constructor (parameterized with default values)
        /**
         *  This is the constructor for the Member class.
         *
         *  It creates a Member object with a first name, last name, age,
         *  gender, and phone number. Default values are "unknown."
         *
         *  @param String $fname the first name of the member
         *  @param String $lname the last name of the member
         *  @param int $age the age of the member
         *  @param String $gender the gender of the member
         *  @param String $phone the phone number of the member
         */
        function __construct($fname="unknown", $lname="unknown",
            $age="unknown", $gender="unknown", $phone="unknown")
        {
            $this->fname = $fname;
            $this->lname = $lname;
            $this->age = $age;
            $this->gender = $gender;
            $this->phone = $phone;
        }
        
        //Setters and Getters
        /**
         *  Function that sets the member's first name.
         *
         *  @param String $fname the member's first name
         *  @return void
         */
        function setFirstName($fname)
        {
            $this->fname = $fname;
        }
        
        /**
         * Function that retrieves the member's first name.
         *
         * @return returns the member's first name
         */
        function getFirstName()
        {
            return $this->fname;
        }
        
        /**
         * Function that sets the member's last name.
         *
         * @param String $lname the member's last name
         * @return void
         */
        function setLastName($lname)
        {
            $this->lname = $lname;
        }

        /**
         * Function that retrieves the member's last name.
         *
         * @return returns the member's last name
         */        
        function getLastName()
        {
            return $this->lname;
        }

        /**
         * Function that sets the member's age.
         *
         * @param int $age the member's age
         * @return void
         */        
        function setAge($age)
        {
            $this->age = $age;
        }

        /**
         * Function that retrieves the member's age.
         *
         * @return returns the member's age
         */        
        function getAge()
        {
            return $this->age;
        }

        /**
         * Function that sets the member's gender.
         *
         * @param String $gender the member's gender
         * @return void
         */        
        function setGender($gender)
        {
            $this->gender = $gender;
        }

        /**
         * Function that retrieves the member's gender.
         *
         * @return returns the member's gender; either male or
         * female
         */        
        function getGender()
        {
            return $this->gender;
        }

         /**
         * Function that sets the member's phone number.
         *
         * @param String $phone the member's phone number
         * @return void
         */        
        function setPhone($phone)
        {
            $this->phone = $phone;
        }

        /**
         * Function that retrieves the member's phone number.
         *
         * @return returns the member's phone number
         */         
        function getPhone()
        {
            return $this->phone;
        }

        /**
         * Function that sets the member's email.
         *
         * @param String $email the member's email
         * @return void
         */         
        function setEmail($email)
        {
            $this->email = $email;
        }
        
        /**
         * Function that retrieves the member's email.
         *
         * @return returns the member's email
         */ 
        function getEmail()
        {
            return $this->email;
        }

        /**
         * Function that sets the member's state.
         *
         * @param String $state the member's state
         * @return void
         */         
        function setState($state)
        {
            $this->state = $state;
        }
        
        /**
         * Function that retrieves the member's state.
         *
         * @return returns the member's state
         */         
        function getState()
        {
            return $this->state;
        }

        /**
         * Function that sets the member's sought out gender.
         *
         * @param String $seeking the member's sought out gender.
         * @return void
         */         
        function setSeeking($seeking)
        {
            $this->seeking = $seeking;
        }
 
        /**
         * Function that retrieves the member's sought out gender.
         *
         * @return returns the member's sought out gender; either
         * male or female
         */         
        function getSeeking()
        {
            return $this->seeking;
        }

        /**
         * Function that sets the member's biography.
         *
         * @param String $bio the member's biography
         * @return void
         */         
        function setBio($bio)
        {
            $this->bio = $bio;
        }

        /**
         * Function that retrieves the member's bio.
         *
         * @return returns the member's bio
         */         
        function getBio()
        {
            return $this->bio;
        }
    }
    
    