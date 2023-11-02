const pies = {
    name: 'Burek',
    age: 4,
    bark: function() { console.log("hau hau");},
    place: 'Buda in Pest'
}

const n = {
    nn: 'name',
    NN: 'name2'
}

const a = {
    "age": 6
}

// a

// różnica polega na metodzie wyszukania 
// . kompilator wie w czasie kompilacji, że jest to atrybut obiektu
// [] wyszukanie ma miejsce w czasie runtimu i trzeb zrobić więcej typecheckingu
// [] jest ok 3x wolniejszy
// console.log(pies['name']);
// console.log(pies.age);

// b
// console.log(pies[1]) // dostajemy 'undefined'
// pies[0] = "Ogórek" // notacja [n] może służyć tylko do zmiany wartości
// console.log(pies);

// // jak argumentem operatora jest inny obiekt to tworzymy klucz nierozróżnialny, chyba że korzystamy z 
// // wartości zgromadzonych w obiekcie
// pies[n] = 2
// console.log(pies);
// pies[a] = 3
// console.log(pies);


// // używamy wartości w obiekcie żeby się do niego dostać
// console.log(pies[n.nn]); // udało się dostać imię
// // modyfikacja imienia
// pies[n.nn] = "Rurek"
// console.log(pies);
// // zmiania nazwy klucza
// pies[n.NN] = pies[n.nn]
// delete pies[n.nn]
// console.log(pies);
// // wpływ programisty na klucz - jak użyjemy obiektu nic nie zmienimy, klucz to anonimowy obiekt,
// można użyć wartości w obiektcie do zrobienia nowego klucza, użycie liczby generuje nowy klucz
// można zrobić klucz postaci ["hello world"]

// c
let tab = [10,9,8,7,6,5,4,3,2,1]

const inny_obiekt = {
    a: 'aaa',
    b: 1
}

const jeszcze_inniejszy = {
    k: 2
}
// jak napis jest liczbą wtedy można zmienić
// tab["1"] = 2
// console.log(tab);

// tab['a'] = 111
// console.log(tab); // dodajemy do tablicy wartość typu key: value

// // używamy wartości z innego obiektu, wtedy można zmienić
// tab[inny_obiekt.b] = 99
// console.log(tab);

// w przypadku obiektu dodajme po prostu anonimowy klucz do tablicy
tab[inny_obiekt] = 2
console.log(tab); // dodany jest po prostu kolejny obiekt do tablicy

tab[jeszcze_inniejszy] = 42
console.log(tab);

// tab['a'] = 222
// console.log(tab);
// for (let i = 0; i < tab.length; i++){
//     console.log(tab[i]);
// }
//tab.forEach((elem) => console.log(elem))
//Czy i jak zmienia się zawartość tablicy jeśli zostanie do niej dopisana właściwość
//pod kluczem, który nie jest liczbą? - do tablicy są dodane obiekty, albo wartości typu key: value,
// nie można po nich iterować i nie wliczają się w długość

// można przestawić długość
// tab.length = 20; // tablica jest uzupełniana undyfined
// console.log(tab);
// for (let i = 0; i < tab.length; i++){
//     console.log(tab[i]);
// }
// tab.length = 5 // zostaje 5 elementów, tylko te z przodu
// console.log(tab);
// for (let i = 0; i < tab.length; i++){
//     console.log(tab[i]);
// }


