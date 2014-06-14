<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

namespace Application\Model;

use Application\Model\ChallengeModel;
use Application\Model\AbstractFactory;
use Zend\Db\Sql\Select;

/**
 * Description of ChallengeModelMapper
 *
 * @author hds
 */
class ChallengeFactory extends AbstractFactory {
    public function __construct() {
        $this->table = 'pkChallenge';
        $this->columnId = 'ChallengeID';
        $this->entity = new ChallengeModel;
    }
}
