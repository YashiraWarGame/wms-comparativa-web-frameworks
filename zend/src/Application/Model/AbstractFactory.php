<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

namespace Application\Model;

use Zend\Db\Adapter\Adapter;
use Zend\Db\Sql\Select;
use Zend\Db\Adapter\AdapterAwareInterface;
use Zend\Db\TableGateway\AbstractTableGateway;
use Zend\Db\ResultSet\HydratingResultSet;
use Zend\Stdlib\Hydrator\ClassMethods;

/**
 * Description of AbstractModelMapper
 *
 * @author hds
 */
class AbstractFactory extends AbstractTableGateway implements AdapterAwareInterface {
    protected $entity;
    protected $columnId;
    
    public function setDbAdapter(Adapter $adapter) {
        $this->adapter = $adapter;
        $this->resultSetPrototype = new HydratingResultSet(new ClassMethods, $this->entity);
    }
    
    public function findById($id) {
        $id = (int) $id;
        
        $row = $this->findByAttribute(array($this->columnId => $id), 1);
        
        if (!$row || $row->count() == 0) {
            throw new \Exception("Registry not found");
        }
        
        return $row->current();
    }
    
    public function findByAttribute($attributes, $limit = 1) {
        $select = new Select();
        $select->from($this->table);
        $select->where($attributes);
        $select->limit($limit);
        
        return $this->selectWith($select);
    }
}
