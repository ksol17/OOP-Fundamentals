#1. Vehicle Registration System

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

# Method to update the owner
    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated to {self.owner}")

# Create instances of Vehicle
vehicle1 = Vehicle("ABC123", "Car", "John Smith")
vehicle2 = Vehicle("XYZ789", "Motorbike", "Jane Doe")

# Print initial owners
print(f"Vehicle 1: Registration: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2: Registration: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

# Update owners
vehicle1.update_owner("Alice Johnson")
vehicle2.update_owner("Bob Brown")

# Print updated owners
print(f"Vehicle 1: Registration: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2: Registration: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

# Task 2: Define the Event class
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  

    # Method to add a participant
    def add_participant(self):
        self.participant_count += 1
        print(f"Participant added. Current count: {self.participant_count}")

    # Method to retrieve the current participant count
    def get_participant_count(self):
        return self.participant_count

# Create an instance of Event
event1 = Event("Tech Conference", "2024-10-15")

# Print initial participant count
print(f"Event: {event1.name} on {event1.date}")
print(f"Initial participant count: {event1.get_participant_count()}")

# Add participants
event1.add_participant()  # Add 1 participant
event1.add_participant()  # Add 1 more participant

# Print the updated participant count
print(f"Updated participant count: {event1.get_participant_count()}")

