<?php
namespace Application\Controller;

use Zend\Mvc\Controller\AbstractActionController;
use Zend\View\Model\ViewModel;
use Application\Form\ChallengeSolveForm;

class ChallengeController extends AbstractActionController
{
    private $service;
    protected $request;
    
    protected function attachDefaultListeners() {
        parent::attachDefaultListeners();
        
        $this->service = $this->getServiceLocator();
        $this->request = $this->getRequest();
    }
    
    public function indexAction() {
    }

    public function addAction() {
    }

    public function editAction() {
    }

    public function deleteAction() {
    }
    
    public function viewAction() {
        $id = $this->params('id');
        
        $challenge = $this->service->get('Challenge');
        $challenge = $challenge->findById($id);

        $form = new ChallengeSolveForm();
        
        if ($this->request->isPost()) {
            $form->setData($this->request->getPost());
            
            if ($form->isValid()) {
                $data = $form->getData();
                $answer = $data['answer'];
                
                $challengeAnswer = $this->service->get('ChallengeAnswer');
                $challenge->setAnswers($challengeAnswer->findByChallengeId($id));
                
                if ($challenge->isValidAnswer($answer)) {
                    $form->get('answer')->setMessages(array('Respuesta valida'));
                } else {
                    $form->get('answer')->setMessages(array('Respuesta inválida'));
                }
            }
        }

        return new ViewModel(array(
            'challenge' => $challenge,
            'form' => $form
        ));
    }
}