/*
W trakcie wykładu pokazano funkcję getLastProto, za pomocą której można spraw-
dzić do jakiego obiektu zbiega łańcuch prototypów. Wykonać eksperyment dla kilku obiek-
tów i potwierdzić (sprawdzając równość referencji) że istotnie, łańcuch prototypów zbiega
do jednego i tego samego obiektu.
*/

let animalProto = {
    action: function(){
        return "Run!";
    },
    name: 'monster'
}

let cat = {
    name: 'cat',
    health: 100,
    desc: 'This is cat property!'
}

let dog = {
    name: 'dog',
    health: 200
}

// ustawiamy prototyp dla naszego obiektu 'cat' i dog
Object.setPrototypeOf(cat, animalProto)
Object.setPrototypeOf(dog, animalProto)

let kitty = {
    name: 'kitty',
    health: 1
}

Object.setPrototypeOf(kitty, cat)

let otherActionProto = {
    todo: function(){
        return console.log("I am eating");
    }
}

Object.setPrototypeOf(otherActionProto, kitty)
// Object.setPrototypeOf(otherActionProto, animalProto) <- relacja przechodnia, mogę tak zrobić
// Object.setPrototypeOf(animalProto, otherActionProto) <- zapętlenie, tak nie wolno 

// nasze drzewo prototypów jest następujące:
//                    animalProto
//                  /            \
//                cat           dog
//              /    
//            kitty  
//          /
//       otherActionProto

// console.log(otherActionProto.action());

function getLastProto(o) {
    var p = o;
    do {
        o = p;
        p = Object.getPrototypeOf(o);
    } while (p);
    return o;
}

// console.log(getLastProto(animalProto));
console.log(getLastProto(animalProto) == getLastProto(cat) && getLastProto(cat) == getLastProto(dog) && getLastProto(animalProto) == getLastProto(otherActionProto) );
