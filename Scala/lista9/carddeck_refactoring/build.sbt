val scala3Version = "3.4.2"



lazy val commonSettings = Seq(
  scalacOptions ++= Seq(
      "-deprecation",          // Emit warning and location for usages of deprecated APIs.
      "-encoding", "utf-8",    // Specify character encoding used by source files.
      "-feature",              // Emit warning and location for usages of features that should be imported explicitly.
      "-unchecked",            // Enable additional warnings where generated code depends on assumptions.
      "-Xlint",                // Enable recommended additional warnings.
      "-Ywarn-unused-import",   // Warn when an import selector is not referenced.
    ),
  scalaVersion := scala3Version,
  // sbt test -> uruchamianie testów
  libraryDependencies += "org.scalatest" %% "scalatest" % "3.2.18" % "test",
)


lazy val core = (project in file("core"))
  .settings(
    commonSettings,
    name := "Core"
  )

lazy val blackjack = (project in file("blackjack"))
  .settings(
    commonSettings,
    name := "Blackjack"
  ).dependsOn(core)

  

lazy val root = project
  .in(file("."))
  .aggregate(blackjack, core)
  .dependsOn(blackjack, core)
  .settings(
    commonSettings,
    name := "CardDeckRefactoring"
    )
