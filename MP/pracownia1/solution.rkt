#lang racket

(provide (struct-out column-info)
         (struct-out table)
         (struct-out and-f)
         (struct-out or-f)
         (struct-out not-f)
         (struct-out eq-f)
         (struct-out eq2-f)
         (struct-out lt-f)
         table-insert
         table-project
         table-sort
         table-select
         table-rename
         table-cross-join
         table-natural-join)

(define-struct column-info (name type) #:transparent)

(define-struct table (schema rows) #:transparent)

( define-struct and-f (l r)) ; koniunkcja formuł

( define-struct or-f (l r)) ; dysjunkcja formuł

( define-struct not-f (e)) ; negacja formuły

( define-struct eq-f ( name val )) ; wartość kolumny name równa val

( define-struct eq2-f ( name name2 )) ; wartości kolumn name i name2 równe

( define-struct lt-f ( name val )) ; wartość kolumny name mniejsza niż val


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

(define countries
  (table
   (list (column-info 'country 'string)
         (column-info 'population 'number))
   (list (list "Poland" 38)
         (list "Germany" 83)
         (list "France" 67)
         (list "Spain" 47))))

(define (empty-table columns) (table columns '()))



; utworzenie narzędzia do typowania
(define (determine-type val)
  (cond ((number? val) 'number)
        ((string? val) 'string)
        ((symbol? val) 'symbol)
        ((boolean? val) 'boolean)
        (else (error "Unknown Type!"))))

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


(define (table-rename col ncol tab)
  (let ([schema (table-schema tab)]
        [rows (table-rows tab)]
        )
    ;będziemy robić nową tabelkę
    (table (map
            (lambda (c)
              ;jak name aktualnie spr kolumny się pokryje ze zmianą
              (if (equal? (column-info-name c) col)
                  ;zamieniam kolumnę na nową
                  (column-info ncol (column-info-type c))
                  c ;zostawiam starą
                  )
              )
            schema
            )rows )
    )
  )





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


;funkcja pomocnicza dla sort
(define (compare-lexico<=? vals-a vals-b)
  (cond
    ((and (null? vals-a) (null? vals-b)) #f) ;oba się skończyły, a to znaczy, że były równe, nie chcemy zmieniać, mamy stabilne sortowanie
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


;złącz ze sobą  xs i ys na odpowienich pozycjach
(define (concat-extend xs ys)
  (foldr (lambda (x acc)
           (append acc
                   (map (lambda (y) (append x y)) ys)))
         '()
         xs))



(define (table-cross-join tab1 tab2)
  ;deklarujemy nową tabelkę
  (table
   (append (table-schema tab1) (table-schema tab2) )
   (concat-extend (table-rows tab1) (table-rows tab2) )
   )
  )



;tworzy listę duplikatów nazw kolumn w 2
;lista składa się z nazw duplikatów
(define (get-duplicats schema1 schema2)
  (let ([names1 (map (lambda (col) (column-info-name col) ) schema1) ]
        [names2 (map (lambda (col) (column-info-name col)) schema2 )]
        )
     (foldl (lambda (col acc-pairs)
           (if (member col names2)
               (cons (cons col (string->symbol (string-append "new-" (symbol->string col)))) acc-pairs)
               acc-pairs))
         '()
         names1)
    )
  )


;znalezienie pierwszego elementu w liście par, równego pozostałym
; zwrócenie drugiego elementu pary
(define (my-assoc first_val lst)
  (foldl
    (lambda (pair result)
      (if (and (not result) (equal? first_val (car pair))) ; jeżeli nie mamy rezultatu, sprawdzam czy key się równa pierwszemu z pary
          pair
          result))
    #f ; jak nie znajdziemy
    lst)) ; lista par do przeszukania


;przerobienie nazw kolumn na nowe nazwy
(define (rename-columns col-pairs tab)
  (let ([schema (table-schema tab)]
        [rows (table-rows tab)])
    (table (map
             (lambda (c)
               (let* ([old-col (column-info-name c)]
                      [new-col (my-assoc old-col col-pairs)])
                 (if new-col
                     (column-info (cdr new-col) (column-info-type c))
                     c)))
             schema)
           rows)))




;pobranie indexów dla każdego elementu pary duplikatów
(define (index-pair pair schema)
  (cons (indexof (car pair) (schema-names schema) 0) (indexof (cdr pair) (schema-names schema) 0)))

;porównanie wartości na duplikatach kolumn
(define (choose-only-same dup-pairs schema rows)
  ;robię listę par indexów
  (let ([pair-indices (map (lambda (pair) (index-pair pair schema)) dup-pairs)])
    ;poszukuję rzędów, w których wszystkie wartości w parze (oryginał, duplikat) są równe
    (filter (lambda (row)
              (andmap (lambda (pair)
                        (equal? (list-ref row (car pair)) (list-ref row (cdr pair))))
                      pair-indices))
            rows)
    ))


;utworzenie nazw, kolumn, niebędących duplikatami
(define (update-col-names schema duplicats)
  (let ([col-names (map (lambda (col) (column-info-name col) ) schema)];lista wszystkich kolumn
        [to-go (map (lambda (elem) (cdr elem) ) duplicats)] ;które kolumny do wyrzucenia
        )
    ;do schema dodaję tylko kolumny, niebądące w to-go
    (filter (lambda (col)
              (not (member col to-go))
              ) col-names)
    )
  )



(define (table-natural-join tab1 tab2)
  (let* ([duplicats (get-duplicats (table-schema tab1) (table-schema tab2))] ;lista par (pierwotna_nazwa_kolumn, new-pierwotna_nazwa_kolumn)
       [renamed-t2 (rename-columns duplicats tab2)];zamiana nazw kolumn w drugiej tabeli
       [cross-join (table-cross-join tab1 renamed-t2)] ;połączenie tab1 i tab2 (z już zmienionymi wartościami)
       [same-vals-rows (choose-only-same duplicats (table-schema cross-join) (table-rows cross-join))];wybierz wiersze z tymi samymi wartościami
       [correct-columns (update-col-names (table-schema cross-join) duplicats)];zebranie nazw kolumn, bez kolumn-duplikatów
       [new-schema (filter (lambda (col) (member (column-info-name col) correct-columns)) (table-schema cross-join))];utworzenie nowego schema, bez kolumn-duplkiatów
       [new-cross (table (table-schema cross-join) same-vals-rows)];utworzenie tabelki ze starą schema i same-vals-rows
       )

       
    (table
        new-schema ;nowe, poprawne listy kolumn
        (table-rows (table-project correct-columns new-cross)) ;projekcja nowej tabelki
        )

    ))


( table-natural-join cities countries )



