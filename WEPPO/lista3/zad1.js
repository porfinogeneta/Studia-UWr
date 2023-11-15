function fib_recu(n){
    if (n == 0){
        return 0
    }else if (n == 1){
        return 1
    }else {
        return fib_recu(n-1) + fib_recu(n-2) 
    }
}

function fibiter(n){
    let prev0 = 0;
    let prev1 = 1;
    if (n > 1){
        for (let i = 1; i < n; i++) {
            let help = prev0;
            prev0 = prev1;
            prev1 = help + prev1;
        }
    }
    return prev1;
}


function memoize(funct){
    var cache = {}

    return function(n){
        if (n in cache) {
            console.log(n);
            return cache[n]
        }else {
            var result = funct(n)
            cache[n] = result
            return result
        }
    }
}

// zapamiętujemy funkcję rekurencyjną
let fib_memo = memoize(fib_recu)
// fib_recu = memoize(fib_recu) // <- tak powinno być 
// console.time('memo');
// // napełniam cache
// fib_memo(15)
// console.timeEnd('memo')

console.time('memo1')
fib_memo(15)
fib_memo(15)
fib_memo(15)
fib_memo(15)
console.timeEnd('memo1')

console.time('memo2')
// korzystam z tego co już tam było w cache
fib_memo(16)
console.timeEnd('memo2')

function measureTime(n){

    for (let i = 1; i < n; i += 3){
        console.log(`For n: ${i}`)
        
        //console.log("Recu version:")
        console.time('fibrecu');
        fib_recu(i);
        console.timeEnd('fibrecu');
        
        //console.log("Iter version:")
        console.time('fibiter');
        fibiter(i);
        console.timeEnd('fibiter');

        //console.log("Recu memoized version:")
        console.time('fibrecu memo');
        fib_memo(i);
        console.timeEnd('fibrecu memo');
        
    }
}

measureTime(20);
