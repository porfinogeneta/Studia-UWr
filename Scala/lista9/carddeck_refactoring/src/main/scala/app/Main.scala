package app

import blackjack._
import core.cards._
import core.deck._

@main def hello(): Unit =
  // val figure = Value("Ace")
  // val color = Color("Hearts")
  // val c = Color
  val deck = Deck(
    List(
      Card(Clubs, Ace),
      Card(Clubs, Num2),
      Card(Diamonds, Num5),
      Card(Spades, Jack)
    )
  )
  val new_deck = deck.pushCard(Card(Diamonds, Num2))
  println(new_deck.isStandard)
  println(new_deck.duplicatesOfCard(Card(Clubs, Num3)))
  println(new_deck.amountOfColor(Clubs))
  println(new_deck.amountOfNumerical(Num2))

  println(new_deck.amountWithNumerical)

  println(new_deck.amountOfFace(Ace))

  println(new_deck.amountWithFace)

  val game = new Blackjack(new_deck)
  game.play(4)

  val game2 = Blackjack(3)
  game2.play(4)
