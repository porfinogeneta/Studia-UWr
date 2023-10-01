#lang plait

(require "zad3syntax.rkt")
(require (typed-in "zad3parsing.rkt"
                   (parse-Exp : (S-Exp -> Exp))))

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

(define (calc s)
  (eval (parse-Exp s)))

(define (parse-op s)
  (run-parser op-parser s))

(define (parse-exp s)
  (run-parser exp-parser s))

(define (parse-Exp s)
  (parse-exp (s-exp-content s)))