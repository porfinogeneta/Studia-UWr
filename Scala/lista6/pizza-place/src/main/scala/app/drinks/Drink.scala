package app.drinks


sealed trait DrinkType {
    val price: Double
}

object lemonade extends DrinkType {val price = 2}