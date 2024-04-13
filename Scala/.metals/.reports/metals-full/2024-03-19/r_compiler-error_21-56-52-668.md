file://<WORKSPACE>/lista4/carddecks/src/main/scala/app/deck/Deck.scala
### java.lang.AssertionError: NoDenotation.owner

occurred in the presentation compiler.

presentation compiler configuration:
Scala version: 3.3.1
Classpath:
<HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala3-library_3/3.3.1/scala3-library_3-3.3.1.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.10/scala-library-2.13.10.jar [exists ]
Options:



action parameters:
offset: 2074
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

    // amount of cards in the deck for given numerical card (2, 3, 4, 5, 6, 7, 8, 9, 10)
    def amountOfNumerical(numerical: Numerical): Int =
        var Map(@@)
        
        




}
```



#### Error stacktrace:

```
dotty.tools.dotc.core.SymDenotations$NoDenotation$.owner(SymDenotations.scala:2582)
	scala.meta.internal.pc.SignatureHelpProvider$.isValid(SignatureHelpProvider.scala:83)
	scala.meta.internal.pc.SignatureHelpProvider$.notCurrentApply(SignatureHelpProvider.scala:92)
	scala.meta.internal.pc.SignatureHelpProvider$.$anonfun$1(SignatureHelpProvider.scala:48)
	scala.collection.StrictOptimizedLinearSeqOps.loop$3(LinearSeq.scala:280)
	scala.collection.StrictOptimizedLinearSeqOps.dropWhile(LinearSeq.scala:282)
	scala.collection.StrictOptimizedLinearSeqOps.dropWhile$(LinearSeq.scala:278)
	scala.collection.immutable.List.dropWhile(List.scala:79)
	scala.meta.internal.pc.SignatureHelpProvider$.signatureHelp(SignatureHelpProvider.scala:48)
	scala.meta.internal.pc.ScalaPresentationCompiler.signatureHelp$$anonfun$1(ScalaPresentationCompiler.scala:398)
```
#### Short summary: 

java.lang.AssertionError: NoDenotation.owner