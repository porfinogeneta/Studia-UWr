// function createFs(n) { // tworzy tablicę n funkcji
//     var fs = []; // i-ta funkcja z tablicy ma zwrócić i
//     // var w for na let
//     for ( var i=0; i<n; i++ ) {
//         fs[i] = function() {
//             return i;
//         };
//     };
//     return fs;
// }

// function createFs(n) { // tworzy tablicę n funkcji
//     var fs = []; // i-ta funkcja z tablicy ma zwrócić i
//     // var w for na let
//     for ( let i=0; i<n; i++ ) {
//         fs[i] = function() {
//             return i;
//         };
//     };
//     return fs;
// }
// var myfs = createFs(10);
// console.log( myfs[0]() ); // zerowa funkcja miała zwrócić 0
// console.log( myfs[2]() ); // druga miała zwrócić 2
// console.log( myfs[7]() );
// // 10 10 10 // ale wszystkie zwracają 10!?


// Jednym ze sposobów skorygowania tego nieoczekiwanego zachowania jest zastąpienie var
// przez let. Wyjaśnić dlaczego tak jest?
// jest tak dlatego że zmienna 'var' ma zasięg do całej funkcji, a nie do bloku 'for' (jak jest w przypadku let),
// tak więc późniejsze wywołania funkcji odnoszą się do ostatniej wartości zmiennej i, która będzie 10,
// oczywiście wywołania funkcji, która jest przypisana do fs[]


function createFs(n) { // tworzy tablicę n funkcji
    var fs = []; // i-ta funkcja z tablicy ma zwrócić i
    // var w for na let
    for ( var i=0; i<n; i++ ) {
        fs[i] = function(p) {
            return function() {
                return p;
            };
        }(i)
    };
    return fs;   
}
var myfs = createFs(10);
console.log( myfs[0]() ); // zerowa funkcja miała zwrócić 0
console.log( myfs[2]() ); // druga miała zwrócić 2
console.log( myfs[7]() );
// 10 10 10 // ale wszystkie zwracają 10!?

// zamiast pobierać wartość i z var przy wywołaniu w console.log, wywołujemy funkcję
// która miała parametr zadeklarowany już w momencie przechodzenia przez pętlę for
// i nie musi się ona posiłkować zmienną 'i' tylko użyje swojego parametru, który dostaje od
// natychmist się wywołującej funkcji bezpośrednio przypisanej do fs[i] 



