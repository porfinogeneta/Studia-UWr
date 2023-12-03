import { one1, one2, somestr } from "./module";
import SomeCustomNewName from "./default_module"

one1(2)
one2(3)

SomeCustomNewName(42)

console.log(somestr);


// główne różnice
// NAMED MODULES
/*
- moduły, w których możemy eksportować kilka różnych wartości, 
- pobieramy konkretne moduły o konkretnych nazwach
*/

// DEFAULT MODULES
/*
- możemy eksportować tylko jedną wartość z takiego modułu
- możemy ją nazwać jak chcemy
*/