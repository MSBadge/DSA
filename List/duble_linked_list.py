# create Node
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # insert at head
    def insert_at_head(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # append element / insert at tail
    def append(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

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
    def traverse_forword(self):
        current = self.head
        print(f"None <->", end=' ')
        while current:
            print(f"{current.val} <->", end=" ")
            current = current.next
        print('None')

    def traverse_backword(self):
        currunt = self.tail
        print(f"None <->", end=' ')
        while currunt:
            print(f"{currunt.val} <->", end=' ')
            currunt = currunt.prev
        print('None')
        
        
    # delete head
    def delete_head(self):
        current = self.head
        if current is not None:
            self.head = current.next
            current.next.prev = None
            current.next = None

    # delete tail
    def delete_tail(self):
        current = self.tail
        if current:
            self.tail = current.prev
            current.prev.next = None
            current.prev = None
        

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
                current.next.prev = current.prev



a = [1,2,3,4,5,6,7,8,9]
n = len(a)
dll = DoubleLinkedList()

for i in range(n):
    dll.append(a[i])

# dll.insert_at_between(44,5)
# dll.delete_head()
# dll.delete_at(5)
# dll.delete_tail()
# dll.traverse_forword()
# dll.traverse_backword()