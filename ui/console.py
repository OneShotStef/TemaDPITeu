from ui.participant_console import ConsoleUIParticipant
from ui.administrator_console import ConsoleUIAdministrator


class ConsoleUI:

    def __init__(self, event_service, participant_service):
        self.__event_service = event_service
        self.__participant_service = participant_service

    def __print_rol(self):
        print("\nAlegeti rolul\n"
              "Optiuni:\n"
              "1.Administrator/Organizator\n"
              "2.Participant\n"
              "0.Iesiti din program")

    def run(self):
        self.__event_service.delete_event(1)
        self.__participant_service.delete_participant("Andrei")
        while True:
            self.__print_rol()
            try:
                command = int(input("Choose the command:").strip())
                if command == 0:
                    break
                elif command == 1:
                    ui = ConsoleUIAdministrator(self.__event_service, self.__participant_service)
                    ui.run()
                elif command == 2:
                    ui = ConsoleUIParticipant(self.__participant_service, self.__event_service)
                    ui.run()
            except Exception as error:
                print(error)



