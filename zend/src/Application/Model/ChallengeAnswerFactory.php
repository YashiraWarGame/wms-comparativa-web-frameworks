<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

namespace Application\Model;

use Zend\Db\Sql\Select;

/**
 * Description of ChallengeAnswerFactory
 *
 * @author hds
 */
class ChallengeAnswerFactory extends AbstractFactory {
    public function __construct() {
        $this->table = 'pkAnswer';
        $this->columnId = 'AnswerID';
        $this->entity = new ChallengeAnswerModel;
    }
    
    public function findByChallengeId($id) {
        $select = new Select();
        $select->from('pkAnswer');
        $select->columns(array('challengeID', 'Answer', 'Salt'));
        $select->where(array('pkAnswer.ChallengeID' => $id));
        $select->join(
                    'ckAnswerType',
                    'pkAnswer.AnswerTypeID = ckAnswerType.AnswerTypeID',
                    array('answerType' => 'Name')
                );
        // SELECT pkAnswer.ChallengeID, pkAnswer.Answer, pkAnswer.Salt, ckAnswerType.Name AS answerType...
        // answerType debe ser atributo de ChallengeAnswerModel, ya que ckAnswerType es un catálogo (invento de g30rg3_x)
        
        return $this->selectWith($select);
    }
}
