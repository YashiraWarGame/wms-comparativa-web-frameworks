<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

namespace Application\Model;

use Zend\Crypt\Utils;
/**
 * Description of ChallengeModel
 *
 * @author hds
 */
class ChallengeModel {
    private $challengeID;
    private $name;
    private $description;
    private $maximumAttempts;
    private $creationDate;
    private $publicationDate;
    private $updateDate;
    private $answers;
    
    public function getChallengeID() {
        return $this->challengeID;
    }

    public function getName() {
        return $this->name;
    }

    public function getDescription() {
        return $this->description;
    }

    public function getMaximumAttempts() {
        return $this->maximumAttempts;
    }

    public function getCreationDate() {
        return $this->creationDate;
    }

    public function getPublicationDate() {
        return $this->publicationDate;
    }

    public function getUpdateDate() {
        return $this->updateDate;
    }

    public function getAnswers() {
        return $this->answers;
    }

    public function setChallengeID($ChallengeID) {
        $this->challengeID = $ChallengeID;
    }

    public function setName($name) {
        $this->name = $name;
    }

    public function setDescription($description) {
        $this->description = $description;
    }

    public function setMaximumAttempts($maximumAttempts) {
        $this->maximumAttempts = $maximumAttempts;
    }

    public function setCreationDate($creationDate) {
        $this->creationDate = $creationDate;
    }

    public function setPublicationDate($publicationDate) {
        $this->publicationDate = $publicationDate;
    }

    public function setUpdateDate($updateDate) {
        $this->updateDate = $updateDate;
    }
    
    public function addAnswer($answer) {
        $this->answers[] = $answer;
    }

    public function setAnswers($answers) {
        $this->answers = array();
        
        foreach ($answers as $answer) {
            $this->answers[] = $answer;
        }
    }
    
    public function isValidAnswer($userAnswer) {
        $valid = false;
        
        foreach ($this->answers as $answer) {
            switch (strtoupper($answer->getAnswerType())) {
                case 'HASH':
                    // SHA1 de prueba
                    $temp = sha1($userAnswer . trim($answer->getSalt()));
                    $valid = Utils::compareStrings($temp, $answer->getAnswer());
                    break;
                case 'REGEX':
                    $valid = preg_match('/^' . $answer->getAnswer() . '$/', $userAnswer);
                    break;
                default:
                    throw new \Exception("Unsupported answer type");
            }
            
            if ($valid) {
                break;
            }
        }
        
        return $valid;
    }
}
