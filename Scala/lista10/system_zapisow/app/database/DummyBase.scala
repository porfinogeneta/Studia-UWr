package database


case class Student(index: Int, name: String, year: Short)
case class Lecture(id: String, name: String)

case class Enrollment(id: String, students: List[Student])


object DB {
    // Hard-code at least 10 students
    val s1 = Student(233190, "Krzysztof Kalisz", 2024)
    val s2 = Student(233191, "Anna Nowak", 2023)
    val s3 = Student(233192, "John Smith", 2024)
    val s4 = Student(233193, "Maria Garcia", 2022)
    val s5 = Student(233194, "Liam Brown", 2023)
    val s6 = Student(233195, "Emma Jones", 2024)
    val s7 = Student(233196, "Oliver Miller", 2022)
    val s8 = Student(233197, "Sophia Davis", 2023)
    val s9 = Student(233198, "Lucas Wilson", 2024)
    val s10 = Student(233199, "Mia Moore", 2022)

    val students = List(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10)

    // enrollments
    val e1 = Enrollment("L1", List(s1, s2, s3))
    val e2 = Enrollment("L2", List(s4, s5, s6))
    val e3 = Enrollment("L3", List(s7, s8, s9))
    val e4 = Enrollment("L4", List(s10, s1, s4, s7))

    val enrollments = List(e1,e2,e3,e4)

    // Hard-code at least 4 lectures
    val l1 = Lecture("L1", "Algorithms")
    val l2 = Lecture("L2", "Data Structures")
    val l3 = Lecture("L3", "Operating Systems")
    val l4 = Lecture("L4", "Database Systems")

    val lectures = List(l1,l2,l3,l4)
}