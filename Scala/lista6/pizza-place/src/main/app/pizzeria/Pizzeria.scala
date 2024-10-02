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
          | Of size: ${prettify(size)} \nWith crust: ${prettify(crust)}
          | Additional meat: ${prettifyOption(extraMeat, "No additional meat")}
          | Extra topping: ${prettifyOption(extraTopping, "No extra topping")}""".stripMargin()

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