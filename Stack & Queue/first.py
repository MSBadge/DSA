# # inplement stack using array / list
# class MyStack:
#     def __init__(self):
#         # Create an empty list to represent the stack
#         self.arr = []
    
#     # Function to push an integer into the stack.
#     def push(self, data):
#         # Add (append) data to the end of the list
#         self.arr.append(data)
    
#     # Function to remove an item from top of the stack.
#     def pop(self):
#         # Check if the stack is empty
#         if not self.arr:
#             return -1  # If empty, return -1
#         return self.arr.pop()  # Remove and return the last element
    
#     def top(self):
#         return self.arr[-1]

#     def size(self):
#         return len(self.arr)
    
# stack = MyStack()
# stack.push(2)
# stack.push(3)
# stack.push(5)

# print(stack.top())
# print(stack.size())

# print(stack.pop())  # Output? 5
# print(stack.pop())  # Output? 3
# print(stack.pop())  # Output? 2
# print(stack.pop())  # Output? -1 (since stack is now empty)







# # implements queue using array / list
# class MyQueue:
#     def __init__(self):
#         self.arr = []  # Empty list for queue
    
#     # Function to push an element x in a queue.
#     def enqueur(self, x):
#         self.arr.append(x)  # Add to end (rear)
    
#     # Function to pop an element from queue and return that element.
#     def dequeur(self):
#         if len(self.arr) == 0:
#             return -1  # Queue empty
#         e = self.arr.pop(0)  # Remove from start (front)
#         return e
    
#     def front(self):
#         if not self.arr:
#             return f"queue is empty"
#         return self.arr[0]
    
#     def rear(self):
#         if not self.arr:
#             return f"queue is empty"
#         return self.arr[-1]

#     def size(self):
#         return len(self.arr)
    

# queue = MyQueue()
# queue.enqueur(3)
# queue.enqueur(5)
# queue.enqueur(2)
# queue.enqueur(9)
# print(queue.arr)
# print(queue.front())
# print(queue.rear())
# print("-------------")
# print(queue.dequeur())
# print(queue.dequeur())
# print(queue.dequeur())
# print(queue.dequeur())
# print("-------------")
# print(queue.arr)
# print(queue.front())
# print(queue.rear())






# # introduction to deque class (Double Ended Queue) it use doubly linked list
# from collections import deque

# queue = deque([])

# queue.append(2)
# queue.append(7)
# queue.append(5)
# print(queue)
# queue.appendleft(1)
# print(queue)
# queue.pop()
# queue.popleft()
# print(queue)









# # impliment stack using queue
# from collections import deque
# class Mystack:
#     def __init__(self):
#         self.arr = deque()

#     def push(self, data):
#         self.arr.append(data)
#         for _ in range(len(self.arr)-1):
#             self.arr.append(self.arr.popleft())

#     def pop(self):
#         if not self.arr:
#             return f"stack is empty"
#         return self.arr.popleft()

# stack = Mystack()
# stack.push(2)
# stack.push(9)
# stack.push(7)
# stack.pop()
# stack.pop()
# print(stack.pop())
# print(stack.pop())
# print(stack.arr)










# # implement queue using stack
# class QueueUsingStacks:
#     def __init__(self):
#         self.stack1 = []  # Main stack that always maintains queue order
#         self.stack2 = []  # Temporary stack
    
#     def enqueue(self, item):
#         """Add item to the queue - O(n) operation"""
#         # Move all elements from stack1 to stack2
#         while self.stack1:
#             self.stack2.append(self.stack1.pop())
        
#         # Push new item to stack1
#         self.stack1.append(item)
#         print(f"Enqueued: {item}")
        
#         # Move all elements back from stack2 to stack1
#         while self.stack2:
#             self.stack1.append(self.stack2.pop())
    
#     def dequeue(self):
#         """Remove and return front item - O(1) operation"""
#         if self.is_empty():
#             print("Queue is empty")
#             return None
        
#         item = self.stack1.pop()
#         print(f"Dequeued: {item}")
#         return item
    
#     def peek(self):
#         """Get front item without removing it"""
#         if self.is_empty():
#             return None
#         return self.stack1[-1]
    
#     def is_empty(self):
#         """Check if queue is empty"""
#         return not self.stack1
    
#     def size(self):
#         """Get number of elements in queue"""
#         return len(self.stack1)
    


# queue = QueueUsingStacks()
# queue. enqueue(5)
# queue. enqueue(5)
# queue. enqueue(5)
# queue. enqueue(7)
# queue. enqueue(9)
# print(queue.stack1)
# print(queue.stack2)











