from ._anvil_designer import CoursesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..CourseItem import CourseItem


class Courses(CoursesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.load_courses()

    self.content_panel.add_component(CourseItem(name = "Python", button_text = "Buy For $39 ", description = " The Best course for you!"))
    # Any code you write here will run before the form opens.
  def load_courses(self):
    courses = anvil.server.call('get_course_details','name').search()
    
    for course in courses:
      print(course['name'])