
package app.games

import app.cards._
import app.deck._

class Blackjack(deck: Deck) {
    // Points calculation:
    // 1. Numerical cards as their numerical value = 2 - 10.
    // 2. Face cards (Jack, Queen, King) = 10
    // 3. Ace = 1 or 11 (player could choose)

    // // loop taking n cards from the deck, pretty-printing them with points & printing the sum of points on the end
    def play(n: Int): Unit = 
        if (n > (deck.amountWithFace + deck.amountWithNumerical)){
            throw Exception("Invalid amount of cards!")
        }
        val n_elems = deck.takeElems(n)
        var points_sum = 0
        for (card <- n_elems){            
            if (card.value == Queen | card.value == King | card.value == Jack){
                points_sum += 10
                println("Card of color: " + card.col + ", value: " + card.value + " points: " + 10)
            }else if (card.value == Ace){
                points_sum += 10
                println("Card of color: " + card.col + ", value: " + card.value + " points: " + 10)
            }else {
                points_sum += card.value.toString().takeRight(1).toInt
                println("Card of color: " + card.col + ", value: " + card.value + " points: " + card.value.toString().takeRight(1))
            }       
        }

        println("Total points: " + points_sum)


    // finds all subsequences of cards which could give 21 points
    // lazy val obliczamy daną wartość tylko jak zostanie ona uzyta w kodzie, nie za kazdym utworzeniem obiektu
    lazy val all21: List[List[Card]] = 
        val allCards = deck.takeElems(deck.amountWithFace + deck.amountWithNumerical) // pobieramy cały deck
        def getPoints(card: Card): Int =
            var points = 0
                if (card.value == Queen | card.value == King | card.value == Jack) {
                    points = 10
                }else if (card.value == Ace){
                    points = 10
                }else {
                    points = card.value.toString().takeRight(1).toInt
                }
            return points


        var res: List[List[Card]] = List()
        def findAllSubsequence(remainingSeqeunce: List[Card], createdSequence: List[Card], remainingValue: Int) =
            if (remainingValue == 0){
                List(createdSequence)
            }else if (remainingValue < 0 | remainingSeqeunce.isEmpty){
                List()
            }else {
                // podzielimy sekwencję która nam została na dwie części,
                // tą w której dodanie jakiejkolwiek karty będzie za duze względem 21 i tą gdzie mozna jeszcze dodać
                val (canBeConsidered, restOfSequence) = remainingSeqeunce.partition(card => {
                    remainingValue - getPoints(card) >= 0
                })

                // println(canBeConsidered)

                for (card <- canBeConsidered) {
                    findAllSubsequence(canBeConsidered, createdSequence :+ card, remainingValue - getPoints(card))
                }

            }

        res = res ++ findAllSubsequence(allCards, List(), 21)



    // def first21(): Unit = ??? // finds and pretty-prints the first subsequence of cards which could give 21 points

}
// // creates Blackjack game
// // having numOfDecks-amount of standard decs with random order
// // of cards. For example, with Blackjack(3) deck would have 156
// // cards
object Blackjack {

    def generateDeck: Deck =
        val colors = List(Clubs, Diamonds, Hearts, Spades)
        val values = List(Num2,Num3,Num4,Num5,Num6,Num7,Num8,Num9,Num10,Ace,Queen,King,Jack)
        val deck = List()
        for (i <- Range(0,4)) {
            for (j <- Range(0,13)){
                deck :+ Card(colors(i), values(j))
            }
        }

        Deck(deck)

    def apply(numOfDecks: Int) = 
        val colors = List(Clubs, Diamonds, Hearts, Spades)
        val values = List(Num2,Num3,Num4,Num5,Num6,Num7,Num8,Num9,Num10,Ace,Queen,King,Jack)
        var deck: List[Card] = List()
        for (k <- Range(0, numOfDecks)) {
            for (i <- Range(0,4)) {
                for (j <- Range(0,13)){
                    deck = Card(colors(i), values(j)) :: deck
                }
            }
        } 
        new Blackjack(Deck(deck))
}