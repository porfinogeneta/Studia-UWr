object Utils {
  def isSorted(as: List[Int], ordering: (Int, Int) => Boolean): Boolean =
    if (as.isEmpty) {
      throw Exception()
    }
    if (as.length == 1){
      throw Exception()
    }
    //checks if as is sorted according to ordering
    // forall sprawdza czy wszystkie elementy kolekcji spełniają predykat
    as.sliding(2).forall(pair => ordering(pair(0), pair(1)))

  def isAscSorted(as: List[Int]): Boolean =
    isSorted(as, _ >= _)
    // //checks if as is sorted in ascending order
    // as.sliding(2).forall(pair => pair(0) < pair(1))
  
  def isDescSorted(as: List[Int]): Boolean =
    isSorted(as, _ <= _)
    //checks if as is sorted in descending order
    // as.sliding(2).forall(pair => pair(0) > pair(1))

  // mamy typy generyczne A i B
  // foldLeft bierze jeden typ i zwraca drugi
  // rekurencyjne
  // def foldLeft[A,B](l: List[A], z: B)(f: (B,A) => B): B = l match {
  //   case Nil => z
  //   case elem::l => {
  //     val result = f(z, elem)
  //     foldLeft(l, result)(f)
  //   }
  // }
  def foldLeft[A,B](l: List[A], z: B)(f: (B,A) => B): B =
    var acc: B = z
    for (elem <- l){
     acc = f(acc, elem) 
    }
    acc
  
  //sum elements of l with usage of foldLeft function
  def sum(l: List[Int]): Int = 
    // foldLeft(l,0)((x: Int, y: Int) => x + y)
    foldLeft(l,0)(_ + _)

  // length of l with usage of foldLeft function
  def length[A](l: List[A]): Int =
    // foldLeft(l,0)((acc: Int, e: A) => acc + 1)
    foldLeft(l,0)((acc: Int, _) => acc + 1)

  //compose two unary functions:compose(f,g)(x) = f(g(x))
  def compose[A,B,C](f: B => C, g: A => B)(x: A): C =
    f(g(x))

  def repaeted[A,B](f: A => A, x: A, n: Int): A =
    if ( n < 0){
      throw Exception()
    }
    if (n == 0) {
      identity[A](x)
    }
    if (n == 1){
      f(x)
    }else {
      f(repaeted(f, x, n-1))
    }

  //converts a binary function f of two arguments into a function of one argument that partially applies f
  def curry[A,B,C](f: (A,B) => C): (A => (B => C)) =
    ((a: A) => ((b: B) => f(a, b)))
  
  // reverse of curry function
  def uncurry[A,B,C](f: (A => (B => C)))(x: A, y: B) = 
    f(x)(y)

  def unSafe[T](ex: Exception)(func: => T): T =
    try {
      func
      func
      func
    } catch {
        case _: Exception =>
          println("Caught Exception: " + ex.getMessage)
          throw ex
    }

  
}
 

// exceptions
case class ListException() extends Exception("aaaa")

@main def hello(): Unit =
  // println(Utils.unSafe(Exception("Could not run command"))(Utils.isSorted(List(1,2,3,1), ((x: Int, y: Int) => x < y))))
  // Utils.unSafe(new ListException("List cannot be empty!")){
  //   Utils.isSorted(List(), ((x: Int, y: Int) => x < y))
  // }
  Utils.unSafe(new Exception("gygygy")) {
    (Utils.isSorted(List(1), ((x: Int, y: Int) => x < y)))
  }
  println(Utils.isAscSorted(List(1,2,3,4)))
  println(Utils.foldLeft(List(1,23,3,4), 0)((x:Int, y:Int) => x + y))
  println(Utils.sum(List(1,23,3,4)))
  println(Utils.length(List(1,23,3,4)))
  println(Utils.length(List("a",23,3,4)))
  println(Utils.compose((x: Float) => x.abs, (x: Float) => x + 3)(-6))
  println(Utils.repaeted((x: Int) => x + 3, 0, 5))
  // currying
  def add(a: Int, b: Int) = a + b
  println(Utils.curry(add)(2)(1))
  println(Utils.uncurry(Utils.curry(add))(2, 1))
