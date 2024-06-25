from ._anvil_designer import CourseItemTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class CourseItem(CourseItemTemplate):
  def __init__(self, name, description,button_text, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name_label.text = name
    self.description_label.text = description
    self.button.text = button_text
    
    

    # Any code you write here will run before the form opens.

  def name_label_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    pass


