let Foo = function(name, age){
    this.name = name
    this.age = age

    let Qux = function () {
        console.log('I am Qux function');
    }
    
    Foo.prototype.Bar = function () {
        console.log(`I am ${this.name}, aged: ${this.age}`);
        Qux()
    }
    
}



let Foo2 = function (name, age, role) {
    Foo.call(this, name, age)
    this.role = role
}

Foo2.prototype = Object.create( Foo.prototype );

// obiekty
foo1 = new Foo('Hugo', 20)
foo1.Bar()

// łańcuch prototypów
foo2 = new Foo2('Tomasz', 23, 'builder');

