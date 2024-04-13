//scalar product of two vectors xs and ys
def scalarUgly(xs: List[Int], ys: List[Int]): Int = 
  var result = 0
  var i = 0
  while (i < xs.length){
    result += xs(i)* ys(i)
    i += 1
  }

  return result

def scalar(xs: List[Int], ys: List[Int]): Int = 
  val products = (xs, ys).zipped.map(_ * _)
  return products.foldLeft(0)((acc, elem) => acc + elem)

//quicksort algorithm

def sortUgly(xs: List[Int]): List[Int] = 
  var lst: List[Int] = xs
  
  def swapUgly(i: Int, j: Int): Unit =
    val temp = xs(i)
    lst = lst.updated(i, xs(j))
    lst = lst.updated(j, temp)

  def divideUgly(start: Int, end: Int): Int =
    var pivot = lst(start)
    var low = start + 1
    var high = end

    while (low <= high){
      while (low <= high && lst(low) <= pivot) {
        low += 1
      }
      while (low <= high && lst(high) >= pivot) {
        high -= 1
      }
      if (low <= high) {
        swapUgly(low, high)
      }
      
    }
      
    swapUgly(start, high)
  
    high 

  def quickUgly(left: Int, right: Int): Unit =
    if (left < right){
      val pi = divideUgly(left, right)
      quickUgly(left, pi - 1)
      quickUgly(pi + 1, right)
    }
    return

  quickUgly(0, lst.length - 1)
    
  lst

// ::: złącza dwie listy, :: dołącza element na początek listy
def sort(xs: List[Int]): List[Int] =
  xs match
    case Nil => Nil
    case pivot :: tail => {
      val (smaller, bigger) = tail.partition(_ < pivot)
      sort(smaller) ::: pivot :: sort(bigger)
    }
  



//checks if n is prime
def isPrimeUgly(n: Int): Boolean = 
  var i = 2
  if (n <= 1){
    return false
  }
  while (i <= Math.sqrt(n)){
    if (n % i == 0){
      return false
    }
    i += 1
  }
  true


def isPrime(n: Int): Boolean =
  if (n <= 1) false
  else if (n == 2 | n == 3) true
  else {
    // badamy kwatyfikatorem dla kadego
    (2 to Math.sqrt(n).toInt + 1).forall(n % _ != 0)
  }

// for given positive integer n, find all pairs of integers i and j,
// where 1 ≤ j < i < n such that i + j is prime
def primePairsUgly(n : Int): List[(Int, Int)] =
  var res: List[(Int, Int)] = List()
  var i = n - 1
  
  while (i >= 2){
    var j = 1
    while(j < i){
      if (isPrime(i + j)){
        res = (i, j) :: res
      }
      j += 1
    }
    i -= 1
  }

  res

def primePairs(n: Int): List[(Int, Int)] =
  (2 to n-1).flatMap(i => (1 until i).filter(j => isPrime(i + j)).map(j => (i,j))).toList


//create a list with all lines from given file
def fileLinesUgly(file: java.io.File): List[String] = {
        var listOfLines = List[String]()
        val lineStream = fromFile(file).getLines()
        if(lineStream.hasNext)
        {
            while(lineStream.hasNext) {
                listOfLines = lineStream.next() :: listOfLines 
            }
            
        }
        listOfLines.reverse
    }

def fileLines(file: java.io.File): List[String] = {
    fromFile(file).getLines.toList
}


val filesHere = new java.io.File("./").listFiles

def printNonEmptyUgly(pattern: String): Unit = 
{
    val files = List()
    var i = 0
    if(i < filesHere.size)
    {
        while(i < filesHere.size)
        {
            val el = filesHere(i)
            if(el.isFile && el.getName.endsWith(pattern) && el.length > 0)
                println(el.getName)
            i += 1
        }
         
    }
}


def printNonEmpty(pattern: String): Unit = 
{
    val files = filesHere.filter(file => file.isFile && file.getName.endsWith(pattern) && file.length > 0)
    files.foreach(file => println(file.getName))
}

import scala.io.Source._



@main def hello(): Unit =
  println(scalarUgly(List(1,3,5,7), List(2,4,6,8)))
  println(scalar(List(1,3,5,7), List(2,4,6,8)))
  println(isPrimeUgly(4))
  println(isPrime(6))
  println(primePairsUgly(6))
  println(primePairs(6))
  val lst = List(3,1,6,8,6)
  println(sortUgly(lst))
  // println(lst)
  println(sort(lst))
  val file = new java.io.File("/Users/szymon/Documents/Studia-UWr/Scala/lista1/uglystuff/src/test.txt")
  println(fileLines(file))
  println(fileLinesUgly(file))
  printNonEmpty(".scala")
  println()
  printNonEmptyUgly(".scala")