package controllers

import javax.inject._
import play.api._
import play.api.mvc._

import database._

@Singleton
class StudentController @Inject()(val controllerComponents: ControllerComponents) extends BaseController {
    def index(id: Int) = Action {implicit request: Request[AnyContent] => 
        val stdn = database.DB.students.filter(s => s.index == id).apply(0)
        val enrolls = database.DB.enrollments.filter(e => e.students.contains(stdn))
        val eIds = enrolls.map(e => e.id)
        val lecs = database.DB.lectures.filter(l => eIds.contains(l.id))
        Ok(views.html.student(student = stdn, lectures = lecs))
    }
}