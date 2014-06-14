<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

namespace Application\Form;

use Zend\Form\Form;
use Zend\InputFilter\InputFilter;
/**
 * Description of ChallengeSolveForm
 *
 * @author hds
 */
class ChallengeSolveForm extends Form {
    public function __construct() {
        // we want to ignore the name passed
        parent::__construct('challenge');
        
        $this->add(array(
            'name' => 'token',
            'type' => 'Csrf'
        ));
        
        $this->add(array(
            'name' => 'answer',
            'type' => 'Text',
            'options' => array(
                'label' => 'Answer',
            ),
        ));
        
        $this->add(array(
            'name' => 'submit',
            'type' => 'Submit',
            'attributes' => array(
                'value' => 'Submit answer',
                'id' => 'submitbutton',
            ),
        ));
        
        $inputFilter = new InputFilter();
        
        $inputFilter->add(array(
            'name' => 'token',
            'options' => array(
                'csrf_options' => array(
                    'timeout' => 600
                )
            )
        ));
        
        $inputFilter->add(array(
            'name'     => 'answer',
            'required' => true,
            'filters' => array(
                array('name' => 'Zend\Filter\StringTrim')
            ),
            'validators' => array(
                array(
                    'name'    => 'StringLength',
                    'options' => array(
                        'encoding' => 'UTF-8',
                        'min'      => 1,
                        'max'      => 256,
                    ),
                ),
            ),
        ));

        $this->setInputFilter($inputFilter);
    }
}
