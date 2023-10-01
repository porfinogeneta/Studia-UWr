#lang racket

;w pliku docelowym
;(require "mqueue.rkt") - drugi moduł
;w module
;provide?
;mqueue?
;nonempty?mqueue?
;make-mqueue
;no i reszta funkcji -> implementacja dba o niezmienniki
;podpięcie kontraktów
;(contract-out
; [mqueue-empty? (-> mqueue? boolean?)]


(provide
 mqueue?
 nonempty-mqueue?
 (contract-out
   [mqueue-empty? (-> mqueue? boolean?)]
   [make-mqueue   (-> mqueue?)]
   [mqueue-push   (-> mqueue? any/c void?)]
   [mqueue-pop    (-> mqueue? any/c)]
   [mqueue-join   (-> nonempty-mqueue? nonempty-mqueue? void?)]))


;set! - forma specjalna, bo funkcje przyjmują wartości, a nie referencje jak set!

;(set! x (cons 1 2)) ;-> x to referencja na parę

;listy nie są mutowalne (list), bo składają się z consów
;(cons) są niemutowalne, nigdy ani wkaźnik ani wartość się nie zmienią


(define p (mcons 1 2)) ;mutowalny cons
;set-mcar! p 3 - ustawienie pierwszego elementu

(cons 1 (mcons 1 2) 4)


;cons po policzeniu funkcji na nim nie zmienia zawartości wpd do mcons

;KOLEJKI
;mutowalna struktura
(struct mqueue (
                [front #:mutable]
                [back #:mutable]))

;push i pop
;wynik funkcji to wyniki ostatniego wyrażenia


;deklarujemy jakieś niezmienniki i korzystamy z naszego kodu, przy ich zachowaniu
(define (mqueue-empty? q)
  (and (null? (mqueue-front q))
       (null? (mqueue-back  q))))

(define (nonempty-mqueue? q)
  (and (mqueue? q) (mpair? (mqueue-front q))))

(define (make-mqueue)
  (mqueue null null))

(define (mqueue-push q x)
  (define p (mcons x null))
  (if (mqueue-empty? q)
      (set-mqueue-front! q p)
      (set-mcdr! (mqueue-back q) p))
  (set-mqueue-back! q p))


(define/contract (mqueue-pop q)
  (-> nonempty-mqueue? any/c)
  (define p (mqueue-front q))
  (set-mqueue-front! q (mcdr p))
  (if (null? (mcdr p))
      ;begin - obliczam wyrażenia i ostatnie z nich jest zwracane
      (begin
        (set-mqueue-back! q null)
        (mcar p)) ;jak był to ostani element w kolejce
      (mcar p)));wpp

;podpinanie jednych kolejek do drugich, to po prostu przepięcie pointera - funkcja mqueue-join
;nie można współdzielić elementów kolejek, dlatego ustawiamy w join element w niepotrzebnej liście na null
(define (mqueue-join q1 q2)
  (set-mcdr! (mqueue-back q1) (mqueue-front q2))
  (set-mqueue-back! q1 (mqueue-back q2))
  (set-mqueue-front! q2 null)
  (set-mqueue-back!  q2 null))







