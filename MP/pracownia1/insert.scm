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


; utworzenie narzędzia do typowania
(define (determine-type val)
  (cond ((number? val) 'number)
        ((string? val) 'string)
        ((symbol? val) 'symbol)
        ((boolean? val) 'boolean)
        (else (error "Unsupported Type!"))))

; map przekazująca również index wywołania
;tworzy pary f(elem, index) reszta listy
(define (map-index f lst)
  (define (iter i xs acc)
    (if (null? xs)
        ;odracamy akumulator, wtedy elementy będą po kolei
        (reverse acc)
        (iter (+ i 1) (rest xs) (cons (f (first xs) i) acc))
        )
    )
  (iter 0 lst '())
  )

(define (new-row-match? row schema)
  (if (not (equal? (length row) (length schema)))
      (error "Number of columns doesn't match")
      ;sprawdzenie typów
      (andmap (lambda (x) (equal? x #t))
             (map-index
               ;sprawdzam czy typ danych zgadza się z typem na konkretnej pozycji w tabeli
              (lambda (elem index)
                (equal? (determine-type elem) (column-info-type (list-ref schema index))))
              row))))




(define (table-insert row tab)
  [let ([schema (table-schema tab)]
        [rows (table-rows tab)]
        )
    (if (new-row-match? row schema)
        (table schema (cons row rows))
        (error "Invalid Input")
        )
    
    ]
  )

(table-insert (list "Japan" 138) countries)