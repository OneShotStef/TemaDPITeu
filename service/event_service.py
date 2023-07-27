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

    def get_all_events(self):
        return self.__repository.get_all()

    def get_events_with_participants(self):
        nou_list = []
        event_list = self.__repository.get_all()
        for event in event_list:
            if event.get_participants() > 0:
                nou_list.append(event)
        return nou_list




