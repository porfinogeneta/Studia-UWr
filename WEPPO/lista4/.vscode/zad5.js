let Foo = function(name, age){
    this.name = name
    this.age = age

    
    // podpięcie do łańcucha prototypów
    Foo.prototype.Bar = function () {
        let Qux = function () {
            console.log('I am Qux function');
        }
            return function(){
                Qux()
            }
        console.log(`I am ${this.name}, aged: ${this.age}`);
        
        
    }()
    
}



let Foo2 = function (name, age, role) {
    Foo.call(this, name, age)
    this.role = role
}

Foo2.prototype = Object.create( Foo.prototype );

// obiekty
foo1 = new Foo('Hugo', 20)
foo1.Bar()

Foo.Qux()

// łańcuch prototypów
foo2 = new Foo2('Tomasz', 23, 'builder');
// foo2.Qux()

