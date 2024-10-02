package controllers

import javax.inject._
import play.api._
import play.api.mvc._

import database._

@Singleton
class LecturesController @Inject()(val controllerComponents: ControllerComponents) extends BaseController {
    def index() = Action {implicit request: Request[AnyContent] => 
        Ok(views.html.lectures(lectures = database.DB.lectures))    
    }
}