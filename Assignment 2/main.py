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
from places_list import PlacesList


class TravelTracker(App):

    def __init__(self):
        super().__init__()
        self.places_list = PlacesList()
        self.filler = Label(text="Krappa")
        self.filler1 = Label(text="Bruh")
        self.filler2 = Label(text="Bruh")
        self.filler3 = Label(text="Bruh")
        self.filler4 = Label(text="Bruh")
        self.filler5 = Label(text="Bruh")
        self.filler6 = Label(text="Bruh")
        self.filler7 = Label(text="Bruh")
        self.filler8 = Label(text="Bruh")
        self.filler9 = Label(text="Bruh")
        self.filler10 = Label(text="Bruh")

    def build(self):
        self.title = "TravelTracker 2.0 by Zwe Nyan Toe"
        self.root = Builder.load_file('app.kv')
        self.places_list.load_places()
        self.build_widgets_left_col()
        return self.root

    def build_widgets_left_col(self):
        self.root.ids.left_layout.add_widget(self.filler)
        self.root.ids.left_layout.add_widget(self.filler1)
        self.root.ids.left_layout.add_widget(self.filler2)
        self.root.ids.left_layout.add_widget(self.filler3)
        self.root.ids.left_layout.add_widget(self.filler4)
        self.root.ids.left_layout.add_widget(self.filler5)
        self.root.ids.left_layout.add_widget(self.filler6)
        self.root.ids.left_layout.add_widget(self.filler7)
        self.root.ids.left_layout.add_widget(self.filler8)
        self.root.ids.left_layout.add_widget(self.filler9)
        self.root.ids.left_layout.add_widget(self.filler10)

TravelTracker().run()
