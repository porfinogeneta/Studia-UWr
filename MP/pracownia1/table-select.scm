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




( define-struct and-f (l r)) ; koniunkcja formuł

( define-struct or-f (l r)) ; dysjunkcja formuł

( define-struct not-f (e)) ; negacja formuły

( define-struct eq-f ( name val )) ; wartość kolumny name równa val

( define-struct eq2-f ( name name2 )) ; wartości kolumn name i name2 równe

( define-struct lt-f ( name val )) ; wartość kolumny name mniejsza niż val


; wzięcie nazw kolumn
(define (schema-names schema)
  (map (lambda (c) (column-info-name c)) schema))

; wskazanie indexu
(define (indexof x xs i)
  (if (null? xs)
      -1
      (if (eq? (first xs) x)
          i
          (indexof x (rest xs) (+ 1 i))
          )
      )
  )


;funkcja umożliwiająca porównywanie różnych typów
(define (comparator a b)
  (cond
    [(and (number? a) (number? b)) (< a b)]
    [(and (string? a) (string? b)) (string<? a b)]
    [(and (symbol? a) (symbol? b))
     (string<? (symbol->string a) (symbol->string b))]
    [else (error "Invalid input: Both arguments must be of the same type - a symbol, string, or number.")])
  )

; utworzenie narzędzia do typowania
(define (determine-type val)
  (cond ((number? val) 'number)
        ((string? val) 'string)
        ((symbol? val) 'symbol)
        ((boolean? val) 'boolean)
        (else 'unknown)))

;wartość kolumny name równa val
(define (equal-vals-in-col row schema col-name col-val)
  (if (not (symbol? col-name))
      (error "Not Valid Name")
      (let* ([col-index (indexof col-name (schema-names schema) 0)]
            [needed-val (column-info-type (list-ref schema col-index))]
            )
        ;sprawdzenie czy typ kolumny i formuły jest tym samym
        (if (equal? (determine-type col-val) needed-val )
            ;sprawdzenie czy wartość w kolumnie jest taka sama
            (equal? (list-ref row col-index) col-val )
            (error "Not Valid Type")
            )
        )))

;utworzenie listy wierszy, w których wartości w kolumnie name = name2
(define (equal-both-names row schema name1 name2)
  (if (not (and (symbol? name1) (symbol? name2)))
      (error "Not Valid Name")
      ;wzięcie indexów kolumn do sprawdzenia
      (let* ([col1-index (indexof name1 (schema-names schema) 0)]
            [col2-index (indexof name2 (schema-names schema) 0)])
        (equal? (list-ref row col1-index) (list-ref row col2-index) ))))

;utworzenie listy wierszy, w których wartość kolumny name jest mniejsza niż val
(define (lesser-than-val row schema name val)
  (if (not (symbol? name))
           (error "Not Valid Name")
           ;indeks kolumny do sprawdzenia
           (let* ([col-index (indexof name (schema-names schema) 0)]
                 [needed-val (column-info-type (list-ref schema col-index))]
                 )
     (if (equal? (determine-type val) needed-val )
            (comparator (list-ref row col-index) val)
            (error "Not Valid Type")
            )        
    ))
  )



;f. wylicza prawdę i fałsz na konkretym wierszu
;później jest to wykorzystywane w procedurze - filter
(define (eval-formula form row schema)
  (cond ((and-f? form)
         (let ((l (and-f-l form))
               (r (and-f-r form)))
           (and (eval-formula l row schema) (eval-formula r row schema))))
        ((or-f? form)
         (let ((l (or-f-l form))
               (r (or-f-r form)))
           (or (eval-formula l row schema) (eval-formula r row schema))))
        ((not-f? form)
         (not (eval-formula (not-f-e form) row schema)))
        ((eq-f? form)
         (equal-vals-in-col row schema (eq-f-name form) (eq-f-val form)))
        ((eq2-f? form)
         (equal-both-names row schema (eq2-f-name form) (eq2-f-name2 form)))
        ((lt-f? form)
         (lesser-than-val row schema (lt-f-name form) (lt-f-val form)))
        (else
         (error "Invalid formula"))))

(define (table-select form tab)
  (let ([rows (table-rows tab)]
        [schema (table-schema  tab)]
        )
    (table
     schema
     (filter (lambda (row) (eval-formula form row schema) ) rows)
     )
    
    )
  )

( table-rows ( table-select ( and-f ( eq-f ' capital #t) ( not-f ( lt-f ' area 300) )) cities ))





