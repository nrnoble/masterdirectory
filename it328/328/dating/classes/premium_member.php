<?php
    /*
    Name: Marlene Leano
    Date: April 23, 2017
    URL: mleano.greenrivertech.net/IT328/dating
    This file is my Premium Member class.
    */
    
/**
 *  The Premium Member class represents members of my
 *  dating website with premium membership.
 *
 *  The Premium Member class has all the properties of the
 *  Member class plus indoor and outdoor interests.
 *
 *  @author Marlene Leano <mleano@mail.greenriver.edu>
 *  @copyright 2017
 */
    class PremiumMember extends Member
    {
        //Properties
        private $_inDoorInterests;
        private $_outDoorInterests;
        
        //Setters and Getters
        /**
         * Function that sets the member's indoor interests.
         *
         * @param array $_inDoorInterests the member's indoor interests
         * @return void
         */
        function setInDoorInterests($_inDoorInterests)
        {
            $this->_inDoorInterests = $_inDoorInterests;
        }
        
        /**
         * Function that retrieves the member's indoor interests.
         *
         * @return returns the member's indoor interests
         */
        function getInDoorInterests()
        {
            return $this->_inDoorInterests;
        }

        /**
         * Function that sets the member's outdoor interests.
         *
         * @param array $_outDoorInterests the member's outdoor interests
         * @return void
         */       
        function setOutDoorInterests($_outDoorInterests)
        {
            $this->_outDoorInterests = $_outDoorInterests;
        }
        
        /**
         * Function that retrieves the member's outdoor interests.
         *
         * @return returns the member's outdoor interests
         */        
        function getOutDoorInterests()
        {
            return $this->_outDoorInterests;
        }
    }