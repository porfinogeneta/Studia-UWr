const message: string = 'Hello, TypeScript!';
const n: number = 2;
const nnext: string = "2"
console.log(message);

// na początku używamy polecenia: 
// tsc zad1.ts => zad1.js => node zad1.js
// albo po prostu ts-node zad1.ts

// tsc --watch pozwala na nasłuchiwanie zmian i log błędów kompilacji
// można debuggować, ale trzeba szybko f11 klikać, bo czasem wyskakuje