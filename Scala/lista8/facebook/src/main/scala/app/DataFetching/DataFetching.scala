package app.DataFetching

import app.ArtificialData._
import scala.concurrent.{Future, ExecutionContext}
import scala.util.{Success, Failure, Random}
import java.io.{BufferedWriter, FileWriter, IOException}
import java.time.LocalDateTime

import ExecutionContext.Implicits.global
import java.nio.Buffer

object FacebookAdapter {
    private val myAppSecret = "" // any String (or Note1)
    val rand = new Random()
    val currentDateTime: LocalDateTime = LocalDateTime.now()

    def fetchUser(name: String): User = {
        Thread.sleep(1000)
        User(name, rand.between(0, 100000))
    }

    def getUserFacebookData(name: String): Future[User] = {
        Future {
            fetchUser(name)
        }
    }

    def writeFile(filename: String, data: String): Future[Unit] = Future {
        val bw = new BufferedWriter(new FileWriter(filename, true))
        
        try {
            bw.write(data)
            bw.newLine()
        } 
        finally {
            bw.close()
        }
    }

    // comapare likes
    def getUsers(names: List[String], filename: String): Unit = {
        // zbieramy futures
        val futures = names.map(getUserFacebookData)
        
        // czekamy az się skończą
        val allFuturesResolved = Future.sequence(futures)

        val x: Future[User] = someFuture
        val y: Future[User] = someFuture


        for {
            user1  <- someFeature
            user2 <- someFeature
        } yield user2
        
        allFuturesResolved.onComplete {
            case Success(users) => 
                val data = s"${currentDateTime}${users.map(_.toString).mkString(", ")}"
                writeFile(filename, data).onComplete{
                    // jak się uda zapisać do pliku
                    case Success(_) => users.foreach(u => {
                        println(s"${u.name}, likes: ${u.likes}")
                    })
                    case Failure(exception) => println(s"Failed to write to file: $exception")
                }
                
            case Failure(exception) => println(s"Failed to fetch user: $exception")
        }
    }
}

