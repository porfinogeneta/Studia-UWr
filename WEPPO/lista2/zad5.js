var foo = {
    _name: "enqirque",
    say: (() => {return 2}),
    get my_name(){
        console.log("I'm getter");
        return foo._name;
    },
    set my_name(new_name){
        console.log("I'm setter");
        foo._name = new_name
    }
}

// dodanie metody
foo.new_method = function (){console.log("I'm a new function!");}
console.log(foo.new_method());
// dostęp do pola
console.log(foo._name);
// dostęp do pola, przy użyciu getter
console.log(foo.my_name)
// zmiana pola, używając setter
foo.my_name = 'hermanez'
console.log(foo.my_name);

// dodanie pola do obiektu
Object.defineProperty(foo, 'specific', {
    value: 'Can add value'
})
// dodanie metody do obiektu
Object.defineProperty(foo, 'specific_method', {
    value: function(){
        return "Can add function"
    }
})
//console.log(foo.specific_method);
console.log(foo);

// dodawanie get/set jest TYLKO możliwe używając Object.defineProperty,
// MOŻNA natomiast dodawać w ten sposób pole i metodę

// get/set używane jest do panowania nad tym co pobieramy/zwracamy z obiektu


Object.defineProperties(foo, {
    specific_set: {
        set: function (new_specific) {
            foo.specific = new_specific;
        }
    }
});

Object.defineProperties(foo, {
    specific_get: {
        get: function() {
            return foo.specific;
        }
    }
});

foo.new_specific = 'New Value'
console.log(foo);