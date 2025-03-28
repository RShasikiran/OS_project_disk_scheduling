import matplotlib.pyplot as plt

# FCFS Algorithm
def fcfs(requests, head):
    total_seek = 0
    order = []
    current = head
    for request in requests:
        total_seek += abs(request - current)
        order.append(request)
        current = request
    return order, total_seek

# SSTF Algorithm
def sstf(requests, head):
    total_seek = 0
    order = []
    current = head
    requests_copy = requests.copy()  # Create a copy of the requests list
    while requests_copy:
        closest = min(requests_copy, key=lambda x: abs(x - current))
        total_seek += abs(closest - current)
        order.append(closest)
        current = closest
        requests_copy.remove(closest)  # Remove from the copy, not the original list
    return order, total_seek

# SCAN Algorithm
def scan(requests, head, direction="right", max_cylinder=199):
    total_seek = 0
    order = []
    current = head
    requests_sorted = sorted(requests)
    if direction == "right":
        for request in requests_sorted:
            if request >= current:
                total_seek += abs(request - current)
                order.append(request)
                current = request
        total_seek += abs(max_cylinder - current)
        current = max_cylinder
        for request in reversed(requests_sorted):
            if request < head:
                total_seek += abs(request - current)
                order.append(request)
                current = request
    else:
        # Implement for left direction
        pass
    return order, total_seek

# C-SCAN Algorithm
def cscan(requests, head, direction="right", max_cylinder=199):
    total_seek = 0
    order = []
    current = head
    requests_sorted = sorted(requests)
    if direction == "right":
        for request in requests_sorted:
            if request >= current:
                total_seek += abs(request - current)
                order.append(request)
                current = request
        total_seek += abs(max_cylinder - current)
        current = 0
        for request in requests_sorted:
            if request < head:
                total_seek += abs(request - current)
                order.append(request)
                current = request
    else:
        # Implement for left direction
        pass
    return order, total_seek

# Visualization Function
def plot_movement(order, head):
    x = list(range(len(order)))
    y = order
    plt.plot(x, y, marker='o')
    plt.title("Disk Head Movement")
    plt.xlabel("Request Order")
    plt.ylabel("Cylinder Number")
    plt.show()

# Main Program
def main():
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    head = 53
    print("Select Algorithm:")
    print("1. FCFS")
    print("2. SSTF")
    print("3. SCAN")
    print("4. C-SCAN")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        order, total_seek = fcfs(requests, head)
    elif choice == 2:
        order, total_seek = sstf(requests, head)
    elif choice == 3:
        direction = input("Enter direction (left/right): ")
        order, total_seek = scan(requests, head, direction)
    elif choice == 4:
        direction = input("Enter direction (left/right): ")
        order, total_seek = cscan(requests, head, direction)
    
    print("Order of processing:", order)
    print("Total seek time:", total_seek)
    print("Average seek time:", total_seek / len(requests))
    plot_movement(order, head)

# Entry Point
if __name__ == "__main__":
    main()