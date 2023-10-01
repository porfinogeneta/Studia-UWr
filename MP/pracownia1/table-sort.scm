#lang racket



;nazwa i typ danych w kolumnach
(define-struct column-info (name type) #:transparent)

;schema pierwsza lista, rows druga lista
(define-struct table (schema rows) #:transparent)

(define countries
  (table
   (list (column-info 'country 'string)
         (column-info 'population 'number))
   (list (list "Poland" 38)
         (list "Germany" 83)
         (list "France" 67)
         (list "Spain" 47))))

(define cities
  (table
   (list (column-info 'city    'string)
         (column-info 'country 'string)
         (column-info 'area    'number)
         (column-info 'capital 'boolean))
   (list (list "Wrocław" "Poland"  293 #f)
         (list "Warsaw"  "Poland"  517 #t)
         (list "Poznań"  "Poland"  262 #f)
         (list "Berlin"  "Germany" 892 #t)
         (list "Munich"  "Germany" 310 #f)
         (list "Paris"   "France"  105 #t)
         (list "Rennes"  "France"   50 #f))))

;pobraie nazw kolumn
(define (schema-names schema)
  (map (lambda (c) (column-info-name c)) schema))

; wskazanie indexu
(define (indexof x xs i)
  (if (null? xs)
      -1
      (if (equal? (first xs) x)
          i
          (indexof x (rest xs) (+ 1 i))
          )
      )
  )


;utwórz listę tylko tych nazw, które są w nazwach kolumn
;będzie to index wystąpienia w podstawowej tabeli
(define (filter-cols cols table)
  (let (
        (schema-names (schema-names (table-schema table)))
        )
    ;filtruję i aplikuję funkcję
    (filter-map
     (lambda (c)
       (if (member c schema-names)
           (indexof c schema-names 0)
           (error "Incorrect Column Name")
       )

            ) cols)))



; utworzenie listy z wartościami z wierszy
(define (extract-sorting-values row cols-idx)
  (map (lambda (index) (list-ref row index) ) cols-idx)
  )

;funkcja umożliwiająca porównywanie różnych typów
(define (comparator a b)
  (cond
    [(and (number? a) (number? b)) (< a b)]
    [(and (string? a) (string? b)) (string<? a b)]
    [(and (symbol? a) (symbol? b))
     (string<? (symbol->string a) (symbol->string b))]
    [(and (boolean? a) (boolean? b))
     (< (if a 1 0) (if b 1 0) )
     ]
    [else (error "Invalid input!")])
  )


#;(define (compare-lexico<=? vals-a vals-b)
  (cond ((and (null? vals-a) (null? vals-b)) #t)
        ((null? vals-a) #t)
        ((null? vals-b) #f)
        ;jeżeli typ to string
        ((and (string? (first vals-a)) (string? (first vals-b)))
         ;są równe, porównuję dalej
         (cond ((string=? (first vals-a) (first vals-b)) (compare-lexico<=? (rest vals-a) (rest vals-b)))
               ;są mniejsze, zwracam true, false wpp
               ((string<? (first vals-a) (first vals-b)) #t)
               (else #f)))
        ;typ to number
        ((and (number? (first vals-a)) (number? (first vals-b)))
         (cond ((= (first vals-a) (first vals-b)) (compare-lexico<=? (first vals-a) (first vals-b)))
               ((< (first vals-a) (first vals-b)) #t)
               (else #f)))
        ((and (boolean? (first vals-a)) (boolean? (first vals-b)))
         (cond ((= (if (first vals-a) 1 0) (if (first vals-b) 1 0)) (compare-lexico<=? (first vals-a) (first vals-b)))
               ((< (if (first vals-a) 1 0) (if (first vals-b) 1 0)) #t)
               (else #f)))
        (else (error "Cannot compare properly"))))

;funkcja pomocnicza dla sort
(define (compare-lexico<=? vals-a vals-b)
  (cond
    ((and (null? vals-a) (null? vals-b)) #f) ;oba się skończyły albo są nullami, a nie jest mniejsze niż b
    ((null? vals-a) #t) ;ten jest nullem tzn, że zawsze będzie mniejszy
    ((null? vals-b) #f) ;jak ten jest nullem znaczy, że vals-a nie jest i vals-a nie może być mniejszy od nulla
    ;jak są równe
    ((equal? (first vals-a) (first vals-b) ) (compare-lexico<=? (rest vals-a) (rest vals-b) ) )
    ;jak jeden jest mniejszy
    (else (comparator (first vals-a) (first vals-b)))
    )
  )


(define (table-sort cols tab)
  (let ([schema (table-schema tab)]
        [rows (table-rows tab)]
        [keys (filter-cols cols tab)] ;indexy kolumn - kluczy
        )
    ;robimy nową tabelę
    (table
     schema
     (sort
      rows
      (lambda (a b)
        ;pobierzemy wartości do porównań
        (let
            ((a-vals (extract-sorting-values a keys))
            (b-vals (extract-sorting-values b keys)))
          (compare-lexico<=? a-vals b-vals)
          )
        )
      )
     )

    )

  )

( table-rows ( table-sort '( country city ) cities ))






