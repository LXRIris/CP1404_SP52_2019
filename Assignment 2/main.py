"""
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
        self.spinner = Spinner(text="Place", values=("Place", "Country", "Priority", "Visited"))
        self.add_label = Label(text="Add New Place:")
        self.name_label = Label(text="Name: ")
        self.text_input = TextInput(write_tab=False, multiline=False)
        self.country_label = Label(text="Country: ")
        self.country_input = TextInput(write_tab=False, multiline=False)
        self.priority_label = Label(text="Priority: ")
        self.priority_input = TextInput(write_tab=False, multiline=False)
        self.add_button = Button(text="Add place")
        self.top_label = Label(id="count_place_label")
        self.clear_button = Button(text="Clear Fields")

    def build(self):
        self.title = "TravelTracker 2.0 by Zwe Nyan Toe"
        self.root = Builder.load_file('app.kv')
        self.places_list.load_places()
        self.build_widgets_left_col()
        self.build_widgets_right_col()
        for place in self.places_list.places_list:
            if place[0].status == "v":
                song_display_button = Button(text="'{}' in  {} ({}) (visited)".format(place[0].place, place[0].country,
                                                                                      place[0].priority))
                song_display_button.background_color = [88, 89, 0, 0.3]
            else:
                song_display_button = Button(text="'{}' in  {} ({})".format(place[0].place, place[0].country, place[0].
                                                                            priority))
                song_display_button.background_color = [0, 88, 88, 0.3]
            self.root.ids.right_layout.add_widget(song_display_button)

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

        self.add_button.bind(on_release=self.handle_add_song)
        self.clear_button.bind(on_release=self.clear_fields)
        self.spinner.bind(text=self.songs_sort)

    

    def build_widgets_right_col(self):
        self.root.ids.top_layout.add_widget(self.top_label)
        self.top_label.text = "To visit: {} places, {} places visited.".format(
            str(self.places_list.get_unvisited_places_count()), self.places_list.get_visited_places_count())


TravelTracker().run()
