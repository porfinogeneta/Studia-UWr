import org.scalatest.funsuite.AnyFunSuite
import core.cards._

class CardTest extends AnyFunSuite {
    test("Card Color should be Diamonds, value King"){
        assert(Card(Diamonds, King).col == Diamonds && Card(Diamonds, King).value == King)
    }
}