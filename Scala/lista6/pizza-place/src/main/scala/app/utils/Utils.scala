package app.utils


object Utils {
    def prettify(value: Any): String =
        value.toString.split("\\.").lastOption.getOrElse("").takeWhile(_ != '$')

    def prettifyOption[T](value: Option[T], defaultVal: String) =
        value.map(prettify).getOrElse(defaultVal)
}