package app.plugins

trait TextManipulation:
    def plugin(s: String): String

trait Reverting extends TextManipulation:
    def reverting(s: String): String =
        s.reverse

trait LowerCasing extends TextManipulation:
    def lowerCasing(s: String): String = 
        s.toLowerCase()

trait SingleSpacing extends TextManipulation:
    def singleSpacing(s: String): String =
        // zamieniemy wszystkie spacje na pojedynczą spację, ucinamy spacje na początku i na końcu
        s.replaceAll("\\s+", " ").trim()

trait NoSpacing extends TextManipulation:
    def noSpacing(s: String): String =
        // wyrzycamy wszystkie whitespacy
        s.filterNot(_.isWhitespace)

trait DuplicateRemoval extends TextManipulation:
    def duplicateRemoval(s: String): String =
        // wyrzucamy litery z count > 1
        s.filter(l => s.count(_ == l) == 1)

trait Rotating extends TextManipulation:
    def rotating(s: String): String =
        if (s.isEmpty() || s.length() == 1) s
        else {
            s.last + s.substring(1, s.length() - 1) + s.head
        }

trait Doubling extends TextManipulation:
    def doubling(s: String): String =
        // tworzymy pary litera, liczba i konstruujemy nowy string za pomocą folda
        s.zipWithIndex.foldLeft("")((str, pair) => 
            if (pair._2 % 2 == 1){
            str + pair._1 + pair._1
        }else {str + pair._1})

trait Shortening extends TextManipulation:
    def shortening(s: String): String =
        // do wynikowego stringa dodajemy tylko parzyste litery
        s.zipWithIndex.foldLeft("")((str, pair) => 
            if (pair._2 % 2 == 0){
                str + pair._1
            }else {
                str + ""
            }
            )