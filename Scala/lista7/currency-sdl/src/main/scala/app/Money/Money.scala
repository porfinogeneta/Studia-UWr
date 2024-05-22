package app.Money

trait Currency
case object PLN extends Currency
case object zl extends Currency
case object $ extends Currency
case object USD extends Currency
case object EUR extends Currency
case object er extends Currency


val conversionRates: Map[(Currency, Currency), BigDecimal] = 
    Map(
        (USD, EUR) -> 0.85, (EUR, USD) -> 1.18,
        (USD, PLN) -> 3.8,  (PLN, USD) -> 0.26,
        (EUR, PLN) -> 4.5,  (PLN, EUR) -> 0.22)

case class CurrencyConverter(
    conversion: Map[(Currency, Currency), BigDecimal]) {
    def convert(from: Currency, to: Currency): BigDecimal = ???
}