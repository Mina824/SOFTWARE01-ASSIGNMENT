
def airport_database():
    airports = {}

    while True:
        print("\nChoose an option:")
        print("1. Enter a new airport")
        print("2. Fetch airport information from a existing one")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            icao = input("Enter ICAO code: ")
            name = input("Enter airport name: ")
            airports[icao] = name
            print(f"Airport {name} ({icao}) has been added.")

        elif choice == "2":
            icao = input("Enter ICAO code: ")
            if icao in airports:
                print(f"Airport: {airports[icao]} ({icao})")
            else:
                print("No airport found with that ICAO code.")

        elif choice == "3":
            print("Program quited")
            break




airport_database()


