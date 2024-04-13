// Zademonstrować w praktyce tworzenie własnych modułów oraz ich włączanie do
// kodu za pomocą require. Czy możliwa jest sytuacja w której dwa moduły tworzą cykl
// (odwołują się do siebie nawzajem)? Jeśli nie - wytłumaczyć dlaczego, jeśli tak - pokazać
// przykład implementacji.

// własny moduł tworzymy na dwa rózne sposoby:
/*
module exports
*/
// 1 SPOSÓB
let a = require('./a');
a.work_a(5);

a.other_a(100)

// 2 SPOSÓB
// const {my_new_function} = require('./a')

// my_new_function()


// TAK moduły mogą być w cyklu

