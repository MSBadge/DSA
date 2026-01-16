# create Node
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    # insert at head
    def insert_at_head(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # append element
    def append(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    # insert at between
    def insert_at_between(self,val,possition):
        new_node = Node(val)
        if possition == 0:
            self.insert_at_head(val)
            return
        current = self.head
        count = 0
        while current and count < possition-1:
            current = current.next
            count+=1
        if not current:
            return f"Position not Exist"
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        


    # print list
    def traverse(self):
        current = self.head
        while current.next:
            print(current.val, end=" ")
            current = current.next
        print()
        while current:
            print(current.val, end=" ")
            current = current.prev
        print()
        
    # delete head
    def delete_head(self):
        current = self.head
        if current is not None:
            self.head = current.next
            current.next.prev = None
            current.next = None

    # delete tail
    # def delete_tail(self):
    #     previous = None
    #     current = self.head
    #     while current:
    #         if current.next == None:
    #             previous = current.prev
    #             current.prev = None
    #             previous.next = None
        

    # delete at position
    def delete_at(self,val):
        current = self.head
        if val == current.val:
            self.delete_head()
            return
        else:
            previous = None
            found = False
            while current:
                if current.val == val:
                    found = True
                    break
                previous = current
                current = current.next
            if found:
                previous.next = current.next
                current.next = current.prev



a = [1,2,3,4,5,6,7,8,9]
n = len(a)
dll = DoubleLinkedList()

for i in range(n):
    dll.append(a[i])

dll.insert_at_between(44,5)
dll.delete_head()
dll.delete_at(5)
# dll.delete_tail()
dll.traverse()