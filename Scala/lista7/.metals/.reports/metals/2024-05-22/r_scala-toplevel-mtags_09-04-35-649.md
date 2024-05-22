error id: file://<WORKSPACE>/currency-sdl/src/main/scala/app/Operations/Operations.scala:[1334..1334) in Input.VirtualFile("file://<WORKSPACE>/currency-sdl/src/main/scala/app/Operations/Operations.scala", "package app.Operations


import app.Currency
import app.Money

object Operations {
    implicit class MoneyOps(val amount) extends AnyVal =
        def EUR: Money = Money(amount, Currency.EUR)
        def USD: Money = Money(amount, Currency.USD)
        def PLN: Money = Money(amount, Currency.PLN)
}

implicit class Money(amount: BigDecimal, currency Currency) =
    val conversionsRate: Map[(Currency, Currency),BigDecimal] = Map(
        (USD, EUR) -> 0.85, (EUR, USD) -> 1.18,
        (USD, PLN) -> 3.8,  (PLN, USD) -> 0.26,
        (EUR, PLN) -> 4.5,  (PLN, EUR) -> 0.22
    )

    def ConvertCurrency(target: Currency): Money =
        if (currency == target) this
        else {
            val rate = conversionsRate((currency, target))
            Money(amount * rate, target)
        }
    
    def +(other: Money): Money =
        // konwertujemy wejściowy obiekt na aktualną walutę
        val convertedOther = other.ConvertCurrency(currency)
        Money(amount + convertedOther.amount, currency)
    
    def -(other: Money): Money =
        val convertedOther = other.ConvertCurrency(currency)
        Money(amount - convertedOther.amount, currency)
    
    def *(other: Money): Money =
        val convertedOther = other.ConvertCurrency(currency)
        Money(amount - convertedOther.amount, currency)
    
    def ")
file://<WORKSPACE>/currency-sdl/src/main/scala/app/Operations/Operations.scala
file://<WORKSPACE>/currency-sdl/src/main/scala/app/Operations/Operations.scala:41: error: expected identifier; obtained eof
    def 
        ^
#### Short summary: 

expected identifier; obtained eof