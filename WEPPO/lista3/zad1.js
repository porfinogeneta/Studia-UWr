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
    let cache = {}

    return function(n){
        if (n in cache) {
            return cache[n]
        }else {
            let result = funct(n)
            cache[n] = result
            return result
        }
    }
}


let fib_memo = memoize(fib_recu)
// console.log(fib_memo(15));

function measureTime(n){

    for (let i = 10; i < n; i++){
        console.log(`For n: ${i}`)
        
        //console.log("Recu version:")
        console.time('fibrecu');
        fib_recu(n);
        console.timeEnd('fibrecu');
        
        //console.log("Iter version:")
        console.time('fibiter');
        fibiter(n);
        console.timeEnd('fibiter');

        //console.log("Recu memoized version:")
        console.time('fibrecu memo');
        fib_memo(n);
        console.timeEnd('fibrecu memo');
        
    }
}

measureTime(7);
