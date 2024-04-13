file://<WORKSPACE>/lista4/carddecks/src/main/scala/app/games/Blackjack.scala
### java.lang.IndexOutOfBoundsException: 0

occurred in the presentation compiler.

presentation compiler configuration:
Scala version: 3.3.1
Classpath:
<HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala3-library_3/3.3.1/scala3-library_3-3.3.1.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.10/scala-library-2.13.10.jar [exists ]
Options:



action parameters:
offset: 432
uri: file://<WORKSPACE>/lista4/carddecks/src/main/scala/app/games/Blackjack.scala
text:
```scala
class Blackjack(deck: Deck) {
    // Points calculation:
    // 1. Numerical cards as their numerical value = 2 - 10.
    // 2. Face cards (Jack, Queen, King) = 10
    // 3. Ace = 1 or 11 (player could choose)

    // // loop taking n cards from the deck, pretty-printing them with points & printing the sum of points on the end
    def play(n: Int): Unit = 
        n_elems = deck.take(n)
        points_sum = n_elems.foldLeft(0)((@@))



    lazy val all21: List[List[Cards]] = ??? // finds all subsequences of cards which could give 21 points

    def first21(): Unit = ??? // finds and pretty-prints the first subsequence of cards which could give 21 points

}
// creates Blackjack game
// having numOfDecks-amount of standard decs with random order
// of cards. For example, with Blackjack(3) deck would have 156
// cards
object Blackjack {

    def apply(numOfDecks: Int) = ??? 
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