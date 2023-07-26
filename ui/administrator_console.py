class ConsoleUIAdministrator:
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
        startDate = input("Data de inceput: ")
        finishDate = input("Data finala: ")

        self.__event_service.add_event(id, name, city, maxSpots, startDate, finishDate)

    def run(self):
        while True:
            self.__print_menu()
            try:
                command = int(input("Choose the command:").strip())
                if command == 0:
                    break
                elif command == 1:
                    print("\naha")
                elif command == 2:
                    print("\non+ho")
            except Exception as error:
                print(error)

