val scala3Version = "3.4.0"

lazy val root = project
  .in(file("."))
  .settings(
    name := "uglystuff",
    version := "0.1.0-SNAPSHOT",

    scalaVersion := scala3Version,

    libraryDependencies += "org.scalameta" %% "munit" % "0.7.29" % Test
  )
