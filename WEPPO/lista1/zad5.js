function fibiter(n){
    let prev0 = 0;
    let prev1 = 1;
    if (n > 1){
        for (let i = 1; i < n; i++) {
            let help = prev0;
            prev0 = prev1;
            prev1 = help + prev1;
        }
    }
    return prev1;
}

function fibrecu(n){
    if (n == 0){
        return 0;
    }else if (n == 1){
        return 1;
    }else if (n == 2){
        return 1;
    }else {
        return fibrecu(n-1) + fibrecu(n-2);
    }
}

function measureTime(n){

    for (let i = 10; i < n; i++){
        console.log(`For n: ${i}`)
        
        //console.log("Recu version:")
        console.time('fibrecu');
        fibrecu(n);
        console.timeEnd('fibrecu');
        
        //console.log("Iter version:")
        console.time('fibiter');
        fibiter(n);
        console.timeEnd('fibiter');
        
    }
}

measureTime(40);

// wyniki Nodejs
// For n: 10
// Recu version:
// fibrecu: 1.036s
// Iter version:
// fibiter: 0.196ms
// For n: 11
// Recu version:
// fibrecu: 1.036s
// Iter version:
// fibiter: 0.092ms
// For n: 12
// Recu version:
// fibrecu: 1.011s
// Iter version:
// fibiter: 0.13ms
// For n: 13
// Recu version:
// fibrecu: 1.024s
// Iter version:
// fibiter: 0.091ms
// For n: 14
// Recu version:
// fibrecu: 1.018s
// Iter version:
// fibiter: 0.113ms
// For n: 15
// Recu version:
// fibrecu: 1.054s
// Iter version:
// fibiter: 0.094ms
// For n: 16
// Recu version:
// fibrecu: 1.012s
// Iter version:
// fibiter: 0.082ms
// For n: 17
// Recu version:
// fibrecu: 1.020s
// Iter version:
// fibiter: 0.083ms
// For n: 18
// Recu version:
// fibrecu: 1.014s
// Iter version:
// fibiter: 0.117ms
// For n: 19
// Recu version:
// fibrecu: 1.010s
// Iter version:
// fibiter: 0.074ms
// For n: 20
// Recu version:
// fibrecu: 1.005s
// Iter version:
// fibiter: 0.078ms
// For n: 21
// Recu version:
// fibrecu: 1.005s
// Iter version:
// fibiter: 0.083ms
// For n: 22
// Recu version:
// fibrecu: 1.016s
// Iter version:
// fibiter: 0.087ms
// For n: 23
// Recu version:
// fibrecu: 1.008s
// Iter version:
// fibiter: 0.085ms
// For n: 24
// Recu version:
// fibrecu: 1.011s
// Iter version:
// fibiter: 0.087ms
// For n: 25
// Recu version:
// fibrecu: 1.010s
// Iter version:
// fibiter: 0.083ms
// For n: 26
// Recu version:
// fibrecu: 1.062s
// Iter version:
// fibiter: 0.087ms
// For n: 27
// Recu version:
// fibrecu: 1.096s
// Iter version:
// fibiter: 0.08ms
// For n: 28
// Recu version:
// fibrecu: 1.019s
// Iter version:
// fibiter: 0.08ms
// For n: 29
// Recu version:
// fibrecu: 1.228s
// Iter version:
// fibiter: 0.078ms
// For n: 30
// Recu version:
// fibrecu: 1.155s
// Iter version:
// fibiter: 0.077ms
// For n: 31
// Recu version:
// fibrecu: 1.080s
// Iter version:
// fibiter: 0.085ms
// For n: 32
// Recu version:
// fibrecu: 1.068s
// Iter version:
// fibiter: 0.078ms
// For n: 33
// Recu version:
// fibrecu: 1.077s
// Iter version:
// fibiter: 0.092ms
// For n: 34
// Recu version:
// fibrecu: 1.043s
// Iter version:
// fibiter: 0.076ms
// For n: 35
// Recu version:
// fibrecu: 1.024s
// Iter version:
// fibiter: 0.072ms
// For n: 36
// Recu version:
// fibrecu: 1.059s
// Iter version:
// fibiter: 0.082ms
// For n: 37
// Recu version:
// fibrecu: 1.059s
// Iter version:
// fibiter: 0.084ms
// For n: 38
// Recu version:
// fibrecu: 1.087s
// Iter version:
// fibiter: 0.081ms
// For n: 39
// Recu version:
// fibrecu: 1.104s
// Iter version:
// fibiter: 0.084ms

// wyniki Chromium
// For n: 10
// zad5.js:34 fibrecu: 1370.491943359375 ms
// zad5.js:39 fibiter: 0.06494140625 ms
// zad5.js:29 For n: 11
// zad5.js:34 fibrecu: 1289.27880859375 ms
// zad5.js:39 fibiter: 0.00390625 ms
// zad5.js:29 For n: 12
// zad5.js:34 fibrecu: 1367.663818359375 ms
// zad5.js:39 fibiter: 0.005859375 ms
// zad5.js:29 For n: 13
// zad5.js:34 fibrecu: 1268.472900390625 ms
// zad5.js:39 fibiter: 0.022216796875 ms
// zad5.js:29 For n: 14
// zad5.js:34 fibrecu: 1264.036865234375 ms
// zad5.js:39 fibiter: 0.0048828125 ms
// zad5.js:29 For n: 15
// zad5.js:34 fibrecu: 1264.869873046875 ms
// zad5.js:39 fibiter: 0.0048828125 ms
// zad5.js:29 For n: 16
// zad5.js:34 fibrecu: 1246.634033203125 ms
// zad5.js:39 fibiter: 0.006103515625 ms
// zad5.js:29 For n: 17
// zad5.js:34 fibrecu: 1241.718017578125 ms
// zad5.js:39 fibiter: 0.00390625 ms
// zad5.js:29 For n: 18
// zad5.js:34 fibrecu: 1249.001953125 ms
// zad5.js:39 fibiter: 0.007080078125 ms
// zad5.js:29 For n: 19
// zad5.js:34 fibrecu: 1274.744873046875 ms
// zad5.js:39 fibiter: 0.0068359375 ms
// zad5.js:29 For n: 20
// zad5.js:34 fibrecu: 1243.646240234375 ms
// zad5.js:39 fibiter: 0.0048828125 ms
// zad5.js:29 For n: 21
// zad5.js:34 fibrecu: 1271.7509765625 ms
// zad5.js:39 fibiter: 0.005126953125 ms
// zad5.js:29 For n: 22
// zad5.js:34 fibrecu: 1238.49609375 ms
// zad5.js:39 fibiter: 0.02197265625 ms
// zad5.js:29 For n: 23
// zad5.js:34 fibrecu: 1301.293212890625 ms
// zad5.js:39 fibiter: 0.006103515625 ms
// zad5.js:29 For n: 24
// zad5.js:34 fibrecu: 1269.845947265625 ms
// zad5.js:39 fibiter: 0.0068359375 ms
// zad5.js:29 For n: 25
// zad5.js:34 fibrecu: 1241.972900390625 ms
// zad5.js:39 fibiter: 0.006103515625 ms
// zad5.js:29 For n: 26
// zad5.js:34 fibrecu: 1276.684814453125 ms
// zad5.js:39 fibiter: 0.008056640625 ms
// zad5.js:29 For n: 27
// zad5.js:34 fibrecu: 1252.177001953125 ms
// zad5.js:39 fibiter: 0.03125 ms
// zad5.js:29 For n: 28
// zad5.js:34 fibrecu: 1263.447021484375 ms
// zad5.js:39 fibiter: 0.001953125 ms
// zad5.js:29 For n: 29
// zad5.js:34 fibrecu: 1287.06494140625 ms
// zad5.js:39 fibiter: 0.002197265625 ms
// zad5.js:29 For n: 30
// zad5.js:34 fibrecu: 1320.163818359375 ms
// zad5.js:39 fibiter: 0.0009765625 ms
// zad5.js:29 For n: 31
// zad5.js:34 fibrecu: 1263.551025390625 ms
// zad5.js:39 fibiter: 0.001953125 ms
// zad5.js:29 For n: 32
// zad5.js:34 fibrecu: 1275.125 ms
// zad5.js:39 fibiter: 0.0009765625 ms
// zad5.js:29 For n: 33
// zad5.js:34 fibrecu: 1294.27197265625 ms
// zad5.js:39 fibiter: 0.002685546875 ms
// zad5.js:29 For n: 34
// zad5.js:34 fibrecu: 1300.5361328125 ms
// zad5.js:39 fibiter: 0.001953125 ms
// zad5.js:29 For n: 35
// zad5.js:34 fibrecu: 1265.08203125 ms
// zad5.js:39 fibiter: 0.0009765625 ms
// zad5.js:29 For n: 36
// zad5.js:34 fibrecu: 1253.530029296875 ms
// zad5.js:39 fibiter: 0.001953125 ms
// zad5.js:29 For n: 37
// zad5.js:34 fibrecu: 1312.409912109375 ms
// zad5.js:39 fibiter: 0.001953125 ms
// zad5.js:29 For n: 38
// zad5.js:34 fibrecu: 1253.36083984375 ms
// zad5.js:39 fibiter: 0.02099609375 ms
// zad5.js:29 For n: 39
// zad5.js:34 fibrecu: 1296.925048828125 ms
// zad5.js:39 fibiter: 0.001953125 ms
// index.html:39 Live reload enabled.


// Wyniki Firefox
// For n: 10 zad5.js:29:17
// Recu version: zad5.js:31:17
// fibrecu: 1649ms - timer ended zad5.js:34:17
// Iter version: zad5.js:36:17
// fibiter: 1ms - timer ended zad5.js:39:17
// For n: 11 zad5.js:29:17
// Recu version: zad5.js:31:17
// fibrecu: 1611ms - timer ended zad5.js:34:17
// Iter version: zad5.js:36:17
// fibiter: 0ms - timer ended zad5.js:39:17
// For n: 12 zad5.js:29:17
// Recu version: zad5.js:31:17
// fibrecu: 1591ms - timer ended zad5.js:34:17
// Iter version: zad5.js:36:17
// fibiter: 0ms - timer ended zad5.js:39:17
// For n: 13 zad5.js:29:17
// Recu version: zad5.js:31:17
// fibrecu: 1607ms - timer ended zad5.js:34:17
// Iter version: zad5.js:36:17
// fibiter: 0ms - timer ended zad5.js:39:17
// For n: 14 zad5.js:29:17
// Recu version: zad5.js:31:17
// fibrecu: 1603ms - timer ended zad5.js:34:17
// Iter version: zad5.js:36:17
// fibiter: 0ms - timer ended zad5.js:39:17
// For n: 15 zad5.js:29:17
// Recu version: zad5.js:31:17
// fibrecu: 1591ms - timer ended zad5.js:34:17
// Iter version: zad5.js:36:17
// fibiter: 0ms - timer ended zad5.js:39:17
// For n: 16 zad5.js:29:17
// Recu version: zad5.js:31:17
// fibrecu: 1593ms - timer ended zad5.js:34:17
// Iter version: zad5.js:36:17
// fibiter: 0ms - timer ended zad5.js:39:17
// For n: 17 zad5.js:29:17
// Recu version: zad5.js:31:17
// fibrecu: 1705ms - timer ended zad5.js:34:17
// Iter version: zad5.js:36:17
// fibiter: 0ms - timer ended zad5.js:39:17
// For n: 18 zad5.js:29:17
// Recu version: zad5.js:31:17
// fibrecu: 1701ms - timer ended zad5.js:34:17
// Iter version: zad5.js:36:17
// fibiter: 0ms - timer ended zad5.js:39:17
// For n: 19 zad5.js:29:17
// Recu version: zad5.js:31:17
// fibrecu: 1717ms - timer ended zad5.js:34:17
// Iter version: zad5.js:36:17
// fibiter: 0ms - timer ended zad5.js:39:17
// For n: 20 zad5.js:29:17
// Recu version: zad5.js:31:17
// fibrecu: 1719ms - timer ended zad5.js:34:17
// Iter version: zad5.js:36:17
// fibiter: 0ms - timer ended zad5.js:39:17
// For n: 21 zad5.js:29:17
// Recu version: zad5.js:31:17
// fibrecu: 1739ms - timer ended zad5.js:34:17
// Iter version: zad5.js:36:17
// fibiter: 0ms - timer ended zad5.js:39:17
// For n: 22 zad5.js:29:17
// Recu version: zad5.js:31:17
// fibrecu: 1749ms - timer ended zad5.js:34:17
// Iter version: zad5.js:36:17