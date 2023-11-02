console.log( (![]+[])[+[]] + (![]+[])[+!+[]] + ([![]]+[][[]])[+!+[]+[+[]]] + (![]+[])[!+[]+!+[]] );

// f
//  (![]+[])[+[]]
// ![] - [] to pusty obiekt, ewaluuje się do true, ![] daje zatem false
// ![] => !true => false
// false+[] - oba parametry + konwertują się do String, czyli mamy
// false+[] => "false"+"" => "false"
// "false"
// +[] - ToNumber
// +[] => ToNumber => ToPrimitive => [[DefaultValue]]
//[ToNumber] - ToPrimitive
// [[DefaultValue]] - dla pustego Array dostajemy 0, zatem
// [0]
// ostatecznie - "false"[0] => "f"

// a
(![]+[])[+!+[]]
// znowu mamy string "false" z pierwszego
// +[] => 0
// !+[] => !0 => true
// +!+[] => +(!0) => +(true) => ToNumber(true) => 1
//ostatecznie
// "false"[1] => "a"

// i
//([![]]+[][[]])[+!+[]+[+[]]]

// zacznijmy od [][[]]
//[[]] => [''] ,bo nie jest to liczba
// zatem mamy
// [][''] => undefined (szukamy w [] czegoś o nazwie '')

//([![]]+[][[]])
// [![]] => false
// [][[]] => undefined (z powyżej)
// ([![]]+[][[]]) => (false+undefined) => ("false"+"undefined") => "falseundefined"

//[+!+[]+[+[]]] <=> [+(!(+[])) + [+[]]]
// [+[]] => [0]

// +[] jest przymuszone do bycia 0
// !(+[]) => !0 => !false => true
// +(!(+[])) => +(!0) => +(true) => 1
// zatem (normalnie by się dodało, ale nie tutaj)
// [+(!(+[])) + [+[]] => [1 + 0] => ["1" + "0"] => ["10"]
// korzystamy z wiedzy, że:
// > [1, 2, 3]["0"]
// 1
// > [1, 2, 3]["1"]
// 2
// String zmienia się w liczbę, gdy próbujemy się dostać do Array

// ostatecznie
//"falseundefined"["10"] => 'i


// l
//(![]+[])[!+[]+!+[]]
// (![]+[]) => "false"

//[!+[]+!+[]]
//!+[] => !0 => true
//[!+[]+!+[]] => [true+true] => [ToNumber(true) + ToNumber(true)] => [1 + 1] = 2
// ostatecznie
// "false"[2] => 'l'




