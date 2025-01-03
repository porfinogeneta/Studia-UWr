#lang plait

;;abstract syntax=======
;typ dla operatorów
(define-type Op
  (add) (sub) (mul) (eql) (leq))

;typ dla wyrażeń
(define-type Exp
  (numE [n : Number])
  (varE [x : Symbol])
  (opE  [op : Op] [e1 : Exp] [e2 : Exp])
  (ifzE [b : Exp] [t : Exp] [e : Exp])
  (letE [x : Symbol] [e1 : Exp] [e2 : Exp])
  (appE [f : Symbol] [args : (Listof Exp)]))

;typ dla definicji
(define-type D
  (funE [fName : Symbol] [args : (Listof Symbol)] [body : Exp]))

;typ dla programu
(define-type Prog
  (progE [d : (Listof D)] [b : Exp]))

;;parser==============
(define (parse [s : S-Exp]) : Prog
  (cond
    [(s-exp-match? `{define {ANY ...} for ANY} s)
     ;raz konwertujemy, żeby dobrać się do pierwszego ANY, drugi raz żeby zrobić listę elementów typu s-exp
     (let ([defs (map parse-def (s-exp->list (second (s-exp->list s))))])
       ;sprawdzamy czy nazwy funkcji się nie powtarzają
       (if (is-set? defs '())
               (progE defs ;parsujemy każdą definicję w programie
                      (parse-exp (fourth (s-exp->list s))))
           (error 'parse "At least double function name!"))       
       )
     ]
    [else (error 'parse "Syntax Error!")])
  )

(define (parse-def [s : S-Exp]) : D
  (cond
    [(s-exp-match? `{fun SYMBOL {SYMBOL ...} = ANY} s)
     (let ([args (map s-exp->symbol (s-exp->list (third (s-exp->list s))))])
       ;sprawdzamy czy nasze argumenty są parami różne
       (if (is-set? args '())
           (funE (s-exp->symbol (second (s-exp->list s))) args (parse-exp (fifth (s-exp->list s))))
           ;jak argumenty nie są parami różne
           (error 'parse-def "Name Collision!")
           )
       )]
    [else (error 'parse-def "Syntax Error")])
  )

;tak naprawdę funkcja z wykładu, z pozmienianą kolejnością rzeczy do parsowania
(define (parse-exp [s : S-Exp]) : Exp
  (cond
    [(s-exp-match? `NUMBER s)
     (numE (s-exp->number s))]
    [(s-exp-match? `{ANY SYMBOL ANY} s)
     (opE (parse-op (s-exp->symbol (second (s-exp->list s))))
          (parse-exp (first (s-exp->list s)))
          (parse-exp (third (s-exp->list s))))]
    [(s-exp-match? `{ifz ANY then ANY else ANY} s)
     (ifzE (parse-exp (second (s-exp->list s)))
          (parse-exp (fourth (s-exp->list s)))
          (parse-exp (sixth (s-exp->list s))))]
    [(s-exp-match? `SYMBOL s)
     (varE (s-exp->symbol s))]
    [(s-exp-match? `{let SYMBOL be ANY in ANY} s)
     (letE (s-exp->symbol (second (s-exp->list s)))
           (parse-exp (fourth (s-exp->list s)))
           (parse-exp (sixth (s-exp->list s))))]
    [(s-exp-match? `{SYMBOL {ANY ...}} s)
     (appE (s-exp->symbol (first (s-exp->list s)))
           (map parse-exp (s-exp->list (second (s-exp->list s)))))]
    [else (error 'parse-exp "Syntax Errror!")]))

;parser dla operatorów
(define (parse-op [op : Symbol]) : Op
  (cond
    [(eq? op '+) (add)]
    [(eq? op '-) (sub)]
    [(eq? op '*) (mul)]
    [(eq? op '<=) (leq)]
    [else (error 'parse "unknown operator")]))

;helper functions
;sprawdzenie czy lista zawiera niepowtarzające się elementy
(define (is-set? lst set)
  (cond [(empty? lst) #t] ;listy pusta jest zbiorem
        [(member (first lst) set) #f] ;jak element już jest w zbiorze to lst nie była zbiorem
        [else (is-set? (rest lst) (cons (first lst) set))]) ;idziemy dalej w rekursji
  )

(define (fifth lst)
  (list-ref lst 4))

(define (sixth lst)
  (list-ref lst 5))

;złączanie dwóch list w jedną listę par
(define (zip lst1 lst2 acc)
  (if (empty? lst1)
      (reverse acc)
      (zip (rest lst1) (rest lst2) (cons (pair (first lst1) (first lst2)) acc))
  )
)

;alias dla wartości, zawsze zwrócimy liczbę
(define-type-alias Value Number)

;definiujemy domknięcie funkcji
(define-type Def-Closure
  (def-closure [args : (Listof Symbol)] [b : Exp] [env : Env]))

;; environments
;w środowisku musimy przechować zarówno zmienne, jak i definicje, bo na tym polega ewaluacja programu
;'obliczenie wartości e, przy użyciu definicji funkcji d'
(define-type Storable
  (valS [v : Value]) ;przechowujemy albo wartości, albo definicje, które później obliczymy do wartości
  (defS [d : Def-Closure])
  (undefS))

(define-type Binding
  (bind [id : Symbol] ;przechowujemy identyfikator do wskaźnika
        [ref : (Boxof Storable)]));referencja

(define-type-alias Env (Listof Binding))

;puste środowisko
(define mt-env empty)

;rozszerzanie środowiska o dany niezdefiniowany wskaźnik
(define (extend-env-undef [env : Env] [id : Symbol]) : Env
  (cons (bind id (box (undefS))) env))

;rozszerzenie środowiska o zmienną
;identyfikatorem jest symbol, reprezentujący nazwę zmiennej
(define (extend-env [env : Env] [id : Symbol] [v : Value]) : Env
  (cons (bind id (box (valS v))) env))


;wyszukiwanie danej zmiennej lub funkcji w środowisku
(define (find [env : Env] [id : Symbol]) : (Boxof Storable)
  (type-case Env env
    [empty (error 'lookup "unbound variable")]
    [(cons b rst-env) (cond
                        [(eq? id (bind-id b))
                         (bind-ref b)]
                        [else
                         (find rst-env id)])]))

;wzięcie ze środowiska wartości danej zmiennej
(define (lookup-env-var [id : Symbol] [env : Env]) : Value
  (type-case Storable (unbox (find env id))
    [(valS v) v]
    [(defS c) (error 'lookup-env-var "Not a variable")]
    [(undefS) (error 'lookup-env-var "undefined variable")]))

;wzięcie ze środowiska wartości danej danej definicji
(define (lookup-env-def [id : Symbol] [env : Env]) : Def-Closure
  (type-case Storable (unbox (find env id))
    [(defS d) d]
    [(valS v) (error 'lookup-env-var "Not a function")]
    [(undefS) (error 'lookup-env-var "undefined variable")]))

;aktualizacja środowiska dla danej funkcji
(define (update-env! [env : Env] [id : Symbol] [args : (Listof Symbol)] [b : Exp] [envD : Env]) : Void
  (set-box! (find env id) (defS (def-closure args b envD))))

;; evaluation

;operators
(define (op->proc [op : Op]) : (Value Value -> Value)
  (type-case Op op
    [(add) +]
    [(sub) -]
    [(mul) *]
    [(leq) (lambda (x y) (if (<= x y) 0 42))] ;zachodzenie warunku daje wartość 0
    [else (error 'eval-op "operator not possible to evaluate!")]
    )
  )

;program evaluation
;przyjmujemy program, zwrócimy obliczoną wartość
;aby zeewaluować program musimy najpierw rozszerzyć środowisko od definicje funkcji
(define (eval [p : Prog]) : Value
  (type-case Prog p
    [(progE defs e)
     ;; rozszerzamy środowisko o definicje, na początku tworzymy tylko wskaźniki z nazwą funkcji i pustym miejscem
     ;robimy to w dwóch krokach nie było problemu z wywłaniami rekurencyjnymi funkcji, chcemy mieć poprawny dostęp do zmiennych, w tym nazwy funkcji
     (let ([new-env (foldr (lambda (def env)
                             (extend-env-undef env (funE-fName def)))
                           mt-env defs)])
       ;teraz rozszerzymy funkcje w środowisku o pełne argumenty
       (begin
        (foldr (lambda (f fs) (type-case D f
                                [(funE id args e)
                                 (update-env! new-env id args e new-env)])) ;aktualizujemy argumenty w danej funkcji
               (void)
               defs)
        (eval-exp e new-env)))]))

;ewaluacja wyrażeń składowych
(define (eval-exp [e : Exp] [env : Env]) : Value
  (type-case Exp e
    [(numE n) n]
    [(varE v) (lookup-env-var v env)] ;jak mamy zmienną to szukamy jej w środowisku
    [(opE o e1 e2) ((op->proc o) (eval-exp e1 env) (eval-exp e2 env))] ;operator to ewaluacja operatora, lewej i prawej gałęzi
    [(ifzE b t el)
     (if (= (eval-exp b env) 0) ;zachodzenie warunku to równość z zerem
         (eval-exp t env) ;then
         (eval-exp el env))] ;else
    [(letE x e1 e2)
     (eval-exp e2 (extend-env env x (eval-exp e1 env)))] ;ewaluacja let'a to obliczenie e2 z rozszerzonym środowiskiem, przez obliczenie e1
    [(appE f args)
     ;będziemy aplikować argumenty do naszej funkcji
     ;wyszukujemy funkcję w środowisku i ewaluujemy argumenty, żeby dostać ich prawidłowe wartości, które będzie można zaaplikować do funkcji
     (apply (lookup-env-def f env) (map (lambda (arg) (eval-exp arg env)) args))])
  )

;aplikacja funkcji, wrzucamy wyliczone argumenty do naszej funkcji, wyciągniętej ze środowiska
(define (apply [d : Def-Closure] [args : (Listof Value)]) : Value
  (type-case Def-Closure d
    ;teraz musimy zeewaluować naszą funkcję,
    ;czyli obliczyć jej wartość dla poprawnie policzonych argumentów (mających jakąś wartość), to będzie nasze nowe środowisko
    ;rozszerzamy środowisko aplikacji o zmienne funkcji i ich wartości
    [(def-closure xargs body env)
     (eval-exp body (foldr (lambda (x*v env) (extend-env env (fst x*v) (snd x*v))) env (zip xargs args '())))] ;jeszcze raz obliczamy funkcję, wym razem w środowisku są poprawnie zdefiniowane wartości argumentów
    )
  )


;uruchomienie parsowania i ewaluacji
(define (run [s : S-Exp]) : Value
  (eval (parse s)))