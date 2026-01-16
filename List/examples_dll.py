# # Reverse a Doubly Linked List
# # class Node:
# #     def __init__(self, val):
# #         self.data = val
# #         self.next = None
# #         self.prev = None

# class Solution:
#     def reverse(self, head):
#         current = head
#         prev = None
        
#         if current.next is Node:
#             return current
            
#         while current:
#             front = current.next
#             current.next = prev
#             current.prev = front
#             prev = current
#             current = front
#         return prev








# #  Delete All Occurrences of a Key in Doubly Linked List 
# '''
# # Node Class
# 	class Node:
# 	    def __init__(self, data):   # data -> value stored in node
# 	        self.data = data
# 	        self.next = None
# 	        self.prev = None
# '''
# class Solution:
#     #Function to delete all the occurances of a key from the linked list.
#     def deleteAllOccurOfX(self, head, x):
#         # Handle empty list
#         if not head:
#             return None
        
#         current = head
#         new_head = head
        
#         while current:
#             if current.data == x:
#                 # Store reference to current node
#                 node_to_delete = current
                
#                 # If current is the head node
#                 if current == new_head:
#                     new_head = current.next
#                     if new_head:
#                         new_head.prev = None
                
#                 else:
#                     # Update previous node's next pointer
#                     if current.prev:
#                         current.prev.next = current.next
                    
#                     # Update next node's previous pointer
#                     if current.next:
#                         current.next.prev = current.prev
                
#                 # Move current to next node BEFORE deleting
#                 current = current.next
                
#                 # Clean up the deleted node
#                 del node_to_delete
                
#             else:
#                 # Only update previous when not deleting
#                 current = current.next
        
#         return new_head









# # Find pairs with given sum in doubly linked list
# # Node Class
# 	# class Node:
# 	#     def __init__(self, data):   # data -> value stored in node
# 	#         self.data = data
# 	#         self.next = None
# 	#         self.prev = None

# class Solution:
#     def findPairsWithGivenSum(self, target, head):

#         result = []
        
#         if not head or not head.next:
#             return result
        
#         # Initialize two pointers
#         left = head
#         right = head
        
#         # Move right pointer to the end of the list
#         while right.next:
#             right = right.next
        
#         # Find pairs using two-pointer technique
#         while left and right and left != right and left.prev != right:
#             current_sum = left.data + right.data
            
#             if current_sum == target:
#                 result.append((left.data, right.data))
#                 left = left.next
#                 right = right.prev
            
#             elif current_sum < target:
#                 left = left.next
            
#             else:  # current_sum > target
#                 right = right.prev
        
#         return result







# # Remove duplicates from a sorted doubly linked list
# # class Node:
# #     def __init__(self, data):   # data -> value stored in node
# #         self.data = data
# #         self.next = None
# #         self.prev = None
# class Solution:
#     #Function to remove duplicates from unsorted linked list.
#     def removeDuplicates(self, head):
        
#         if not head or not head.next:
#             return head
            
#         current = head
        
#         while current and current.next:
#             if current.data == current.next.data:
#                 duplicate = current.next
                
#                 current.next = duplicate.next
                
#                 if duplicate.next:
#                     duplicate.next.prev = current
                    
#                 del duplicate
                
#             else:
#                 current = current.next
#         return head