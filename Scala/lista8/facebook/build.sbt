val scala3Version = "3.4.2"

lazy val root = project
  .in(file("."))
  .settings(
    name := "facebook",
    version := "0.1.0-SNAPSHOT",

    scalaVersion := scala3Version,

    libraryDependencies ++= Seq(
      "org.scalameta" %% "munit" % "0.7.29" % Test,
      "com.restfb" % "restfb" % "VERSION"
      )
  )
