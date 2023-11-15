var n = 12.2;
// liczba ma prototyp?
console.log( typeof Object.getPrototypeOf( n ) );
// można jej dopisać pole/funkcję?
n.foo = 'foo';

console.log( n.foo = 'foo' );
console.log( n.foo );
console.log( n.toFixed() );

// Czy wartości typów prostych też mają prototypy? 
// typy proste nie mają prototypów, ale JS opakowuje typy proste w
// prototype od obiektu, gdy jest to potrzebne, np gdy wywołujemy
// na danym typie jakieś operacje
// ale ta zamiana na obiekt jest tylko chwilowa i nie można podpinać właściowści do takich obiektów
// tuż po wykonaniu tej funkcji na typie prymitywnym jest zmieniany z powrotem na typ prymitywny z obiektu

// Wyjaśnić wynik działania linii console.log( n.foo = 'foo' ) programu:
// Zwraca ona undyfined, ponieważ n jest tylko na chwilę zamieniony na obiekt (new Number()) a potem
// już jak tym obiektem być nie musi traci właściwości obiektowe
