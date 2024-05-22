package app.Operations
import scala.math.BigDecimal.RoundingMode
import app.Money._


case class Money(amount: BigDecimal, currency: Currency) {

    // funkcja do zmiany symbolu na walutę
    private def convertCurrencySymbol(curr: Currency): Currency = {
        // `` pattern matching jest dzięki temu na konkretnych obiektach
        curr match {
            case `zl` => PLN
            case `$` => USD
            case `er` => EUR
            case _ => curr
        }
    }

    def convertCurrency(target: Currency): Money = {
        val convertedCurrency = convertCurrencySymbol(currency)
        val convertedTarget = convertCurrencySymbol(target)
        if (convertedCurrency == convertedTarget) {
        this
        } else {
            // bierzemy conversion rate, albo jak nie ma to jest conversion rate =1
        val rate = conversionRates.getOrElse((convertedCurrency, convertedTarget), BigDecimal(1))
        Money((amount * rate).setScale(2, RoundingMode.HALF_UP), convertedTarget)
        }
    }

    def +(other: Money): Money = {
        val convertedOther = other.convertCurrency(currency)
        Money(amount + convertedOther.amount, currency)
    }

    def -(other: Money): Money = {
        val convertedOther = other.convertCurrency(currency)
        Money(amount - convertedOther.amount, currency)
    }

    def *(factor: BigDecimal): Money = {
        Money(amount * factor, currency)
    }

    def >(other: Money): Boolean =
        val convertedOther = other.convertCurrency(currency)
        amount > convertedOther.amount

    def <(other: Money): Boolean =
        val convertedOther = other.convertCurrency(currency)
        amount < convertedOther.amount

}


// kompilator szuka metody apply dla Double, nie znajduje i odpala naszą metodę apply
implicit class DoubleMoney(amount: Double) {
  def apply(currency: Currency) = Money(amount, currency)
}


