file://<WORKSPACE>/lista1/uglystuff/src/main/scala/Main.scala
### java.lang.AssertionError: NoDenotation.owner

occurred in the presentation compiler.

presentation compiler configuration:
Scala version: 3.3.1
Classpath:
<HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala3-library_3/3.3.1/scala3-library_3-3.3.1.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.10/scala-library-2.13.10.jar [exists ]
Options:



action parameters:
offset: 1399
uri: file://<WORKSPACE>/lista1/uglystuff/src/main/scala/Main.scala
text:
```scala
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

  def divideUgly(low: Int, high: Int): Int =
    var mid = Math.floor((low + high) / 2).toInt
    var pivot = lst(mid)
    var left = low
    var right = high
    swapUgly(right, mid)
    
    right -= 1
    
    while (left < right){
      if (lst(left) < pivot){
        left += 1
      } else if (lst(right) > pivot){
        right -= 1
      }else {
        swapUgly(left, right)
        left += 1
        right -= 1
      }
    }
  
    left

  def quickUgly(left: Int, right: Int): Unit =
    if (left < right){
      val pi = divideUgly(left, right)
      quickUgly(left, pi - 1)
      quickUgly(pi, right)
    }
    return

  quickUgly(0, lst.length - 1)
    

  lst

def sort(xs: List[Int]): List[Int] = 
  xs match
    case Nil => Nil
    case pivot :: tail => {
      val (less, greater) = tail.partition(_ < p[@@])
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

import scala.io.Source
//create a list with all lines from given file

def fileLinesUgly(file: java.io.File): List[String] = 
  if (!file.isFile) {
    throw new IllegalArgumentException("Input must be a file")
  }

  try {
    val source = Source.fromFile(file)
    val lines = source.getLines.toList
    source.close() // Ensure proper resource closing
    println(lines)
    lines
  } catch {
    case e: Exception => throw new RuntimeException(s"Error reading file ${file.getName}: ${e.getMessage}")
  }


@main def hello(): Unit =
  println(scalarUgly(List(1,3,5,7), List(2,4,6,8)))
  println(scalar(List(1,3,5,7), List(2,4,6,8)))
  println(isPrimeUgly(4))
  println(isPrime(6))
  println(primePairsUgly(6))
  println(primePairs(6))
  val lst = List(3,1,6,8)
  // sortUgly(lst)
  println(lst)
  // val filePath = "test.txt" // Replace with actual file path
  // val lines = fileLinesUgly(new java.io.File(filePath))
  // println(lines) 
```



#### Error stacktrace:

```
dotty.tools.dotc.core.SymDenotations$NoDenotation$.owner(SymDenotations.scala:2582)
	scala.meta.internal.pc.SignatureHelpProvider$.isValid(SignatureHelpProvider.scala:83)
	scala.meta.internal.pc.SignatureHelpProvider$.notCurrentApply(SignatureHelpProvider.scala:96)
	scala.meta.internal.pc.SignatureHelpProvider$.$anonfun$1(SignatureHelpProvider.scala:48)
	scala.collection.StrictOptimizedLinearSeqOps.loop$3(LinearSeq.scala:280)
	scala.collection.StrictOptimizedLinearSeqOps.dropWhile(LinearSeq.scala:282)
	scala.collection.StrictOptimizedLinearSeqOps.dropWhile$(LinearSeq.scala:278)
	scala.collection.immutable.List.dropWhile(List.scala:79)
	scala.meta.internal.pc.SignatureHelpProvider$.signatureHelp(SignatureHelpProvider.scala:48)
	scala.meta.internal.pc.ScalaPresentationCompiler.signatureHelp$$anonfun$1(ScalaPresentationCompiler.scala:398)
```
#### Short summary: 

java.lang.AssertionError: NoDenotation.owner