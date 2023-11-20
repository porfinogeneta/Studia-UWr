var Person = function(name, surname) {
    this.name = name;
    this.surname = surname;
    console.log('elo');
}
Person.prototype.say = function() {
    return `${this.name} ${this.surname}`;
}

var Worker = function(name, surname, age) {
    // wywołanie bazowej funkcji konstruktorowej
    Person.call( this, name, surname );
    this.age = age;
}
// // powiązanie łańcucha prototypów
// tworzy nowy obiekt używając już istniejącego jako prototypu
//  Object.create() tworzy nową instancję obiektu i ustawia jej wskazany obiekt jako prototyp
// Worker.prototype = Object.create( Person.prototype );

// // Worker.prototype.say = function() {
// //     // "wywołanie metody z klasy bazowej"
// //     var _ = Person.prototype.say.call( this );
// //         return `${_} ${this.age}`;
// // }

// var w = new Worker('jan', 'kowalski', 48);
// console.log( w.say() )

// // Dlaczego jest to podejście prawidłowe?
// // Oszczędzamy pamięć, bo nie potrzebujemy kopii tej samej funkcji
// // w nie uruchamiamy konstruktora kilkukrotnie - jak w new()


// ================================================


// Worker.prototype = Person.prototype ;

// Worker.prototype.say = function() {
//     // "wywołanie metody z klasy bazowej"
//     var _ = Person.prototype.say.call( this );
//         return `${_} ${this.age}`;
// }

// var w = new Worker('jan', 'kowalski', 48);
// console.log( w.say() )
// console.log( w.say2() )

// Dlaczego łańcucha prototypów nie można zestawiać tak:
// Worker.prototype = Person.prototype ;
// Nie można w taki sposób go zestawiać, ponieważ w takim przypadku
// mieszamy prototypy Worker i Person, Worker miał być 'dzieckiem' Person, a w tym momencie
// go zrównujemy, oprócz tego teraz każde wywołanie Worker.prototype.say 
// będzie powodowało nieskończoną rekursję, bo będziemy uruchamiać tę samą porcedurę w kółko

// =================================================

// Worker.prototype = new Person() ;

// Worker.prototype.say = function() {
//     // "wywołanie metody z klasy bazowej"
//     var _ = Person.prototype.say.call( this );
//         return `${_} ${this.age}`;
// }

// var w = new Worker('jan', 'kowalski', 48);
// console.log( w.say() )
// console.log( w.say2() )

// Dlaczego nie używać
// Worker.prototype = new Person() ; ?
// Główna różnica z Object.create() polega na tym, że
// Object.create zwraca nowy obiekt, podczas gdy new zwraca konstrukor obiektu albo sam obiekt
// new() de facto wywołuje funkcję konstrukora, a Object.create() tego nie robi
// na teście console.log dwa razy się uruchamia z Person, przy użyciu new()
// raz dla skonstruoowania Person - Person.call() z Worker, drugi raz przez new()

// Możliwe wady to a) brak możliwości nadpisywania metod, b) niepotrzebne uruchamianie konstruktora kilka razy

