class VacuumCleaner:
    def __init__(self, environment):
        """
        Initializes the vacuum cleaner with a given environment.
        environment: A dictionary where keys are room names ('A', 'B', etc.)
                     and values are 'dirty' or 'clean'.
        """
        self.environment = environment
        self.location = 'A'  # Starting location of the vacuum cleaner

    def sense(self):
        """Sense the status of the current room."""
        return self.environment[self.location]

    def clean(self):
        """Clean the current room."""
        print(f"Cleaning room {self.location}...")
        self.environment[self.location] = 'clean'

    def move(self, next_location):
        """Move to the specified room."""
        print(f"Moving from {self.location} to {next_location}.")
        self.location = next_location

    def run(self):
        """Run the vacuum cleaner agent until all rooms are clean."""
        print("Starting cleaning process...")
        while 'dirty' in self.environment.values():
            if self.sense() == 'dirty':
                self.clean()
            else:
                print(f"Room {self.location} is already clean.")

            # Determine next room to move to (simple left-right traversal)
            rooms = list(self.environment.keys())
            current_index = rooms.index(self.location)
            next_index = (current_index + 1) % len(rooms)
            self.move(rooms[next_index])

        print("All rooms are clean!")

# Example usage:
if __name__ == "__main__":
    # Define the environment
    environment = {
        'A': 'dirty',
        'B': 'clean',
        'C': 'dirty'
    }

    # Initialize and run the vacuum cleaner
    vacuum = VacuumCleaner(environment)
    vacuum.run()
