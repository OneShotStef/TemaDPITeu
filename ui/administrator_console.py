from service.event_service import EventService


class ConsoleUIAdministrator:

    def __init__(self, event_service):
        self.__event_service = event_service

    def __print_menu(self):
        print("\nAdministrare aplicatie\n"
              "Optiuni:\n"
              "1.Adaugati un eveniment\n"
              "2.Stergeti un eveniment\n"
              "3.Modificati datele unui eveniment\n"
              "4.Vizualizati evenimentele\n"
              "5.Vizualizati evenimentele dintr-un anumit oras\n"
              "6.Vizualizati participantii de la un anumit eveniment\n"
              "7.Vizualizati evenimentele care au participanti\n"
              "0.Iesiti din modul administrator\n")

    def __add_event(self):
        print("Introduceti informatiile despre eveniment:")
        id = input("ID: ")
        name = input("Nume: ")
        city = input("Oras: ")
        maxSpots = int(input("Numar maxim de locuri: "))
        participantsNumber = int(input("Numarul participantilor: "))
        startDate = input("Data de inceput: ")
        finishDate = input("Data finala: ")

        self.__event_service.add_event(id, name, city, participantsNumber, maxSpots, startDate, finishDate)

    def __delete_event(self):
        id = input("Event id: ")
        self.__event_service.delete_event(id)

    def __show_all_events(self):
        for event in self.__event_service.get_all_events():
            print(event)

    def __show_events_with_participants(self):
        for event in self.__event_service.get_all_events()

    def run(self):
        while True:
            self.__print_menu()
            try:
                command = int(input("Choose the command:").strip())
                if command == 0:
                    break
                elif command == 1:
                    self.__add_event()
                elif command == 2:
                    self.__delete_event()
                elif command == 3:
                    print("something")
                elif command == 4:
                    self.__show_all_events()
                elif command == 5:
                    print("udk")
                elif command == 6:
                    print("idk")
                elif command == 7:
                    self.__show_events_with_participants()
            except Exception as error:
                print(error)

