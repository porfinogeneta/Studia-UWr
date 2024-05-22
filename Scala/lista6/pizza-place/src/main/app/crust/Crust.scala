package app.crust


sealed trait CrustType

case object thin extends CrustType
case object thick extends CrustType