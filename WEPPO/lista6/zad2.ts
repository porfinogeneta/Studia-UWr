function fib_recu(n: number): number{
    if (n == 0){
        return 0
    }else if (n == 1){
        return 1
    }else {
        return fib_recu(n-1) + fib_recu(n-2) 
    }
}



function memoize(funct: Function){
    // robimy custom'owy typ do Cache z obiektem key i number
    type Cache = {[key: number]: number}
    const cache: Cache = {}

    return function(n: number): number{
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

let fib_memo = memoize(fib_recu)

console.log(fib_memo(20));
