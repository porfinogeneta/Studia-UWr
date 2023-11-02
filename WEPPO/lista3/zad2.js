function forEach(a, f){
    for (let i = 0; i < a.length; i++){
        f(a[i])
    }
}


var a = [1,2,3,4];
// forEach( a, _ => { console.log( _ ); } );
// forEach(a, function(x) {console.log(x)})

function map(a, f){
    const result = []
    for (let i = 0; i < a.length; i++){
        result.push(f(a[i]))
    }
    return result
}

map( a, _ => _ * 2 );
let new_a = map(a, function(x) { return x * 2})
console.log(new_a);

function filter(a, f){
    const result = []
    for (let i = 0; i < a.length; i++) {
        if (f(a[i])){
            result.push(a[i])
        }
    }
    return result
}

let new_a1 = filter( a, _ => _ < 3 );
// filter(a, function(x) { return x < 3; })
console.log(new_a1);

// console.log(a.filter((item) => item < 3));