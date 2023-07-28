class Event:
    def __init__(self, id, name, city, participantsNumber, maxSpots, startDate, finishDate, participantsList = []):
        self.__id = id
        self.__name = name
        self.__city = city
        self.__participantsNumber = participantsNumber
        self.__maxSpots = maxSpots
        self.__startDate = startDate
        self.__finishDate = finishDate
        self.__participantsList = participantsList

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

    def set_participants(self, new_participants):
        self.__participantsNumber = new_participants

    def get_start_date(self):
        return self.__startDate

    def get_finish_date(self):
        return self.__finishDate

    def get_max_spots(self):
        return self.__maxSpots

    def get_participants_list(self):
        return self.__participantsList

    def add_participant_in_event(self, participant):
        if self.__participantsNumber >= self.__maxSpots:
            print("Not enough spots")
        else:
            self.__participantsList.append(participant)
            self.__participantsNumber += 1

    def __str__(self):
        return "Event id: " + str(self.__id) + "\nName: " + str(self.__name) + "\nCity: " + str(self.__city) + " Participants: " + str(self.__participantsNumber) + " Max spots: " + str(self.__maxSpots) + " Start date: " + str(self.__startDate) + " Finish date: " + str(self.__finishDate)

    def __eq__(self, other):
        return self.__id == other.__id

