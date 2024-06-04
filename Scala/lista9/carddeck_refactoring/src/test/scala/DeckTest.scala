import org.scalatest.funsuite.AnyFunSuite
import core.cards._
import core.deck._

class DeckTest extends AnyFunSuite {
  test("Newly created deck should be standard") {
    val deck = Deck(
      List(
        Card(Clubs, Ace),
        Card(Clubs, Num2),
        Card(Diamonds, Num5),
        Card(Spades, Jack)
      )
    )
    assert(deck.isStandard == false)
  }

  test("Pushing a card onto deck should increase its size") {
    val deck = Deck(
      List(
        Card(Clubs, Ace),
        Card(Clubs, Num2),
        Card(Diamonds, Num5),
        Card(Spades, Jack)
      )
    )
    val new_deck = deck.pushCard(Card(Diamonds, Num2))
    assert(new_deck.length() == deck.length() + 1)
  }

  test("Amount of Clubs in the deck should be correct") {
    val deck = Deck(
      List(
        Card(Clubs, Ace),
        Card(Clubs, Num2),
        Card(Diamonds, Num5),
        Card(Spades, Jack)
      )
    )
    assert(deck.amountOfColor(Clubs) == 2)
  }

  test("Amount of numerical cards in the deck should be correct") {
    val deck = Deck(
      List(
        Card(Clubs, Ace),
        Card(Clubs, Num2),
        Card(Diamonds, Num5),
        Card(Spades, Jack)
      )
    )
    assert(deck.amountOfNumerical(Num2) == 1)
  }

  test("Amount of cards with faces in the deck should be correct") {
    val deck = Deck(
      List(
        Card(Clubs, Ace),
        Card(Clubs, Num2),
        Card(Diamonds, Num5),
        Card(Spades, Jack)
      )
    )
    assert(deck.amountOfFace(Ace) == 1)
  }

  test("Pulling a card from deck should decrease its size") {
    val deck = Deck(
      List(
        Card(Clubs, Ace),
        Card(Clubs, Num2),
        Card(Diamonds, Num5),
        Card(Spades, Jack)
      )
    )
    val new_deck = deck.pull()
    assert(new_deck.length() == deck.length() - 1)
  }
}
