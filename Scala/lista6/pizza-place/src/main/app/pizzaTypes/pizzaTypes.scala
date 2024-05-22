package app.pizzaTypes


sealed trait PizzaType {
    val price: Double
}

object Margarita extends PizzaType {val price = 5.0}
object Pepperoni extends PizzaType { val price = 6.5}
object Funghi extends PizzaType { val price = 7.0}