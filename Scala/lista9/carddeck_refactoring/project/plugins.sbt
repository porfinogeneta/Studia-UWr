
// uruchamianie sbt scalafmt -> naprawa kodu, zeby wyglądał jako tako
addSbtPlugin("org.scalameta" % "sbt-scalafmt" % "2.5.2")

// uruchamianie sbt scalafix -> linter
addSbtPlugin("ch.epfl.scala" % "sbt-scalafix" % "0.12.1")

// plugin do testów jest jako dependency w build.sbt

// aby uruchomić sbt clean coverage test , potem sbt coverageReport
val pluginSbtScoverageVersion = sys.props.getOrElse(
  "plugin.sbtscoverage.version", "2.0.9"
)

addSbtPlugin("org.scoverage" % "sbt-scoverage" % pluginSbtScoverageVersion)