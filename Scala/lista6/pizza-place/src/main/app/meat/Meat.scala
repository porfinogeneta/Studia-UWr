package app.meat


sealed trait MeatType {
    val price: Double
}

object salami extends MeatType {val price = 1.0}