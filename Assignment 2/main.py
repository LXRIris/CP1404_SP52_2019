"""

ADD YOUR SHIT HERE.

Name:
Date:
Brief Project Description:
GitHub URL:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from places_list import PlacesList


class TravelTracker(App):

    def __init__(self):
        super().__init__()
        self.places_list = PlacesList()
        self.sort_label = Label(text="Sort by:")
        self.spinner = Spinner(text="Place", values = ("Place", "Country", "Priority", "Visited"))
        self.add_label = Label(text="Add New Place:")
        self.name_label = Label(text="Name: ")
        self.text_input = TextInput(write_tab=False, multiline=False)
        self.country_label = Label(text="Country: ")
        self.country_input = TextInput(write_tab=False, multiline=False)
        self.priority_label = Label(text="Priority: ")
        self.priority_input = TextInput(write_tab=False, multiline=False)
        self.add_button = Button(text="Add song")
        self.clear_button = Button(text="Clear Fields")

    def build(self):
        self.title = "TravelTracker 2.0 by Zwe Nyan Toe"
        self.root = Builder.load_file('app.kv')
        self.places_list.load_places()
        self.build_widgets_left_col()
        return self.root

    def build_widgets_left_col(self):
        self.root.ids.left_layout.add_widget(self.sort_label)
        self.root.ids.left_layout.add_widget(self.spinner)
        self.root.ids.left_layout.add_widget(self.add_label)
        self.root.ids.left_layout.add_widget(self.name_label)
        self.root.ids.left_layout.add_widget(self.text_input)
        self.root.ids.left_layout.add_widget(self.country_label)
        self.root.ids.left_layout.add_widget(self.country_input)
        self.root.ids.left_layout.add_widget(self.priority_label)
        self.root.ids.left_layout.add_widget(self.priority_input)
        self.root.ids.left_layout.add_widget(self.add_button)
        self.root.ids.left_layout.add_widget(self.clear_button)

TravelTracker().run()
