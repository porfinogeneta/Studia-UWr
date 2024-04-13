
// package rationals

package app
import app.figures._
import app.rationals._



object singleton {
  def areaSum(figures: List[Shape]): Double =
    // figures.foldLeft(0.0)((acc, f) => acc + f.area)
    figures.map(_.area).sum
  def printAll(figures: List[Shape]): Unit =
    for (f <- figures){
      println(f.description)
    }
}


@main def testing(): Unit =
  // val half = Rational(3, 2)
  // val quater = Rational(1,4)
  // val sum_r = half + quater
  // println(sum_r.toString)
  // val triangle =  Triangle((Rational(0), Rational(0)), (Rational(0), Rational(1)), (Rational(1), Rational(0)))
  // val rectangle = Rectangle((Rational(1), Rational(1)), (Rational(6), Rational(3)))
  // val square = Rectangle((Rational(1), Rational(1)), (Rational(3), Rational(3)))
  // println(triangle.area)
  // println(rectangle.area)
  // println(rectangle.description)
  // println(square.area)
  // println(square.description)
  // val shapes = List(triangle, rectangle, square)
  // val sum = singleton.areaSum(shapes)
  // println(sum)
  // singleton.printAll(shapes)
  // **Test Cases for Rational Class**

  println("**Testing Rational Class:**")

  // Test addition
  val half = Rational(1, 2)
  val quarter = Rational(1, 4)
  val sum = half + quarter
  assert(sum.toString == "3/4", "Addition failed")
  println(s"1/2 + 1/4 = $sum")

  // Test subtraction
  val difference = half - quarter
  assert(difference.toString == "1/4", "Subtraction failed")
  println(s"1/2 - 1/4 = $difference")

  // Test absolute value
  val negative = Rational(-3, 2)
  assert(negative.abs().toString == "1 1/2", "Absolute value failed")
  println(s"|-3/2| = ${negative.abs()}")

  // Test equality
  assert(half.equal(Rational(2, 4)) == true, "Equality check failed")
  println(s"1/2 == 2/4: ${half.equal(Rational(2, 4))}")

  // Test multiplication
  val product = half * quarter
  assert(product.toString == "1/8", "Multiplication failed")
  println(s"1/2 * 1/4 = $product")

  // Test division
  val quotient = half / quarter
  assert(quotient.toString == "2", "Division failed")
  println(s"1/2 / 1/4 = $quotient")

  // Test toString
  val rationalString = Rational(3, 5).toString
  assert(rationalString == "3/5", "toString failed")
  println(s"Rational string representation: $rationalString")

  // Test toDouble
  val doubleValue = Rational(7, 2).toDouble()
  assert(doubleValue == 3.5, "toDouble failed")
  println(s"7/2 as double: $doubleValue")


  // **Test Cases for Shapes**

  println("\n**Testing Shapes:**")

  // Test triangle area
  val triangle = Triangle((Rational(0), Rational(0)), (Rational(0), Rational(1)), (Rational(1), Rational(0)))
  assert(triangle.area.toString == "0.5", "Triangle area calculation failed")
  println(s"Triangle area: ${triangle.area}")

  // Test rectangle area and description
  val rectangle = Rectangle((Rational(1), Rational(1)), (Rational(6), Rational(3)))
  assert(rectangle.area.toString == "10.0", "Rectangle area calculation failed")
  println(s"Rectangle area: ${rectangle.area}")
  assert(rectangle.description == "Rectangle", "Rectangle description failed")
  println(s"Rectangle description: ${rectangle.description}")

  // Test square area and description (assuming square inherits from rectangle)
  val square = Rectangle((Rational(1), Rational(1)), (Rational(3), Rational(3)))
  assert(square.area.toString == "4.0", "Square area calculation failed")
  println(s"Square area: ${square.area}")
  assert(square.description == "Square", "Square description failed")
  println(s"Square description: ${square.description}")

  // Test areaSum and printAll functions
  val shapes = List(triangle, rectangle, square)
  val totalArea = singleton.areaSum(shapes)
  assert(totalArea == 14.5, "areaSum calculation failed")
  println(s"Total area of shapes: $totalArea")
  singleton.printAll(shapes)

  println("\n**All Tests Passed!**")



