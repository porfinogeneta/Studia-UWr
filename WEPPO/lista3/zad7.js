function* fib() {
    let prev_1 = 1
    let prev_2 = 1

    while (true){
        let state = prev_1 + prev_2
        prev_1 = prev_2
        prev_2 = state
        yield state
    }
}

function* take(it, top) {
    for (let i = 0; i < top; i++){
        // nasz generator pod yield zwraca funkcję next, zwracającą podany niżej obiekt
        // nie robimy kolejnej pętli żeby yield się nie restartowało
        const {value, done} = it.next() // pobieramy value i done z obiektu zwróconego przez generator
        if (done) {
            break
        }
        yield value
    }
}
    // zwróć dokładnie 10 wartości z potencjalnie
    // "nieskończonego" iteratora/generatora

for (let num of take( fib(), 10 ) ) {
    console.log(num);
}