var p = {
    name: 'jan'
}
var q = {
    name: 'Elon',
    surname: 'kowalski'
}

var w = {
    name: 'Rodriguez'
}

// p - czyj prototyp, q - kto nim będzie
Object.setPrototypeOf( p, q );
Object.setPrototypeOf(q, w);
// console.log( p.name );
// console.log( p.surname );

// zwraca prawdę, jak pole jest z obiektu, fałsz wpp
let isFromObject = function(obj, field){
    return (Object.keys(obj).includes(field)) 
}

// console.log(q.hasOwnProperty('name'));

// enumeracja pól/funkcji z obiektu
let enumObject = function(obj){
    const keys = Object.keys(obj)
    keys.forEach(key => {
        console.log(key, obj[key]);
    })
}

// enumeracja pól/funkcji które są w obiekcie oraz w łańcuchu prototypów
let enumObjectAndPrototypeChain = function (obj) {
    let o = obj
    let p = o
    // lista na pola/funkcje w obiekcie i prototypach
    do {
        o = p
        p = Object.getPrototypeOf(o)
        
        if (p == null){
            break
        }
        keys = Object.keys(p) // bierzemy wszystkie klucze z obiektu
        // iteracja po kluczach i wydobycie tylko tych które były w obiekcie i prototypie
        keys.forEach(key => {
            if (isFromObject(obj, key)){
                console.log(key, p[key]);
            }
        })
        
    }while(p)
}

console.log("W obiekcie:");
enumObject(p)
console.log("W obiekcie oraz łańcuchu prototypów (wartość z łańcucha):");
enumObjectAndPrototypeChain(p)