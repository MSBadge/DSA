# # ₹ implement stack using doubly linked list
# class Node:
#     """Node class for doubly linked list"""
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None


# class Stack:
#     """Stack implementation using doubly linked list"""
#     def __init__(self):
#         self.top = None
#         self.size = 0
    
#     def push(self, data):
#         """Add an element to the top of the stack"""
#         new_node = Node(data)
        
#         if self.is_empty():
#             self.top = new_node
#         else:
#             new_node.prev = self.top
#             self.top.next = new_node
#             self.top = new_node
        
#         self.size += 1
#         return True
    
#     def pop(self):
#         """Remove and return the top element from the stack"""
#         if self.is_empty():
#             raise IndexError("Pop from empty stack")
        
#         popped_data = self.top.data
        
#         if self.top.prev:
#             self.top = self.top.prev
#             self.top.next = None
#         else:
#             self.top = None
        
#         self.size -= 1
#         return popped_data
    
#     def peek(self):
#         """Return the top element without removing it"""
#         if self.is_empty():
#             raise IndexError("Peek from empty stack")
#         return self.top.data
    
#     def is_empty(self):
#         """Check if the stack is empty"""
#         return self.top is None
    
#     def get_size(self):
#         """Return the number of elements in the stack"""
#         return self.size
    
#     def clear(self):
#         """Remove all elements from the stack"""
#         self.top = None
#         self.size = 0
    
#     def __str__(self):
#         """Return string representation of the stack (from bottom to top)"""
#         if self.is_empty():
#             return "Stack: Empty"
        
#         # Traverse from bottom to top
#         current = self._get_bottom()
#         elements = []
        
#         while current:
#             elements.append(str(current.data))
#             current = current.next
        
#         return f"Stack: {' -> '.join(elements)} (Top)"
    
#     def _get_bottom(self):
#         """Helper method to get the bottom node"""
#         if self.is_empty():
#             return None
        
#         current = self.top
#         while current.prev:
#             current = current.prev
        
#         return current
    
#     def display_reverse(self):
#         """Display stack from top to bottom"""
#         if self.is_empty():
#             return "Stack: Empty"
        
#         elements = []
#         current = self.top
        
#         while current:
#             elements.append(str(current.data))
#             current = current.prev
        
#         return f"Stack (Top to Bottom): {' -> '.join(elements)}"


# # Create a stack
# stack = Stack()

# # Test operations
# print("Pushing elements:")
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print(stack)  # Output: Stack: 10 -> 20 -> 30 (Top)

# print(f"\nTop element: {stack.peek()}")  # Output: 30

# print(f"\nStack size: {stack.get_size()}")  # Output: 3

# print("\nPopping elements:")
# print(f"Popped: {stack.pop()}")  # Output: 30
# print(stack)  # Output: Stack: 10 -> 20 (Top)

# print(f"\nIs empty? {stack.is_empty()}")  # Output: False

# print("\nDisplay reverse (top to bottom):")
# print(stack.display_reverse())  # Output: Stack (Top to Bottom): 20 -> 10

# stack.push(40)
# stack.push(50)
# print(f"\nAfter pushing more elements:")
# print(stack)  # Output: Stack: 10 -> 20 -> 40 -> 50 (Top)

# print(f"\nClearing stack...")
# stack.clear()
# print(f"Is empty? {stack.is_empty()}")  # Output: True
# print(stack)  # Output: Stack: Empty

















# implement queue using DDL
class Node:
    """Node class for doubly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    """Queue implementation using doubly linked list"""
    def __init__(self):
        self.front = None  # Points to the front of the queue (for removal)
        self.rear = None   # Points to the rear of the queue (for insertion)
        self.size = 0
    
    def enqueue(self, data):
        """Add an element to the rear of the queue"""
        new_node = Node(data)
        
        if self.is_empty():
            # If queue is empty, both front and rear point to the new node
            self.front = new_node
            self.rear = new_node
        else:
            # Add new node at the rear
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
        return True
    
    def dequeue(self):
        """Remove and return an element from the front of the queue"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        
        dequeued_data = self.front.data
        
        if self.front == self.rear:
            # Only one element in the queue
            self.front = None
            self.rear = None
        else:
            # Move front to the next node
            self.front = self.front.next
            self.front.prev = None
        
        self.size -= 1
        return dequeued_data
    
    def peek_front(self):
        """Return the front element without removing it"""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.data
    
    def peek_rear(self):
        """Return the rear element without removing it"""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.rear.data
    
    def is_empty(self):
        """Check if the queue is empty"""
        return self.front is None
    
    def get_size(self):
        """Return the number of elements in the queue"""
        return self.size
    
    def clear(self):
        """Remove all elements from the queue"""
        self.front = None
        self.rear = None
        self.size = 0
    
    def __str__(self):
        """Return string representation of the queue (from front to rear)"""
        if self.is_empty():
            return "Queue: Empty"
        
        elements = []
        current = self.front
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        return f"Queue: {' -> '.join(elements)} (Front -> Rear)"
    
    def display_reverse(self):
        """Display queue from rear to front"""
        if self.is_empty():
            return "Queue: Empty"
        
        elements = []
        current = self.rear
        
        while current:
            elements.append(str(current.data))
            current = current.prev
        
        return f"Queue (Rear -> Front): {' -> '.join(elements)}"
    
    def contains(self, data):
        """Check if the queue contains a specific element"""
        current = self.front
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def to_list(self):
        """Convert queue to Python list (front to rear)"""
        result = []
        current = self.front
        while current:
            result.append(current.data)
            current = current.next
        return result



# Create a queue
queue = Queue()

# Test enqueue operations
print("Enqueue elements:")
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
print(queue)  # Output: Queue: 10 -> 20 -> 30 -> 40 -> 50 (Front -> Rear)

# Test queue properties
print(f"\nFront element: {queue.peek_front()}")  # Output: 10
print(f"Rear element: {queue.peek_rear()}")      # Output: 50
print(f"Queue size: {queue.get_size()}")         # Output: 5

# Test dequeue operations
print("\nDequeue elements:")
print(f"Dequeued: {queue.dequeue()}")  # Output: 10
print(f"Dequeued: {queue.dequeue()}")  # Output: 20
print(queue)  # Output: Queue: 30 -> 40 -> 50 (Front -> Rear)

# Test remaining properties
print(f"\nFront element: {queue.peek_front()}")  # Output: 30
print(f"Queue size: {queue.get_size()}")         # Output: 3

# Test contains method
print(f"\nContains 40? {queue.contains(40)}")    # Output: True
print(f"Contains 99? {queue.contains(99)}")      # Output: False

# Test reverse display
print("\nDisplay reverse (rear to front):")
print(queue.display_reverse())  # Output: Queue (Rear -> Front): 50 -> 40 -> 30

# Test more enqueue operations
print("\nEnqueue more elements:")
queue.enqueue(60)
queue.enqueue(70)
print(queue)  # Output: Queue: 30 -> 40 -> 50 -> 60 -> 70 (Front -> Rear)
print(f"Queue size: {queue.get_size()}")  # Output: 5

# Test to_list method
print(f"\nQueue as list: {queue.to_list()}")  # Output: [30, 40, 50, 60, 70]

# Test is_empty
print(f"\nIs empty? {queue.is_empty()}")  # Output: False

# Test clear
print("\nClearing queue...")
queue.clear()
print(f"Is empty? {queue.is_empty()}")  # Output: True
print(f"Queue size: {queue.get_size()}")  # Output: 0
print(queue)  # Output: Queue: Empty

# Test edge cases
print("\nTesting edge cases:")
queue.enqueue(100)
queue.enqueue(200)
print(queue)  # Output: Queue: 100 -> 200 (Front -> Rear)
print(f"Dequeued: {queue.dequeue()}")  # Output: 100
print(f"Dequeued: {queue.dequeue()}")  # Output: 200
print(f"Is empty? {queue.is_empty()}")  # Output: True

# Test error handling for empty queue
try:
    queue.dequeue()
except IndexError as e:
    print(f"\nError when dequeuing from empty queue: {e}")

try:
    queue.peek_front()
except IndexError as e:
    print(f"Error when peeking from empty queue: {e}")