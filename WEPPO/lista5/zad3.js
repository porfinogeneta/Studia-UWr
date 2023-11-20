
console.log("Welcome, to the guessing game! I am choosing number for you.");
const number = Math.floor(Math.random() * 100) // wybieramy liczbę [0,1) * 100 i zaokrąglamy
console.log("Choose number");
process.stdin.on("data", input => {
    num = Number(input)
    if (num < number) {
        process.stdout.write("Too small, aim higher!\n")
    }else if (num > number){
        process.stdout.write("To high in the sky!\n")
    }else if (num == number) {
        process.stdout.write("You won!\n")
        process.exit() // zakończenie zczytywania
    }
})
    
