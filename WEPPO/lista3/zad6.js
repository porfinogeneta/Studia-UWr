function fib() {
    let prev_1 = 1;
    let prev_2 = 1;
    return {
        next : function() {
            let state = prev_1 + prev_2
            prev_1 = prev_2
            prev_2 = state
            return {
                value : state,
                done : false
            }
        }
    }
}


//// WHILE
// var it = fib();
// var _result;
// while ( _result = it.next(), !_result.done ) {
//     console.log( _result.value );
// }

//// FOR OF
// let iter = {
//     [Symbol.iterator]: fib
// }
// for (let f of iter) {
//     console.log(f);
// }

function *fib_gen() {
    let prev_1 = 1
    let prev_2 = 1

    while (true){
        let state = prev_1 + prev_2
        prev_1 = prev_2
        prev_2 = state
        yield state
    }
}

//// WHILE
// var it = fib_gen();
// var _result;
// while ( _result = it.next(), !_result.done ) {
//     console.log( _result.value );
// }

//// FOR OF
let iter = {
    [Symbol.iterator]: fib_gen
}
for (let f of iter) {
    console.log(f);
}

// W obu przypadkach można można iterować za pomocą for of