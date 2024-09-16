#Task 2: Define the Event class

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


