package app.deck

import scala.util.Random
import app.cards._

class Deck(cards: List[Card]) {
    //creates new deck without first card
    def pull() = 
        require(!cards.isEmpty)
        cards.tail

    // creates new deck with given card pushed on top
    def pushCard(c: Card) = 
        new Deck(List.concat(List(c), cards))

    // get first n elements of the list
    def takeElems(n: Int): List[Card] =
        cards.take(n)

    //creates new deck with new card(color, value) pushed on top
    def pushDeck(color: Color, value: Value) = 
        pushCard(Card(color, value))


    def checkDeck(): Boolean = 
        if (cards.length != 52) {
            return false
        }
        val (clubs, diamonds, hearts, spades) = countColors
        if (clubs != 13 || diamonds != 13 || hearts != 13 || spades != 13) {
            return false
        }

        val numerics = List(Num2,Num3,Num4,Num5,Num6,Num7,Num8,Num9,Num10)
        if (numerics.exists(elems => amountOfNumerical(elems) != 4)){
            return false
        }

        true
    
    // checks if deck is a standard deck
    val isStandard: Boolean =
        checkDeck()

    // amount of duplicates of the given card in the deck
    def duplicatesOfCard(card: Card): Int = 
        var counter = 0
        for (deckCard <- cards) {
            if (deckCard == card) {
                counter += 1
            }
        }

        counter

    def countColors: (Int, Int, Int, Int) =
        var clubs_cnt = 0
        var diamonds_cnt = 0
        var hearts_cnt = 0
        var spades_cnt = 0
        // filter/collect
        for (card <- cards){
            card.match
                case Card(Clubs, _) => clubs_cnt += 1
                case Card(Diamonds, _) => diamonds_cnt += 1
                case Card(Hearts, _) => hearts_cnt += 1
                case Card(Spades, _) => spades_cnt += 1
        }

        (clubs_cnt, diamonds_cnt, hearts_cnt, spades_cnt)
    
    //amount of cards in the deck for the given color
    def amountOfColor(color: Color): Int = 
        val (clubs, diamonds, hearts, spades) = countColors
        color.match
            case Clubs => clubs
            case Diamonds => diamonds
            case Hearts => hearts
            case Spades => spades

    def countValues: Map[Card, Int] =
        return cards.groupBy(identity).mapValues(_.size).toMap

    // amount of cards in the deck for given numerical card (2, 3, 4, 5, 6, 7, 8, 9, 10)
    def amountOfNumerical(numerical: Numerical): Int =
        // one liner deck.filter
        var res = 0
        val values = countValues
        values.foreach(pair => {
            if (pair._1.value == numerical) {
                res += 1
            }
        })
        res
    
    // amount of all numerical cards in the deck (2, 3, 4, 5, 6, 7, 8, 9, 10)
    val amountWithNumerical: Int = 
        var res = 0
        val values = countValues
        values.foreach(pair => {
            pair._1.match
                case Card(_, Num2) => res += 1
                case Card(_, Num3) => res += 1
                case Card(_, Num4) => res += 1
                case Card(_, Num5) => res += 1
                case Card(_, Num6) => res += 1
                case Card(_, Num7) => res += 1
                case Card(_, Num8) => res += 1
                case Card(_, Num9) => res += 1
                case Card(_, Num10) => res += 1
                case _ => 0
        })
        res

    // amount of cards in the deck for the given face (Jack, Queen & King)
    def amountOfFace(face: Face) : Int =
        var res = 0
        val values = countValues
        values.foreach(pair => {
            if (pair._1.value == face) {
                res += 1
            }
        })
        res

    // amount of all cards in the deck with faces (Jack, Queen & King)
    val amountWithFace: Int = 
        var res = 0
        val values = countValues
        values.foreach(pair => {
            pair._1.match
                case Card(_, Jack) => res += 1
                case Card(_, Queen) => res += 1
                case Card(_, King) => res += 1
                case _ => 0
        })
        res

}

// creates the standard deck with random order of cards. Check Random.shuffle1 function
object Deck {
    def apply(cards: List[Card]) = 
        val deck = Random.shuffle(cards)
        new Deck(cards)
}
