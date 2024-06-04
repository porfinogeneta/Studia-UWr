file://<WORKSPACE>/carddeck_refactoring/src/test/scala/BlackjackTest.scala
### java.lang.IndexOutOfBoundsException: 0

occurred in the presentation compiler.

presentation compiler configuration:
Scala version: 3.3.3
Classpath:
<HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala3-library_3/3.3.3/scala3-library_3-3.3.3.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.12/scala-library-2.13.12.jar [exists ]
Options:



action parameters:
offset: 461
uri: file://<WORKSPACE>/carddeck_refactoring/src/test/scala/BlackjackTest.scala
text:
```scala
import org.scalatest.funsuite.AnyFunSuite
import core.cards._
import core.deck._
import blackjack._

class BlackjackTest extends AnyFunSuite {
  test("Playing Blackjack with 4 cards should display correct points") {
    val deck = Deck(
      List(
        Card(Clubs, Ace),
        Card(Diamonds, Num2),
        Card(Hearts, Num5),
        Card(Spades, Jack)
      )
    )
    val game = new Blackjack(deck)
    assert("Total points: 21") {
      game.play(4),@@
    }
  }

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
    assert(game.deckLen() == 156) // 3 decks * 52 cards each
  }

  test("Playing Blackjack game generated with 3 decks with 4 cards should display correct points") {
    val game = Blackjack(3)
    assert("Total points:") {
      game.play(4)
    }
  }

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
	scala.meta.internal.pc.ScalaPresentationCompiler.signatureHelp$$anonfun$1(ScalaPresentationCompiler.scala:412)
```
#### Short summary: 

java.lang.IndexOutOfBoundsException: 0