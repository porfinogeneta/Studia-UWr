// zad 1
type myPick<T, K extends keyof T> = {
    [k in K]: T[k]
}

// zad 2
// P ma myć kluczem T i wartości nie możemy zmieniać
type myReadonly<T> = {
    readonly [P in keyof T]: T[P]
}

// zad 3
type TupleToObject<T extends readonly string[]> = {
    [P in T[number]]: P
  }

// zad 4
type First<T extends any[]> = T extends []? never : T[0]

// zad 5
type Length<T extends readonly any[]> = T['length'] 

// zad 6
type MyExclude<T, U> = U extends T ? never : T

// zad 7
// infer zapewnia kompilator że wszystko jest explicite zadeklarowane
// sprawdzamy czy T jest Promise, pobieramy wartość typu generycznego z tego Promise
// jeśli N będzie Promise, rekurencyjnie dalej odpakowujemy, jak nie to go zwracamy
// jak T nie był Promise to zwracamy never, nigdy takie coś nie nastąpi
type MyAwaited<T extends Promise<any>> = T extends Promise<infer N> ?
  N extends Promise<any> ? MyAwaited<N> : N : never

// zad 8
type If<C extends boolean, T, F> = C extends true ? T : F

// zad 9 
// używamy unknown, bo  no operations are permitted on an unknown without
// first asserting or narrowing to a more specific type.

//unknown is the parent type of all other types. it's a regular type in the type system.
// any means "disable the type check". it's a compiler directive.
type Concat<T extends readonly any[], U extends readonly any[]> = [...T, ...U]

// zad 10
// wydobywamy pierwszy element i rekurencyjnie badamy tablicę
type Includes<T extends readonly any[], U> = T extends [infer First, ...infer Rest] ?
    Equal<First, U> extends true ? true : Includes<Rest, U> : false
    
// zad 11
type Push<T extends unknown[], U> = [...T, U]

// zad 12
type Unshift<T extends unknown[], U> = [U, ...T]

// zad 13
// extends nakłada wymagania na T, ma być odpowiednią funkcją
// sprawdzamy czy T jest funkcją, pobieramy argumenty i je zwracamy jak T jest funkcją
type MyParameters<T extends (...args: any[]) => any> = T extends (...args: infer U) => any ? U : any 