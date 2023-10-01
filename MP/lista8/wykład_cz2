#lang plait
;SKŁADNIA ABSTRAKCYJNA
;zdefiniujemy składnie
;zdefiniujemy drzewo wyrażeń oraz typ operatorów
(define-type Op
  (op-add) (op-mul) (op-sub) (op-div))

;to jest nasz składnia abstrakcyjna,
;czyli sposób reprezentacji naszej struktury
(define-type Exp
  (exp-number [n : Number])
  (exp-op [op : Op] [e1 : Exp] [e2 : Exp]))

;konwertowanie s-wyrażenia do symboli 
(define (parse-Op s)
  (let ([sym (s-exp->symbol s)])
  (cond
    [(equal? sym '+) (op-add)]
    [(equal? sym '-) (op-sub)]
    [(equal? sym '*) (op-mul)]
    [(equal? sym '/) (op-div)]
    )))


;wykorzystamy cytowanie do parsowania
;'(+ 2 2) -> '(+ 2 2) dostajemy dobrze sparsowane drzewo
;` quasi cytownaie zwraca S-Exp `(+ 2 2) -> '(+ 2 2) - dostajemy z wyrażenie

;parse-Exp, korzystamy z s-wyrażeń
;s-exp->number s - bierze liczbę z s-wyrażenia
;parsing - analiza składniowa

(define (parse-Exp s)
  (cond
    [(s-exp-number? s) (exp-number (s-exp->number s))]
    [(s-exp-list? s)
     (let ([xs (s-exp->list s)])
       (exp-op (parse-Op  (first  xs))
               (parse-Exp (second xs))
               (parse-Exp (third  xs))))]))

; ==============================================
; INTERPRETER


(define (eval-op op)
  (type-case Op op
    [(op-add) +]
    [(op-sub) -]
    [(op-mul) *]
    [(op-div) /]))

(define (eval e)
  (type-case Exp e
    [(exp-number n)    n]
    [(exp-op op e1 e2)
     ((eval-op op) (eval e1) (eval e2))]))

(define (eval-Exp s)
  (eval (parse-Exp s))
  )


