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


; wzięcie nazw kolumn
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



(define (table-project cols tab)

  ;funkcja do wyciągania danych z wiersza
  (define (extract-row-cols row cols-idx)
    (map (lambda (index) (list-ref row index) ) cols-idx)
    )
  
  (let* (
        [rows (table-rows tab)] ;nasze rzędy
        [col-indx (filter-cols cols tab)] ;kolumny, które potrzebujemy, ich indexy
        [new-rows (map (lambda (elem) (extract-row-cols elem col-indx) ) rows)] ;iterujemy po danych w tabeli
        [cols (table-schema tab)]
        [new-cols (filter
                   ;chcemy tylko kolumny będące cols w argumencie
                   (lambda (col) (member (indexof col cols 0) col-indx ))
                   cols)]
        )
    
    (table new-cols new-rows )
    
    )
  
  )

(table-project (list 'city 'country) cities)





