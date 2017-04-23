<?php

namespace DatingSite;


class PremiumMember extends Member
{

    private $inDoorInterests;
    private $outDoorInterests;

    /**
     * @return mixed
     */
    public function getInDoorInterests()
    {
        return $this->inDoorInterests;
    }

    /**
     * @param mixed $inDoorInterests
     */
    public function setInDoorInterests($inDoorInterests)
    {
        $this->inDoorInterests = $inDoorInterests;
    }

    /**
     * @return mixed
     */
    public function getOutDoorInterests()
    {
        return $this->outDoorInterests;
    }

    /**
     * @param mixed $outDoorInterests
     */
    public function setOutDoorInterests($outDoorInterests)
    {
        $this->outDoorInterests = $outDoorInterests;
    }
}

