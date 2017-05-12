<?php
    /**

     *
     * @author Neal Noble <nrnoble@hotmail.com>
     * @version 1.0
     */

    //CONNECT
    class PetsDB
    {
        private $_dbConnection;
        
        function __construct()
        {
            require_once("/home/nnoble/config.php");

            
            try {
                //Establish database connection
                $this->_dbConnection = new PDO( DB_DSN, DB_USERNAME, DB_PASSWORD );
                
                //Keep the connection open for reuse to improve performance
                $this->_dbConnection->setAttribute( PDO::ATTR_PERSISTENT, true);
                
                //Throw an exception whenever a database error occurs
                $this->_dbConnection->setAttribute( PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION );
            }
            catch (PDOException $e) {
                die( "Error!: " . $e->getMessage());
            }
        }
        

        /**
         * Add a new member to the dating site DB
         * 
         * @param $firstName the first name of the member
         * @param $lastName the last name of the member
         * @param $age the age of the member
         * @param $gender the gender of the member
         * @param $phone the phone of the member
         * @param $premium true if the member is a premium members
         * @param $email the email of the member
         * @param $state the state of the member
         * @param $seeking the gender the member is seeking 
         * @param $bio the members biography
         * @param $outdoor list of outdoor interests
         * @param $indoor list of indoor interests
         * @return true if the insert was successful, otherwise false
         */
        function addMember($firstName, $lastName, $age, $gender, $phone,$premium,$email,$state,$seeking,$bio,$indoor,$outdoor)
        {
            $insert = 'INSERT INTO pets (firstName, lastName, age, gender, phone, premium, email, state, seeking, bio, indoor, outdoor) 
                                 VALUES (:firstName, :lastName, :age, :gender, :phone, :premium, :email, :state, :seeking, :bio, :indoor, :outdoor)';
             
            $statement = $this->_dbConnection->prepare($insert);
            $statement->bindValue(':firstName', $firstName, PDO::PARAM_STR);
            $statement->bindValue(':lastName', $lastName, PDO::PARAM_STR);
            $statement->bindValue(':age', $age, PDO::PARAM_INT);
            $statement->bindValue(':gender', $gender, PDO::PARAM_STR);
            $statement->bindValue(':phone', $phone, PDO::PARAM_STR);
            $statement->bindValue(':premium', $premium, PDO::PARAM_INT);
            $statement->bindValue(':email', $email, PDO::PARAM_STR);
            $statement->bindValue(':state', $state, PDO::PARAM_STR);
            $statement->bindValue(':seeking', $seeking, PDO::PARAM_STR);
            $statement->bindValue(':bio', $bio, PDO::PARAM_STR);
            $statement->bindValue(':indoor', $indoor, PDO::PARAM_STR);
            $statement->bindValue(':outdoor', $outdoor, PDO::PARAM_STR);
            

            $statement->execute();

            //Return ID of inserted row
            return $this->_dbConnection->lastInsertId();
        }
         
        //READ
        /**
         * Returns all members in the database collection.
         *
         * @access public
         *
         * @return an associative array of members indexed by id
         */
        public function allPets()
        {
            $select = 'SELECT id, name, type, color FROM pets';
            $statement = this->_pdo->prepare($select);
            $results $statement->fetchall(pdo::FETCH_ASSOC);
            $results = $this->_dbConnection->query($select);
            return $results;
             
            $resultsArray = array();
             
            //map each pet id to a row of data for that pet
            while ($row = $results->fetch(PDO::FETCH_ASSOC)) {
                $resultsArray[$row['id']] = $row;
            }
             
            return $resultsArray;
        }
         
        /**
         * Returns a pet that has the given id.
         *
         * @access public
         * @param int $id the id of the pet
         *
         * @return an associative array of pet attributes, or false if
         * the pet was not found
         */
        publuc function memberById($id)
        {
            $select = 'SELECT id, name, type, color FROM pets WHERE id=:id';
             
            $statement = $this->_dbConnection->prepare($select);
            $statement->bindValue(':id', $id, PDO::PARAM_INT);
            $statement->execute();
             
            return $statement->fetch(PDO::FETCH_ASSOC);
        }
         
        /**
         * Returns true if the name is used by a pet in the database.
         *
         * @access public
         * @param string $name the name of the pet to look for
         *
         * @return true if the name already exists, otherwise false
         */   
        function petNameExists($name)
        {            
            $select = 'SELECT id, name, type, color FROM pets WHERE name=:name';
             
            $statement = $this->_dbConnection->prepare($select);
            $statement->bindValue(':name', $name, PDO::PARAM_STR);
            $statement->execute();
             
            $row = $statement->fetch(PDO::FETCH_ASSOC);
             
            return !empty($row);
        }
         
        //UPDATE
      
         /**
         * Updates the attributes for a pet in the database.
         *
         * @access public
         * @param int $id the id of the pet
         * @param string $name the name of the pet
         * @param string $type the type of pet (giraffe, turtle, bear, ...)
         * @param string $color the color of the animal
         */  
        function updatePet($id, $name, $type, $color)
        {          
            $update = 'UPDATE pets SET name=:name, type=:type, color=:color
                                   WHERE id=:id';
             
            $statement = $this->_dbConnection->prepare($update);
            $statement->bindValue(':name', $name, PDO::PARAM_STR);
            $statement->bindValue(':type', $type, PDO::PARAM_STR);
            $statement->bindValue(':color', $color, PDO::PARAM_STR);
            $statement->bindValue(':id', $id, PDO::PARAM_INT);
             
            $statement->execute();
        }
         
        //DELETE
         
        /**
         * Deletes the pet associated with the input id.
         *
         * @access public
         * @param int $id the id of the pet
         *
         * @return true if the delete was successful, otherwise false
         */
        function deletePet($id)
        {        
            $delete = 'DELETE FROM pets WHERE id=:id';
             
            $statement = $this->_dbConnection->prepare($delete);
            $statement->bindValue(':id', $id, PDO::PARAM_INT);
             
            return $statement->execute();
        }
    }