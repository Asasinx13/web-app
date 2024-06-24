from ._anvil_designer import CarsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..CarItem import CarItem


class Cars(CarsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.load_cars()
    c=CarItem(name = ["Mark"], button_text = "Buy For $", description = " The Best car for you!")
   
    # Any code you write here will run before the form opens.
  def load_cars(self):
    cars = anvil.server.call('get_cars_details', 'name').search()
    print(cars)
    for car in cars:
      print(car['Mark '],car['Model'])