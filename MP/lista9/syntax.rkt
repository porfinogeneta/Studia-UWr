#lang plait

;definicje operatorów
(define-type Op
  (op-add) (op-mul) (op-sub) (op-div))

;typy wyrażeń
(define-type Exp
  (exp-number [n : Number])
  (exp-op [op : Op] [e1 : Exp] [e2 : Exp]))