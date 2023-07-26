from ui.participant_console import ConsoleUIParticipant
from ui.administrator_console import ConsoleUIAdministrator


class ConsoleUI:
    def __print_rol(self):
        print("\nAlegeti rolul\n"
              "Optiuni:\n"
              "0.Administrator/Organizator\n"
              "1.Participant\n"
              "2.Iesiti din program")

    def run(self):
        while True:
            self.__print_rol()
            try:
                command = int(input("Choose the command:").strip())
                if command == 0:
                    ui = ConsoleUIAdministrator()
                    ui.run()
                elif command == 1:
                    ui = ConsoleUIParticipant()
                    ui.run()
                elif command == 2:
                    break
            except Exception as error:
                print(error)



