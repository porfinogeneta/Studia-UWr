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






































; wskazanie indexu
#;(define (indexof x xs i)
  (if (null? xs)
      -1
      (if (equal? (first xs) x)
          i
          (indexof x (rest xs) (+ 1 i))
          )
      )
  )

; znajdziemy indeksy tych samych kolumn
#;(define (indexof-same schema1 schema2 acc)
  (if (null? schema1)
      acc
      (if (member (first schema1) schema2)
          (indexof-same (rest schema1) schema2 (cons (indexof (first schema1) schema2 0) acc))
          (indexof-same (rest schema1) schema2 acc)
          )
      )
  )

; map przekazująca również index wywołania
;tworzy pary f(elem, index) reszta listy
#;(define (map-index f lst)
  (define (iter i xs acc)
    (if (null? xs)
        ;odracamy akumulator, wtedy elementy będą po kolei
        (reverse acc)
        (iter (+ i 1) (rest xs) (cons (f (first xs) i) acc))
        )
    )
  (iter 0 lst '())
  )

;czy można połączyć wiersz
#;(define (merge-able row1 row2 same-cols1 same-cols2)
  (map-index (lambda (idx i)
               ;porównanie wartości w opowiednich kolumnach
              (equal? (list-ref row1 (list-ref same-cols1 i) ) (list-ref row2 (list-ref same-cols2 i) ))
               )same-cols1
  ) )


#;(define (row-columnless row idx-cols)
  (define (keep? idx) (not (member idx idx-cols)))
  (let loop ([row row]
             [idx 0]
             [result '()])
    (cond
      [(null? row) (reverse result)]
      [(keep? idx) (loop (cdr row) (+ idx 1) (cons (car row) result))]
      [else (loop (cdr row) (+ idx 1) result)])))



#;(define (merge-rows row1 row2 same-cols1 same-cols2)
  (if (merge-able row1 row2 same-cols1 same-cols2)
      (append row1 (row-columnless row2 same-cols2))
      '()
      )
  ) 

;na której pozycji w drugiej tabeli powtarzają się kolumny
#;(indexof-same (table-schema cities) (table-schema countries) '())

#;(define (table-natural-join tab1 tab2)
  (let* (
        [schema1 (table-schema tab1)]
        [schema2 (table-schema tab2)]
        [same-cols2 (indexof-same schema1 schema2 '())]
        [same-cols1 (indexof-same schema2 schema1 '())]
        [merged-schema (append schema1 (filter (lambda (col2) (not (member col2 schema1)) ) schema2) )]
        [rows1 (table-rows tab1)]
        [rows2 (table-rows tab2)] 
        [merged-rows
         (map
     (lambda (row1)
       (map
        (lambda (row2)
          ;połączenie wierszy jeśli są równe w odpowiedniej kolumnie
          (merge-rows row1 row2 same-cols1 same-cols2) 
          )
        rows2) )
         rows1)
         ]
        )
    (table merged-schema merged-rows)
    )
  )

;( table-natural-join cities countries )












