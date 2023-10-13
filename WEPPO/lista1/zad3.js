function easyPrimes(range){
    let primes = [];
    for (let num = 2; num < range; num++) {
        let isPrime = true;
        for (let i = 2; i < num; i++) {
             if (num % i == 0){
                isPrime = false;
                break;
             }
        }
        if (isPrime) {primes.push(num)};
    }
    return primes;
}

console.log(easyPrimes(10000));