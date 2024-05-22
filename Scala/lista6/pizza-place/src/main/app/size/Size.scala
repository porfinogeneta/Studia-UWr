package app.size


sealed trait SizeType

case object small extends SizeType
case object regular extends SizeType
case object large extends SizeType