# # middele of linkedList (TortoiseHase Method)
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def append(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             currunt = self.head
#             while currunt.next is not None:
#                 currunt = currunt.next
#             currunt.next = new_node
    
#     def traverse(self):
#         if self.head is None:
#             print("Empty List")
#         else:
#             current = self.head
#             while current is not None:
#                 print(current.data, end=" ")
#                 current = current.next
#             print()


#     def middele(self):
#         slow = fast = self.head

#         while fast and fast.next is not None:
#             slow = slow.next
#             fast = fast.next.next
#         return slow.data


# a = [1,2,3,4,5]
# sll = LinkedList()
# for i in range(len(a)):
#     sll.append(a[i])
# sll.traverse()
# print(sll.middele())















# # Reverse a Linked list
# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None

# class SingliLinkedList:
#     def __init__(self):
#         self.head = None

#     def reverse(self,nums):
#         # add Node
#         n = len(nums)
#         for i in range(n):
#             new_node = Node(nums[i])
#             if not self.head:
#                 self.head = new_node
#             else:
#                 current = self.head
#                 while current.next is not None:
#                     current = current.next
#                 current.next = new_node
                
#         # reverse list
#         current = self.head
#         prev = None
#         while current is not None:
#             front = current.next
#             current.next = prev
#             prev = current
#             current = front

#         # Print List
#         current = prev
#         while current:
#              print(current.val, end=" ")
#              current = current.next
#         print()

# a = [1,2,3,4,5,6,7,8,9]
# sll = SingliLinkedList()

# sll.reverse(a)









# # Linked List cycle 1
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def __init__(self):
#         self.head = None

#     def hasCycle(self, head, pos):
        
#         #add Node
#         n = len(head)
#         for i in range(n):
#             new_node = ListNode(head[i])
#             if not self.head:
#                 self.head = new_node
#             else:
#                 current = self.head
#                 while current.next is not None:
#                     current = current.next
#                 current.next = new_node

#         if pos >= 0:
#             current = self.head
#             while current.next is not None:
#                 current = current.next
#             current.next = ListNode(head[pos])

#         slow = self.head
#         fast = self.head
        
#         while fast and fast.next:
#             print(slow, slow.val)
#             print(fast, fast.val)
#             slow = slow.next          
#             fast = fast.next.next
            
#             if slow == fast:
#                 return True
        
#         return False
    
#     def traverse(self):
#             current = self.head
#             while current:
#                 print(current.val, end=" ")
#                 current = current.next
    
# head = [3,2,0,-4,2]
# pos = 2
# sll = Solution()
# print(sll.hasCycle(head,pos))
# sll.traverse()













# # Linked List Cycle 2
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         # Step 1: Find if there's a cycle using Floyd's algorithm
#         slow = head
#         fast = head
        
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
            
#             # Cycle detected
#             if slow == fast:
#                 # Step 2: Find the starting node of the cycle
#                 # Reset slow to head, keep fast at meeting point
#                 slow = head
                
#                 # Move both one step at a time
#                 while slow != fast:
#                     slow = slow.next
#                     fast = fast.next
                
#                 # They meet at the start of the cycle
#                 return slow
        
#         # No cycle found
#         return None











# # Lingth of loop in LL
# # class Node:
# #     def __init__(self, data): 
# #         self.data = data
# #         self.next = None

# class Solution:
#     def lengthOfLoop(self, head):
#         slow = fast = head
#         count = 0
        
#         while fast and fast.next:
#             slow = slow.next 
#             fast = fast.next.next
            
#             if slow == fast:
#                 slow = slow.next
#                 count+=1
                
#                 while slow != fast:
#                     slow = slow.next
#                     count+=1
#                 return count

#         return count










# # 328. Odd Even Linked List
# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):
#     def oddEvenList(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         if not head or not head.next:
#             return head
#         odd = head
#         even = head.next
#         even_head = even
#         while even and even.next is not None:
#             odd.next = odd.next.next
#             odd = odd.next
#             even.next = even.next.next
#             even = even.next
#         odd.next = even_head
#         return head










# # 19. Remove Nth Node From End of List
# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: Optional[ListNode]
#         :type n: int
#         :rtype: Optional[ListNode]
#         """
#         s = f = head
#         for _ in range(n):
#             f = f.next
#         if f == None:
#             return s.next
#         while f.next is not None:
#             s = s.next
#             f = f.next
#         s.next = s.next.next
        
#         return head