class Event:
    def __init__(self, id, name, city, participantsNumber, maxSpots, startDate, finishDate):
        self.__id = id
        self.__name = name
        self.__city = city
        self.__participantsNumber = participantsNumber
        self.__maxSpots = maxSpots
        self.__startDate = startDate
        self.__finishDate = finishDate

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_id(self):
        return self.__id

    def get_city(self):
        return self.__city

    def get_participants(self):
        return self.__participantsNumber

    def  get_startdate(self):
        return self.__startDate

    def get_finishdate(self):
        return self.__finishDate

    def get_maxspots(self):
        return self.__maxSpots

    def __str__(self):
        return "Event id: " + str(self.__id) + " Name: " + str(self.__name) + " City: " + str(self.__city) + " Participants: " + str(self.__participantsNumber) + " Max spots: " + str(self.__maxSpots) + " Start date: " + str(self.__startDate) + " Finish date: " + str(self.__finishDate)

    def __eq__(self, other):
        return self.__id == other.__id

