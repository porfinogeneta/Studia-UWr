import org.scalatest.funsuite.AnyFunSuite
import core.cards._
import core.deck._
import blackjack._

class BlackjackTest extends AnyFunSuite {


  test("Playing Blackjack with more cards than available should throw an exception") {
    val deck = Deck(
      List(
        Card(Clubs, Ace),
        Card(Diamonds, Num2),
        Card(Hearts, Num5),
        Card(Spades, Jack)
      )
    )
    val game = new Blackjack(deck)
    assertThrows[Exception] {
      game.play(5)
    }
  }

  test("Generating Blackjack game with 3 decks should have correct number of cards") {
    val game = Blackjack(3)
    assert(game.deckLen == 156) // 3 decks * 52 cards each
  }


}
