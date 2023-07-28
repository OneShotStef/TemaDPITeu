from entities.participant import Participant
from repository.repository import Repository
from datetime import datetime


class ParticipantService:

    def __init__(self, repository: Repository):
        self.__repository = repository

    def add_participant(self, id, name, eventsList = []):
        participant = Participant(id, name, eventsList)
        self.__repository.add(participant)

    def participant_exist(self, participant_id):
        return self.__repository.find_position(Participant(participant_id, 0)) is not None

    def delete_participant(self, name):
        participant = Participant(name, None, None)
        self.__repository.delete(participant)

    def get_all_participants(self):
        return self.__repository.get_all()
