import app.pizzeria._
import app.size._
import app.pizzaTypes._
import app.crust._
import app.discounts._
import app.drinks._
import app.meat._
import app.topping._
import app.order._

@main def hello(): Unit =
  val pizza = Pizza(Margarita, large, thin)
  val pizza2 = Pizza(Funghi, small, thick, Some(salami))
  var order = Order("ddsds", "efeew", "+48345234234", List(pizza, pizza, pizza2), List(lemonade))
  // println(pizza)
  // println(pizza.price)
  println(order)
  println(order.extraMeatPrice)
  println(order.drinksPrice)
  println(order.pizzasPrice)
  println(order.priceByType(Funghi))
  println(order.price)

