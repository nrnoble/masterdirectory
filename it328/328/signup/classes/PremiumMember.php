<?php
/**
 * Neal Noble
 * Course: IT 328 - Full-Stack Web Development
 * Assignment: The sign-up form
 * April 2017
 * Instructor: Tina Ostrander
 */

namespace DatingSite;

/**
 * Class PremiumMember extendsd Member class
 * 
 * PremiumMember extends by add the follow properties
 *   inDoorInterests
 *   outDoorInterests
 * 
 * @package DatingSite
 * @author Neal Noble <nnoble2@mail.greenriver.edu>
 * @copyright 2017
 * @license https://opensource.org/licenses/MIT
 * 
 */
class PremiumMember extends Member
{

    private $inDoorInterests = null;
    private $outDoorInterests = null;

    /**
     * Get list of indoor interestes
     * @return array of indoor interests
     */
    public function getInDoorInterests()
    {
        return $this->inDoorInterests;
    }

    /**
     * Set list of indoor interests
     * @param mixed $inDoorInterests
     */
    public function setInDoorInterests($inDoorInterests)
    {
        $this->inDoorInterests = $inDoorInterests;
    }

    
    /**
     * Get list of outdoor interests
     * @return array of outdoor interests
     */
    public function getOutDoorInterests()
    {
        return $this->outDoorInterests;
    }

    /**
     * Set out door interests
     * @param array $outDoorInterests
     */
    public function setOutDoorInterests($outDoorInterests)
    {
        $this->outDoorInterests = $outDoorInterests;
    }


    /**
     * @return null|string return a string that contains indoor interests
     */
    public function indoorInterestsToString()
    {

        if ($this->outDoorInterests == null)
            return null;

        $indoorInterest = "";
        foreach ($this->getInDoorInterests() as $value) {
            $indoorInterest = $indoorInterest . " " . $value;
        }
        return $indoorInterest;
    }


    /**
     * @return null|string return a string that contains outdoor interests
     */
    public function outdoorInterestsToString()
    {
        if ($this->inDoorInterests == null)
            return null;

        $outdoorInterest = "";

        foreach ($this->getOutDoorInterests() as $value) {
            $outdoorInterest = $outdoorInterest . " " . $value;
        }
        return $outdoorInterest;
    }
}

