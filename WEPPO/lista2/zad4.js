// typeof zwraca string, reprezentujący typ danych albo wartości
// do typów prymitywnych raczej
typeof 5; // Returns "number"
typeof "hello"; // Returns "string"
typeof true; // Returns "boolean"
typeof {} // Returns "object"
typeof [] // Returns "object"
typeof null // Returns "object" (a quirk in JavaScript)
typeof function() {} // Returns "function"

// instanceof - sprawdza czy obiekt jest przykładem konkretnego konstruktora czy klasy
// sprawdza łańcuch prototypów obiektu, żeby się przekonać co skonstruuowało obiekt
function Car(make, model) {
    this.make = make;
    this.model = model;
  }
  
  const mytrue = new Boolean(false)
  const myCar = new Car("Toyota", "Camry");
  console.log(myCar instanceof Car); // Returns true
  console.log(typeof Car + " typeof"); // Returns true
  console.log(true instanceof Boolean);
  console.log(mytrue instanceof Boolean);
  console.log(true instanceof Boolean);

  console.log(typeof 3)

  //typeof - typ danych wartości lub zmiennych, zwraca konkretnie ten typ
  // instanceof - czy obiekt jest przykładem konkretneo konstruktora lub klasy, zwraca Boolean
  
