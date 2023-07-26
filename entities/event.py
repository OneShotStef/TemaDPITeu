class Event:
    def __init__(self, id, name, city, participantsNumber, maxSpots, startDate, finishDate):
        self.id = id
        self.name = name
        self.city = city
        self.participantsNumber = participantsNumber
        self.maxSpots = maxSpots
        self.startDate = startDate
        self.finishDate = finishDate

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name