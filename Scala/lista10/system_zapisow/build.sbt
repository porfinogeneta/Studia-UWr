import dependencies._
name := """system_zapisow"""
organization := "system_zapisow"

version := "1.0-SNAPSHOT"

lazy val root = (project in file(".")).enablePlugins(PlayScala)

scalaVersion := "2.13.14"

libraryDependencies += guice
libraryDependencies += play

// Adds additional packages into Twirl
//TwirlKeys.templateImports += "system_zapisow.controllers._"

// Adds additional packages into conf/routes
// play.sbt.routes.RoutesKeys.routesImport += "system_zapisow.binders._"
