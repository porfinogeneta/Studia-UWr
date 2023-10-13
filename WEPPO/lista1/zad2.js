
function findCorrect(range){
    let set = [];
    for (let i = 1; i < range; i++){
        // get numbers from a number
        let correct = true;
        const strVersion = i.toString();
        const digits = strVersion.split("").map(Number);
        // check if divisible by all digits
        for (let j = 0; j < digits.length; j++) {
            const element = digits[j];
            if (i % element != 0){
                correct = false;
            }
        }
        // check if divisible by sum of digits, if so add to set
        if (correct && (i % digits.reduce((sum, e) => sum + e, 0) == 0)){
            set.push(i);
        }
    }
    return set; 
}

console.log(findCorrect(100000))