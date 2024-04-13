file://<WORKSPACE>/lista6/pizza-place/src/main/scala/app/orders/Order.scala
### java.lang.IndexOutOfBoundsException: 0

occurred in the presentation compiler.

presentation compiler configuration:
Scala version: 3.3.1
Classpath:
<HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala3-library_3/3.3.1/scala3-library_3-3.3.1.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.10/scala-library-2.13.10.jar [exists ]
Options:



action parameters:
offset: 2215
uri: file://<WORKSPACE>/lista6/pizza-place/src/main/scala/app/orders/Order.scala
text:
```scala
package app.order

import app.pizzeria._
import app.size._
import app.pizzaTypes._
import app.crust._
import app.discounts._
import app.drinks._
import app.meat._
import app.topping._
import app.drinks._

import app.utils._

import scala.util.matching.Regex
import scala.collection.StringOps


class Order(
    name: String,
    address: String,
    phone: String,
    pizzas: List[Pizza],
    drinks: List[DrinkType],
    discount: Option[discount] = None,
    specialInfo: Option[String] = None
) {

    
    def apply(name: String, address: String, phone: String, pizzas: List[Pizza],
     drinks: List[DrinkType], discount: Option[discount] = None, specialInfo: Option[String] = None): Order = 
        require(
            isValidPhoneNumber(phone)
        )
        new Order(name, address, phone, pizzas, drinks, discount,specialInfo)
    
    private def isValidPhoneNumber(phone: String): Boolean = {
        val phoneRegex = """^\+?\d{6,18}$"""
        phone.matches(phoneRegex)
    }

    override def toString: String = 
        val pz = s"${pizzas.map(_.toString).mkString(", \n======\n")}"
        val dr = s"${drinks.map(Utils.prettify).mkString(", ")}" // korzystamy z funkcji z Utils dla kadego elementu, na koniec przerabiamy kolekcję na String, korzystając z mkString
        val ds = s"${Utils.prettifyOption(discount, "")}"
        val sI = s"${Utils.prettifyOption(specialInfo, "")}"
        s"====\nOrder for:\n${name}\n====\nHouse: ${address}\n====\nPizzas: \n${pz}\n====\nDrinks: ${dr}\n====\nDiscount: ${ds}\n====\nSpecial Info: ${sI}"


    def extraMeatPrice: Option[Double] =
        pizzas.flatMap(_.extraMeat).map(meatPrice).reduceOption(_ + _)

    private def meatPrice(meatType: MeatType): Double =
        meatType match
            case salami => salami.price

    def pizzasPrice: Option[Double] =
        pizzas.map(_.price).reduceOption(_ + _)
    
    def drinksPrice: Option[Double] = 
        drinks.map(_.price).reduceOption(_ + _)

    def priceByType(typ: PizzaType): Option[Double] =
        pizzas.filter(p => p.pizzaType == typ).map(_.totalPrice).reduceOption(_ + _)

    val price: Double = 
        if (discount == student) {
            pizzas.foldLeft(0.0)((acc, @@))
        }
    
}
// zapytać się o rónicę między companion object a tym wyzej
// object Order {
//     def apply(name: String, address: String, phone: String, pizzas: List[Pizza],
//      drinks: List[DrinkType], discount: Option[discount] = None, specialInfo: Option[String] = None): Order = 
//         require(
//             isValidPhoneNumber(phone)
//         )
//         new Order(name, address, phone, pizzas, drinks, discount,specialInfo)
    
//     private def isValidPhoneNumber(phone: String): Boolean = {
//         val phoneRegex = """^\+?\d{6,18}$"""
//         phone.matches(phoneRegex)
//     }

    

//     // private def prettify(value: Any): String =
//     //     value.toString.split("\\.").lastOption.getOrElse("").takeWhile(_ != '$')

//     // private def prettifyOption[T](value: Option[T], defaultVal: String) =
//     //     value.map(prettify).getOrElse(defaultVal)
// }
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