class DiskFCFS:
    def __init__(self, initial_position, num_requests):
        self.initial_position = initial_position
        self.num_requests = num_requests
        self.requests = []
        self.total_head_movement = 0

    def process_requests(self):
        current_position = self.initial_position
        for request in self.requests:
            # Calculate the head movement
            self.total_head_movement += abs(request - current_position)

            # Update the current position of the disk arm
            current_position = request

    def display_results(self):
        print("\n===== FCFS Disk Scheduling =====")
        print("Order of Requests Served:")
        print(" -> ".join(map(str, self.requests)))
        print("\nTotal Head Movement:")
        print(f"{self.total_head_movement} tracks")

# Main Execution
if __name__ == "__main__":
    initial_position = int(input("Enter the initial position of the disk arm: "))
    num_requests = int(input("Enter the number of track requests: "))

    disk = DiskFCFS(initial_position, num_requests)

    print("Enter the track requests:")
    disk.requests = [int(input(f"Request {i + 1}: ")) for i in range(num_requests)]

    disk.process_requests()
    disk.display_results()
