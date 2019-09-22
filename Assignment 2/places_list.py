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

    def sort(self, sort_method):
        if sort_method == "Place":
            self.places_list.sort(key=lambda sort: (sort[0].place, sort[0].country))
        elif sort_method == "Country":
            self.places_list.sort(key=lambda sort: sort[0].country)
        elif sort_method == "Priority":
            self.places_list.sort(key=lambda sort: (sort[0].priority, sort[0].country))
        else:
            self.places_list.sort(key=lambda i: (i[0].status, i[0].country))

    def __str__(self):
        return self.places_list

