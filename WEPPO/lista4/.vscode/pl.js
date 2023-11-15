function Foo(initialValue) {
    // Składowa prywatna
    let privateVariable = initialValue;
  
    // Metoda publiczna
    this.Bar = function () {
      // Wywołujemy funkcję prywatną z domknięcia
      Qux();
      console.log("Metoda publiczna Bar. Wartość prywatnej zmiennej: " + privateVariable);
    };
  
    // Funkcja prywatna
    function Qux() {
      console.log("Funkcja prywatna Qux");
    }
  }
  
  // Utwórz instancję obiektu Foo
  const myObject = new Foo(42);
  
  // Wywołaj publiczną metodę Bar, która z kolei wywoła funkcję prywatną Qux
  myObject.Bar();
  console.log(myObject.privateVariable);