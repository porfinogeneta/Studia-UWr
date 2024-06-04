package core.cards

// colors: Clubs ♣, Diamonds ♦, Hearts ♥ and Spades ♠
// sealed mówi ze wszelkie dziedziczenie moze się odbywać tylko w tym pliku
sealed trait Color

// róznica między case object a case class jest taka ze case object nie moze zmieniać wartości
case object Clubs extends Color
case object Diamonds extends Color
case object Hearts extends Color
case object Spades extends Color

// // values: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King
sealed trait Value
sealed trait Numerical // kolejny trait, którym rozszerzamy obiekt
sealed trait Face

// case class Numerical2(value: Int){
//     require(value >=2 && value <= 10)
// }

case object Ace extends Value with Face
case object Num2 extends Value with Numerical
case object Num3 extends Value with Numerical
case object Num4 extends Value with Numerical
case object Num5 extends Value with Numerical
case object Num6 extends Value with Numerical
case object Num7 extends Value with Numerical
case object Num8 extends Value with Numerical
case object Num9 extends Value with Numerical
case object Num10 extends Value with Numerical
case object Jack extends Value with Face
case object Queen extends Value with Face
case object King extends Value with Face

case class Card(col: Color, value: Value)
