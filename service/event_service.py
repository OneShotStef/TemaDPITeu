from entities.event import Event
from repository.repository import Repository


class EventService:
    def __init__(self, repository: Repository):
        self.__repository = repository

    def add_event(self, id, name, city, participantsNumber, maxSpots, startDate, finishDate):
        event = Event(id, name, city, participantsNumber, maxSpots, startDate, finishDate)
        self.__repository.add(event)

    def event_exist(self, event_id):
        return self.__repository.find_position(Event(event_id, 0, 0, 0, 0, 0, 0)) is not None

    def delete_event(self, id):
        event = Event(id, 0, 0, 0, 0, 0, 0)
        self.__repository.delete(event)

    def get_all_animals(self):
        return self.__repository.get_all()
