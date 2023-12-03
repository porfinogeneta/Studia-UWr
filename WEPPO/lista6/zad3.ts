let arr = [1,2,3,4,5,6]

// funcja przyjmuje dwa typy generyczne - T - input tablica, G - output tablica
function map<T, G> (t: T[], f: (t: T) => G): G[]{
    const res: G[] = [];
    t.forEach(elem => res.push(f(elem)));
    return res;
}

console.log(map(arr, (elem => 2*elem)));


// forEach nam niczego nie zwróci
function forEach<T>(t: T[], f: (t: T) => void): void{
    for (let i = 0; i < t.length; i++) {
        f (t[i])
    }
}

forEach(arr,(elem => console.log(elem)))

function filter<T>( a: T[], f: (t: T) => boolean ): T[] {
    const res: T[] = []
    for (let i = 0; i < a.length; i++) {
        if (f(a[i])) {res.push(a[i])}        
    }
    return res
}

console.log(filter(arr, (elem => elem % 2 == 0 ? true : false)));
