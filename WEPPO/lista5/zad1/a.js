

// a.js
// 1 SPOSÓB
module.exports = { work_a, other_a }; // z tego moduło zostanie zwrócone work_a

let b = require('./b');

function work_a(n) {
    if ( n > 0 ) {
        console.log( `a: ${n}`);
        b.work_b(n-1);
    }
}

function other_a(n) {
    console.log(n + 100);
}

// 2 SPOSÓB
// exports.my_new_function = () => {
//     console.log('the other type of module');
// }
