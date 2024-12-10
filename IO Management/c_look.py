class DiskArm:
    def __init__(self, initial_position):
        """Initialize the Disk Arm with the initial position."""
        self.position = initial_position
        self.requests = []
        self.movement = 0
        self.movement_details = []  # To store detailed movement calculations

    def add_requests(self, requests):
        """Add I/O requests to the queue."""
        self.requests.extend(requests)

    def process_requests(self):
        """Process the requests using the C-LOOK algorithm."""
        # Sort requests into two groups: those to the right and those to the left of the current position.
        right = [track for track in self.requests if track >= self.position]
        left = [track for track in self.requests if track < self.position]

        # Sort both groups
        right.sort()
        left.sort()

        # Serve requests to the right first, then wrap around to the smallest track on the left.
        order_of_access = right + left

        # Calculate total head movement.
        for track in right:
            movement = abs(self.position - track)
            self.movement += movement
            self.movement_details.append(f"Move from {self.position} → {track}: |{track} - {self.position}| = {movement} units")
            self.position = track

        if left:
            # Wrap to the smallest track on the left.
            movement_to_leftmost = abs(self.position - left[0])
            self.movement += movement_to_leftmost
            self.movement_details.append(
                f"Move from {self.position} → {left[0]} (wrap): |{left[0]} - {self.position}| = {movement_to_leftmost} units"
            )
            self.position = left[0]

            for track in left[1:]:
                movement = abs(self.position - track)
                self.movement += movement
                self.movement_details.append(f"Move from {self.position} → {track}: |{track} - {self.position}| = {movement} units")
                self.position = track

        return order_of_access

if __name__ == "__main__":
    initial_position = int(input("Enter the initial position of the disk arm (in track units): "))

    disk_arm = DiskArm(initial_position)

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
