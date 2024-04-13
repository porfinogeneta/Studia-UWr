package app
import app.plugins._
import app.actions._

// object Tester extends Shortening {val name: String = "ab cd"}


@main def hello(): Unit =
  println(Actions.actionA.plugin("te st     ing")) // Output: "test ng"
  println(Actions.actionB.plugin("ab   cd      efg    h")) // Output: "addfhh"
  println(Actions.actionC.plugin("HELLO WORLD")) // Output: "heelllo  woorlld"
  println(Actions.actionD.plugin("hello world")) // Output: "de wrh"
  println(Actions.actionE.plugin("ab   c d      e       f")) // Output: "ecca"
  println(Actions.actionF.plugin("hello")) // Output: "olleh"
  println(Actions.actionG.plugin("aa bb   cc")) // Output: "abb"
