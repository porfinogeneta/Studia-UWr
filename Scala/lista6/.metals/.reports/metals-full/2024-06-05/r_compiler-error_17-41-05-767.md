file://<WORKSPACE>/pizza-place/src/main/app/pizzeria/Pizzeria.scala
### java.lang.IndexOutOfBoundsException: 0

occurred in the presentation compiler.

presentation compiler configuration:
Scala version: 3.3.3
Classpath:
<HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala3-library_3/3.3.3/scala3-library_3-3.3.3.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.12/scala-library-2.13.12.jar [exists ]
Options:



action parameters:
offset: 665
uri: file://<WORKSPACE>/pizza-place/src/main/app/pizzeria/Pizzeria.scala
text:
```scala
package app.pizzeria
import app.size._
import app.pizzaTypes._
import app.crust._
import app.discounts._
import app.drinks._
import app.meat._
import app.topping._


case class Pizza(
    pizzaType: PizzaType,
    size: SizeType,
    crust: CrustType,
    extraMeat: Option[MeatType] = None,
    extraTopping: Option[ToppingType] = None
) {
    override def toString: String =
        s"""Pizza: ${prettify(pizzaType)}
 Of size: ${prettify(size)} \nWith crust: ${prettify(crust)}
 Additional meat: ${prettifyOption(extraMeat, "No additional meat")}
 Extra topping: ${prettifyOption(extraTopping, "No extra topping")}""".stripMargin(@@)

    private def prettify(value: Any): String =
        value.toString.split("\\.").lastOption.getOrElse("").takeWhile(_ != '$')

    private def prettifyOption[T](value: Option[T], defaultVal: String) =
        value.map(prettify).getOrElse(defaultVal)

    val price: Double =

        if (size == small) {
            pizzaType.price * 0.9
        }else if (size == large) {
            pizzaType.price * 1.5
        }else {
            pizzaType.price
        }

    def totalPrice: Double = 
        val topping = extraTopping.map(t => t.price).getOrElse(0.0) // przechodzimy po opcji i zwracamy cenę, jak istnieje
        val meat = extraMeat.map(m => m.price).getOrElse((0.0))
        val additions = topping + meat
        price + additions
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