from parking import ParkingSystem

def menu():
    print("\n--- Smart Parking System ---")
    print("1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Show Status")
    print("4. Exit")

parking = ParkingSystem(5)

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        vehicle = input("Enter vehicle number: ")
        parking.park_vehicle(vehicle)

    elif choice == '2':
        vehicle = input("Enter vehicle number to remove: ")
        parking.remove_vehicle(vehicle)

    elif choice == '3':
        parking.get_status()

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice!")