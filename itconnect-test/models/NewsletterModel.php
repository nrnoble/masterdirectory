<?php
/**
MIT License

Copyright (c) 2016 Michael Lant, Bogdan Pshonyak, Yegor Shemereko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
 */

/**
 * Class NewsletterModel - Interacts with the newsletter table in the database
 */
class NewsletterModel
{

    // Fields
    protected $db;

    // Constructor
    public function __construct(PDO $db)
    {
        $this->db = $db;
    }

    /**
     * Add email to newletter subscribtion list
     *
     * @param $email Email to subscribe
     * @return bool True if email was added successfully
     */
    public function addEmail($email)
    {
        //$sql = "INSERT INTO newsletter (email) VALUES (:email)";
        $sql = "INSERT INTO newsletter (`email`, `sha_email_hash`) VALUES ('$email', sha1 ('$email'))";
        $q = $this->db->prepare($sql);
        $q->bindValue("email", $email, PDO::PARAM_STR);
        return $q->execute();

    }

    /**
     * Retrieves all email subscribed to newsletter
     *
     * @return Array Array of emails
     */
    public function getEmails()
    {
        $sql = "SELECT email from newsletter";
        $q = $this->db->prepare($sql);
        $q->execute();

        $result = array();

        $emails = $q->fetchAll();

        foreach ($emails as $data) {
            foreach ($data as $email) {
                array_push($result, $email);
            }
        }

        return $result;

    }

}
