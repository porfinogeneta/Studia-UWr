package app.topping


sealed trait ToppingType {
    val price: Double
}

object ketchup extends ToppingType { val price = 0.5}
object garlic extends ToppingType { val price = 0.5}