class ConsoleUIParticipant:
    def __print_menu(self):
        print("\nParticipant choose\n"
              "Optiuni:\n"
              "0.Idk\n"
              "1.idk")
    def run(self):
        while True:
            self.__print_menu()
            try:
                command = int(input("Choose the command:").strip())
                if command == 0:
                    print("\noho")
                elif command == 1:
                    print("\naha")
                elif command == 2:
                    break
            except Exception as error:
                print(error)