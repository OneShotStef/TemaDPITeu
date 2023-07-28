class Participant:
    def __init__(self, name, photoLink, eventsSigned = 0):
        self.__name = name
        self.__photoLink = photoLink
        self.__eventsSigned = eventsSigned

    def get_name(self):
        return self.__name

    def get_photoLink(self):
        return self.__photoLink

    def get_eventsSigned(self):
        return self.__eventsSigned

    def set_name(self, newName):
        self.__name = newName

    def set_photoLink(self, newPhotoLink):
        self.__photoLink = newPhotoLink

    def add_one_event(self):
        self.__eventsSigned += 1

    def __str__(self):
        return "Name: {0}, Photo Link: {1}, Events Signed: {2}".format(self.__name, self.__photoLink, self.__eventsSigned)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.get_name() == other.get_name()
