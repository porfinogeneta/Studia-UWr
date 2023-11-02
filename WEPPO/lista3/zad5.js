function createGenerator(n) {
    var _state = 0;
    return {
        next : function() {
        return {
            value : _state,
            done : _state++ >= n
            }
        }
    }
}

// dzięki temu możemy używać for of
// argumentem [Symbol.iterator] musi być jakaś funckja, zwracająca obiekt iterator z metodą next,
// po prostu podpięcie zewnętrznej funkcji
var foo = {
    [Symbol.iterator] : function() {return createGenerator(10)}
};

var foo1 = {
    [Symbol.iterator] : function() {return createGenerator(15)}
}

var foo2 = {
    [Symbol.iterator] : function() {return createGenerator(20)}
}

for ( var f of foo ){
    console.log(f);
}

for ( var f of foo1 ){
    console.log(f);
}

for ( var f of foo2 ){
    console.log(f);
}