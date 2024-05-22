file://<WORKSPACE>/currency-sdl/src/main/scala/app/Operations/Operations.scala
### dotty.tools.dotc.core.TypeError$$anon$1: Toplevel definition <error> is defined in
  <WORKSPACE>/currency-sdl/src/main/scala/app/Operations/Operations.scala
and also in
  <WORKSPACE>/currency-sdl/src/main/scala/app/Operations/Operations.scala
One of these files should be removed from the classpath.

occurred in the presentation compiler.

presentation compiler configuration:
Scala version: 3.3.3
Classpath:
<HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala3-library_3/3.3.3/scala3-library_3-3.3.3.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.12/scala-library-2.13.12.jar [exists ]
Options:



action parameters:
offset: 134
uri: file://<WORKSPACE>/currency-sdl/src/main/scala/app/Operations/Operations.scala
text:
```scala
package app.Operations


import _.app.Currency

object Operations {
    implicit class MoneyOps(val amount) extends AnyVal =
        d@@
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
    
    def 
```



#### Error stacktrace:

```

```
#### Short summary: 

dotty.tools.dotc.core.TypeError$$anon$1: Toplevel definition <error> is defined in
  <WORKSPACE>/currency-sdl/src/main/scala/app/Operations/Operations.scala
and also in
  <WORKSPACE>/currency-sdl/src/main/scala/app/Operations/Operations.scala
One of these files should be removed from the classpath.