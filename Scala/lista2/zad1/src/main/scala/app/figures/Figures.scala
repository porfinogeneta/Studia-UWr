// import rationals._

package app.figures
import app.rationals._

// najmniejsza moliwa klasa, trzyma tylko te wartości
case class Point(x: Rational, y: Rational)

object Point {
  def apply(x: Rational, y: Rational): Point = new Point(x, y)
}

trait Shape {
  def area: Double
  val description: String
}

class Triangle(p1: Point, p2: Point, p3: Point) extends Shape {
  val (x1, y1) = (p1.x, p1.y)
  val (x2, y2) = (p2.x, p2.y)
  val (x3, y3) = (p3.x, p3.y)
  // pole trójkąta to pole prostokąta, bez pól 3 trójkątów
  // aby policzyć pole prostokąta trzema wziąć max x i max y - min x i min y
  val mxx = x3.max(x1.max(x2))
  val mix = x3.min(x1.min(x2))

  val mxy = y3.max(y1.max(y2))
  val miy = y3.min(y1.min(y2))
  override val area = (((mxx - mix).abs() * (mxy - miy).abs()) -
   Rational(1,2) * ((x3 - x2).abs() * (y3 - y2).abs()
   + (x2 - x1).abs() * (y2 - y1).abs() + (x3 - x1).abs() * (y3 - y1).abs())).toDouble()
  override val description = "Triangle"
}

object Triangle {
  def apply(p1: (Rational, Rational), p2: (Rational, Rational), p3: (Rational, Rational)): Triangle = 
    new Triangle(Point(p1._1, p1._2), Point(p2._1, p2._2), Point(p3._1, p3._2))
}

class Rectangle(p1: Point, p2: Point) extends Shape {
  val (x1, y1) = (p1.x, p1.y)
  val (x2, y2) = (p2.x, p2.y)

  override val area = ((x1 - x2).abs() * (y1 - y2).abs()).toDouble()
  override val description: String = 
    if ((x1 - x2).abs().equal((y1 - y2).abs())) "Square" else "Rectangle"
}

object Rectangle {
  def apply(p1: (Rational, Rational), p2: (Rational, Rational)): Rectangle = 
    new Rectangle(Point(p1._1, p1._2), Point(p2._1, p2._2))
}