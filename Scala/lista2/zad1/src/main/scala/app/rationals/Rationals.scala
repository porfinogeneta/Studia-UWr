// package rationals
package app.rationals
// kazda liczba rzeczywista jest ułamkiem
class Rational(nominator: Int, denominator: Int){
  require(denominator != 0, "Denominator cannot be 0!")

  // skracamy podany ułamek
  private val g = gcd(nominator, denominator)
  val nom = nominator / g
  val denom = denominator / g

  def +(other: Rational): Rational = 
    new Rational(
      nom * other.denom + other.nom * denom, denom * other.denom
    )
  
  def -(other: Rational): Rational = 
    new Rational(
      nom * other.denom - other.nom * denom, denom * other.denom
    )

  def abs(): Rational = {
    if (nom < 0 || denom < 0){
      Rational(math.abs(nom), math.abs(denom))
    }else {
      this
    }
  }

  def equal(other: Rational): Boolean = {
    (other.nom == nom)
  }

  def *(other: Rational): Rational =
    new Rational(
      nom * other.nom, denom * other.denom
    )

  def /(other: Rational): Rational = 
    new Rational(
      nom * other.denom, denom * other.nom
    )

  override def toString(): String = 
    val whole = nom / denom
    val remainder = nom % denom
    if (remainder == 0) whole.toString
    else 
      if (whole == 0) s"${remainder}/${denom}" else s"${whole} ${remainder}/${denom}"

  def toDouble(): Double =
    nom.toDouble / denom.toDouble

  // funkcje min i max zwracające inną liczbę albo samą siebie
  def max(other: Rational): Rational = 
    val cmn_denominator = gcd(denom, other.denom)
    val n1 = nom * (other.denom / cmn_denominator)
    val n2 = other.nom * (denom / cmn_denominator)
    if (n1 > n2) this else other

  def min(other: Rational): Rational = 
    val cmn_denominator = gcd(denom, other.denom)
    val n1 = nom * (other.denom / cmn_denominator)
    val n2 = other.nom * (denom / cmn_denominator)
    if (n1 < n2) this else other

  private def gcd(a: Int, b: Int): Int = 
    if (b == 0) a else gcd(b, a % b)
}

// chcemy zrobić 'companion object with factory methods'
// czyli obiekt pozwalający na szybsze korzystanie z klasy
object Rational {
  // dzięki apply nie musimy juz pisać zawsze 'new', teraz
  // wystarczą nawiasy, i domyślnue zrobimy liczbę
  def apply(n: Int, d: Int = 1): Rational = new Rational(n, d)
  val zero = Rational(0)
  val one = Rational(1)
}