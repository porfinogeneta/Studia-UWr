// Różnica między apply a call polega na tym że rzeczywiste argumenty wywołania są podawane albo
// przez tablicę (apply) albo przez listę argumentów oddzielonych przecinkiem (call)


function sum(...args) {
    // Array.prototype.slice.call(args) -> zwinięcie argumentów do Array
    // call mówi slice na czym ma operować, na argumentach po przecinku
    // slice konwertuje do Array
    //  na końcu zwinięcie reduce'em
    return Array.prototype.slice.call(args).reduce((sum, elem) => sum + elem, 0)
}

sum(1,2,3);
console.log(sum(1,2,3));
// // 6
console.log(sum(1,2,3,4,5));
// 15

//you're essentially telling the slice method to treat args as the array on which it should operate.
//This allows you to convert the array-like args into a real array so that you can use array methods 
//like reduce on it.