class DiskArm:
    def __init__(self, initial_position, total_tracks):
        """Initialize the Disk Arm with the initial position and the total number of tracks."""
        self.position = initial_position
        self.total_tracks = total_tracks
        self.requests = []
        self.movement = 0
        self.movement_details = []  # To store detailed movement calculations

    def add_requests(self, requests):
        """Add I/O requests to the queue."""
        self.requests.extend(requests)

    def process_requests(self):
        """Process the requests using the C-SCAN algorithm."""
        # Sort requests into two groups: those to the right and those to the left of the current position.
        right = [track for track in self.requests if track >= self.position]
        left = [track for track in self.requests if track < self.position]

        # Sort both groups
        right.sort()
        left.sort()

        # Serve requests to the right first, then wrap around to the beginning.
        order_of_access = right + left

        # Calculate total head movement.
        for track in right:
            movement = abs(self.position - track)
            self.movement += movement
            self.movement_details.append(f"Move from {self.position} → {track}: |{track} - {self.position}| = {movement} units")
            self.position = track

        if left:
            # Move to the end of the disk and wrap around to the beginning.
            movement_to_end = abs(self.position - (self.total_tracks - 1))
            self.movement += movement_to_end
            self.movement_details.append(
                f"Move from {self.position} → {self.total_tracks - 1} (end): |{self.total_tracks - 1} - {self.position}| = {movement_to_end} units"
            )
            self.position = 0  # Wrap to the start.
            self.movement_details.append(f"Wrap to track 0: No movement added")

            for track in left:
                movement = abs(self.position - track)
                self.movement += movement
                self.movement_details.append(f"Move from {self.position} → {track}: |{track} - {self.position}| = {movement} units")
                self.position = track

        return order_of_access

if __name__ == "__main__":
    total_tracks = int(input("Enter the total number of tracks on the disk (in units): "))
    initial_position = int(input("Enter the initial position of the disk arm (in track units): "))

    disk_arm = DiskArm(initial_position, total_tracks)

    # Input requests.
    requests = list(map(int, input("Enter the sequence of track requests (in track units, comma-separated): ").split(',')))
    disk_arm.add_requests(requests)

    # Process the requests.
    order = disk_arm.process_requests()

    print("\nOrder of track access (in track units):", order)
    print("Detailed head movement calculations:")
    for detail in disk_arm.movement_details:
        print(detail)
    print(f"Total head movement (in track units): {disk_arm.movement} units")
