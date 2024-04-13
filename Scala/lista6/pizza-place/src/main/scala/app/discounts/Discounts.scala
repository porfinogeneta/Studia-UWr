package app.discounts

sealed trait discount

case object student extends discount
case object senior extends discount