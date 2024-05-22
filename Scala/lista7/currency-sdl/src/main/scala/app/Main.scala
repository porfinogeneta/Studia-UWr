import app.Operations._
import app.Money._


@main def hello(): Unit =
  // val money1: Int = 10
  val money1 = 10.0(PLN)
  val money2: Money = 20.0(EUR)
  // val result = money1 + money2
  // println(result) // Should print the result in USD
  // val conv1: Money = 150.01(USD) AS EUR

  val sum1: Money = 100.01(USD) + 200(EUR) //result in dollars
  val sum2: Money = 100.01(zl) + 200($) //result in złoty
  val sum3: Money = 5(zl) + 3(PLN) + 20.5(USD) //result in złoty

  val sub: Money = 300.01(USD) - 200(EUR)
  println(sum1)
  println(sum2)
  println(sum3)
  println("===============")
  println(sub)
  println("===============")
  val mult1: Money = 30(zl) * 20 //result in złoty
  val mult2: Money = 20($) * 11 //result in dollars
  println(mult1)
  println(mult2)
  println("===============")
  val compare1: Boolean = 300.30(USD) > 200(er)
  val compare2: Boolean = 300.30($) < 1(EUR)
  println(compare1)
  println(compare2)