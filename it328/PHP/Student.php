<?php

/**
 * Created by PhpStorm.
 * User: Neal
 * Date: 5/9/2017
 * Time: 2:32 AM
 */
class Student
{
    protected $_sid;
    protected $_name;
    protected $_gpa;

    function __construct($csid, $cname, $cgpa)
    {
        $this->_sid = $csid;
        $this->_name = $cname;
        $this->_gpa = $cgpa;
    }

    /**
     * @return mixed
     */
    public function getSid()
    {
        return $this->_sid;
    }

    /**
     * @param mixed $sid
     */
    public function setSid($sid)
    {
        $this->_sid = $sid;
    }

    public function toString()
    {
        return $this_sid . " " . $this->_name . $this->_gpa;
    }
}


$student = new Student("840076346","Neal Noble",4.0);
$student->toString();