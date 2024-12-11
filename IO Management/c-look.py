class RequestNode:
    def __init__(self, request):
        self.request = request
        self.next = None

class DiskCLOOK:
    def __init__(self, initial_position, track_size):
        self.initial_position = initial_position
        self.track_size = track_size
        self.total_head_movement = 0
        self.requests = None

    def process_requests(self, requests):
        low = None
        high = None

        # Split requests into low and high lists
        for req in requests:
            node = RequestNode(req)
            if req < self.initial_position:
                low = self._insert_sorted(low, node)
            else:
                high = self._insert_sorted(high, node)

        # Calculate total head movement
        current_position = self.initial_position
        high_movement = self._calculate_movement(high, current_position)
        low_movement = self._calculate_movement(low, low.request if low else 0)

        self.total_head_movement = high_movement + low_movement

        # Concatenate high and low requests
        self.requests = high
        if high:
            tail = self._get_tail(high)
            tail.next = low

    def _insert_sorted(self, head, node):
        if not head or node.request < head.request:
            node.next = head
            return node

        current = head
        while current.next and current.next.request < node.request:
            current = current.next
        node.next = current.next
        current.next = node
        return head

    def _calculate_movement(self, head, start_position):
        current_position = start_position
        total_movement = 0
        current = head
        while current:
            total_movement += abs(current.request - current_position)
            current_position = current.request
            current = current.next
        return total_movement

    def _get_tail(self, head):
        while head and head.next:
            head = head.next
        return head

    def display_results(self):
        print("\n===== C-LOOK Disk Scheduling =====")
        print("Order of Requests Served:")
        current = self.requests
        requests_order = []
        while current:
            requests_order.append(current.request)
            current = current.next
        print(" -> ".join(map(str, requests_order)))
        print("\nTotal Head Movement:")
        print(f"{self.total_head_movement} tracks")

# Main Execution
if __name__ == "__main__":
    track_size = int(input("Enter the track size on the disk: "))
    initial_position = int(input("Enter the initial position of the disk arm: "))

    disk = DiskCLOOK(initial_position, track_size)

    num_requests = int(input("Enter the number of track requests: "))
    requests = [int(input(f"Enter request {i + 1}: ")) for i in range(num_requests)]

    disk.process_requests(requests)
    disk.display_results()
