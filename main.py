from service.event_service import EventService
from ui.console import ConsoleUI
from repository.repository import Repository
from entities.event import Event
from service.participant_service import ParticipantService
from entities.participant import Participant
from ui.administrator_console import ConsoleUIAdministrator
from ui.participant_console import ConsoleUIParticipant

from datetime import datetime


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


"""def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""
event = Event(1, "Concert", "Bucuresti", 0, 100, "2021-05-01", "2021-05-02")
repo = Repository([event])
eventService = EventService(repo)
participant = Participant("Andrei", None, 0)
repo = Repository([participant])
participantService = ParticipantService(repo)
ui = ConsoleUI(eventService, participantService)
ui.run()
