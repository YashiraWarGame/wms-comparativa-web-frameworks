<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

namespace Application\Model;

/**
 * Description of ChallengeAnswerModel
 *
 * @author hds
 */
class ChallengeAnswerModel {
    private $challengeID;
    private $answerType;
    private $answer;
    private $salt;
    
    public function getChallengeID() {
        return $this->challengeID;
    }
    
    public function getAnswerType() {
        return $this->answerType;
    }

    public function getAnswer() {
        return $this->answer;
    }

    public function getSalt() {
        return $this->salt;
    }

    public function setChallengeID($challengeID) {
        $this->challengeID = $challengeID;
    }
    
    public function setAnswerType($answerType) {
        $this->answerType = $answerType;
    }

    public function setAnswer($answer) {
        $this->answer = $answer;
    }

    public function setSalt($salt) {
        $this->salt = $salt;
    }

}
