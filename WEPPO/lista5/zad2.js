// callback - funkcja zwrotna, funkcja którą wywołamy, gdy inna się już skończy

console.log("Welcome, type your name:");
process.stdin.on("data", data => {
    data = data.toString()
    process.stdout.write(`Witaj ${data}\n`)
})

