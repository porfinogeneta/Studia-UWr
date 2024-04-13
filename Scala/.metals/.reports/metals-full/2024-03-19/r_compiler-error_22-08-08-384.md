file://<WORKSPACE>/lista4/carddecks/src/main/scala/app/deck/Deck.scala
### java.lang.IndexOutOfBoundsException: 0

occurred in the presentation compiler.

presentation compiler configuration:
Scala version: 3.3.1
Classpath:
<HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala3-library_3/3.3.1/scala3-library_3-3.3.1.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.10/scala-library-2.13.10.jar [exists ]
Options:



action parameters:
offset: 1985
uri: file://<WORKSPACE>/lista4/carddecks/src/main/scala/app/deck/Deck.scala
text:
```scala
package app.deck

import app.cards._

class Deck(cards: List[Card]) {
    //creates new deck without first card
    def pull() = 
        cards.tail

    // creates new deck with given card pushed on top
    def pushCard(c: Card) = 
        new Deck(List.concat(List(c), cards))

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
        for (card <- cards){
            card.match
                case Card(Clubs, _) => clubs_cnt += 1
                case Card(Diamonds, _) => diamonds_cnt += 1
                case Card(Hearts, _) => hearts_cnt += 1
                case Card(Spades, _) => spades_cnt += 1
        }

        return (clubs_cnt, diamonds_cnt, hearts_cnt, spades_cnt)
    
    //amount of cards in the deck for the given color
    def amountOfColor(color: Color): Int = 
        val (clubs, diamonds, hearts, spades) = countColors
        color.match
            case Clubs => clubs
            case Diamonds => diamonds
            case Hearts => hearts
            case Spades => spades

    def countNumerics: List[Int] =
        var numerics = List.fill(9)(@@)
        for (card <- cards) {
            card.match
                case Card(_, Num2) => numerics(0) += 1
                case Card(_, Num3) => numerics(1) += 1
                case Card(_, Num4) => numerics(2) += 1
                case Card(_, Num5) => numerics(3) += 1
                case Card(_, Num6) => numerics(4) += 1
                case Card(_, Num7) => numerics(5) += 1
                case Card(_, Num8) => numerics(6) += 1
                case Card(_, Num9) => numerics(7) += 1
                case Card(_, Num10) => numerics(8) += 1
        }

        return numerics

    // amount of cards in the deck for given numerical card (2, 3, 4, 5, 6, 7, 8, 9, 10)
    def amountOfNumerical(numerical: Numerical): Int =
        val nums = countNumerics
        numerical.match
            case Num2 => nums(0)
            case Num3 => nums(1)
            case Num4 => nums(2)
            case Num5 => nums(3)
            case Num6 => nums(4)
            case Num7 => nums(5)
            case Num8 => nums(6)
            case Num9 => nums(7)
            case Num10 => nums(8)

        

        
        




}
```



#### Error stacktrace:

```
scala.collection.LinearSeqOps.apply(LinearSeq.scala:131)
	scala.collection.LinearSeqOps.apply$(LinearSeq.scala:128)
	scala.collection.immutable.List.apply(List.scala:79)
	dotty.tools.dotc.util.Signatures$.countParams(Signatures.scala:501)
	dotty.tools.dotc.util.Signatures$.applyCallInfo(Signatures.scala:186)
	dotty.tools.dotc.util.Signatures$.computeSignatureHelp(Signatures.scala:94)
	dotty.tools.dotc.util.Signatures$.signatureHelp(Signatures.scala:63)
	scala.meta.internal.pc.MetalsSignatures$.signatures(MetalsSignatures.scala:17)
	scala.meta.internal.pc.SignatureHelpProvider$.signatureHelp(SignatureHelpProvider.scala:51)
	scala.meta.internal.pc.ScalaPresentationCompiler.signatureHelp$$anonfun$1(ScalaPresentationCompiler.scala:398)
```
#### Short summary: 

java.lang.IndexOutOfBoundsException: 0