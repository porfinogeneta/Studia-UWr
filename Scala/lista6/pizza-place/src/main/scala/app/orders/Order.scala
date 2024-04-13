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
        pizzas.map(_.totalPrice).reduceOption(_ + _)
    
    def drinksPrice: Option[Double] = 
        drinks.map(_.price).reduceOption(_ + _)

    def priceByType(typ: PizzaType): Option[Double] =
        pizzas.filter(p => p.pizzaType == typ).map(_.totalPrice).reduceOption(_ + _)

    private def receipt: Double = 
        val totalPizzas = pizzas.foldLeft(0.0)((acc, p) => p.totalPrice + acc)
        val totalDrinks = drinks.foldLeft(0.0)((acc, d) => d.price + acc)
        if (discount == student) {
            return totalPizzas * 0.05 + totalDrinks
        }else if (discount == senior){
            return (totalPizzas + totalDrinks)*0.07
        }else {
            return totalPizzas + totalDrinks
        }
    
    val price: Double =
        receipt
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