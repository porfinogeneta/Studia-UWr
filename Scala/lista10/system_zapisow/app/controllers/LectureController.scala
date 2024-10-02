package controllers

import javax.inject._
import play.api._
import play.api.mvc._

import database._

@Singleton
class LectureController @Inject()(val controllerComponents: ControllerComponents) extends BaseController {
    def index(id: String) = Action {implicit request: Request[AnyContent] => 
        val enrolls = database.DB.enrollments.filter(e => e.id == id).apply(0)
        val lec = database.DB.lectures.filter(e => e.id == id).apply(0)
        Ok(views.html.lecture(lecture = lec, enrollment = enrolls))
    }
}