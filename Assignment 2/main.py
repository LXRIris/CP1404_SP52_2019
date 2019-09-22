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
from kivy.uix.textinput import TextInput
from places_list import PlacesList


class TravelTracker(App):

    def __init__(self):
        super().__init__()
        self.places_list = PlacesList()
        self.sort_label = Label(text="Sort by:")
        self.filler1 = Label(text="Bruh")
        self.add_label = Label(text="Add New Place:")
        self.name_label = Label(text="Name: ")
        self.text_input = TextInput(multiline=False)
        self.country_label = Label(text="Country: ")
        self.country_input = TextInput(multiline=False)
        self.priority_label = Label(text="Priority: ")
        self.priority_input = TextInput(multiline=False)
        self.filler9 = Label(text="Bruh")
        self.filler10 = Label(text="Bruh")

    def build(self):
        self.title = "TravelTracker 2.0 by Zwe Nyan Toe"
        self.root = Builder.load_file('app.kv')
        self.places_list.load_places()
        self.build_widgets_left_col()
        return self.root

    def build_widgets_left_col(self):
        self.root.ids.left_layout.add_widget(self.sort_label)
        self.root.ids.left_layout.add_widget(self.filler1)
        self.root.ids.left_layout.add_widget(self.add_label)
        self.root.ids.left_layout.add_widget(self.name_label)
        self.root.ids.left_layout.add_widget(self.text_input)
        self.root.ids.left_layout.add_widget(self.country_label)
        self.root.ids.left_layout.add_widget(self.country_input)
        self.root.ids.left_layout.add_widget(self.priority_label)
        self.root.ids.left_layout.add_widget(self.priority_input)
        self.root.ids.left_layout.add_widget(self.filler9)
        self.root.ids.left_layout.add_widget(self.filler10)

TravelTracker().run()
