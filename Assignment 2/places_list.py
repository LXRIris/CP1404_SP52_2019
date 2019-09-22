class PlacesList:
    def __init__(self):
        self.places_list = []

    def load_places(self):
        open_file = open("places.csv","r")
        for place in open_file.readlines():
            place = place.strip()
            file = place.strip(",")
            place_country_priority_listed = file.split(",")
            self.places_list.append(place_country_priority_listed)
        open_file.close()
        return self.places_list

    def get_visited_places_count(self):
        visited_places = 0
        for place in self.places_list:
            if place[0].status == 'y':
                visited_places += 1
        return visited_places

    def __str__(self):
        return self.places_list

