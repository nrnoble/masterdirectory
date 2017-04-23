<?php
/**
 * @category IT328
 * @package DatingSite
 * @author Neal Noble
 * @license https://opensource.org/licenses/MIT
 */


namespace DatingSite;

/**
 * Class Member
 * @package DatingSite
 */
class Member
{
    private $firstName;
    private $lastName;
    private $age;
    private $gender;
    private $phone;
    private $email;
    private $state;
    private $seekingGender;
    private $bio;
    private $premiumMember;




    function __construct($first, $last, $yearsOld, $sexualIdentity, $telephone, $premium)
    {
        $this->firstName = $first;
        $this->lastName = $last;
        $this->age = $yearsOld;
        $this->gender = $sexualIdentity;
        $this->phone = $telephone;
        $this->premiumMember = $premium;
    }


    /**
     * @return mixed
     */
    public function getBio()
    {
        return $this->bio;
    }

    /**
     * @param mixed $bio
     */
    public function setBio($bio)
    {
        $this->bio = $bio;
    }



    /**
     * @return mixed
     */
    public function getPremiumMember()
    {
        return $this->premiumMember;
    }

    /**
     * @param mixed $premiumMember
     */
    public function setPremiumMember($premiumMember)
    {
        $this->premiumMember = $premiumMember;
    }


    public function getFullName()
    {
        return $this->firstName . " " . $this->lastName;
    }


    /**
     * @return mixed first and last name
     */
    public function getFirstName()
    {
        return $this->firstName;
    }


    /**
     * @param mixed $firstName
     */
    public function setFirstName($firstName)
    {
        $this->firstName = $firstName;
    }


    /**
     * @return mixed
     */
    public function getLastName()
    {
        return $this->lastName;
    }


    /**
     * @param mixed $lastName
     */
    public function setLastName($lastName)
    {
        $this->lastName = $lastName;
    }


    /**
     * @return mixed
     */
    public function getAge()
    {
        return $this->age;
    }


    /**
     * @param mixed $age
     */
    public function setAge($age)
    {
        $this->age = $age;
    }


    /**
     *
     * @return mixed
     */
    public function getGender()
    {
        return $this->gender;
    }

    /**
     * @param mixed $gender
     */
    public function setGender($gender)
    {
        $this->gender = $gender;
    }


    /**
     * @return mixed
     */
    public function getPhone()
    {
        return $this->phone;
    }


    /**
     * @param mixed $phone
     */
    public function setPhone($phone)
    {
        $this->phone = $phone;
    }


    /**
     * @return mixed
     */
    public function getEmail()
    {
        return $this->email;
    }


    /**
     * @param mixed $email
     */
    public function setEmail($email)
    {
        $this->email = $email;
    }


    /**
     * @return mixed
     */
    public function getState()
    {
        return $this->state;
    }


    /**
     * @param mixed $state
     */
    public function setState($state)
    {
        $this->state = $state;
    }


    /**
     * @return mixed
     */
    public function getSeekingGender()
    {
        return $this->seekingGender;
    }


    /**
     * @param mixed $seekingGender
     */
    public function setSeekingGender($seekingGender)
    {
        $this->seekingGender = $seekingGender;
    }


    /**
     * @return mixed
     */
    public function getInterests()
    {
        return $this->interests;
    }


    /**
     * @param mixed $interests
     */
    public function setInterests($interests)
    {
        $this->interests = $interests;
    }

}