import app.DataFetching._


@main def hello(): Unit =
  FacebookAdapter.getUsers(List("Alice", "Bob", "Carly"), "logFile.txt")

def msg = "I was compiled by Scala 3. :)"
