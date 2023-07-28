from service.event_service import EventService
from entities.participant import Participant
from administrator_console import ConsoleUIAdministrator


class ConsoleUIParticipant:

    def __init__(self, participant_service):
        self.__participant_service = participant_service

    def __print_menu(self):
        print("\nParticipant choose\n"
              "Optiuni:\n"
              "0.Iesiti din modul participant\n"
              "1.Vizualizati toate evenimentele\n"
              "2.Inscrieti-va la un eveniment\n"
              "3.Vizualizati evenimentele in urmatoarele 7 zile\n"
              "4.Vizualizati evenimentele dintr-o anumita luna\n")

    def __show_all_events(self):
        for event in self.__event_service.get_all_events():
            print(event)

    def __show_events_in_next_7days(self):
        for event in self.__event_service.get_events_in_next_7days():
            print(event)

    def __show_events_in_month(self):
        month = input("Introduceti numarul lunii (1-12): ")
        for event in self.__event_service.get_events_in_next_month(month):
            print(event)

    def __register_event(self):
        event_id = input("Introduceti ID-ul evenimentului: ")
        name = input("Nume participant: ")
        photo_link = input("Link poza participant: ")
        participant = Participant(name, photo_link, [])

        self.__event_service.register_event(event_id, participant)

    def run(self):
        while True:
            self.__print_menu()
            try:
                command = int(input("Choose the command:").strip())
                if command == 0:
                    break
                elif command == 1:
                    self.__show_all_events()
                elif command == 2:
                    self.__register_event()
                elif command == 3:
                    self.__show_events_in_next_7days()
                elif command == 4:
                    self.__show_events_in_month()
            except Exception as error:
                print(error)