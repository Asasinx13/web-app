from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..Cars import Cars

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def main_image_mouse_move(self, x, y, **event_args):
    """This method is called when the mouse cursor moves over this component"""
    pass

  def main_image_show(self, **event_args):
    """This method is called when the Image is shown on the screen"""
    pass

  def view_cars_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Cars())