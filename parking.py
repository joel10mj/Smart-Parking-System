class ParkingSystem:

    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.slots = {}

    def park_vehicle(self, vehicle_number, vehicle_type):

        if len(self.slots) < self.total_slots:

            slot_number = len(self.slots) + 1

            self.slots[slot_number] = {
                "number": vehicle_number,
                "type": vehicle_type
            }

            return f"{vehicle_type} {vehicle_number} parked at slot {slot_number}"

        else:
            return "Parking Full!"



    def remove_vehicle(self, vehicle_number):

        for slot, vehicle in list(self.slots.items()):

            if vehicle["number"] == vehicle_number:

                del self.slots[slot]

                return f"Vehicle {vehicle_number} removed from slot {slot}"

        return "Vehicle not found!"



    def get_status(self):
        return self.slots